import time
from user import User
from product import Product

def display_admin_menu():
    """Displays the admin menu and handles admin operations."""
    while True:
        print("\n" + "=" * 50)
        print(" " * 12 + "Admin Menu".center(26) + " ")
        print("=" * 50)
        print("| 1. Add Product".ljust(48) + "|")
        print("| 2. Update Product".ljust(48) + "|")
        print("| 3. Delete Product".ljust(48) + "|")
        print("| 4. View Products".ljust(48) + "|")
        print("| 5. Logout".ljust(48) + "|")
        print("=" * 50)

        choice = input("Choose an option: ")

        if choice == '1':
            print("\nAdding a New Product".center(50, "-"))
            try:
                product_id = input("Enter Product ID: ")
                name = input("Enter Product Name: ")
                category = input("Enter Product Category: ")
                price = float(input("Enter Product Price: "))
                stock_quantity = int(input("Enter Stock Quantity: "))
                product = Product(product_id, name, category, price, stock_quantity)
                Product.add_product(product)
                print("\n✅ Product added successfully!")
            except ValueError:
                print("❌ Invalid input! Ensure price and stock are numbers.")

        elif choice == '2':
            print("\nUpdating a Product".center(50, "-"))
            product_id = input("Enter Product ID to update: ")
            name = input("Enter New Name (leave blank to keep current): ")
            category = input("Enter New Category (leave blank to keep current): ")
            price = input("Enter New Price (leave blank to keep current): ")
            stock_quantity = input("Enter New Stock Quantity (leave blank to keep current): ")

            Product.update_product(
                product_id,
                name=name if name else None,
                category=category if category else None,
                price=float(price) if price else None,
                stock_quantity=int(stock_quantity) if stock_quantity else None
            )
            print("\n✅ Product updated successfully!")

        elif choice == '3':
            print("\nDeleting a Product".center(50, "-"))
            product_id = input("Enter Product ID to delete: ")
            Product.delete_product(product_id)
            print("\n✅ Product deleted successfully!")

        elif choice == '4':
            print("\nViewing All Products".center(50, "-"))
            Product.view_products()

        elif choice == '5':
            print("\nLogging out...".center(50))
            time.sleep(1)  # Pause to simulate logout
            break

        else:
            print("❌ Invalid choice. Please select again.")

def display_user_menu():
    """Displays the user menu with view-only access."""
    print("\n" + "=" * 50)
    print(" " * 12 + "User Menu".center(26) + " ")
    print("=" * 50)
    print("Viewing all products:")
    print("-" * 50)
    Product.view_products()

def main():
    """Main function to start the IMS and handle user login and role-based access."""
    while True:
        print("=" * 50)
        print(" Welcome to the Inventory Management System ".center(50, "="))
        print("=" * 50)
        
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        # Simulating processing for better user experience
        print("\nAuthenticating...", end="")
        time.sleep(1)  # Short pause for realism

        user = User(email, password)
        if user.login():
            print(f"\n✅ Login successful! Welcome, {user.role.capitalize()}.")
            if user.role == 'admin':
                display_admin_menu()
            elif user.role == 'user':
                display_user_menu()
        else:
            print("\n❌ Login failed. Please check your credentials and try again.")
            time.sleep(1)  # Pause to allow user to read the message

if __name__ == "__main__":
    main()
