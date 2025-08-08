# Portfolio de Data Science

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/tu-usuario/data-science-portfolio)

Este repositorio contiene una colección de proyectos de Data Science que responden a diferentes preguntas y problemas de análisis de datos.

## 📁 Estructura del Proyecto

```
data-science-portfolio/
├── proyectos/           # Carpetas individuales para cada proyecto
├── datos/              # Datasets y archivos de datos
├── documentacion/      # Documentación técnica y reportes
├── notebooks/          # Jupyter notebooks de análisis
├── scripts/           # Scripts de Python para automatización
├── requisitos/        # Archivos de dependencias
└── README.md          # Este archivo
```

## 🎯 Proyectos Incluidos

### [Proyecto 1: Análisis del Dataset de Iris]
- **Pregunta:** ¿Podemos clasificar especies de iris basándonos en sus características morfológicas?
- **Estado:** ✅ Completado
- **Tecnologías:** Python, Pandas, Matplotlib, Seaborn, Scikit-learn
- **Resultados:** Modelo Random Forest con >95% precisión

### [Proyecto 2: Predicción de Precios]
- **Pregunta:** ¿Podemos predecir el precio de viviendas basándonos en características del mercado?
- **Estado:** Planificado
- **Tecnologías:** Python, Scikit-learn, XGBoost

### [Proyecto 3: Análisis de Sentimientos]
- **Pregunta:** ¿Cuál es la percepción de los usuarios sobre nuestros productos?
- **Estado:** Planificado
- **Tecnologías:** Python, NLTK, Transformers

## 🚀 Instalación y Configuración

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/data-science-portfolio.git
cd data-science-portfolio
```

2. Crea y activa el ambiente virtual:
```bash
# Crear ambiente virtual
python3 -m venv venv_iris

# Activar ambiente virtual
source venv_iris/bin/activate

# O usar el script de activación
source scripts/activate_env.sh
```

3. Instala las dependencias:
```bash
pip install -r requisitos/requirements.txt
```

4. Configura Jupyter Notebook:
```bash
jupyter notebook
```

### 🌍 Gestión del Ambiente Virtual

- **Activar**: `source venv_iris/bin/activate` o `source scripts/activate_env.sh`
- **Desactivar**: `deactivate`
- **Verificar**: El prompt debería mostrar `(venv_iris)`
- **Reinstalar dependencias**: `pip install -r requisitos/requirements.txt --force-reinstall`

## 📊 Tecnologías Utilizadas

- **Python 3.8+**
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Computación numérica
- **Matplotlib/Seaborn** - Visualización de datos
- **Scikit-learn** - Machine Learning
- **Jupyter Notebook** - Análisis interactivo

## 📝 Convenciones de Código

- Usar nombres descriptivos para variables y funciones
- Documentar funciones y clases
- Seguir PEP 8 para estilo de código
- Incluir docstrings en todas las funciones

## 🤝 Contribuciones

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👨‍💻 Autor

**Tu Nombre**
- GitHub: [@andresdambrosio](https://github.com/aandresdambrosio)
- LinkedIn: [Andrés D'Ambrosio](https://www.linkedin.com/in/andresdambrosio/)
- Email: andresdambrosio@gmail.com

## 📊 Estado del Proyecto

- ✅ **Proyecto 1**: Análisis de Iris - Completado

## 🎯 Próximos Pasos

1. Agregar más información al análisis
2. Probar con más modelos y otras técnicas
3. Armar contenido didáctico y explicativo

---

⭐ Si te gusta este proyecto, ¡dale una estrella! 