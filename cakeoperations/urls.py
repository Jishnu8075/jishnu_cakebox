from django.urls import path
from cakeoperations.views import SignUpView,SignInView,IndexView,CakeCreateView,CategoryCreateView,\
CakeListView,CakeUpdateView,remove_cakeview,CakeDetailView,CakeVarientCreateView,CakeVarientUpdateView,remove_varient,\
OfferCreateView,offer_delete_view,sign_out_view



urlpatterns=[
    path('signup/',SignUpView.as_view(),name='signin'),
    path('',SignInView.as_view(),name='login'),
    path('index/',IndexView.as_view(),name='index'),
    path('cake/add',CakeCreateView.as_view(),name='cake-add'),
    path('category/add',CategoryCreateView.as_view(),name='category-add'),
    path('cake/list',CakeListView.as_view(),name='cake-list'),
    path('cake/<int:pk>/change',CakeUpdateView.as_view(),name='cake-change'),
    path('cake/<int:pk>/remove',remove_cakeview,name="cake-remove"),
    path('cake/<int:pk>/',CakeDetailView.as_view(),name='cake-detail'),
    path('cake/<int:pk>/varient/add',CakeVarientCreateView.as_view(),name='varient-add'),
    path('cake/<int:pk>/varient/change',CakeVarientUpdateView.as_view(),name='varient-change'),
    path('cake/<int:pk>/varient/remove',remove_varient,name='varient-remove'),
    path('offers/<int:pk>/add',OfferCreateView.as_view(),name='offer-add'),
    path('offers/<int:pk>/delete',offer_delete_view,name='offer-delete'),
    path('logout/',sign_out_view,name='signout')
]