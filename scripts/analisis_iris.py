#!/usr/bin/env python3
"""
Script de Análisis del Dataset de Iris
=======================================

Este script realiza un análisis completo del dataset de Iris, incluyendo:
- Carga y limpieza de datos
- Análisis exploratorio
- Visualizaciones
- Preparación para machine learning

Autor: Tu Nombre
Fecha: 2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Configuración de visualización
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)

class IrisAnalyzer:
    """
    Clase para el análisis completo del dataset de Iris
    """
    
    def __init__(self, data_path='datos/iris/Iris.csv'):
        """
        Inicializar el analizador
        
        Args:
            data_path (str): Ruta al archivo CSV del dataset
        """
        self.data_path = data_path
        self.df = None
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def load_data(self):
        """Cargar y preparar los datos"""
        print("📊 Cargando datos...")
        self.df = pd.read_csv(self.data_path)
        
        # Eliminar la columna Id si existe
        if 'Id' in self.df.columns:
            self.df = self.df.drop('Id', axis=1)
            
        print(f"✅ Datos cargados: {self.df.shape[0]} filas, {self.df.shape[1]} columnas")
        return self.df
    
    def explore_data(self):
        """Análisis exploratorio básico"""
        print("\n🔍 Análisis Exploratorio:")
        print("=" * 50)
        
        # Información básica
        print(f"📋 Forma del dataset: {self.df.shape}")
        print(f"📋 Tipos de datos:\n{self.df.dtypes}")
        
        # Valores faltantes
        missing_values = self.df.isnull().sum()
        print(f"\n❓ Valores faltantes:\n{missing_values}")
        
        # Estadísticas descriptivas
        print(f"\n📊 Estadísticas descriptivas:")
        print(self.df.describe())
        
        # Distribución de especies
        species_counts = self.df['Species'].value_counts()
        print(f"\n🌺 Distribución de especies:")
        for species, count in species_counts.items():
            print(f"  - {species}: {count} muestras ({count/len(self.df)*100:.1f}%)")
    
    def create_visualizations(self):
        """Crear visualizaciones del dataset"""
        print("\n📈 Creando visualizaciones...")
        
        # Configurar subplots
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Análisis Visual del Dataset de Iris', fontsize=16, fontweight='bold')
        
        # 1. Distribución de especies
        species_counts = self.df['Species'].value_counts()
        axes[0, 0].pie(species_counts.values, labels=species_counts.index, autopct='%1.1f%%')
        axes[0, 0].set_title('Distribución de Especies')
        
        # 2. Boxplots por variable
        numeric_cols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
        for i, col in enumerate(numeric_cols):
            row = i // 2
            col_idx = i % 2 + 1
            self.df.boxplot(column=col, by='Species', ax=axes[row, col_idx])
            axes[row, col_idx].set_title(f'{col} por Especie')
            axes[row, col_idx].set_xlabel('')
        
        # 3. Matriz de correlación
        correlation_matrix = self.df[numeric_cols].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                   square=True, linewidths=0.5, ax=axes[1, 2])
        axes[1, 2].set_title('Matriz de Correlación')
        
        plt.tight_layout()
        plt.savefig('proyectos/analisis_iris/correlacion_iris.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Pairplot
        plt.figure(figsize=(12, 10))
        sns.pairplot(self.df, hue='Species', diag_kind='hist')
        plt.suptitle('Análisis de Pares de Variables', y=1.02, fontsize=16, fontweight='bold')
        plt.savefig('proyectos/analisis_iris/pairplot_iris.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("✅ Visualizaciones guardadas en proyectos/analisis_iris/")
    
    def prepare_for_ml(self):
        """Preparar datos para machine learning"""
        print("\n🤖 Preparando datos para Machine Learning...")
        
        # Separar features y target
        self.X = self.df.drop('Species', axis=1)
        self.y = self.df['Species']
        
        # Dividir en train y test
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42, stratify=self.y
        )
        
        # Escalar los datos
        scaler = StandardScaler()
        self.X_train_scaled = scaler.fit_transform(self.X_train)
        self.X_test_scaled = scaler.transform(self.X_test)
        
        print(f"✅ Datos preparados:")
        print(f"  - X_train: {self.X_train.shape}")
        print(f"  - X_test: {self.X_test.shape}")
        print(f"  - y_train: {self.y_train.shape}")
        print(f"  - y_test: {self.y_test.shape}")
    
    def train_model(self):
        """Entrenar un modelo de clasificación"""
        print("\n🎯 Entrenando modelo Random Forest...")
        
        # Entrenar modelo
        rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_model.fit(self.X_train_scaled, self.y_train)
        
        # Predicciones
        y_pred = rf_model.predict(self.X_test_scaled)
        
        # Evaluación
        print("\n📊 Resultados del Modelo:")
        print("=" * 40)
        print(classification_report(self.y_test, y_pred))
        
        # Matriz de confusión
        cm = confusion_matrix(self.y_test, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                   xticklabels=rf_model.classes_, 
                   yticklabels=rf_model.classes_)
        plt.title('Matriz de Confusión')
        plt.ylabel('Valor Real')
        plt.xlabel('Predicción')
        plt.savefig('proyectos/analisis_iris/matriz_confusion.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Importancia de features
        feature_importance = pd.DataFrame({
            'feature': self.X.columns,
            'importance': rf_model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(data=feature_importance, x='importance', y='feature')
        plt.title('Importancia de Features')
        plt.xlabel('Importancia')
        plt.savefig('proyectos/analisis_iris/importancia_features.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("\n🏆 Importancia de features:")
        for idx, row in feature_importance.iterrows():
            print(f"  - {row['feature']}: {row['importance']:.3f}")
        
        return rf_model
    
    def generate_report(self):
        """Generar reporte completo"""
        print("\n📝 Generando reporte...")
        
        report = f"""
