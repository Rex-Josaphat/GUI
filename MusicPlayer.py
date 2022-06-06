from pygame import mixer_music

mixer_music.load('C:\\Users\\Home\\Desktop\\k_music\\6ix9ine_punani_official_music_video_mp3_5023.mp3')
mixer_music.set_volume(0.2)
mixer_music.play()

while(True):
    print('Press "p" to pause "r" resume')
    print('Press "e" to exit the programm')
    query = input('>>>')

    if query == 'p':
        mixer_music.pause()
    elif query == 'r':
        mixer_music.unpause()
    elif query == 'e':
        mixer_music.stop()

        break
