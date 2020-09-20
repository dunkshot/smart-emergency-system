import os
import time

#os.system('speak.sh test.txt')
#os.system('omxplayer output.mp3')
#os.system('bash record.sh 5')

os.system('bash record.sh 4')
time.sleep(0.2)

os.system('python stt-kor.py voice.wav')
os.system('python3 pysql.py')
time.sleep(0.2)