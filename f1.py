import subprocess

#adds googletrans module
subprocess.call('(pip3 install googletrans)', shell = True)

#adds google-speech module
subprocess.call('(pip3 install google-speech)', shell = True)

#installs sox library for google-speech
subprocess.call('(sudo apt-get install sox libsox-fmt-mp3)', shell = True)

#installs xclip
subprocess.call('(sudo aptitude install xclip)', shell = True)
