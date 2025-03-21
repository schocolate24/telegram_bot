import requests
import socket
import subprocess
import fcntl
import struct


# Configuración de Telegram
BOT_TOKEN = "********************************"
CHAT_ID = ["**************","*************"]

def obtener_ip():
    """Obtiene la dirección IP local de la Raspberry Pi."""
   # hostname = socket.gethostname()
   # ip_local = socket.gethostbyname(hostname)
   # return ip_local

    """Obtiene la dirección IP de la interfaz wlan0 de la Raspberry Pi."""
    interfaz = "wlan0"  # Cambia a "eth0" si estás usando cable Ethernet
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ip = socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR (Get Interface Address)
            struct.pack('256s', interfaz[:15].encode("utf-8"))
        )[20:24])
        return ip
    except IOError:
        return "No se pudo obtener la IP"  


def enviar_mensaje_telegram(mensaje):
    """Envía un mensaje a Telegram."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    #datos = {"chat_id": CHAT_ID, "text": mensaje}
    #requests.post(url, data=datos)
    for dato in CHAT_ID :
        content = {"chat_id": dato, "text":mensaje}
        requests.post(url, data=content)

def verificar_conexion():
    """Verifica si hay conexión a Internet."""
    try:
        # Intenta hacer ping a Google (8.8.8.8)
        subprocess.check_call(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    # Verifica si hay conexión a Internet
    if verificar_conexion():
        ip = obtener_ip()
        mensaje = f"La IP de la Raspberry Pi es: {ip}"
        enviar_mensaje_telegram(mensaje)
        print("Mensaje enviado a Telegram.")
    else:
        print("No hay conexión a Internet. El mensaje no se ha enviado.")
