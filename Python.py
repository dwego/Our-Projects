import webbrowser
import speech_recognition as sr

# Defining the command to start the program
start = 'open google' or 'open chrome' or 'chrome' or 'google'

print('Listening...')

def listen_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        # Recognizing the spoken command
        phrase = recognizer.recognize_google(audio, language='en-US')
        phrase_leitura = phrase.lower()
        
        print(f'You said: {phrase}')
        
        # Opening Google if the command is recognized
        if phrase_leitura == start:
            webbrowser.open('www.google.com', new=0, autoraise=True)
        else:
            webbrowser.open(f'{phrase}', new=0, autoraise=True)
        
        print('')
    except sr.UnknownValueError:
        print('Sorry, I didn\'t understand that.')

listen_microphone()
