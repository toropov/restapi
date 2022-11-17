from flask import Flask
from flask_restx import Api
from .orders.views import order_namespace
from .auth.views import auth_namespace
from .config.config import config_dict
from .models.orders import Order
from .models.users import User
from .utils.db import db

from flask_migrate import Migrate


def create_app(config=config_dict['dev']):  
    app=Flask(__name__)


    app.config.from_object(config)

    api = Api(app)

    api.add_namespace(order_namespace)
    api.add_namespace(auth_namespace, path='/auth')

    db.init_app(app)
    migrate=Migrate(app,db)


# таблицы создаются следующим образом
# export FLASK_APP=api
# flask shell
# db.create_all()

# если надо удалить созданные таблицы
# db.drop_all()

    @app.shell_context_processor
    def make_shell_context():
        return{
            'db':db,
            'User':User,
            'Order':Order,
        }

    return app