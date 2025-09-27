from flask import Flask, send_file, request
from datetime import datetime, timedelta
import telebot
import io

app = Flask(__name__)
bot = telebot.TeleBot("77672606:ABEFPzIH2hFVf2d6WFZIY1W3Y")
telegram_id = "635306"

@app.route('/canary')
def canary():
    ip = request.remote_addr

    timestamp = (datetime.utcnow() + timedelta(hours=5)).strftime('%Y-%m-%d %H:%M:%S')

    bot.send_message(telegram_id, f"🐤 Канарейка сработала!\n🕓 Время: {timestamp}\n🌐 IP: {ip}")

    img_bytes = io.BytesIO()
    transparent_pixel = bytes([137,80,78,71,13,10,26,10] + [0]*100)
    img_bytes.write(transparent_pixel)
    img_bytes.seek(0)

    return send_file(img_bytes, mimetype='image/png')
if __name__ == '__main__':
    app.run(debug=True, port=5000)



