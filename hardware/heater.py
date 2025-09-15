# Mock heater: stampa a console quando cambia stato
_heater_status = False

def set_heater(status: bool):
    global _heater_status
    if status != _heater_status:
        _heater_status = status
        print(f"[HEATER] {'ON' if status else 'OFF'}")

def get_heater_status():
    return _heater_status
