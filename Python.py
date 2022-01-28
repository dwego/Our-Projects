import webbrowser
import speech_recognition as sr

start = 'abrir google' or 'abrir chrome' or 'chrome' or 'google'

print('Estou ouvindo ')
def ouvir_microfone():
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source)
        try:

            frase = microfone.recognize_google(audio,language='pt-BR')
            frase_leitura = frase.lower()
            print(frase)
            if frase_leitura == start:
                webbrowser.open('www.google.com', new=0, autoraise=True)
            else:
                 webbrowser.open(f'{frase}', new=0, autoraise=True)
            print('\033[36m''Voce falou: ''\033[36m' + f'\033[34m'+f'{frase}'+'\033[0;0m')
            print('')
        except sr.UnknownValueError:
            print('\033[34m'+'Nao entendi'+'\033[0;0m')

ouvir_microfone()