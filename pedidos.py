#Módulo de pedidos
import sqlite3



class BaseDatosPedidos: 
    
    def __init__(self, nombre_archivo="pedidos.db"):
        self.nombre_archivo = nombre_archivo
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()

    def crear_tabla_pedidos(self):
        # Crear una tabla de pedidos si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos 
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                pedido INTEGER NOT NULL,
                                nombre TEXT NOT NULL,
                                producto TEXT NOT NULL,
                                precio INTEGER NOT NULL
                                );''')
        self.conexion.commit()

    def agregar_pedido(self, pedido, nombre, producto, precio):
        # Agregar un pedido a la tabla
        self.cursor.execute("INSERT INTO pedidos (pedido, nombre, producto, precio) VALUES (?,?,?,?)",
                            (pedido, nombre, producto, precio))
        self.conexion.commit()

    def obtener_pedidos(self):
        # Obtener todos los pedidos de la tabla
        self.cursor.execute("SELECT * FROM pedidos")
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        # Cerrar la conexión a la base de datos
        self.conexion.close()

def pedir_datos_pedido():
    pedido = input("Ingrese el número de pedido: ")
    nombre = input("Ingrese el nombre de la persona: ")
    producto = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    return pedido, nombre, producto, precio




    #Menu de funcionalidad de la base de datos

def mostrar_lista_productos(base_datos_pedidos):
    pedidos = base_datos_pedidos.obtener_pedidos()
    print("Lista de pedidos:")
    for pedido in pedidos:
        print(pedido)

def agregar_pedido(base_datos_pedidos):
    pedido, nombre, producto, precio = pedir_datos_pedido()
    base_datos_pedidos.agregar_pedido(pedido, nombre, producto, precio)
    print("Pedido agregado correctamente.")

def modificar_pedidos(base_datos_pedidos):
    pedido = input("Ingrese el número de pedido que desea modificar: ")
    
    # Solicitar los nuevos datos del pedido
    nuevo_pedido = input("Ingrese el nuevo número de pedido: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    nuevo_producto = input("Ingrese el nuevo producto: ")
    nuevo_precio = input("Ingrese el nuevo precio: ")
    
    # Actualizar los datos del producto en la base de datos
    base_datos_pedidos.cursor.execute("UPDATE pedidos SET pedido=?, nombre=?, producto=?, precio=? WHERE pedido=?",
                                   (nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio, pedido))
    base_datos_pedidos.conexion.commit()
    print("Pedido modificado correctamente.")
    


def eliminar_pedido(base_datos_pedidos):
    pedido = input("Ingrese el número de pedido que desea eliminar: ")
    base_datos_pedidos.cursor.execute("DELETE FROM pedidos WHERE pedido=?", (pedido,))
    base_datos_pedidos.conexion.commit()
    print("Pedido eliminado correctamente.")


def mostrar_menu():
    print("Menú:")
    print("1. Ver lista de pedidos")
    print("2. Agregar pedido")
    print("3. Modificar pedido por número de pedido")
    print("4. Eliminar pedido por número de pedido")
    print("5. Salir")

def main():
    base_datos_pedidos = BaseDatosPedidos()
    base_datos_pedidos.crear_tabla_pedidos()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_lista_productos(base_datos_pedidos)
        elif opcion == '2':
            agregar_pedido(base_datos_pedidos)
        elif opcion == '3':
            modificar_pedidos(base_datos_pedidos)
        elif opcion == '4':
            eliminar_pedido(base_datos_pedidos)
        elif opcion == '5':
            print("Hasta luego!!!!.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    base_datos_pedidos.cerrar_conexion()

if __name__ == "__main__":
    main()

