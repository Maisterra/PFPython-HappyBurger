#Módulo de clientes
import sqlite3



class BaseDatosClientes:
    def __init__(self, nombre_archivo="clientes.db"):
        self.nombre_archivo = nombre_archivo
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()

    def crear_tabla_clientes(self):
        # Crear una tabla de clientes si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes 
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                clave TEXT NOT NULL,
                                nombre TEXT NOT NULL,
                                direccion TEXT NOT NULL,
                                email TEXT NOT NULL,
                                telefono TEXT NOT NULL
                                );''')
        self.conexion.commit()

    def agregar_cliente(self, clave, nombre, direccion, email, telefono):
        # Agregar un cliente a la tabla
        self.cursor.execute("INSERT INTO clientes (clave, nombre, direccion, email, telefono) VALUES (?,?,?,?,?)",
                            (clave, nombre, direccion, email, telefono))
        self.conexion.commit()

    def obtener_clientes(self):
        # Obtener todos los clientes de la tabla
        self.cursor.execute("SELECT * FROM clientes")
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        # Cerrar la conexión a la base de datos
        self.conexion.close()

def pedir_datos_cliente():
    clave = input("Ingrese la clave del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    email = input("Ingrese el email del cliente: ")
    telefono = input("Ingrese el telefono del cliente: ")
    return clave, nombre, direccion, email, telefono




    #Menu de funcionalidad de la base de datos

def mostrar_lista_clientes(base_datos_clientes):
    clientes = base_datos_clientes.obtener_clientes()
    print("Lista de clientes:")
    for cliente in clientes:
        print(cliente)

def agregar_cliente(base_datos_clientes):
    clave, nombre, direccion, email, telefono = pedir_datos_cliente()
    base_datos_clientes.agregar_cliente(clave, nombre, direccion, email, telefono)
    print("Cliente agregado correctamente.")

def modificar_cliente(base_datos_clientes):
    clave = input("Ingrese la clave del cliente que desea modificar: ")
    
    # Solicitar los nuevos datos del cliente
    nueva_clave = input("Ingrese la nueva clave del cliente: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
    nueva_direccion = input("Ingrese la nueva dirección del cliente: ")
    nuevo_email = input("Ingrese el nuevo email del cliente: ")
    nuevo_telefono = input("Ingrese el nuevo teléfono del cliente: ")
    
    # Actualizar los datos del producto en la base de datos
    base_datos_clientes.cursor.execute("UPDATE clientes SET clave=?, nombre=?, direccion=?,email=?, telefono=? WHERE clave=?",
                                   (nueva_clave, nuevo_nombre, nueva_direccion, nuevo_email, nuevo_telefono, clave))
    base_datos_clientes.conexion.commit()
    print("Cliente modificado correctamente.")
    


def eliminar_cliente(base_datos_clientes):
    clave = input("Ingrese la clave del cliente que desea eliminar: ")
    base_datos_clientes.cursor.execute("DELETE FROM clientes WHERE clave=?", (clave,))
    base_datos_clientes.conexion.commit()
    print("Cliente eliminado correctamente.")


def mostrar_menu():
    print("Menú:")
    print("1. Ver lista de clientes")
    print("2. Agregar cliente")
    print("3. Modificar cliente por clave")
    print("4. Eliminar cliente por clave")
    print("5. Salir")

def main():
    base_datos_clientes = BaseDatosClientes()
    base_datos_clientes.crear_tabla_clientes()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_lista_clientes(base_datos_clientes)
        elif opcion == '2':
            agregar_cliente(base_datos_clientes)
        elif opcion == '3':
            modificar_cliente(base_datos_clientes)
        elif opcion == '4':
            eliminar_cliente(base_datos_clientes)
        elif opcion == '5':
            print("Hasta luego!!!!.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    base_datos_clientes.cerrar_conexion()

if __name__ == "__main__":
    main()


