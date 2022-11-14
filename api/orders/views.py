from flask_restx import Resource, Namespace

order_namespace = Namespace('orders', description="namespace for orders")


@order_namespace.route('/orders')
class OrderGetCreate(Resource):

    def get(self):
        """
            Получить все заказы
        """
        pass

    def post(self):
        """
            Разместить новый заказ
        """
        pass


@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):

    def get(self, order_id):
        """
            Получить заказ по id
        """
        pass

    def put(self, order_id):
        """
            Обновить заказ по id
        """
        pass

    def delete(self, order_id):
        """
            Удалить заказ по id
        """
        pass


@order_namespace.route('/user/<int:user_id>/order/<int:order_id>/')
class GetSpecificOrderByUser(Resource):

    def get(self, user_id, order_id):
        """
            Получить конкретный заказ для покупателя
        """
        pass


@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):

    def get(self, user_id):
        """
            Получить все заказы конкретного пользователя
        """
        pass


@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):

    def patch(self, order_id):
        """
            Обновить статус конкретного заказа
        """
        pass
