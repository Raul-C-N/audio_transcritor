import speech_recognition as sr

#função para ouvir e reconhecer fala
def ouvir_mic():
    #habilita o mic do usuário
    microfone = sr.Recognizer()
    
    #usando o mic
    with sr.Microphone() as source:
        #chama algoritmo de redução de ruídos
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuário dizer algo
        print ("Diga alguma coisa")
        
        #Armazena o que foi dito numa variável
        audio = microfone.listen(source)
    try:
        #passa a varíavel para um algorítmo 
        frase = microfone.recognize_google(audio,language='pt-BR')
        #Retorna a frase pronunciada
        print ('você disse: '+frase)
    except sr.UnknownValueError:
        print ('Não entendi')
    return frase

ouvir_mic()