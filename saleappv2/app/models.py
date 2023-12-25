import hashlib

from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, Enum, DateTime
from app import db, app
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from datetime import datetime
import enum


class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)
    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(500),
                   default='https://mega.com.vn/media/news/1025_cach_cai_hinh_nen_may_tinh_vo_cung_don_gian.jpg')
    active = Column(Boolean, default=True)
    category_id = Column(Integer,ForeignKey(Category.id), nullable=False)
    receipt_details= relationship('ReceiptDetails', backref='receipt', lazy=True)

    def __str__(self):
        return self.name

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar= Column(String(100),
                   default='https://mega.com.vn/media/news/1025_cach_cai_hinh_nen_may_tinh_vo_cung_don_gian.jpg')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    receipt = relationship('Receipt', backref='User', lazy=True)

class BaseModel(db.Model):

    __abstract__ = True
    id = Column(Integer, primary_key=True)
    activate = Column(Boolean, default=True)
    created_date = Column(DateTime, default= datetime.now())

class Receipt(BaseModel):
    user_id = Column(Integer, ForeignKey(User.id), nullable= False)

class ReceiptDetails(BaseModel):

    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)






if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # u = User(name='Admin', username='admin',
        #          password=hashlib.md5('123456'.encode('utf-8')).hexdigest(),
        #          user_role = UserRoleEnum.ADMIN)
        # db.session.add(u)
        # db.session.commit()
        # c1 = Category(name = 'Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Computer')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.commit()
        #
        #
        # p1 = Product(name = 'iphone1', price=200000,category_id=1)
        # p2 = Product(name='iphone2', price=200000, category_id=2)
        # p3 = Product(name='iphone3', price=200000, category_id=1)
        # p4 = Product(name='iphone4', price=200000, category_id=2)
        # p5 = Product(name='iphone5', price=200000, category_id=3)
        # db.session.add_all([p1,p2,p3,p4,p5])
        # db.session.commit()
