from googletrans import Translator
from google_speech import Speech

ts = Translator()
inp = 'gusta'
print(' 1:eng to esp\n 2:esp to eng')

while(True):
	inp = input('\n-> ')
	if inp == '':
		break

	if inp[0] == '1':
		des,src = 'en','es'
		s = ts.translate(inp[1:],dest=des,src=src)
	else:
		des,src = 'es','en'
		s = ts.translate(inp,dest=des,src=src)
	print('   '+s.text)
	snd = Speech(s.text, 'en')
	snd.play()






'''
from gtts import gTTS
from io import BytesIO
from playsound import playsound
my_variable = 'hello' # your real code gets this from the chatbot
mp3_fp = BytesIO()
tts = gTTS(my_variable, 'en')
tts.write_to_fp(mp3_fp)
playsound('mp3_fp.mp3')
'''

'''

to run command from python
subprocess.call('(command)')

'''