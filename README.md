# Happy Burger

Desarrollé este proyecto como parte del bootcamp Programación con Python nivel avanzado del certificado FullStack Developer de Tecmilenio. Mi aplicación es un sistema administrativo para una franquicia de hamburguesas y con ella se pueden registrar clientes, productos y pedidos desde una interfaz de consola.

Mi proyecto tiene persistencia de datos vía SQLite, generación de tickets en archivos de texto, una consulta web desarrollada con Flask y pruebas automatizadas con Pytest.

## Descripción del proyecto

Comencé a desarrollar Happy Burger como una aplicación de consola y fue creciendo durante cuatro avances. En todas las etapas estuve trabajando con nuevos conceptos de Python hasta desarrollar el sistema completo, lo organicé en módulos y está basado en programación orientada a objetos.

Con mi aplicación puedo realizar lo siguiente:

- Registrar, consultar, actualizar y eliminar clientes.
- Registrar, consultar, actualizar y eliminar productos del menú.
- Crear pedidos a partir de un cliente y un producto registrados.
- Calcular automáticamente el total de cada pedido.
- Consultar pedidos mediante su número.
- Mostrar el historial de pedidos registrados.
- Cancelar pedidos activos.
- Crear un ticket de consumo en formato TXT.
- Consultar pedidos desde la interfaz web que desarrollé con Flask.
- Conservar la información gracias a una base de datos SQLite.

## Funcionalidades principales

### Administración de clientes

Desde el menú de clientes puedo registrar:

- Clave del cliente.
- Nombre.
- Dirección.
- Correo electrónico.
- Teléfono.

También puedo consultar el directorio completo, actualizar los datos de un cliente o eliminarlo cuando sea necesario.

### Administración de productos

El módulo del menú me deja registrar productos con:

- Clave del producto.
- Nombre.
- Precio.

Aparte de agregar productos, puedo consultar el menú disponible, modificar la información registrada o eliminar un producto.

### Administración de pedidos

Para registrar un pedido, mi aplicación pide la clave de un cliente, la clave de un producto y la cantidad requerida.

Mi sistema consulta la información almacenada en SQLite, obtiene el nombre del cliente, el producto y su precio, calcula el total y registra el pedido con un número consecutivo. Todos los pedidos conservan los siguientes datos:

- Número de pedido.
- Clave y nombre del cliente.
- Clave y nombre del producto.
- Precio unitario.
- Cantidad solicitada.
- Total.
- Estado del pedido.
- Fecha de registro.

Los pedidos se crean con el estado `ACTIVO` y pueden cambiar al estado `CANCELADO` con la opción correspondiente.

### Generación de tickets

Cada vez que registro un pedido, mi sistema crea automáticamente un archivo TXT dentro de la carpeta `tickets`.

El ticket tiene la información principal de la compra:

- Número y fecha del pedido.
- Nombre del cliente.
- Producto.
- Precio unitario.
- Cantidad.
- Total.
- Estado.

Los archivos pueden identificarse con nombres como:

```text
ticket_pedido_1.txt
ticket_pedido_2.txt
```

### Consulta web con Flask

Desarrollé una interfaz web para consultar pedidos con su número.

Cuando el pedido existe, la página muestra:

- Número de pedido.
- Cliente.
- Producto.
- Precio unitario.
- Cantidad.
- Total.
- Estado.
- Fecha de registro.

Si el número que se ingresó no corresponde a un pedido almacenado, la página muestra un mensaje de que no se encontró el registro.

## Tecnologías que utilicé

- Python 3.
- SQLite.
- Flask.
- Pytest.
- HTML5.
- CSS3.
- Git y GitHub.
- Visual Studio Code.

## Organización del código

Organicé el proyecto en distintos módulos para separar las responsabilidades de la aplicación y hacer más fácil su lectura.

### `database`

Contiene la configuración de SQLite, la creación de las tablas y la función utilizada para obtener conexiones a la base de datos.

