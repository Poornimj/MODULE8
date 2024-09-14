from geopy.distance import geodesic
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
    ICAOCode = input("Enter the ICAO code :").upper()
    selectQuery = ("SELECT ap.latitude_deg as la_deg,ap.longitude_deg as lo_deg, c.name as country_name"
                   " FROM airport ap "
                   " join country c on ap.iso_country = c.iso_country "
                   " where ap.ident = %s ")
    cursor.execute(selectQuery, (ICAOCode,))
    result1 = cursor.fetchall()

    ICAOCode2 = input("Enter the ICAO code 2:").upper()
    selectQuery2 = ("SELECT ap.latitude_deg as la_deg,ap.longitude_deg as lo_deg, c.name as country_name"
                   " FROM airport ap "
                   " join country c on ap.iso_country = c.iso_country "
                   " where ap.ident = %s ")
    cursor.execute(selectQuery2, (ICAOCode2,))
    result2 = cursor.fetchall()

    location_1_map = ""
    location_2_map = ""
    location1_name = ""
    lcoation2_name = ""

    if result1:
        first_row = result1[0]
        latitude_deg = first_row[0]
        longitude_deg = first_row[1]
        location1_name = first_row[2]

        location_1_map = (latitude_deg, longitude_deg)
    else:
        print(f"No data found for ICAO code {ICAOCode}.")

    if result2:
        first_row = result2[0]
        latitude_deg = first_row[0]
        longitude_deg = first_row[1]
        lcoation2_name = first_row[2]

        location_2_map = (latitude_deg, longitude_deg)
    else:
        print(f"No data found for ICAO code {ICAOCode2}.")

    if location_1_map != "" and location_2_map != "":
        distance = geodesic(location_1_map, location_2_map).kilometers
        print(f"The distance between {location1_name} and {lcoation2_name} is {distance:.2f} km.")
    else:
        print("One or both locations are missing, cannot calculate the distance.")

    cursor.close()
    conn.close()

main()
