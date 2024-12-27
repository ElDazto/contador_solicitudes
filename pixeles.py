import pyautogui

# Obtiene y muestra las coordenadas del puntero del mouse en tiempo real
try:
    while True:
        x, y = pyautogui.position()
        print(f"Coordenadas del puntero: X={x}, Y={y}", end='\r')
except KeyboardInterrupt:
    print("\nPrograma terminado.")
