from limpiador import procesar_texto
import keyboard
import os
import pyautogui
import pytesseract
import datetime
from menu import menu

# Variable para almacenar el contador
contador = 0
x1, y1, x2, y2 = menu()

os.system('cls')
def on_triggered(event):
    global contador
    
    if (event.event_type == keyboard.KEY_DOWN and event.name == 'l' and keyboard.is_pressed('ctrl')) or (event.event_type == keyboard.KEY_DOWN and event.name == 'L' and keyboard.is_pressed('ctrl')):
        contador += 1
        print(f'Se ha presionado Ctrl + L {contador} veces.')
        
        # Capturar la zona de la pantalla
        screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
        
        # Extraer el texto utilizando PyTesseract
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        texto = pytesseract.image_to_string(screenshot)
        texto = procesar_texto(texto)
        
        # Guardar el texto en un archivo de texto
        fecha = datetime.datetime.now()
        dia_actual = fecha.day
        mes_actual = fecha.month
        año_actual = fecha.year
        
        archivo = f'texto_capturado_{mes_actual}_{dia_actual}.txt'
        carpeta = fr'D:\Documentos\Lotes\{año_actual}_{mes_actual}'
        ruta = os.path.join(f"D:\Documentos\Lotes\{año_actual}_{mes_actual}", archivo)
        
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f'Se ha creado la carpeta {carpeta}')
        
        with open(ruta, 'a') as f:
            f.write(texto + '\n')  # Agregar una nueva línea después de cada texto capturado

        print(f'Se ha guardado el texto capturado en {archivo}')
        

def on_triggered_reset(event):
    global contador
    if event.event_type == keyboard.KEY_DOWN and event.name == 'r' and keyboard.is_pressed('ctrl'):
        contador = 0
        os.system('cls')
        print('Se ha reseteado el contador')

# Crea el hook para detectar eventos
keyboard.hook(on_triggered)
keyboard.hook(on_triggered_reset)
# keyboard.hook(on_trigggered)

# Mantén el programa en ejecución
keyboard.wait()
