import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='Assi',
    autocommit=True
)

from geopy import distance

def getairport_distance(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident='" + icao + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

airport1 = input("Syötä ensimmäisen lentokentän ICAO: ")
airport1_results = getairport_distance(airport1)
airport2 = input("Syötä toisen lentokentän ICAO: ")
airport2_results = getairport_distance(airport2)

print(f"Lentokenttien välinen etäisyys on {distance.distance(airport1_results, airport2_results).km:.2f} kilometriä.")