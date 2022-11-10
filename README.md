# Análisis de clientes Regulados
Este desarrollo permite realizar análisis a los clientes Comerciales e Industriales que se encuentran en el mercado
regulado de la compañía que presentan bajo consumo en el periodo evaluado.

# Funcionalidad

1. Para obtener precisión en el análisis, se obtiene un consumo promedio del sistema de facturación legado.
2. Los clientes nuevos que no se encuentran en el sistema legado, se les calcula un promedio.
3. Calculamos valores MINIMOS y MAXIMOS históricos del cliente.
4. Se realiza una diferencia porcentual entre el consumo MINIMO y el CONSUMO PROMEDIO y se filtran los clientes.

# Observación
> De esta forma podemos encontrar o determinar que clientes en un principio su consumo disminuyo por algún motivo para el mes en evaluación. 
Se requiere realizar una evaluación más detallada a cada uno, teniendo en cuenta otro tipo de variables (Mercado, estacionalidad, Agenda de lectura).

# Archivo BATCH
Lo utilizo para que el desarrollo se puede ejecutar.

# Visualizacion
> Seleccionamos el mes a Evaluar y ejecutamos.
![image](https://user-images.githubusercontent.com/20642907/201192256-5422a201-3ed5-4956-a9fa-4f5dbef69136.png)

Una vez termine y previamente damos la ruta para guardar el archivo tenemos el resultado del analisis.
![image](https://user-images.githubusercontent.com/20642907/201193059-17353898-ed39-46f7-8bb2-fc938063543b.png)
