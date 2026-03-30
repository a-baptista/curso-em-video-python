'''from playsound import playsound
playsound ('musica.mp3.mp3')'''

from pygame import mixer
mixer.init()
mixer.music.load('musica.mp3.mp3')
mixer.music.play()
input('A tocar...prime ENTER para parar.')
mixer.music.stop()
input('Música parada com sucesso!')




