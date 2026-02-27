from Calculator import add, sub, mul, div

def read_number(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Entrada inválida. Escribe un número (ej. 3, 3.5, -2).")

def read_option() -> str:
    valid = {"1", "2", "3", "4", "0"}
    while True:
        opt = input("Elige una opción: ").strip()
        if opt in valid:
            return opt
        print("Opción inválida.")

def main() -> None:
    while True:
        print("\n=== Calculadora simple ===")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("0) Salir")

        option = read_option()
        if option == "0":
            print("Saliendo...")
            break

        a = read_number("Ingresa el primer número: ")
        b = read_number("Ingresa el segundo número: ")

        try:
            if option == "1":
                result = add(a, b)
                op_name = "Suma"
            elif option == "2":
                result = sub(a, b)
                op_name = "Resta"
            elif option == "3":
                result = mul(a, b)
                op_name = "Multiplicación"
            else:  # "4"
                result = div(a, b)
                op_name = "División"

            print(f"{op_name}: {result}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()