# Import date module
from datetime import date

# Define header function
def header():
    print("Name: LastName, FirstName")
    print("Course: CourseNumber")
    print("Assignment: Lab 3.4 - Python Variables and Operators")
    print("Current Date:", date.today())

    print("\n" * 5)


# Dictionary named 'assets' for cybersecurity assets
assets = {}

# Define add_asset function
def add_asset(name, quantity, asset_type, vendor):
    assets[name] = {
        "name": name,
        "quantity": quantity,
        "type": asset_type,
        "vendor": vendor
    }

    print("\nAsset added successfully!")


# Define update_quantity function
def update_quantity(name, quantity):
    assets[name]["quantity"] = quantity
    print("\nAsset updated successfully!\n")


# Define search_asset function
def search_asset(name):
    asset = assets[name]
    print("\nAsset Details:")
    print("Name:", asset["name"])
    print("Quantity:", asset["quantity"])
    print("Type:", asset["type"])
    print("Vendor:", asset["vendor"])
    print()


# Define generate_report function
def generate_report():
    print("\nAsset Report:")
    print("--------------------------------------")

    if not assets:
        print("No assets are currently stored.")
        print("--------------------------------------")
        return
    for name, asset in assets.items():
        print("Asset:", name)
        print("Quantity:", asset["quantity"])
        print("Type:", asset["type"])
        print("Vendor:", asset["vendor"])
        print("--------------------------------------")


# Define main program function
def main():
    header()

    while True:
        print("\n\n=== Cybersecurity Asset Management ===\n\n")
        print("1. Add an asset")
        print("2. Update asset quantity")
        print("3. Search for an asset")
        print("4. Generate asset report")
        print("5. Exit\n")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\n=== Add Asset ===\n")
            name = input("Enter the name of the asset: ")

            if name in assets:
                print("\nAn asset with that name already exists. Please try again.")
                continue

            try:
                quantity = int(input("Enter the quantity of the asset: "))
                if quantity < 0:
                    print("\nQuantity cannot be negative.")
                    continue
            except ValueError:
                print("\nQuantity must be a valid integer.")
                continue

            asset_type = input("Enter the type of asset (e.g., device, software, tool): ")

            vendor = input("Enter the vendor or manufacturer of the asset: ")

            add_asset(name, quantity, asset_type, vendor)

        elif choice == "2":
            print("\n=== Update Asset Quantity ===\n")
            name = input("Enter the name of the asset: ")

            if name not in assets:
                print("\nAn asset with that name does not exist.\n")
                continue

            try:
                quantity = int(input("Enter the new quantity for that asset: "))
                if quantity < 0:
                    print("\nQuantity cannot be negative.")
                    continue
            except ValueError:
                print("\nQuantity must be a valid integer.")
                continue

            update_quantity(name, quantity)

        elif choice == "3":
            print("\n=== Search Asset ===\n")
            name = input("Enter the name of the asset: ")

            if name not in assets:
                print("\nAn asset with that name does not exist.\n")
                continue
            search_asset(name)

        elif choice == "4":
            print("\n=== Generate Asset Report===\n")
            generate_report()

        elif choice == "5":
            print("\nExiting the program...\n")
            break
        else:
            print("\nThat option has not been configured yet.\n")


# Call the main program
main()
        

