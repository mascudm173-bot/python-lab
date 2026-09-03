from utils import square, is_even, celsius_to_fahrenheit


def main():
    try:
        user_input = input("Enter a number: ")
        number = float(user_input)

        print(f"Square: {square(number)}")
        print(f"Is even: {is_even(number)}")
        print(f"Fahrenheit: {celsius_to_fahrenheit(number)}°F")
    except ValueError:
        print("Error: Please enter a valid numerical value.")


if __name__ == "__main__":
    main()
