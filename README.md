# myBank
Proyecto del curso **Python** de la plataforma Coderhouse.
<p>
myBank es un proyecto en Django que posee una aplicación "/myBankApp" para la gestión de la base de datos de un banco.
La app cuenta con varias vistas que poseen las siguientes funciones.
</p>

- Inicio: Homepage de la app.
- Clientes: Dar de alta un nuevo cliente.
- Cuentas: Crear una nueva cuenta en la base de datos del banco.
- Nómina: Agregar un nuevo empleado a la nómina del banco.
- Buscar Cuenta: Buscar en la base de datos una cuenta existente en función del número de cuenta asociado.
- Listar Clientes: Posee el CRUD del modelo "Clientes", donde podemos crear, leer, editar y eliminar un cliente de la base de datos.
- Panel Admin: Muestra el panel de administración de Django.
- Acerca De: Información personal y de la aplicación web.
- Iniciar Sesión: Login de usuario.
- Registrarse: Creación de un nuevo usuario.

Para poder interactuar con la base de datos, es necesario estar logueado con algun usuario.
La app cuenta con el siguiente superuser:

- User: admin
- Password: calabro1234

Cuando un usuario está logueado, en el Header se visualiza el username y un botón para poder editar dicho usuario.

Próximas features:
- Búsquedas en la base de datos para todos los modelos.
- CRUD de todos los modelos.
- Upgrade del frontend.

Clónatelo!
``
git clone https://github.com/nicolascalabro/myBank.git
``