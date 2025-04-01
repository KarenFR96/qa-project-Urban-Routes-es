# Urban Routes - Automatización de Pruebas para Servicio de Taxi

## Descripción del Proyecto
"Urban Routes" es una plataforma web que ofrece servicios de solicitud de taxis. Este proyecto se enfoca en la **automatización de pruebas** para asegurar que el flujo completo de solicitud de un taxi funcione correctamente. Las pruebas incluyen:
- Selección de rutas
- Elección del tipo de vehículo
- Método de pago
- Preferencias adicionales como mensajes al conductor y opciones de comodidad

El objetivo es garantizar que todos los aspectos del sistema estén funcionando como se espera, utilizando pruebas automatizadas para mejorar la eficiencia y fiabilidad del servicio.

## Tecnologías y Herramientas Utilizadas
- **Selenium WebDriver**: Utilizado para automatizar interacciones con el navegador web.
- **Python**: Lenguaje de programación utilizado para escribir las pruebas automatizadas.
- **Pytest**: Framework de pruebas que facilita la organización, ejecución y reporte de las pruebas.
- **Page Object Model (POM)**: Patrón de diseño para mejorar la mantenibilidad del código de las pruebas, separando la lógica de interacción con las páginas.
- **WebDriverWait**: Utilizado para gestionar esperas explícitas y hacer las pruebas más robustas.
- **Git**: Herramienta de control de versiones para gestionar el código fuente y el historial de cambios.

## Requisitos Previos
Antes de ejecutar las pruebas, asegúrate de tener lo siguiente instalado en tu sistema:

1. **Python 3.13+**: Puedes descargar la última versión de Python desde [python.org](https://www.python.org/downloads/).
2. **ChromeDriver**: Asegúrate de tener la versión compatible con tu navegador Chrome. Descárgalo desde [aquí](https://sites.google.com/a/chromium.org/chromedriver/) y colócalo en una ubicación accesible o añádelo al PATH.

## Instalación de Dependencias
Una vez tengas Python y ChromeDriver configurados, instala las librerías necesarias ejecutando:

pip install selenium pytest

# Pasos para Ejecutar las Pruebas

## Clona el Repositorio:

1. Clona el repositorio en tu máquina local:

    ```bash
    git clone <URL-del-repositorio>
    ```

2. Navega a la carpeta del proyecto:

    ```bash
    cd qa-project-Urban-Routes-es
    ```

## Ejecuta las Pruebas:

1. **Para ejecutar todas las pruebas**:

    ```bash
    pytest main.py -v
    ```

2. **Para ejecutar una prueba específica**:

    ```bash
    pytest main.py::TestUrbanRoutes::test_set_route -v
    ```

## Ver los Resultados
Los resultados de las pruebas se mostrarán directamente en la consola. Asegúrate de que todas las pruebas pasen sin errores.

---

# Configuración Adicional

## Variables de Entorno
Las URLs y otros datos de prueba, como direcciones están configurados en el archivo `data.py`. Puedes modificar estos valores según sea necesario para personalizar las pruebas.

## Logs
Las pruebas están configuradas para capturar logs del navegador. Esto puede ser útil para la depuración en caso de que alguna prueba falle.

---

# Estructura del Proyecto
El proyecto está organizado de la siguiente manera:
qa-project-Urban-Routes-es/
├── data.py                # Datos de prueba (URLs, direcciones, números de teléfono, etc.)
├── main.py                # Clases de automatización y pruebas
├── .gitignore             # Archivos y directorios a excluir del control de versiones
├── README.md              # Este archivo de documentación
├── pytest.ini             # Configuración de pytest (opcional)
└── config/                # Archivos de configuración para el entorno de desarrollo (opcional)

