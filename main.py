import obd

# future plans: integrate TPMS with RTL-SDR readings.

# Initialize the OBDII interface.
connection = obd.OBD()

# Load callsign from disk. This is important when using amateur frequencies.
try:
    callsign = open('callsign.txt', 'r')
except FileNotFoundError:
    callsign = "N/A"

while True:
    speed = connection.query(obd.commands.SPEED)
    rpm = connection.query(obd.commands.RPM)
    throttle_position = connection.query(obd.commands.RELATIVE_THROTTLE_POS)  # Subject to change with future testing.
    coolant_temp = connection.query(obd.commands.COOLANT_TEMP)
    fuel_level = connection.query(obd.commands.FUEL_LEVEL)
    output = f"SPEED {speed.mph} MPH RPM {rpm} THROTTLEPOS {throttle_position} TEMP {coolant_temp} FUEL_LEVEL {fuel_level} CALLSIGN {callsign}"

    # send to netcat listener on pit laptop
