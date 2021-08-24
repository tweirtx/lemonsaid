import obd

# future plans: integrate TPMS with RTL-SDR readings.

# Initialize the OBDII interface.
connection = obd.OBD()

# Load callsign from disk. This is important when using amateur frequencies.
try:
    callsign = open('callsign.txt', 'r').read()
except FileNotFoundError:
    callsign = "N/A"

while True:
    # Read parameters from the OBDII system.
    speed = connection.query(obd.commands.SPEED)
    rpm = connection.query(obd.commands.RPM)
    throttle_position = connection.query(obd.commands.RELATIVE_THROTTLE_POS)  # Subject to change with future testing.
    coolant_temp = connection.query(obd.commands.COOLANT_TEMP)
    fuel_level = connection.query(obd.commands.FUEL_LEVEL)

    # Read tire pressures with software defined radio. TODO
    fl_psi = 30.0  # Testing value
    fr_psi = 30.0  # Testing value
    bl_psi = 30.0  # Testing value
    br_psi = 30.0  # Testing value

    # Construct data string
    output = f"SPEED {speed.mph} MPH RPM {rpm} THROTTLEPOS {throttle_position} TEMP {coolant_temp} " \
             f"FUEL_LEVEL {fuel_level} CALLSIGN {callsign} FL_PSI {fl_psi} FR_PSI {fr_psi} BL_PSI {bl_psi}" \
             f" BR_PSI {br_psi}"

    # send to netcat listener on pit laptop
    # TODO
