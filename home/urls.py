from django.urls import path


from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('hero/create', views.hero_create, name='hero-create'),
    path('hero/update/<int:id>', views.hero_update, name="hero"),
]
