from PIL import ImageGrab
import os
import time

ISOTIMEFORMAT='%Y_%m_%d'

pic = ImageGrab.grab()
filename ='C:/'+str(time.strftime(ISOTIMEFORMAT)) + ".jpg"
pic.save('1.jpg')
os.execvp("mspaint",('mspaint',filename))