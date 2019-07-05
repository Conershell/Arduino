#servidor web que envia datos (1 y 0) CON BOTONES WEB y activa via serial led de arduino
#instalar para version de serial que viene en este enlace: https://sourceforge.net/projects/pyserial/

from wsgiref.simple_server import make_server
from cgi import parse_qs
import serial
import time

def encender():
        arduino = serial.Serial("COM6", 9600)
        time.sleep(2)
        arduino.write(b'1')
        arduino.close()     

def apagar():
        arduino = serial.Serial("COM6", 9600)
        time.sleep(2)
        arduino.write(b'0')
        arduino.close()
        
while (True):

        html = """     
        <html>
        <body>
        <h1><center>CONTROL DE LUCES VIA WEB (Arduino y Python)</center></h1>
        <form name="formulario" method="get" action="http://localhost:8000">
        ENCEDER LUCES <center><input type="submit" value='1' name="nombre" formaction="" style='width:300px; height:130px; color: #003366; background-color: #00FF00'></center>
        APAGAR LUCES <center><input type="submit" value='0' name="nombre" formaction="" style='width:300px; height:130px; color: #003366; background-color: #FF0000'></center>
        </form>
        <p>
        <h1> dato %(nombre)s </h1>
        </body>
        </html>
        """

        def application(environ, start_response):
                valores = parse_qs(environ['QUERY_STRING'])
                nombre = valores.get('nombre','el nombre no existe')
                nombre = nombre[0]
                headers = [('Content-type', 'text/html')]
                response = html % { 'nombre' : nombre}
                start_response('200 OK', headers)
                if nombre [0]=='1':
                        encender()
                if nombre [0]=='0':
                        apagar()
                        
                return [bytes (response, 'utf-8')]
                
                

        servidor = make_server('192.168.0.16',8000,application)
        servidor.handle_request()