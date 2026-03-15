import requests
import time

TOKEN = "8423599860:AAHTsGNzDLF8n19Mum0ryvjkbhdd_tsxIwI"
CHAT_ID = "8144489845"

def enviar_mensaje(texto):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": texto
    }

    requests.post(url, data=data)

print("Bot iniciado")

while True:

    enviar_mensaje("🤖 Bot funcionando correctamente")

    time.sleep(3600)