import sys
sys.path.append('src')

from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    print("--- Python Lab Program ---")
    
    # Collect name for greeting
    name_input = input("Enter your name: ")
    print(greet(name_input))
    
    try:
        user_input = float(input("Enter a number: "))
        
        sq_val = square(user_input)
        even_check = "Even" if is_even(user_input) else "Odd"
        fah_val = celsius_to_fahrenheit(user_input)
        
        print(f"Square of the number: {sq_val}")
        print(f"The number is: {even_check}")
        print(f"As Celsius, Fahrenheit equivalent is: {fah_val:.2f}°F")
        
    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    main()
