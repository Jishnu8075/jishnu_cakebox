from django.urls import path
from api import views
from api.views import UserCreationView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("cakes",views.CakeView,basename="cakes")

urlpatterns=[
    path("register",UserCreationView.as_view())
    



]+router.urls                                                                                           