# -*- coding: utf-8 -*-
"""
    Analisis clientes Comerciales, Industriales.
    @author: sfherrera
"""
import pandas as pd
import os
from conexion import conectar, consulta

def run():
    os.system('cls')
    mes = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }

    while True:
        pass
        print(
            f"""
         _____  _   _   ___   _      _   _   ___   _____  _____  _____  _   _
        |  ___|| | | | / _ \ | |    | | | | / _ \ /  __ \|_   _||  _  || \ | |
        | |__  | | | |/ /_\ \| |    | | | |/ /_\ \| /  \/  | |  | | | ||  \| |
        |  __| | | | ||  _  || |    | | | ||  _  || |      | |  | | | || . ` |
        | |___ \ \_/ /| | | || |____| |_| || | | || \__/\ _| |_ \ \_/ /| |\  |
        \____/  \___/ \_| |_/\_____/ \___/ \_| |_/ \____/ \___/  \___/ \_| \_/
        """)
        i = 1
        for i in mes:
            print(i, '-', mes[i])
        print('Digite Opcion: ')
        opcion = int(input('OPCION: '))
        eleccion = ''
        if opcion in mes:
            eleccion = mes[opcion]
            break
        else:
            os.system('cls')
            print(
                "==========================================================================================================")
            print("Digite opcion VALIDA")
            print(
                "==========================================================================================================")

    conexion = conectar()
    SQL = consulta()
    
    #CONSUMOS_PIVOT_CONSUMOS_ACTIVA
    data = pd.read_sql_query(SQL, conexion)
    data.loc[data['Prom_OPEN'].isna(), 'Prom_OPEN'] = data.loc[:,
                                                               'Mayo': 'Octubre'].mean(axis=1)
    """
    ======================================================
    Cambiar parametros de mes para calcular el promedio 
    para los clientes que no se les puede calcular.
    ======================================================
    """
    print(data.columns)
    data = data.sort_values(by='Prom_OPEN', ascending=False)
    """
    ======================================================
                    ORGANIZAR LA INFORMACION
    ======================================================
    """
    data_2 = data[(data['Enero'] > 0) & (data['Febrero'] > 0) & (
        data['Marzo'] > 0) & (data['Abril'] > 0) & (data['Mayo'] > 0) &
        (data['Junio'] > 0) & (data['Julio'] > 0) & (
            data['Julio'] > 0) & (data['Agosto'] > 0)
        & (data['Septiembre'] > 0) & (data['Octubre'] > 0) & (data['Noviembre'] > 0) & (data['Diciembre'] > 0)
    ]
    data_2['MAXIMO'] = data_2.loc[:, 'Enero': 'Diciembre'].max(axis=1)
    data_2['MINIMO'] = data_2.loc[:, 'Enero': 'Diciembre'].min(axis=1)
    """
    ======================================================
                            LOGICA
    ======================================================
    """
    data_3 = data_2[(data_2[eleccion] <= data_2['MINIMO'])]
    data_3 = data_3[(data['Prom_OPEN'] > 1000)]
    """
    ======================================================
    Se realiza una diferencia porcentual entre el consumo
    MINIMO y el CONSUMO PROMEDIO y se filtran los clientesL
    que presentan mayor a 30%
    ======================================================
    """
    data_3 = data_3[100-(data_3['MINIMO']/data_3['Prom_OPEN'] * 100) > 30]
    """
    ======================================================
    Se quitan los clientes que aun no tienen Sector asignado.
    y se exporta los clientes.
    ======================================================
    """
    data_3 = data_3[(data_3['SECTOR'] == 'SUR') | (data_3['SECTOR'] == 'NORTE') | (
        data_3['SECTOR'] == 'CENTRO') | (data_3['SECTOR'] == 'CETSA') | (data_3['SECTOR'] == 'PACIFICO')]
    data_3.to_excel(
        'C:\\Users\\sfherrera\\Documents\\ANALISIS_CLIENTES\\DATOS.xlsx', index=False)
    os.system('cls')
    print(
        f"""
    ==========================================================================================================
         _____  _   _   ___   _      _   _   ___   _____  _____  _____  _   _
        |  ___|| | | | / _ \ | |    | | | | / _ \ /  __ \|_   _||  _  || \ | |
        | |__  | | | |/ /_\ \| |    | | | |/ /_\ \| /  \/  | |  | | | ||  \| |
        |  __| | | | ||  _  || |    | | | ||  _  || |      | |  | | | || . ` |
        | |___ \ \_/ /| | | || |____| |_| || | | || \__/\ _| |_ \ \_/ /| |\  |
        \____/  \___/ \_| |_/\_____/ \___/ \_| |_/ \____/ \___/  \___/ \_| \_/
    ==========================================================================================================
        Exportando Informacion Ruta: C:\\Users\\sfherrera\\Documents\\ANALISIS_CLIENTES\\DATOS.xlsx
    ==========================================================================================================
        """)
    os.system('pause')


if __name__ == '__main__':
    run()
