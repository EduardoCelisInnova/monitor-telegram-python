# Monitor con alertas

print("Monitor con alertas")

import socket
import time
import requests
from datetime import datetime

def escanearPuerto(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(5)

    try:
        server.connect((host, port))
        return True
        
    except:
        return False
    
    finally:
        server.close()

estadoAnterior = None


def actualizarEstado(ip, puerto):
    global estadoAnterior
    while True:
        estadoActual = escanearPuerto(ip, puerto)
        if estadoActual != estadoAnterior:
            if estadoActual == True:
                texto = "ABIERTO"
            else:
                texto = "CERRADO"

            print(f"El puerto {puerto} en {ip} ahora está {texto}")

            enviarAlerta(ip, puerto, texto)

            estadoAnterior = estadoActual
        time.sleep(10)


#configuracion del telegram

TOKEN = "8278517953:AAEQD5mD1cpxHe9E3OSr6CEAkwIK02ttQp4"
CHATID = "1545610312"


#funcion para enviar correo

def enviarAlerta(ip, puerto, estado):
    # Enviar mensaje
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    mensaje = f"⚠️ ALERTA: El puerto {puerto} en {ip} ahora está {estado} desde las {fecha}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    datos = {"chat_id": CHATID, "text":mensaje}
    
    try:
        requests.post(url, data=datos)
        print("✅ Alerta enviada a Telegram")
        
    except Exception as e:
        print(f"❌ Error al enviar el alerta {e}")

    # Cerrar conexión

ip = input("Introduce la direccion IP")
puerto = int(input("Introduce puerto asociado"))

print("--- MONITOREANDO PUERTO ---")

actualizarEstado(ip, puerto)
