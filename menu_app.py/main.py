# Función para agregar una compra a la lista
def agregar_compra(compras):
    monto_compra = float(input("Ingrese el monto de la compra: "))
    compras.append(monto_compra)
    print("Compra agregada correctamente.")
    return monto_compra

# Función para mostrar las compras realizadas
def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        for i, compra in enumerate(compras, start=1):
            print(f"Compra {i}: ${compra:.2f}")

#Función para mostrar el total gastado
def mostrar_total(total_gastado):
    print(f"Total gastado: ${total_gastado:.2f}")


#Función principal
def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Selecione una opción: ")

        if opcion == "1":
            total_gastado += agregar_compra(compras)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion== "3":
            mostrar_total(total_gastado)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()