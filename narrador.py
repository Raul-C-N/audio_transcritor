#função que cria audio a partir do texto interno
def generateMP3(texto):
    mp3FileName = 'myAudio.mp3'
    #pip install pyttsx3
    import pyttsx3 as tts
    
    engine = tts.init()
    
    engine.save_to_file(
        texto, mp3FileName
    )
    engine.runAndWait()

    return mp3FileName

texto = 'Um homem de 25 anos matou quatro crianças e feriu outras cinco hoje de manhã após invadir uma creche em Blumenau (SC) com uma machadinha.... - Veja mais em https://noticias.uol.com.br/cotidiano/ultimas-noticias/2023/04/05/ataque-creche-blumenau-santa-catarina.htm?cmpid=copiaecola'
generateMP3(texto)