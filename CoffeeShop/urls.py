from CoffeHouse.urls import path
from CoffeeShop import views

urlpatterns=[
    path('',views.index,name="my_home"),
    path('about',views.about,name="my_about"),
    path('gallery',views.gallery,name="my_gallery"),
    path('services',views.services,name="my_services"),
    path('contact',views.contact,name="my_contact")
]