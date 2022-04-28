#Set up a docker environment for this code, and don't try to include superfluous packages!
from PIL import Image, ImageDraw
import csv
from scipy import constants
import numpy as np
import openSSL
import os

color = 128 * np.ones(shape=[3], dtype=np.uint8)
tuplevals = tuple(color)
im = Image.new('RGB', (512, 512), tuplevals)
draw = ImageDraw.Draw(im)
draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
draw.text((100, 200), "You did it!", fill=(int(constants.speed_of_light), 0, 0))
im.save( "pythonCode2Image.png")

try:
    with open('temp.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
except:
    pass

key = crypto.PKey()
key.generate_key(crypto.TYPE_RSA, 2048)

certificate = crypto.X509()
certificate.get_subject().country = 'United States'
certificate.get_subject().state = 'Nevada'
certificate.get_subject().city = 'Reno'
certificate.get_subject().org = 'University of Nevada, Reno'
certificate.get_subject().department = 'CSE'
certificate.get_subject().comname = os.environ.get('USERNAME')

certificate.set_serial_number(42)
certificate.gmtime_adj_notAfter(1577788000) # corresponds to 5 years in seconds
certificate.set_issuer(certificate.get_subject())

certificate.set_pubkey(key)

certificate.sign(key, 'sha512')
#modify this code so that it also generates self signed certificate and keys