from app.models import Product, Category
from app import app, db
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView


class MyProductView(ModelView):
    column_list = ['id', 'name', 'price', 'active']
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    can_export = True
    edit_modal = True


class MyCategoryView(ModelView):
    column_list = ['name', 'products']


class MyStastView(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')



admin = Admin(app=app, name='Quan tri ban hang', template_mode='bootstrap4')

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStastView(name="Thong Ke"))
