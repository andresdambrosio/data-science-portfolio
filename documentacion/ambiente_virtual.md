# Ambiente Virtual del Proyecto Iris

## 🌍 Configuración del Ambiente Virtual

Este proyecto utiliza un ambiente virtual de Python para mantener las dependencias organizadas y evitar conflictos con otros proyectos.

### 📁 Estructura del Ambiente

```
data-science-portfolio/
├── venv_iris/           # Ambiente virtual específico para Iris
│   ├── bin/             # Scripts de activación
│   ├── lib/             # Librerías instaladas
│   └── ...
├── datos/
├── proyectos/
├── notebooks/
├── scripts/
└── ...
```

## 🚀 Comandos Básicos

### 1. Activar el Ambiente Virtual

```bash
# Desde la raíz del proyecto
source venv_iris/bin/activate

# Verificar que está activado (debería mostrar (venv_iris) en el prompt)
(venv_iris) ➜  data-science-portfolio
```

### 2. Desactivar el Ambiente Virtual

```bash
deactivate
```

### 3. Verificar Dependencias Instaladas

```bash
# Listar todas las dependencias
pip list

# Ver dependencias específicas del proyecto
pip list | grep -E "(pandas|numpy|matplotlib|seaborn|scikit-learn)"
```

## 📦 Gestión de Dependencias

### Instalar Nuevas Dependencias

```bash
# Activar el ambiente primero
source venv_iris/bin/activate

# Instalar nueva dependencia
pip install nombre_paquete

# Actualizar requirements.txt
pip freeze > requisitos/requirements.txt
```

### Reinstalar Dependencias

```bash
# Si necesitas reinstalar todo
pip install -r requisitos/requirements.txt --force-reinstall
```

## 🔧 Configuración para Jupyter

### 1. Instalar Kernel para Jupyter

```bash
# Activar el ambiente
source venv_iris/bin/activate

# Instalar ipykernel si no está instalado
pip install ipykernel

# Crear kernel para Jupyter
python -m ipykernel install --user --name=venv_iris --display-name="Python (Iris Project)"
```

### 2. Usar el Kernel en Jupyter

1. Abrir Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. En el notebook, ir a `Kernel` → `Change kernel` → `Python (Iris Project)`

## 🐛 Solución de Problemas

### Problema: Ambiente no se activa

```bash
# Verificar que el ambiente existe
ls -la venv_iris/

# Si no existe, recrearlo
python3 -m venv venv_iris
source venv_iris/bin/activate
pip install -r requisitos/requirements.txt
```

### Problema: Dependencias no encontradas

```bash
# Verificar que el ambiente está activado
which python
# Debería mostrar: /path/to/data-science-portfolio/venv_iris/bin/python

# Reinstalar dependencias
pip install -r requisitos/requirements.txt
```

### Problema: Jupyter no encuentra el kernel

```bash
# Reinstalar el kernel
python -m ipykernel install --user --name=venv_iris --display-name="Python (Iris Project)" --force
```

## 📋 Checklist de Configuración

- [ ] Ambiente virtual creado (`venv_iris/`)
- [ ] Dependencias instaladas (`pip install -r requisitos/requirements.txt`)
- [ ] Kernel de Jupyter configurado
- [ ] Scripts funcionando correctamente
- [ ] Notebooks ejecutándose sin errores

## 🎯 Ventajas del Ambiente Virtual

1. **Aislamiento**: Dependencias específicas del proyecto
2. **Reproducibilidad**: Mismas versiones en diferentes máquinas
3. **Limpieza**: Fácil eliminación y recreación
4. **Colaboración**: Compartir requirements.txt con otros desarrolladores

## 📝 Notas Importantes

- **Siempre activar** el ambiente virtual antes de trabajar en el proyecto
- **No committear** la carpeta `venv_iris/` al repositorio (ya está en .gitignore)
- **Actualizar** `requirements.txt` cuando agregues nuevas dependencias
- **Documentar** cambios importantes en las dependencias

---

*Este ambiente virtual asegura que el proyecto funcione de manera consistente en diferentes entornos.*