Mi aplicación trabaja con tres tablas:

- `clientes`
- `menu`
- `pedidos`

### `modelos`

Contiene las clases principales del sistema:

- `EntidadBase`: clase para compartir atributos y aplicar herencia.
- `Cliente`: organiza las operaciones relacionadas con los clientes.
- `Menu`: organiza los productos y sus precios.
- `Pedido`: registra, consulta, lista y cancela pedidos.

Las clases tienen métodos para realizar las operaciones correspondientes sobre la base de datos.

### `servicios`

Contiene la lógica encargada de generar los tickets de consumo en archivos TXT. Decidí separar esta función para no colocar responsabilidades extra dentro de la clase `Pedido`.

### `templates` y `static`

Estas carpetas contienen la interfaz web:

- `templates` almacena el documento HTML utilizado por Flask.
- `static/css` contiene los estilos visuales de la página.

### `tests`

Contiene las pruebas automatizadas de los modelos y de la consulta web. Las pruebas utilizan una base de datos temporal para evitar modificaciones en la información real de mi aplicación.

## Base de datos

La base de datos se crea automáticamente cuando ejecuto el proyecto por primera vez. No es necesario instalar un servidor de base de datos adicional, pues SQLite forma parte de Python.

Las relaciones entre los registros comprueban que todo pedido se encuentre asociado con un cliente y un producto existentes.

## Requisitos

Para ejecutar mi proyecto se necesita:

- Python 3.8 o una versión posterior.
- `pip`.
- Un entorno virtual de Python, lo recomiendo para aislar las dependencias.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/chgiselle0210/happy-burger-python.git
```

### 2. Entrar en la carpeta del proyecto

```bash
cd happy-burger-python
```

### 3. Crear el entorno virtual

```bash
python -m venv .venv
```

### 4. Activar el entorno virtual

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

En la consola de comandos de Windows:

```cmd
.venv\Scripts\activate.bat
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

### 5. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

## Ejecución de la aplicación de consola

Con el entorno virtual activado, ejecuto:

```bash
python main.py
```

Mi programa muestra el menú principal:

```text
1. Pedidos
2. Clientes
3. Menú
4. Salir
```

Desde estas opciones puedo acceder a cada uno de los módulos administrativos.

## Ejecución de la interfaz web

Para iniciar mi aplicación Flask, ejecuto:

```bash
python app.py
```

Después abro la siguiente dirección en el navegador:

```text
http://127.0.0.1:5000
```

En la página puedo introducir un número de pedido y consultar la información guardada en SQLite.

Para detener el servidor utilizo `Ctrl + C` en la terminal.

## Pruebas automatizadas

Agregué pruebas con Pytest para comprobar las operaciones principales sin alterar la base de datos que utiliza mi aplicación.

Las pruebas revisan:

- Registro, consulta, actualización y eliminación de clientes.
- Registro, consulta, actualización y eliminación de productos.
- Registro de pedidos.
- Cálculo del total.
- Generación del ticket TXT.
- Cancelación de pedidos.
- Consulta web de pedidos existentes.
- Respuesta de la página ante pedidos inexistentes.

Para ejecutar las pruebas utilizo:

```bash
python -m pytest -v
```

El resultado esperado es:

```text
6 passed
```

## Resultado final

Con este proyecto junté en una sola aplicación los principales temas que estudié durante el bootcamp. Mi sistema funciona tanto desde la consola como desde una interfaz web, conserva la información en SQLite y genera tickets para los pedidos registrados.

La organización por módulos me ayudó a mantener separadas la conexión con la base de datos, las clases del sistema, la generación de archivos, la interfaz web y las pruebas. Cada parte la pude comprobar de forma independiente gracias a esto último.

## Autora

Giselle Cantú Chávez

Proyecto final del bootcamp Programación con Python nivel avanzado del certificado FullStack Developer de Tecmilenio.