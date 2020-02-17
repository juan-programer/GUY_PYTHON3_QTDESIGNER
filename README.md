# GUY_PYTHON3_QTDESIGNER
INTERFAZ DE USUARIO INTERACTIVA
ESTA  APLICACION PERMITE CALCULAR LOS CABALLOS DE POTENCIA DE UNA CONDENSADORA APARTIR DE SU MEDIDA Y NUMERO DE CODOS.

DOCUMENTACION DEL SOFTWARE:

En este código:  crear_db.py

Primero, definimos una función llamada crear_conexion() que se conecta a una base de datos SQLite especificada por el archivo de base de datos db_file . Dentro de la función, llamamos a la función connect() del módulo sqlite3.

La función connect() abre una conexión a una base de datos SQLite. Devuelve un objeto Connection que representa la base de datos. Al usar el objeto Connection , puede realizar varias operaciones de base de datos.

En caso de que ocurra un error, lo detectamos dentro del try except bloque y mostramos el mensaje de error. Si todo está bien, mostramos el "CONNECION EXITOSA" por consola.

Es una buena práctica de programación que siempre debe cerrar la conexión de la base de datos cuando la complete.

En segundo lugar, pasamos la ruta del archivo de la base de datos a la función crear_conexion() para crear la base de datos. Tenga en cuenta que el prefijo r en la r"C:\sqlite\db\Condesadora.db" indica a Python que estamos pasando una cadena sin formato.

Ejecutemos el programa y verifiquemos la carpeta que creamos aver si hay un archivo con extencion.db
