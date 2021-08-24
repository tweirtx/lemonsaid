import obd

# obd init stuff

while True:
    output = f"SPEED {speed.mph} MPH RPM {rpm} THROTTLEPOS {throttleposition} TEMP {coolant_temp} FUEL_LEVEL {fuel_level}"
    # send to netcat listener on pit laptop
