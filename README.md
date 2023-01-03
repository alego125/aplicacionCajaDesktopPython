# App Caja Dia 💲
----
> Se trata de una aplicación en la cual podremos descargar y correr en nuestro pc, donde se podrán realizar registros de ingresos y egresos diarios, así como también generación de reportes en Excel y búsquedas por fecha.
>
> Todo este programa se basa en el almacenamiento de la información sobre una base de datos local SQLite. Esta es generada en la raíz del proyecto así como también el reporte en Excel.

## Descripción de la app ✍
----
##### Ventana principal
imagen principal

Acá tendremos los campos para realizar la selección del detalle del ingreso o egreso, también podremos seleccionar si ese input es un ingreso o un egreso. En la parte mas abajo tendremos casilleros donde podremos ingresar el monto del ingreso o del egreso dependiendo de que estemos haciendo y alguna observación o descripción que queramos agregar, seguido a esto tenemos un casillero de mercado pago para hacer referencia a si esta seleccionado se trata de un pago online o por tarjeta y si esta sin seleccionar es un pago en efectivo. Por ultimo tenemos el botón de guardar, el cual nos guarda en la base de datos nuestros registros.

## 🚧 Antes de continuar

> Antes de continuar se debe una vez iniciado el programa en la pantalla principal, debemos presionar en archivo y luego en crear base de datos, luego seguidamente ir en el mismo lugar archivo>Ver lista detalles, y aquí agregar algún detalle, para luego volver a la pantalla principal y poder comenzar a agregar registros a la base de datos local.

#### ✅ Ventana principal menú de opciones
imagen menús

Acá tendremos varias opciones para elegir, primeramente en el archivo tenemos la primer opción que es:

##### ✅ Ver registros del día
imagen

Acá se nos abre la venta que vemos en pantalla en la imagen de acá arriba, en esta tenemos un listado con los registros que se han realizado en el día, acá podemos seleccionar el que queramos y presionar en el botón eliminar para borrarlo permanentemente de la base de datos en caso de habernos equivocado

Luego la segunda opción de archivo es:

##### ✅ Ver lista detalles
imagen

Acá se nos abre la venta que nos permite ver el listado de detalles para agregar a cada registro, en esta podremos seleccionar el que queramos de esta tabla y presionar en eliminar para que se borre permanentemente de la base de datos, también podemos ingresar un nuevo detalle en el casillero y guardarlo mediante el botón agregar detalle.

La tercera opción es:

##### ✅ Actualizar ventana

Acá simplemente lo que se hace es recargar la ventana para así se puedan ver los detalles que podamos haber agregado desde la opción ver detalles y que no se reflejen en el menú desplegable por ejemplo.

Como cuarta opción tenemos:

##### ✅ Crear base de datos

En esta opción se inicializa la base de datos en caso de que esta no este creada la crea con sus respectivas tablas y campos. En el caso de que este creada esta opción estará deshabilitada.

Por último tenemos la opción de salir que nos saca del todo el programa

El segundo es Edición, acá tenemos las siguientes opciones:

##### ✅ Generar reporte del día

Con esta opción lo que hacemos es generar un archivo Excel con el reporte del día.

Seguidamente tenemos la opción de:

##### ✅ Buscar registros por fecha
imagen

Con esta opción lo que tenemos es que se nos abrirá una ventana con un selector de calendario para elegir la fecha que queremos visualizar, seguidamente tendemos una tabla que nos mostrará los registros de dicha fecha. Pero para ver estos registros primeramente tenderemos que primero seleccionar la fecha que queremos y luego presionar el botón de Buscar, luego si lo deseamos también podremos generar el reporte de esa fecha con el botón de generar reporte.

## ⚙ Setup
----

Para realizar la instalación de este programa siga los siguientes pasos, vamos a tener dos maneras usted puede usar la que mas le guste.

#### 🐍 Opción instalando Python en Windows

> Para las instalaciones siguientes debemos abrir la línea de comando situándonos en el directorio del proyecto

1) Descargamos y configuramos Python en nuestro pc si no lo tenemos. Para esto podemos seguir el siguiente video [Instalando y configurando Python desde cero](https://youtu.be/_T3UC_okLiM)

2) Descargamos el repo a un directorio local

3) Iniciamos un entorno virtual para esto instalamos mediante <code>pip virtualenv</code> para esto usamos el comando <code>pip install virtualenv</code>

4) Luego de esto creamos el entorno virtual con <code>virtualenv venv</code> seguidamente luego que se instaló lo ejecutamos con <code>venv/Scripts/activate</code>

5) Seguidamente instalamos las dependencias con <code>pip install -r requirements.txt</code>

6) Una vez instaladas las dependencias lo que debemos hacer es correr ya nuestro programa con <code>python main.py</code>

7) Seguidamente inicializamos la base de datos, creamos detalles para agregar y finalmente agregamos registros

#### ⚡ Opcion ejecutar .exe

Dentro de la carpeta dist se encuentra un archivo llamado main.exe, directamente ejecutamos este archivo y podremos hacer uso de la aplicación de manera rápida y simple.

