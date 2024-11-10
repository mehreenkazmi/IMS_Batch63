# main.py
import time
from user import User
from product import Product

def display_admin_menu():
    """Displays the admin menu and handles admin operations."""
    while True:
        print("\n" + "=" * 50)
        print(" Admin Options ".center(50, " "))
        print("=" * 50)
        print("| 1. Add New Product".ljust(48) + "|")
        print("| 2. Modify Product Details".ljust(48) + "|")
        print("| 3. Remove Product".ljust(48) + "|")
        print("| 4. View Current Inventory".ljust(48) + "|")
        print("| 5. Search Product".ljust(48) + "|")
        print("| 6. Log Out".ljust(48) + "|")
        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nStarting new product entry...".center(50, "-"))
            try:
                product_id = input("Enter Product ID: ")
                name = input("Enter Product Name: ")
                category = input("Enter Product Category: ")
                price = float(input("Enter Product Price: "))
                stock_quantity = int(input("Enter Stock Quantity: "))
                product = Product(product_id, name, category, price, stock_quantity)
                Product.add_product(product)
            except ValueError:
                print("❌ Please make sure to enter numbers for price and stock quantity.")

        elif choice == '2':
            print("\nPreparing to update product...".center(50, "-"))
            product_id = input("Enter Product ID to update: ")
            name = input("New Name (press Enter to keep existing): ")
            category = input("New Category (press Enter to keep existing): ")
            price = input("New Price (press Enter to keep existing): ")
            stock_quantity = input("New Stock Quantity (press Enter to keep existing): ")

            Product.update_product(
                product_id,
                name=name if name else None,
                category=category if category else None,
                price=float(price) if price else None,
                stock_quantity=int(stock_quantity) if stock_quantity else None
            )

        elif choice == '3':
            print("\nDeleting product from the system...".center(50, "-"))
            product_id = input("Enter Product ID to delete: ")
            Product.delete_product(product_id)

        elif choice == '4':
            print("\nDisplaying Inventory...".center(50, "-"))
            Product.view_products()

        elif choice == '5':
            print("\nProduct Search".center(50, "-"))
            search_term = input("Enter Product ID or Name to search: ")
            Product.search_product(search_term)

        elif choice == '6':
            print("\nLogging out. See you next time!".center(50))
            time.sleep(1)
            break

        else:
            print("Please enter a valid option (1-6).")

def display_user_menu():
    """Displays the user menu with view-only access."""
    while True:
        print("\n" + "=" * 50)
        print(" Welcome, User! ".center(50, " "))
        print("=" * 50)
        print("| 1. View All Products".ljust(48) + "|")
        print("| 2. Search Product".ljust(48) + "|")
        print("| 3. Log Out".ljust(48) + "|")
        print("=" * 50)

        choice = input("Choose an option: ")

        if choice == '1':
            print("\nDisplaying All Products".center(50, "-"))
            Product.view_products()
        
        elif choice == '2':
            print("\nProduct Search".center(50, "-"))
            search_term = input("Enter Product ID or Name to search: ")
            Product.search_product(search_term)

        elif choice == '3':
            print("\nLogging out. See you next time!".center(50))
            break

        else:
            print("Invalid option. Please select again.")

def main():
    """Main function to start the IMS and handle user login and role-based access."""
    while True:
        print("=" * 50)
        print(" Welcome to the Inventory Management System ".center(50, "="))
        print("=" * 50)
        
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        print("\nVerifying your credentials...", end="")
        time.sleep(1)

        user = User(email, password)
        if user.login():
            print(f"\n🎉 Welcome back, {user.role.capitalize()}!")
            if user.role == 'admin':
                display_admin_menu()
            elif user.role == 'user':
                display_user_menu()
        else:
            print("\n🔒 Unable to login. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
