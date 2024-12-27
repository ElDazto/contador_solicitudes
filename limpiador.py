
def procesar_texto(texto):
    texto = texto.replace(' ', '')
    texto = texto.replace('\n', '')
    if texto and (texto[-1] == '.' or texto[-1] == ','):
        texto = texto[:-1]
        
        pass
    ultimos_siete = texto[-7:]
    
    return ultimos_siete
