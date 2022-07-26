from django.urls import path
from . import views
urlpatterns=[
    # path('',views.fun1,name='fun1'),
    # path('',views.fun2),
    path('fn3',views.fun3,name='fun'),
    path('fn4',views.fun4,name='fun1'),
]