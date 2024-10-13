import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

while True:
    # Display the menu to the user
    print("Choose an LED color:")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("Press 'q' to quit")

    user_input = input("Enter your choice: ")

    # Check if the user wants to quit
    if user_input.lower() == 'q':
        print("Exiting the program. Goodbye!")
        break

    try:
        # Convert the user input to an integer
        choice = int(user_input)

        # Initialize the RGB values
        red, green, blue = 0, 0, 0

        # Set the LED color based on the user's choice
        if choice == 1:
            red = 255
        elif choice == 2:
            green = 255
        elif choice == 3:
            blue = 255
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue  # Skip the loop iteration and ask for input again

        # Gradually decrease the brightness of the chosen color
        max_brightness = 255
        while max_brightness > 0:
            for i in range(10):
                cp.pixels[i] = (red * max_brightness // 255, 
                                green * max_brightness // 255, 
                                blue * max_brightness // 255)
            cp.pixels.show()
            time.sleep(0.3)

            max_brightness -= 1

    except ValueError:
        print("Invalid input. Please enter a number (1, 2, 3) or 'q' to quit.")
