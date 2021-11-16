import os
import pyttsx3
import datetime
import webbrowser
import smtplib

engine = pyttsx3.init()
def speak(audio):
	engine.say(audio)
	engine.runAndWait()
print('how may i help you!')
speak('how may i help you!')

while True:
	speak('Enter The serivce :')
	print()
	n = str(input('Enter The service Name: '))
	cmd = n.lower()

	if 'chrome' in cmd:
		os.system('chrome')

	elif 'facebook' in cmd:
		os.system('https://www.facebook.com')
	elif 'youtube' in cmd:
		os.system('chrome https://www.youtube.com')
	elif 'vscode' in cmd:
		os.system('code')
	elif 'Django' in cmd:
		os.system('/home/revan/Desktop/django')
	elif 'music' in cmd:
		pass
	elif 'browser' in cmd:
		webbrowser.open('www.google.com')
	elif 'time' in cmd:
		strTime = datetime.datetime.now().strftime('%H:%M:%S')
		print('The time is (0)'.format(strTime))

		speak('The time is (0)'.format(strTime))
	elif 'email' in cmd:
		s = smtplib.SMTP('smtp.gmail.com',587)
		s.starttls()
		s.login('revanmore8@gmail.com','Revan@1233')
		message = input('Enter The Message for Mail :')
		s.sendmail('revanmore8@gmail.com','revanmore8@gmail.com',message)
		s.quit()
	elif 'exit' in cmd:
		print('Byeee ! your Out from The Program')

		speak('Byeee ! your Out from The Program')
		break
	else:
		print('Invalid command')
		speak('Invalid command')