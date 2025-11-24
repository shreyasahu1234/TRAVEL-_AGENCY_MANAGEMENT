import datetime
from manager import TravelAgencyManager

def initialize_agency(manager):
    """Sets up initial data for demonstration."""
    now = datetime.datetime.now()
    # Schedule flights for one and two weeks in the future
    one_week = now + datetime.timedelta(days=7)
    two_weeks = now + datetime.timedelta(days=14)

    # Add initial flights
    manager.add_flight("UA101", "NYC", "LAX", one_week.strftime('%Y-%m-%d 08:00'), 450.00, 150)
    manager.add_flight("AA202", "LAX", "MIA", one_week.strftime('%Y-%m-%d 14:30'), 320.00, 80)
    manager.add_flight("DL303", "ATL", "SFO", two_weeks.strftime('%Y-%m-%d 10:00'), 510.50, 45)
    manager.add_flight("SW404", "DEN", "ORD", two_weeks.strftime('%Y-%m-%d 16:00'), 180.00, 5)

    # Add initial customers
    manager.add_customer("Alice Johnson", "alice@example.com") # ID 1001
    manager.add_customer("Bob Smith", "bob@example.com")       # ID 1002

    print("\n--- Agency Initialized with sample data ---")

def main():
    """Main function to run the travel agency manager demo and CLI."""
    manager = TravelAgencyManager()
    initialize_agency(manager)

    while True:
        print("\n==============================================")
        print("    ✈️ TRAVEL AGENCY MANAGEMENT SYSTEM MENU ✈️")
        print("==============================================")
        print("1. List Available Flights")
        print("2. List All Customers")
        print("3. Create New Customer")
        print("4. Create Booking")
        print("5. List All Bookings")
        print("6. Cancel Booking")
        print("7. Exit")
        print("----------------------------------------------")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            manager.list_available_flights()

        elif choice == '2':
            manager.list_all_customers()

        elif choice == '3':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            manager.add_customer(name, email)

        elif choice == '4':
            try:
                # Use input().strip() to remove any accidental spaces
                customer_id = int(input("Enter Customer ID for booking: "))
                flight_number = input("Enter Flight Number (e.g., UA101) to book: ")
                passengers = int(input("Enter number of passengers: "))
                manager.create_booking(customer_id, flight_number.strip(), passengers)
            except ValueError:
                print("❌ Invalid input. Customer ID or Passengers must be a number.")
            except Exception as e:
                print(f"❌ An unexpected error occurred: {e}")

        elif choice == '5':
            manager.list_all_bookings()

        elif choice == '6':
            try:
                booking_id = int(input("Enter Booking ID to cancel: "))
                manager.cancel_booking(booking_id)
            except ValueError:
                print("❌ Invalid input for Booking ID. Please enter a number.")

        elif choice == '7':
            print("\nThank you for using the Travel Agency Manager. Happy travels! 👋")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
