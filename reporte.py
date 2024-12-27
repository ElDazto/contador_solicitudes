from limpiador import procesar_texto
import keyboard
import os
import pyautogui
import pytesseract

def on_trigggered(event):
    global contador
    aumento = 21
    if (event.event_type == keyboard.KEY_DOWN and event.name == 'm' and keyboard.is_pressed('ctrl')) or (event.event_type == keyboard.KEY_DOWN and event.name == 'M' and keyboard.is_pressed('ctrl')):
        x1, y1, x2, y2 = 103, 193, 249, 213
        while True:
            screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
            y1 += aumento
            y2 += aumento
            
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            texto = pytesseract.image_to_string(screenshot)
            texto = procesar_texto(texto)
            print(texto)
            archivo = 'texto_reportado.txt'
            with open(archivo, 'a') as f:
                f.write(texto + '\n')  # Agregar una nueva línea después de cada texto capturado
            
            if y1 == (193 + (38 * aumento)):
                break
            
# Crea el hook para detectar eventos
keyboard.hook(on_trigggered)

# Mantén el programa en ejecución
keyboard.wait()