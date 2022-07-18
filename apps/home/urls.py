from django.urls import path, re_path
from apps.home import views


urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    path('addLembrete', views.addLembrete, name='addLembrete'),
    path('altLembrete/<int:id>', views.altLembrete, name='altLembrete'),
    path('delLembrete/<int:id>', views.delLembrete, name='delLembrete'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]