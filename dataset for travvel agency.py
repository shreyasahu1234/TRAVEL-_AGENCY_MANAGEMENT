import random
import datetime

def generate_flight_data(num_records=500):
    """
    Generates a list of mock flight data records.
    Each record contains all necessary fields for a Flight object.
    """
    cities = [
        "JFK (New York)", "LAX (Los Angeles)", "ORD (Chicago)", "ATL (Atlanta)",
        "LHR (London)", "CDG (Paris)", "HND (Tokyo)", "DXB (Dubai)",
        "SYD (Sydney)", "AMS (Amsterdam)", "BOM (Mumbai)", "GRU (Sao Paulo)"
    ]
    airlines = ["AA", "DL", "UA", "BA", "AF", "LH", "EK", "SQ"]
    flights = []
    
    start_date = datetime.datetime.now() + datetime.timedelta(days=1)
    
    print(f"--- GENERATING {num_records} MOCK FLIGHT RECORDS ---")
    print("FlightNumber,Origin,Destination,DepartureTime,Price,SeatsAvailable")
    print("-------------------------------------------------------------------")

    for i in range(1, num_records + 1):
        # 1. Generate Flight Number
        airline_code = random.choice(airlines)
        flight_num = f"{airline_code}{random.randint(100, 999)}"
        
        # 2. Generate Route
        origin = random.choice(cities)
        destination = random.choice([c for c in cities if c != origin])
        
        # 3. Generate Departure Time (random time within the next 30 days)
        days_in_future = random.randint(1, 30)
        time_offset = datetime.timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
        dep_time = start_date + datetime.timedelta(days=days_in_future) + time_offset
        dep_time_str = dep_time.strftime('%Y-%m-%d %H:%M')
        
        # 4. Generate Price (higher for longer/international routes)
        if len(origin) == len(destination): # Simple proxy for distance
            base_price = random.uniform(200.00, 800.00)
        else:
            base_price = random.uniform(450.00, 1500.00)
        
        # 5. Generate Seats
        max_seats = random.choice([150, 200, 250])
        seats_available = random.randint(10, max_seats)
        
        # Print the record (CSV format)
        record = (f"{flight_num},{origin},{destination},{dep_time_str},"
                  f"{base_price:.2f},{seats_available}")
        print(record)
        flights.append(record)
    
    print("-------------------------------------------------------------------")
    print(f"--- Finished generating {len(flights)} records. ---")
    return flights

if __name__ == "__main__":
    generate_flight_data()
import random
import datetime

def generate_flight_data(num_records=500):
    """
    Generates a list of mock flight data records.
    Each record contains all necessary fields for a Flight object.
    """
    cities = [
        "JFK (New York)", "LAX (Los Angeles)", "ORD (Chicago)", "ATL (Atlanta)",
        "LHR (London)", "CDG (Paris)", "HND (Tokyo)", "DXB (Dubai)",
        "SYD (Sydney)", "AMS (Amsterdam)", "BOM (Mumbai)", "GRU (Sao Paulo)"
    ]
    airlines = ["AA", "DL", "UA", "BA", "AF", "LH", "EK", "SQ"]
    flights = []
    
    start_date = datetime.datetime.now() + datetime.timedelta(days=1)
    
    print(f"--- GENERATING {num_records} MOCK FLIGHT RECORDS ---")
    print("FlightNumber,Origin,Destination,DepartureTime,Price,SeatsAvailable")
    print("-------------------------------------------------------------------")

    for i in range(1, num_records + 1):
        # 1. Generate Flight Number
        airline_code = random.choice(airlines)
        flight_num = f"{airline_code}{random.randint(100, 999)}"
        
        # 2. Generate Route
        origin = random.choice(cities)
        destination = random.choice([c for c in cities if c != origin])
        
        # 3. Generate Departure Time (random time within the next 30 days)
        days_in_future = random.randint(1, 30)
        time_offset = datetime.timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
        dep_time = start_date + datetime.timedelta(days=days_in_future) + time_offset
        dep_time_str = dep_time.strftime('%Y-%m-%d %H:%M')
        
        # 4. Generate Price (higher for longer/international routes)
        if len(origin) == len(destination): # Simple proxy for distance
            base_price = random.uniform(200.00, 800.00)
        else:
            base_price = random.uniform(450.00, 1500.00)
        
        # 5. Generate Seats
        max_seats = random.choice([150, 200, 250])
        seats_available = random.randint(10, max_seats)
        
        # Print the record (CSV format)
        record = (f"{flight_num},{origin},{destination},{dep_time_str},"
                  f"{base_price:.2f},{seats_available}")
        print(record)
        flights.append(record)
    
    print("-------------------------------------------------------------------")
    print(f"--- Finished generating {len(flights)} records. ---")
    return flights

if __name__ == "__main__":
    generate_flight_data()
