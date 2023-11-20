from app.models import Product, Category, UserRoleEnum
from app import app, db
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user
from flask import redirect

class AuthenticationAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN

class AuthenticationUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyProductView(AuthenticationAdmin):
    column_list = ['id', 'name', 'price', 'active']
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    can_export = True
    edit_modal = True


class MyCategoryView(AuthenticationAdmin):
    column_list = ['name', 'products']


class MyStatsView(AuthenticationUser):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')

class LogoutView(AuthenticationUser):
    @expose("/")
    def __index__(self):
        logout_user()
        return redirect('/admin')


admin = Admin(app=app, name='Quan tri ban hang', template_mode='bootstrap4')

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name="Thong Ke"))
admin.add_view(LogoutView(name="Dang xuat"))
