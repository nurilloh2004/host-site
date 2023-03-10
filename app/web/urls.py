from django.urls import path

from .views import *

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
    path('banners/<int:pk>/', BannerDetail.as_view(), name='banner-detail'),
    path('abouts/', AboutList.as_view(), name='about-list'),
    path('subabouts/', SubAboutList.as_view(), name='sub-about-list'),
    path('services/', ServicesList.as_view(), name='services-list'),
    path('services/<int:pk>/', ServicesDetail.as_view(), name='services-detail'),
    path('items_domain/', ItemsDomainList.as_view(), name='items_domain-list'),
    path('items_domain/<int:pk>/', ItemsDomainDetail.as_view(), name='items_domain-detail'),
    path('domains/', DomainList.as_view(), name='domain-list'),
    path('domains/<int:pk>/', DomainDetail.as_view(), name='domain-detail'),
    path('orderdomains/', OrderDomainListCreateAPIView.as_view(), name='orderdomain-list-create'),
    path('orderdomains/<int:pk>/', OrderDomainRetrieveUpdateDestroyAPIView.as_view(), name='orderdomain-retrieve-update-delete'),
    

]
