import time  # For adding delays to improve user experience

# Step 1: Define the menu as a dictionary
menu = {
    'a': {'name': 'Chicken Biryani', 'price': 300},
    'b': {'name': 'Raita', 'price': 50},
    'c': {'name': 'Coke', 'price': 60},
    'd': {'name': 'Seekh Kabab', 'price': 150},
    'e': {'name': 'Paratha', 'price': 40}
}

# Step 2: Function to display the menu
def display_menu():
    print("\nPlease select from the following menu:")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - Rs. {item['price']}")
    print()

# Step 3: Function to take an order
def take_order():
    order = []  # List to store the user's order
    while True:
        display_menu()
        choices = input("Enter the letters corresponding to your choices (e.g., 'a b c', or 'done' to finish): ").lower()

        if choices == 'done':
            if order:  # Exit only if there are items in the order
                break
            else:
                print("You haven't ordered anything yet. Please select an item before finishing.")
                continue

        # Split the input into individual choices (by spaces or commas)
        choices = choices.replace(",", " ").split()

        valid_item_added = False  # Flag to track if at least one valid item was added

        for choice in choices:
            if choice not in menu:  # Check if the input is valid
                print(f"Invalid choice: {choice}. Please select valid options from the menu.")
                continue

            item = menu[choice]
            try:
                quantity = int(input(f"How many {item['name']} would you like to order? "))
                if quantity <= 0:  # Ensure quantity is valid
                    print("Please enter a valid quantity greater than 0.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            # Add the item to the order
            subtotal = item['price'] * quantity
            order.append({'name': item['name'], 'price': item['price'], 'quantity': quantity, 'subtotal': subtotal})
            valid_item_added = True  # Set the flag to True

        if valid_item_added:
            print("Items added to your order!\n")  # Only display this if valid items were added

        # Ask if the user wants to add more items
        add_more = input("Do you want to add more items? (yes/no): ").lower()
        if add_more != 'yes':
            break

    return order

# Step 4: Function to calculate and display the bill
def display_bill(order):
    if not order:
        print("\nYou have not ordered anything. Thank you for visiting!")
        return
    
    print("\nYour Order Summary:")
    total = 0
    for idx, item in enumerate(order, 1):
        print(f"{idx}. {item['name']} x{item['quantity']} = Rs. {item['subtotal']}")
        total += item['subtotal']

    print("----------------------------")
    print(f"Total: Rs. {total}")
    print("----------------------------\n")
    time.sleep(1)

# Step 5: Function to collect a review
def collect_review():
    print("\nThank you for dining with us!")
    review = input("How was your experience with the food? Please leave a review: ")
    print("\nThank you for your feedback!")
    time.sleep(1)
    return review

# Step 6: Main program
def main():
    print("Welcome to Desi Tadka - A Taste of Pakistan!")
    time.sleep(1)

    # Step 6.1: Take the user's order
    order = take_order()  
    
    # Step 6.2: Collect the user's review after placing the order
    collect_review()
    
    # Step 6.3: Display the final bill
    display_bill(order)
    
    # Step 6.4: Thank the user
    print("Thank you for visiting Desi Tadka! We hope to see you again soon. Have a great day!")

# Run the program
if __name__ == "__main__":
    main()
