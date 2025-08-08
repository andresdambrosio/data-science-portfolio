#!/bin/bash

# Script para activar el ambiente virtual del proyecto Iris
# Uso: source scripts/activate_env.sh

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🌍 Activando ambiente virtual para el proyecto Iris...${NC}"

# Verificar si estamos en el directorio correcto
if [ ! -d "venv_iris" ]; then
    echo -e "${RED}❌ Error: No se encontró el ambiente virtual 'venv_iris'${NC}"
    echo -e "${YELLOW}💡 Asegúrate de estar en el directorio raíz del proyecto${NC}"
    echo -e "${YELLOW}💡 Directorio actual: $(pwd)${NC}"
    return 1
fi

# Activar el ambiente virtual
source venv_iris/bin/activate

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Ambiente virtual activado exitosamente${NC}"
    echo -e "${BLUE}🐍 Python version: $(python --version)${NC}"
    echo -e "${BLUE}📦 Pip version: $(pip --version)${NC}"
    
    # Verificar dependencias principales
    echo -e "${YELLOW}🔍 Verificando dependencias principales...${NC}"
    
    if python -c "import pandas" 2>/dev/null; then
        echo -e "${GREEN}✅ pandas instalado${NC}"
    else
        echo -e "${RED}❌ pandas no encontrado${NC}"
    fi
    
    if python -c "import numpy" 2>/dev/null; then
        echo -e "${GREEN}✅ numpy instalado${NC}"
    else
        echo -e "${RED}❌ numpy no encontrado${NC}"
    fi
    
    if python -c "import matplotlib" 2>/dev/null; then
        echo -e "${GREEN}✅ matplotlib instalado${NC}"
    else
        echo -e "${RED}❌ matplotlib no encontrado${NC}"
    fi
    
    if python -c "import seaborn" 2>/dev/null; then
        echo -e "${GREEN}✅ seaborn instalado${NC}"
    else
        echo -e "${RED}❌ seaborn no encontrado${NC}"
    fi
    
    if python -c "import sklearn" 2>/dev/null; then
        echo -e "${GREEN}✅ scikit-learn instalado${NC}"
    else
        echo -e "${RED}❌ scikit-learn no encontrado${NC}"
    fi
    
    echo -e "${GREEN}🎉 ¡Listo para trabajar en el proyecto Iris!${NC}"
    echo -e "${YELLOW}💡 Para desactivar el ambiente: deactivate${NC}"
    echo -e "${YELLOW}💡 Para ejecutar el análisis: python scripts/analisis_iris.py${NC}"
    echo -e "${YELLOW}💡 Para abrir Jupyter: jupyter notebook${NC}"
    
else
    echo -e "${RED}❌ Error al activar el ambiente virtual${NC}"
    return 1
fi
