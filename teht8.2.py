import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='Assi',
    autocommit=True
)

#määritelty kysely
maakoodi = input("Anna lentoaseman maakoodi:\n"
"> ")
sql = "SELECT type, count(*) FROM airport WHERE iso_country = '" + maakoodi + "' group by type"
print(sql)

#suositetaan kysely
kursori = yhteys.cursor()
kursori.execute(sql)

#haetaan ja käsitellään tulosrivit
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")