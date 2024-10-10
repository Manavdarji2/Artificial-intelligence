import speech_recognition as sr

def command():
    print("Listining......")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        audio=r.listen(source)
        try:
            print("Recogizing...")
            query=r.recognize_google(audio,language="en-In")
            print("User Say: ",query)
            return query
        except Exception as e:
            print(e)
