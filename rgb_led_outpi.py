#wagwan this is the script
#ill teach u the basic stuff it does

#importing modules
from subprocess import check_output,Popen, PIPE
import RPi.GPIO as GPIO

#this sets the board up
GPIO.setmode(GPIO.BOARD)

#this sets the pins

#red
GPIO.setup(21, GPIO.OUT)

#green
GPIO.setup(20, GPIO.OUT)


#in the two boxes below, place the path to the audio file.
#audio 1 is green
#audio 2 is red

#do it like this
#audio1 = ("home/usr/sound.mp3")

audio1 = ("")
audio2 = ("")

while True:
    try:
        lsout = Popen(['lsof', audio1], stdout=PIPE, shell=False)
        check_output(["grep", audio1], stdin=lsout.stdout, shell=False)
        print("audio1 open")
        GPIO.output(20, GPIO.HIGH)
    except:
        print("audio1 closed")
        GPIO.output(20, GPIO.LOW)

    try:
        lsout = Popen(['lsof', audio2], stdout=PIPE, shell=False)
        check_output(["grep", audio2], stdin=lsout.stdout, shell=False)
        print("audio2 open")
        GPIO.output(21, GPIO.HIGH)
    except:
        print("audio2 closed")
        GPIO.output(21, GPIO.HIGH)
