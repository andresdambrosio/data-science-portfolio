# Proyecto: Análisis del Dataset de Iris

## 📋 Descripción del Proyecto

Este proyecto realiza un análisis completo del dataset clásico de Iris, que contiene mediciones de 150 flores de iris de tres especies diferentes. El objetivo es demostrar habilidades en análisis exploratorio de datos, visualización y machine learning.

### 🎯 Objetivos

1. **Análisis Exploratorio**: Comprender las características del dataset
2. **Visualización**: Crear gráficos informativos sobre las relaciones entre variables
3. **Machine Learning**: Implementar un modelo de clasificación para predecir especies
4. **Documentación**: Generar reportes técnicos completos

## 📊 Dataset

### Fuente
- **Dataset**: Iris Flower Dataset
- **Autor original**: R.A. Fisher (1936)
- **Repositorio**: UCI Machine Learning Repository

### Variables
- **SepalLengthCm**: Longitud del sépalo (cm)
- **SepalWidthCm**: Ancho del sépalo (cm)
- **PetalLengthCm**: Longitud del pétalo (cm)
- **PetalWidthCm**: Ancho del pétalo (cm)
- **Species**: Especie de iris (target)

### Especies
- Iris-setosa
- Iris-versicolor
- Iris-virginica

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **Pandas**: Manipulación de datos
- **NumPy**: Computación numérica
- **Matplotlib/Seaborn**: Visualización
- **Scikit-learn**: Machine Learning
- **Jupyter Notebook**: Análisis interactivo

## 📁 Estructura del Proyecto

```
proyectos/analisis_iris/
├── correlacion_iris.png
├── pairplot_iris.png
├── matriz_confusion.png
├── importancia_features.png
└── reporte_analisis.md

notebooks/
└── 01_analisis_exploratorio_iris.ipynb

scripts/
└── analisis_iris.py

documentacion/
└── proyecto_iris.md
```

## 🚀 Instalación y Uso

### 1. Instalar dependencias
```bash
pip install -r requisitos/requirements.txt
```

### 2. Ejecutar análisis automatizado
```bash
cd scripts
python analisis_iris.py
```

### 3. Abrir notebook interactivo
```bash
jupyter notebook notebooks/01_analisis_exploratorio_iris.ipynb
```

## 📈 Resultados Esperados

### Análisis Exploratorio
- Distribución balanceada de especies (50 muestras cada una)
- No hay valores faltantes
- Correlaciones fuertes entre variables de pétalos
- Separabilidad clara entre especies

### Machine Learning
- Modelo Random Forest con alta precisión (>95%)
- Variables de pétalos más importantes para clasificación
- Matriz de confusión con pocos errores

### Visualizaciones
- Gráficos de distribución por especie
- Matriz de correlación
- Pairplot mostrando relaciones entre variables
- Gráfico de importancia de features

## 📝 Hallazgos Principales

1. **Balance del Dataset**: Perfectamente balanceado con 50 muestras por especie
2. **Calidad de Datos**: Sin valores faltantes o duplicados
3. **Correlaciones**: 
   - Fuerte correlación positiva entre PetalLength y PetalWidth
   - Correlación moderada entre SepalLength y PetalLength
4. **Separabilidad**: Las especies muestran patrones distintos de mediciones
5. **Machine Learning**: Random Forest logra excelente precisión en clasificación

## 🔍 Métricas de Evaluación

- **Precisión**: >95%
- **Recall**: >95% para todas las especies
- **F1-Score**: >95% para todas las especies
- **Accuracy**: >95%

## 📊 Archivos de Salida

1. **correlacion_iris.png**: Matriz de correlación entre variables
2. **pairplot_iris.png**: Análisis de pares de variables
3. **matriz_confusion.png**: Matriz de confusión del modelo
4. **importancia_features.png**: Importancia de variables en el modelo
5. **reporte_analisis.md**: Reporte técnico completo

## 🎯 Próximos Pasos

1. **Análisis más profundo**: Implementar otros algoritmos de ML
2. **Validación cruzada**: Mejorar evaluación del modelo
3. **Optimización de hiperparámetros**: Usar GridSearch o RandomSearch
4. **Aplicación web**: Crear interfaz para predicciones
5. **Análisis de outliers**: Investigar casos especiales

## 👨‍💻 Autor

**Tu Nombre**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- LinkedIn: [Tu LinkedIn](https://linkedin.com/in/tu-perfil)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

---

*Este proyecto demuestra habilidades fundamentales en Data Science: limpieza de datos, análisis exploratorio, visualización y machine learning.*
