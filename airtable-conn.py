#hack4Venezuela
#This code is meant to upload data from a csv file to the Airtable base
import pandas as pd
from datetime import datetime as dt
from requests import get, put, patch, post, delete

URL_BASE = "https://api.airtable.com/v0/appytbljri69Kz9kSCS7z/"
HEAD = {"Authorization": "Bearer keyGnW1mEMIIjqHIm"}
journos = [{'natalia.matamoros': 'rec05W4ZjBJjmi84i'},
            {'darvinson.rojas': 'rec5Ah0YrHNT4hBG9'},
            {'juan.brinceno': 'rec7tVeabzimXs5Gw'},
            {'lorena.melendez': 'recAcGNHxlhaPjTgU'},
            {'carlos.dhoy': 'recEGz1NPgy95zmBc'},
            {'lysaura.fuentes': 'recHzMsPHjXAhoehn'},
            {'vanessa.moreno': 'recPD5Tq1VojF4anu'},
            {'juan.mejia': 'recS5jheR7sR98vWC'},
            {'yohana.marra': 'recpgfLsyHSJk1l2t'},
            {'daisy.galaviz': 'recsY5vOcePsJ2Y1y'}]
# Fcuk doing this shit by hand

preset = {"fields": {
    "Nombre de la víctima": "",
    "Sexo": "",
    "Usuario": [""],
    "Parroquia": [""],
    "Indicar fecha y hora del crimen": "",
    "Lugar del crimen": ""
    "¿La víctima estaba armada?": "",
    "Parroquia": "",
    "Municipality": "",
    "Estado": "",
    "Detalles de la muerte (¿cómo ocurrió? )": "",
    "Descripción adicional de lugar del crime": "",
    "¿Existen otras víctimas en la familia?": "",
    "Contexto del crimen": "",
    "Fuente de la información": "",
    "Teléfono de contacto": "",
    "Nombre del contacto": "",
    "Parentesco del contacto": "",
    "Color de piel": "",
    "Cantidad de hijos de la víctima (menores de 18 años)": "",
    "Cantidad de hijos de la víctima (mayores de 18 años)": "",
    "Nivel Educativo": "",
    "Tipo de arma": "",
    "Oficio de la víctima": "",
    "Nacionalidad de la víctima": "",
    "Edad de la víctima": "",
    "Cédula de la víctima": "",
    "Contexto del crimen": "",
    "Punto de referencia o dirección": "",
    "Indicar sector del crimen": "",
    "Lugar del crimen (Estado, Municipio, Parroquia)": "",
    "Fecha y hora del crimen (formato 24 horas)": "",
    "Origen del arma de fuego (lugar de fabricación)": "",
    "Relación víctima - victimario": "",
    "¿La víctima estaba armada?": "",
    "Móvil de muerte": "",
    "¿Es conocido el victimario?": "",
    "Tipo de victimario": "",
    "Cantidad de impactos de bala": ""
    }

def main():
    predata = pd.DataFrame.from_csv("/Users/marcus/Downloads/BD Trimestral Abril-Julio.xlsx - Abril-Julio 2017.csv")
    for index, row in predata.iterrows():
        row_data = preset
        #TODO: Match columns to input data
        row_data['fields']['Nombre'] = row['Nombre']

        #TODO: Validation against double uploading (because Airtable is stupid)

        #TODO: Match journalists with their ids

        #TODO: POST data to Airtable
        response = post(url=URL_BASE+"Homicides", headers=HEAD, json=row_data)
