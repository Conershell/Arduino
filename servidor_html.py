#servidor que despliega archivo html estatic

from wsgiref.simple_server import make_server
from cgi import parse_qs
import io
import serial
import time

arduino = serial.Serial("COM6", 9600)
time.sleep(2)

def encender():
    #arduino = serial.Serial("COM6", 9600)
    time.sleep(2)
    arduino.write(b'1')
    pass

def apagar():
    #arduino = serial.Serial("COM6", 9600)
    time.sleep(2)
    arduino.write(b'0')
    pass

while(True):
	def application(environ, start_response):
			valores = parse_qs(environ['QUERY_STRING'])
			nombre = valores.get('nombre','el nombre no existe')
			nombre = nombre[0]
			headers = [('Content-type', 'text/html')]
			response = html % { 'nombre' : nombre}
			start_response('200 OK', headers)
			if (nombre [0] == '1'):
				encender()
				pass
			if (nombre [0] == '0'):
				apagar()
				pass
			return [bytes (html, 'utf-8')]

	archivo = open("index3.html","r")
	html = archivo.read()

	servidor = make_server('192.168.0.16',8000,application)
	servidor.handle_request()