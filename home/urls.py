from django.urls import path
from . import views

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('login/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('order/<int:table_id>/<int:order_id>/',
         views.order_view, name='order'),
    path('table/', views.table_view, name='table'),
    path('test', views.testView, name='test'), #testing url for post
    # path('billing/',views.)

    # customer details api url
    path('customer_details_phone/<str:phone>/',
         views.CustomerDetailsPhone.as_view()),
    path('customer_details_email/<str:email>/',
         views.CustomerDetailsEmail.as_view()),

    # veg item's api url
    path('veg_breakfast/', views.VegBreakfastItems.as_view()),
    path('veg_meal/', views.VegMealItems.as_view()),
    path('veg_snacks/', views.VegSnacksItems.as_view()),
    path('veg_dinner/', views.VegDinnerItems.as_view()),

    # non-veg item's api url
    path('non_veg_breakfast/', views.NonVegBreakfastItems.as_view()),
    path('non_veg_meal/', views.NonVegMealItems.as_view()),
    path('non_veg_snacks/', views.NonVegSnacksItems.as_view()),
    path('non_veg_dinner/', views.NonVegDinnerItems.as_view())
]
