import os
import csv
import requests
from datetime import datetime, timedelta

CAMPOS = [
    "Año_comercial",
    "País",
    "Provincia",
    "Estado",
    "Titulación_interés_principal",
    "Fuente_de_posible_alumno",
]

API_BASE = "https://www.zohoapis.com/crm/v2"
MODULE = "Leads"


def obtener_periodos(inicio, fin):
    """Devuelve periodos: seleccionado, -1 año, -2 años."""
    di = datetime.strptime(inicio, "%Y-%m-%d")
    df = datetime.strptime(fin, "%Y-%m-%d")
    delta = df - di

    periodos = []
    for offset in range(3):
        start = di.replace(year=di.year - offset)
        end = start + delta
        periodos.append((start, end))
    return periodos


def buscar_leads(token, inicio, fin):
    criteria = f"(Created_Time:between:{inicio}T00:00:00+00:00:{fin}T23:59:59+00:00)"
    params = {"criteria": criteria, "fields": ",".join(CAMPOS)}
    headers = {"Authorization": f"Zoho-oauthtoken {token}"}
    resp = requests.get(f"{API_BASE}/{MODULE}/search", params=params, headers=headers)
    resp.raise_for_status()
    return resp.json().get("data", [])


def guardar_csv(datos, nombre):
    with open(nombre, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()
        for item in datos:
            row = {campo: item.get(campo, "") for campo in CAMPOS}
            writer.writerow(row)


def main():
    token = os.getenv("ZOHO_ACCESS_TOKEN")
    if not token:
        token = input("Introduce tu token de acceso: ").strip()

    inicio = input("Fecha inicio (YYYY-MM-DD): ")
    fin = input("Fecha fin (YYYY-MM-DD): ")

    periodos = obtener_periodos(inicio, fin)
    nombres = ["actual", "-1_ano", "-2_anos"]
    for (ini, fi), nombre in zip(periodos, nombres):
        datos = buscar_leads(token, ini.date().isoformat(), fi.date().isoformat())
        guardar_csv(datos, f"leads_{nombre}.csv")
        print(f"Período {nombre}: {len(datos)} registros guardados")


if __name__ == "__main__":
    main()
