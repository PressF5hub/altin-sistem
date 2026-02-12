from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Altın Yönetim Sistemi çalışıyor!</h1><p>Kullanıcı ekleme ve giriş yakında eklenecek.</p>"

if __name__ == '__main__':
    app.run()
