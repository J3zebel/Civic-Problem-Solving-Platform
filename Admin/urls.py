from django.urls import path
from Admin import views
app_name="Admin"

urlpatterns = [
    path('Sum/',views.sum,name="sum"),
    path('Largest/',views.largest,name="largest"),
    path('Salary/',views.salary,name="salary"),
    path('District/',views.district,name="district"),
    path('Category/',views.category,name="category"),
    path('Admin/',views.admin,name="Admin"),
    path('deladmin/<int:id>',views.deladmin,name="deladmin"),
    path('editadmin/<int:id>',views.editadmin,name="editadmin"),
    path('deldistrict/<int:id>',views.deldistrict,name="deldistrict"),
    path('editdistrict/<int:id>',views.editdistrict,name="editdistrict"),
    path('delcategory/<int:id>',views.delcategory,name="delcategory"),
    path('Place/',views.place,name="place"),
    path('SubCategory/',views.subcategory,name="subcategory"),
    path('delsub/<int:id>',views.delsub,name="delsub"),
    path('editsub/<int:id>',views.editsub,name="editsub"),
    path('LocalPlace/',views.localplace,name="localplace"),
]