from pydub import *


def main():

song = AudioSegment.from_mp3("epicsaxguy.mp3")

chunk1 = song[:30000]
reverse = chunk1.reverse()

start = chunk1.append(reverse, crossfade=5000)

chunk2 = song[31000:60000]
decVolume = reverse -3
blender = popin.overlay(chunk2)

chunk3 = song[60000:90000]
speed = chunk3.speedup(2)
middle = blender.append(speed, crossfade = 5000)


complete = start + middle
complete.export ("test.mp3", format="mp3", bitrate="192k")


if __name__ == '__main__':
    main()
