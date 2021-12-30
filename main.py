import obd

# future plans: integrate TPMS with RTL-SDR readings.

# Initialize the OBDII interface.
# Activate connection on Linux: sudo rfcomm bind rfcomm0 00:1D:A5:22:E3:FD (or other device MAC)
connection = obd.OBD()

# Load callsign from disk. This is important when using amateur frequencies.
try:
    callsign = open('callsign.txt', 'r').read()
except FileNotFoundError:
    callsign = "N/A"
    print("Callsign not set. Depending on data transfer method, this may be illegal!")

while True:
    # Read parameters from the OBDII system.
    # speed = connection.query(obd.commands.SPEED).value.to("mph") # TODO fix
    speed = 0
    rpm = connection.query(obd.commands.RPM).value
    throttle_position = connection.query(obd.commands.RELATIVE_THROTTLE_POS).value  # Subject to change with future testing. TODO determine correct
    coolant_temp = connection.query(obd.commands.COOLANT_TEMP).value
    fuel_level = connection.query(obd.commands.FUEL_LEVEL).value

    # Read tire pressures with software defined radio. TODO
    fl_psi = 30.0  # Testing value
    fr_psi = 30.0  # Testing value
    bl_psi = 30.0  # Testing value
    br_psi = 30.0  # Testing value

    # Construct data string
    output = f"SPEED {speed} MPH RPM {rpm} THROTTLEPOS {throttle_position} TEMP {coolant_temp} " \
             f"FUEL_LEVEL {fuel_level} CALLSIGN {callsign} FL_PSI {fl_psi} FR_PSI {fr_psi} BL_PSI {bl_psi}" \
             f" BR_PSI {br_psi}"

    print(output)

    # send to netcat listener on pit laptop
    # TODO
