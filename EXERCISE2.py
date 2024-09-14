import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="POOH",
    database="flight_game",
    collation="utf8mb4_general_ci"
)

cursor = conn.cursor()

if conn.is_connected():
    print("Connected to MariaDB")

def main():

    areaCode = input("Enter the Area code :").upper()
    selectQuery = ("SELECT ap.type as airportType,count(ap.ident) as airportCount,c.name as countryName"
                    " FROM airport ap "
                    " join country c on ap.iso_country = c.iso_country "
                    " where ap.iso_country = %s group by ap.type order by ap.type ")
    cursor.execute(selectQuery, (areaCode,))

    result = cursor.fetchall()

    if result:
        country_data = {}

        # Process the result array
        for entry in result:
            airport_type, airport_count, country_name = entry

            if country_name not in country_data:
                country_data[country_name] = []

            country_data[country_name].append(f"{airport_count} {airport_type}")

        # Print the formatted output
        for country, types in country_data.items():
            print(f"{country} has {', '.join(types)}")
    else:
        print(f"No data found for area code {areaCode}.")

    cursor.close()
    conn.close()

main()
