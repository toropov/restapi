from flask_restx import Resource, Namespace, fields
from http import HTTPStatus
from flask_jwt_extended import jwt_required,get_jwt_identity
from ..models.orders import Order
from ..models.users import User

order_namespace = Namespace('orders', description="namespace for orders")


order_model=order_namespace.model(
    'Order',{
        'id':fields.Integer(description="An id"),
        'size':fields.String(required=True,enum=['SMALL','MEDIUM','LARGE','EXTRA_LARGE'],
            description="Size of order"
        ),
        'order_status':fields.String(required=True, enum=['PENDING','IN_TRANSIT','DELIVERED'],
            description="Order status")
    }
)


@order_namespace.route('/orders')
class OrderGetCreate(Resource):
    @order_namespace.marshal_with(order_model)
    @jwt_required()
    def get(self):
        """
            Получить все заказы
        """
        
        orders=Order.query.all()

        return orders,HTTPStatus.OK


    @order_namespace.expect(order_model)
    @order_namespace.marshal_with(order_model)
    @jwt_required()
    def post(self):
        """
            Разместить новый заказ
        """
        
        data=order_namespace.payload


        new_order=Order(
            size=data['size'],
            quantity=data['quantity'],
            flavour=data['flavour']
        )
        username=get_jwt_identity()
        current_user=User.query.filter_by(username=username).first()
        new_order.user=current_user

        new_order.save()


        return new_order, HTTPStatus.CREATED


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
