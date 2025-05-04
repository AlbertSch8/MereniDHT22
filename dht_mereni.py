dht_mereni.py

import time
import board
import adafruit_dht
import sqlite3
import datetime
from datetime import datetime

# Sensor data pin is connected to GPIO 4
sensor = adafruit_dht.DHT22(board.D4)
#sensor = adafruit_dht.DHT11(board.D4)
#now = datetime.datetime.now()
#con = sqlite3.connect('bertiho_db')
try:
        # Print the values to the serial port
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity
        print("{0:%c}  Temp={1:0.1f}ºC, Temp={2:0.1f}ºF, Humidity={3:0.1f}%".format(datetime.now(),temperature_c, temperature_f, humidity))

except RuntimeError as error:
        print(error.args[0])
except Exception as error:
        sensor.exit()

        raise error

# Connect to a database
connection = sqlite3.connect('/opt/bertiho_db')

try:
    # Database operations
    print("Pokus o zapis do DB bertiho_db a tabulky mereniDHT22")
    connection.execute("INSERT INTO mereniDHT22 (teplota, vlhkost) VALUES (?, ?)", (temperature_c, humidity))
    connection.commit()
    connection.close()
    # ...
except sqlite3.Error as e:
    # Handle the exception
    print(f"An error occurred: {e}")
