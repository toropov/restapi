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