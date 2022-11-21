Пример создания секретного ключа

python
import secrets
secrets.token_hex()


Для запуска приложения под linux
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=api
python runserver.py

Пример вызова: curl -X GET -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2OTAyMDIyMCwianRpIjoiMmMzNmMwYjUtN2Q5My00ODcyLTg4Y2EtMWMzMWIzOGYwZGZiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImE0Mjc3IiwibmJmIjoxNjY5MDIwMjIwLCJleHAiOjE2NjkwMjIwMjB9.pm-Ts0bzCtVeoKgg2kv-sOys0q1ovHIrSIomoJy8UjY' -i 'http://127.0.0.1:5000/orders/orders'