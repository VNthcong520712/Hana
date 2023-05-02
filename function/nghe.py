import speech_recognition as spe 
re = spe.Recognizer()
def nghe_():
    with spe.Microphone() as aud: 
        audio = re.listen(aud)
        try:
            out = re.recognize_google(audio, language="vi-VN")
        except:
            out = "NULL"
    return(out.lower())

if __name__ == "__main__":
	print(nghe_())

