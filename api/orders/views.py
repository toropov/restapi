from flask_restx import Resource, Namespace, fields
from http import HTTPStatus
from flask_jwt_extended import jwt_required,get_jwt_identity
from ..models.orders import Order
from ..models.users import User
from ..utils.db import db

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

order_status_model=order_namespace.model(
    'Order_status',{
        'order_status':fields.String(required=True,description="Order status",
        enum=['PENDING','IN_TRANSIT','DELIVERED']
        )
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


    @jwt_required()
    @order_namespace.expect(order_model)
    @order_namespace.marshal_with(order_model)    
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

    @order_namespace.marshal_with(order_model)
    def get(self, order_id):
        """
            Получить заказ по id
        """
    
        order=Order.get_by_id(order_id)

        return order,HTTPStatus.OK


    @jwt_required()
    @order_namespace.expect(order_model)
    @order_namespace.marshal_with(order_model)    
    def put(self, order_id):
        """
            Обновить заказ по id
        """
        
        order_to_update=Order.get_by_id(order_id)

        data=order_namespace.payload

        order_to_update.quantity=data['quantity']
        order_to_update.size=data['size']
        order_to_update.flavour=data['flavour']

        db.session.commit()

        return order_to_update,HTTPStatus.OK

    @jwt_required()
    @order_namespace.marshal_with(order_model)    
    def delete(self, order_id):
        """
            Удалить заказ по id
        """
        order_to_delete=Order.get_by_id(order_id)
        order_to_delete.delete()

        return order_to_delete, HTTPStatus.OK



@order_namespace.route('/user/<int:user_id>/order/<int:order_id>/')
class GetSpecificOrderByUser(Resource):
    
    @jwt_required()
    @order_namespace.marshal_with(order_model)
    def get(self, user_id, order_id):
        """
            Получить конкретный заказ для покупателя
        """
        user=User.get_by_id(user_id)
        order=Order.query.filter_by(id=order_id).filter_by(user=user).first()

        return order, HTTPStatus.OK



@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):
    @jwt_required()
    @order_namespace.marshal_list_with(order_model)
    def get(self, user_id):
        """
            Получить все заказы конкретного пользователя
        """
        
        user=User.get_by_id(user_id)

        orders=user.orders

        return orders, HTTPStatus.OK


@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):

    @jwt_required()
    @order_namespace.expect(order_status_model)
    @order_namespace.marshal_with(order_model)
    def patch(self, order_id):        
        """
            Обновить статус конкретного заказа
        """

        data=order_namespace.payload
        order_to_update=Order.get_by_id(order_id)        

        order_to_update.order_status=data['order_status']

        db.session.commit()

        return order_to_update, HTTPStatus.OK

