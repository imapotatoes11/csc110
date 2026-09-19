# A smart home system decides whether it should activate energy-saving mode.
#
# Energy-saving mode should activate when:
#   1. The homeowner is away and the house temperature is above 22°C.
#
#       OR
#
#   2. The electricity price is high and the house has no occupants.
#
# Note that Energy-saving mode should never activate if the emergency override is enabled.

# Task 1: Write Python code that:
#   - captures the required sensor information.
#   - creates meaningful Boolean expressions to output True iff Energy-Saving mode is active

homeowner_away = input("Homeowner is away? (y/n): ")
house_temp = int(input("House temperature (ºC): "))
price_high = False
EMERGENCY_OVERRIDE = False
house_has_occupants = homeowner_away == "y"

energy_saving = False
if not EMERGENCY_OVERRIDE:
    if homeowner_away == "y" and house_temp > 22:
        energy_saving = True
    elif price_high and not house_has_occupants:
        energy_saving = True


print(f"Energy Saving is: {energy_saving}")

# one liner (?)
#EMERGENCY_OVERRIDE = False; print(f"Energy saving is: {not EMERGENCY_OVERRIDE and ((homeowner_away := input("Homeowner is away? (y/n): ") == "y" and int(input("House temperature (ºC): ")) > 22) or (price_high := True and not homeowner_away))}")