# Reporte de Análisis del Dataset de Iris
## Resumen Ejecutivo

### Datos del Dataset:
- **Total de muestras**: {len(self.df)}
- **Variables**: {len(self.df.columns) - 1} features + 1 target
- **Especies**: {len(self.df['Species'].unique())}
- **Balance**: {self.df['Species'].value_counts().to_dict()}

### Calidad de Datos:
- **Valores faltantes**: {self.df.isnull().sum().sum()}
- **Duplicados**: {self.df.duplicated().sum()}

### Variables Numéricas:
{self.df.describe().to_string()}

### Correlaciones:
{self.df.drop('Species', axis=1).corr().to_string()}

### Conclusiones:
1. El dataset está perfectamente balanceado (50 muestras por especie)
2. No hay valores faltantes
3. Las variables de pétalos muestran mayor correlación
4. Las especies son bien diferenciables por sus características

### Archivos Generados:
- correlacion_iris.png
- pairplot_iris.png
- matriz_confusion.png
- importancia_features.png
"""
        
        # Guardar reporte
        with open('proyectos/analisis_iris/reporte_analisis.md', 'w', encoding='utf-8') as f:
            f.write(report)
        
        print("✅ Reporte guardado en proyectos/analisis_iris/reporte_analisis.md")
    
    def run_complete_analysis(self):
        """Ejecutar análisis completo"""
        print("🚀 Iniciando Análisis Completo del Dataset de Iris")
        print("=" * 60)
        
        # Ejecutar todos los pasos
        self.load_data()
        self.explore_data()
        self.create_visualizations()
        self.prepare_for_ml()
        model = self.train_model()
        self.generate_report()
        
        print("\n🎉 ¡Análisis completado exitosamente!")
        print("📁 Los resultados se han guardado en proyectos/analisis_iris/")

def main():
    """Función principal"""
    analyzer = IrisAnalyzer()
    analyzer.run_complete_analysis()

if __name__ == "__main__":
    main()
