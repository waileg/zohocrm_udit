# zohocrm_udit

## Extraer Leads de Zoho CRM

Este repositorio incluye un ejemplo de script en Python para descargar datos del módulo **Leads** de Zoho CRM.

### Requisitos
- Python 3
- [Requests](https://pypi.org/project/requests/) (`pip install requests`)
- Un `access token` válido para la API de Zoho CRM (se puede especificar mediante la variable de entorno `ZOHO_ACCESS_TOKEN` o introducirlo al ejecutar el script).

### Uso
1. Instala las dependencias:
   ```bash
   pip install requests
   ```
2. Ejecuta el script `extraer_leads.py` y sigue las indicaciones para introducir las fechas y el token:
   ```bash
   python extraer_leads.py
   ```
3. Se generarán tres archivos CSV (uno para el período seleccionado, otro para el mismo rango un año atrás y otro dos años atrás) con los campos:
   - Año comercial
   - País
   - Provincia
   - Estado
   - Titulación interés principal
   - Fuente de posible alumno
