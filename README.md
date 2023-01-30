# OnesticReportesPrueba

# Description


He realizado la siguiente prueba.

* Developer Junior Engineer
  * [Backend](https://github.com/onestic/interviews/tree/main/developer_junior_engineer/backend)

Para la realización de la prueba he elegido Python, ya que me siento muy comodo y para trabajar con
datos en formato csv es muy sencillo. He desarrollado una clase Reports.py, donde se encuentran tres metodos, cada metodo genera un reporte. Luego he usado el frameword de Django, donde 
he creado un pequeño frontend para subir los tres archivos productos.csv, orders.csv y customers.cvs.
Una vez iniciado el servidor ir a tu navegador, debe de ser Google Chrome, a la siguiente URL http://localhost:8000/uploadfiles/ .Una vez subidos se apreta al boton "Subir Archivos" y automaticamente el cliente hace una peticion POST al servidor http://127.0.0.1:8000/uploadfiles/downloadfiles y te descarga automaticamente un .zip que contiene los tres reportes. En conclusion, he cubierto los requisitos minimos de la prueba, creado una pequeña API y un frontend basico para interactuar. Hago incapie en que debe ser Google Chrome el navegador ya que yo uso de normal Firefox y me daba errores. La prueba esta hecha asumiendo que los archivos .csv tienen el formato correcto.

# Iniciar el Proyecto

Para iniciar el servidor de desarrollo, ejecuta el siguiente comando en la consola 
en el directorio donde se encuentra el manage.py:

```
python .\manage.py runserver
```

Una vez iniciado el servidor en tu entorno local ir al siguiente enlace:

http://localhost:8000/uploadfiles/


## Casos de uso a cubrir

Nuestros compañeros del departamento, nos presentan tres casos de uso que generarán distintos reportes de información a partir de unos ficheros que se suben a la plataforma.

### Reporte 1

El equipo de ventas quiere saber el total de cada pedido. Debe generar un fichero llamado “order_prices.csv” con las siguientes columnas: 

id: ID del pedido

total: Total del pedido en euros

### Reporte 2

El equipo de marketing quiere saber que clientes han comprado cada producto. Debe generar un fichero llamado “product_customers.csv” con las siguientes columnas: 

id: ID del producto

customer_ids: Lista de todos los ID’s que han comprado ese producto (Separados por un espacio)

### Reporte 3

 Para evaluar a los clientes, necesitamos un fichero que contenga todos los pedidos ordenados descendentemente por el total en euros:

Debe generar un fichero llamado “customer_ranking.csv" con las siguientes columnas: 

id: ID del cliente

name: Nombre del cliente

lastname: Apellidos del cliente

total: Total en euros que el cliente ha comprado en productos.

Las columnas deben ir correctamente identificadas con el nombre de cada columna en la primera fila de los ficheros.

