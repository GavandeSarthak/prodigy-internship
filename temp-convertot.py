def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    print("Temperature Conversion Program")
    print("Supported temperature units: Celsius, Fahrenheit, Kelvin")
    temperature = float(input("Enter temperature value: "))
    unit = input("Enter original unit of measurement (C/F/K): ").upper()

    if unit == 'C':
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{temperature}°C is equal to {fahrenheit}°F and {kelvin} K")
    elif unit == 'F':
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{temperature}°F is equal to {celsius}°C and {kelvin} K")
    elif unit == 'K':
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{temperature} K is equal to {celsius}°C and {fahrenheit}°F")
    else:
        print("Invalid unit. Please enter C, F, or K.")

if __name__ == "__main__":
    main()
