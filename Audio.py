import speech_recognition as rs

r=rs.Recognizer()

with sr.Microphone() as source:
	print("Please speak:")
	audio=r.listen(source)

	try:
		text=r.recognize_google(audio)
		print("You said : {}".format(text))
	except:
		print("Sorry cannot hear you!!!")