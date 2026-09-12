# 🛡️ Data Validator & Anomaly API

![CI Pipeline](https://github.com/JosePacheco-dev/data-validator-api/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-e91e63.svg)

Una API RESTful de grado de producción diseñada para la validación estricta de contratos de datos y la detección de anomalías en lecturas de sensores de equipos industriales.

El proyecto implementa una **Arquitectura en 3 Capas** (*Transport*, *Domain*, *Contracts/Schemas*), pruebas automatizadas con `pytest` e **Integración Continua (CI)** mediante GitHub Actions.

---

## 🏗️ Arquitectura del Proyecto

El código está estructurado siguiendo los principios de separación de responsabilidades y bajo acoplamiento:

```text
data-validator-api/
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline de Integración Continua (GitHub Actions)
├── app/
│   ├── main.py             # Capa de Transporte (Rutas e Interfaces HTTP)
│   ├── schemas.py          # Contratos de Datos y Validaciones (Pydantic v2)
│   └── services.py         # Capa de Dominio y Lógica de Negocio
├── tests/
│   └── test_main.py        # Suite de pruebas de integración y unitarias
├── .gitignore              # Archivos excluidos de control de versiones
├── requirements.txt        # Dependencias fijadas del proyecto
└── README.md               # Documentación general
```

---

## 🛠️ Especificación de Endpoints

### 1. Estado del Servicio

- **HTTP Method:** `GET`
- **Path:** `/`
- **Response:**

```json
{
  "status": "ok",
  "message": "Data-Validator API is running"
}
```

### 2. Validación de Datos de Lectura

- **HTTP Method:** `POST`
- **Path:** `/api/v1/validate`
- **Request Payload (Ejemplo Exitoso):**

```json
{
  "equipment_id": "DEV-200",
  "value": 15.0,
  "min_limit": 5.0,
  "max_limit": 25.0
}
```

- **Response `200 OK` (Sin Anomalía):**

```json
{
  "equipment_id": "DEV-200",
  "value": 15.0,
  "is_anomaly": false,
  "status": "VALID"
}
```

- **Response `200 OK` (Con Anomalía):**

```json
{
  "equipment_id": "DEV-200",
  "value": 35.0,
  "is_anomaly": true,
  "status": "ANOMALY_DETECTED"
}
```

- **Response `422 Unprocessable Entity` (Contrato Inválido):** Lanzado automáticamente por Pydantic cuando faltan campos, se envían tipos incorrectos o los datos no cumplen las restricciones de validación.

---

## 🚀 Instalación y Ejecución Local

### Prerrequisitos

- Python 3.12+

### Pasos

1. Clonar el repositorio:

```bash
git clone https://github.com/JosePacheco-dev/data-validator-api.git
cd data-validator-api
```

2. Crear y activar el entorno virtual:

   - En Windows:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

   - En Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Iniciar la aplicación en modo desarrollo:

```bash
uvicorn app.main:app --reload
```

La API estará accesible en `http://127.0.0.1:8000`. La documentación interactiva Swagger UI estará disponible en `http://127.0.0.1:8000/docs`.

---

## 🧪 Ejecución de Pruebas Automatizadas

El proyecto cuenta con una suite completa de pruebas unitarias e integración con `pytest`:

```bash
pytest
```

---

## 🔄 Integración Continua (CI/CD)

El pipeline de GitHub Actions se ejecuta automáticamente en cada `push` o `pull_request` a la rama `main`. Ejecuta los siguientes pasos sobre un contenedor `ubuntu-latest`:

1. Configura el entorno de Python 3.12.
2. Instala las dependencias del `requirements.txt`.
3. Ejecuta la suite completa de `pytest`.
