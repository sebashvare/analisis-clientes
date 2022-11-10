"""
Informacion de movimientos comerciales: Esta permite llevar un control de 
los clientes que ingresan y salen en un periodo determinado, informacion
importante para validar los clientes del indicador de perdidas.
==========================================
Campos
==========================================
    Requerimiento
    Código SIC
    Nombre de la Frontera
    Tipo de Solicitud
    Estado
    Motivacion
    Fecha de Publicación
    Fecha Máxima de Objeción
    Fecha de Cálculo de Garantías
    Fecha Probable de Registro
    Agente Representante Actual
    Agente que Solicita el Registro
    Operador de Red
    Exportador Físico
    Importador Físico
    CGM
    Tipo de Frontera
    Ciudad-Departamento
    Dirección
    NIU
    Voltaje
    Nivel de Tensión
    Tipo de Punto de Medición
    Número de Serie del Med. Principal
    Número de Serie del Med. Respaldo
    Clase del Medidor
    Clase del TC
    Clase del TP

@author: sfherrera
"""

import pandas as pd
import os

columnas = ['Requerimiento', 'Código SIC', 'Nombre de la Frontera',
            'Tipo de Solicitud', 'Estado', 'Fecha de Publicación',
            'Fecha Máxima de Objeción', 'Fecha de Cálculo de Garantías',
            'Fecha Probable de Registro', 'Agente Representante Actual',
            'Agente que Solicita el Registro', 'Operador de Red',
            'Exportador Físico', 'Importador Físico', 'CGM', 'Tipo de Frontera',
            'Ciudad-Departamento', 'Dirección', 'NIU', 'Voltaje',
            'Nivel de Tensión', 'Tipo de Punto de Medición',
            'Número de Serie del Med. Principal',
            'Número de Serie del Med. Respaldo', 'Clase del Medidor',
            'Clase del TC', 'Clase del TP']

mes_migrar = '07'
anio = '2022'
busqueda = '{}-{}'.format(anio, mes_migrar)
listado_mes = []

listado_archivos = os.listdir(
    'C:\\Users\\sfherrera\\Documents\\AENC\\MOVIMIENTOS_COMERCIALES')

for mes in listado_archivos:
    if mes.__contains__(busqueda):
        listado_mes.append(mes)

for x in listado_mes:
    data = pd.read_excel(
        'C:\\Users\\sfherrera\\Documents\\AENC\\MOVIMIENTOS_COMERCIALES\\{}'.format(x), usecols=columnas)
    data.rename(columns={
        'Requerimiento': 'REQUERIMIENTO',
        'Código SIC': 'COD_SIC',
        'Nombre de la Frontera': 'NOM_FRONTERA',
        'Tipo de Solicitud': 'TIP_SOLICITUD',
        'Estado': 'ESTADO',
        'Fecha de Publicación': 'FEC_PUBLICACION',
        'Fecha Máxima de Objeción': 'FEC_MAX_OBJ',
        'Fecha de Cálculo de Garantías': 'FEC_CALC_GARANTIAS',
        'Fecha Probable de Registro': 'FEC_PROB_REG',
        'Agente Representante Actual': 'AGENTE_REPR_ACTUAL',
        'Agente que Solicita el Registro': 'AGENTE_SOLI_REG',
        'Operador de Red': 'OR',
        'Exportador Físico': 'EXP_FISICO',
        'Importador Físico': 'IMP_FISICO',
        'Tipo de Frontera': 'TIP_FRONTERA',
        'Ciudad-Departamento': 'CIUDAD_DEPARTAMENTO',
        'Dirección': 'DIRECCION',
        'Voltaje': 'VOLTAJE',
        'Nivel de Tensión': 'NT',
        'Tipo de Punto de Medición': 'TIP_PUNTO_MEDICION',
        'Número de Serie del Med. Principal': 'NUM_SERIE_PRIN',
        'Número de Serie del Med. Respaldo': 'NUM_SERIE_RESP',
        'Clase del Medidor': 'CLASE_MED',
        'Clase del TC': 'CLASE_TC',
        'Clase del TP': 'CLASE_TP'
    }, inplace=True)

print(data.columns)
