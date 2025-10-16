
def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Parameters:
    - fahrenheit (float): Temperature in Fahrenheit.
    
    Returns:
    - float: Temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
  
# Main program
if __name__ == "__main__":
    try:
        fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
        celsius_output = fahrenheit_to_celsius(fahrenheit_input)
        print(f"Temperature in Celsius: {celsius_output:.2f} °C")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
      # In case of typing error. Supports numeric values ONLY.
