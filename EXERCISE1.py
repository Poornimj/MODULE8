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

    icaoInput = input("Enter the ICAO code of the airport to fetch:").upper()
    select_query = "SELECT ap.name as airport_name,c.name as country_name FROM airport ap join country c on ap.iso_country=c.iso_country where ap.ident = %s "
    cursor.execute(select_query, (icaoInput,))

    result = cursor.fetchall()

    if result:
        first_row = result[0]
        airport_name = first_row[0]
        country_name = first_row[1]
        print(f"The airport name for ICAO code {icaoInput} is: {airport_name} and country name is :{country_name}")
    else:
        print(f"No airport found with ICAO code {icaoInput}.")

    cursor.close()
    conn.close()

main()
