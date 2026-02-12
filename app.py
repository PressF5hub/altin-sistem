from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Altın Yönetim Sistemi çalışıyor!</h1><p>Kullanıcı ekleme ve giriş yakında eklenecek.</p>"

if __name__ == '__main__':
    app.run()
from flask import render_template, request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Giriş denendi! (Şimdilik veritabanı yok, yakında gerçek olacak)"
    return render_template('login.html')
# Bu yorum deploy'u tetiklesin
# Bu satır deploy'u tetiklesin abi
