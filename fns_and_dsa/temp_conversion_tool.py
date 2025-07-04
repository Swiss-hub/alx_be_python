FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
  temp_input = input("Enter the temperature to convert: ")
  try:
      temp = float(temp_input)
  except ValueError:
     raise ValueError("Invalid temperature. Please enter a numeric value.")
  
  unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
  if unit == "F":
      celsius = convert_to_celsius(temp)
      print(f"{temp} °F is {celsius}°C")
  elif unit == "C":
      fahrenheit = convert_to_fahrenheit(temp)
      print(f"{temp}°C is {fahrenheit}°F")
  else:
      print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()













# The .strip() method in Python removes any leading (spaces at the beginning) 
# and trailing (spaces at the end) whitespace characters from a string. 
# This helps clean up user input or text data.

# Example:

# text = "   hello world   "
# cleaned = text.strip()
# print(cleaned)  # Output: "hello world"

# It can also remove other specified characters if you provide them 
# as an argument (e.g., .strip(".,!")).