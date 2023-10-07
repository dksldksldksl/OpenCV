import pyaudio
import numpy as np
import cv2
import os

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

PATH = os.getcwd()

while True:
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    volume = int(np.average(np.abs(data)))

    if volume < 300:
        img = cv2.imread(os.path.join(PATH, "C:\\Users\\User\\Downloads\\iloveimg-resized\\on.png"))
    else:
        img = cv2.imread(os.path.join(PATH, "C:\\Users\\User\\Desktop\\iloveimg-resized\\off.png"))

    cv2.imshow("gif", img) 
    
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.stop_stream()
stream.close()
p.terminate()

cv2.destroyAllWindows()

