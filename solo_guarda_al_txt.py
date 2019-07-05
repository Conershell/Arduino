#servidor que despliega archivo html estatic

from wsgiref.simple_server import make_server
from cgi import parse_qs
import io
import serial
import time

def bytesToStr(linea):
	#print(type(linea))
	lineaSTR = linea.decode("utf-8")
	#print(type(lineaSTR))
	return lineaSTR

def writeTxtArduino(linea):
	lineaSTR = bytesToStr(linea)
	if(lineaSTR != "Activando brazo..." and lineaSTR != "Activando piston..." and  lineaSTR != "PROCESO EXITOSO"):
		print(lineaSTR)
		archivo2 = open("archivo.txt", "a")
		archivo2.write("La luminosidad es del: " + lineaSTR + "%") #ESCRIBE EL DATO
		archivo2.close()
	else:
		writeTxt(lineaSTR)
	pass

def writeTxt(frase):
	archivo2 = open("archivo.txt", "a")
	archivo2.write(frase)
	archivo2.close()
	pass

arduino = serial.Serial("COM6", 9600)
time.sleep(2)

while(True):
	linea = arduino.readline()
	print("Guardando...")
	linea = linea.rstrip()
	writeTxtArduino(linea) #SE LLAMA A LA FUNCION PARA ESCRIBIR EL DATO
	writeTxt('\n') #SE ESCRIBE EL ENTER
