import hmac
import hashlib
import json
from flask import Flask, request



app = Flask(__name__)

SECRET_KEY = '8064671049:AAErI2A9UoX0nSrmlMH61jAW3fD5gzOxozw'

def verify_telegram_auth(data):
    # Получаем строку для верификации
    check_string = f"{data['id']}{data['first_name']}{data['last_name']}{data['username']}{data['auth_date']}"
    
    # Создаем хеш
    hash = hmac.new(SECRET_KEY.encode('utf-8'), check_string.encode('utf-8'), hashlib.sha256).hexdigest()
    
    # Сравниваем хеши
    return hash == data['hash']

@app.route('/auth', methods=['POST'])
def auth():
    if request.method == 'POST':
        # Получаем данные пользователя
        data = request.form
        
        # Проверяем подпись
        if verify_telegram_auth(data):
            # Аутентификация успешна, выполняем действия (например, создание сессии)
            return "Authentication successful", 200
        else:
            return "Authentication failed", 403

if __name__ == '__main__':
    app.run()
