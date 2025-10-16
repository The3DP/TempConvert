# REVISED Code
def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Parameters:
    - fahrenheit (float): Temperature in Fahrenheit.
    
    Returns:
    - float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Parameters:
    - celsius (float): Temperature in Celsius.
    
    Returns:
    - float: Temperature in Fahrenheit.
    """
    return (celsius * 9 / 5) + 32

def main():
    while True:
        print("\n--- Temperature Converter ---")
        print("1. Convert Fahrenheit to Celsius")
        print("2. Convert Celsius to Fahrenheit")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            try:
                f = float(input("Enter temperature in Fahrenheit: "))
                c = fahrenheit_to_celsius(f)
                print(f"{f:.2f} °F is {c:.2f} °C")
            except ValueError:
                print("❌ Invalid input. Please enter a numeric value.")
        
        elif choice == '2':
            try:
                c = float(input("Enter temperature in Celsius: "))
                f = celsius_to_fahrenheit(c)
                print(f"{c:.2f} °C is {f:.2f} °F")
            except ValueError:
                print("❌ Invalid input. Please enter a numeric value.")
        
        elif choice == '3':
            print("Goodbye! ❄️🔥")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
