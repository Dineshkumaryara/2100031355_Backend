import mysql.connector

# MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="zaq1mlp0",
    database="safertek1"
)
cursor = conn.cursor()


# Function to insert values into countries table
def insert_countries():
    input("---------------------Countries Table-------------------(Give country ID same for both tables)")
    country_id = input("Enter country ID: ")
    country_name = input("Enter country name: ")
    region_id = input("Enter region ID: ")
    cursor.execute("INSERT INTO countries (country_id, country_name, region_id) VALUES (%s, %s, %s)",
                   (country_id, country_name, region_id))
    conn.commit()
    print("'Inserted Successfully'")


# Function to insert values into locations table
def insert_locations():
    input("---------------------Locations Table-------------------(Give country ID same for both tables)")
    location_id = input("Enter location ID: ")
    street_address = input("Enter street address: ")
    postal_code = input("Enter postal code: ")
    city = input("Enter city: ")
    state_province = input("Enter state/province: ")
    country_id = input("Enter country ID: ")
    cursor.execute(
        "INSERT INTO locations (location_id, street_address, postal_code, city, state_province, country_id) VALUES (%s, %s, %s, %s, %s, %s)",
        (location_id, street_address, postal_code, city, state_province, country_id))
    conn.commit()

    print("'Inserted Successfully'")


# Function to search for address using JOIN
def search_address_with_join():
    country_name = input("Enter country name to search for address: ")
    cursor.execute("""
                    SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name
                    FROM locations l
                    JOIN countries c ON l.country_id = c.country_id
                    WHERE c.country_name = %s
                    """, (country_name,))
    addresses = cursor.fetchall()
    if addresses:
        for address in addresses:
            print(address)
    else:
        print("Invalid country name.")


# Function to search for address without using JOIN
def search_address_without_join():
    country_id = input("Enter country ID to search for address: ")
    cursor.execute("""
                    SELECT l.location_id, l.street_address, l.city, l.state_province, 
                           (SELECT country_name FROM countries WHERE country_id = %s) AS country_name
                    FROM locations l
                    WHERE l.country_id = %s
                    """, (country_id, country_id))
    addresses = cursor.fetchall()
    if addresses:
        for address in addresses:
            print(address)
    else:
        print("Invalid country ID.")


# Main function
def main():
    while True :
        choice = input("Would you like to insert values or search for an address? (insert/search): ").lower()
        if choice == "insert":
            insert_countries()
            insert_locations()
        elif choice == "search":
            join_choice = input("How would you like to find the address? (join/not join): ").lower()
            if join_choice == "join":
                search_address_with_join()
            elif join_choice == "not join":
                search_address_without_join()
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice.")

        continue_choice = input("Would you like to continue? (yes/no): ").lower()
        if continue_choice != "yes":
            break


# Call the main function
main()

# Close the connection
conn.close()
