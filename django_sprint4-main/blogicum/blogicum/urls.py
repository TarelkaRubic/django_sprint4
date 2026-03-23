from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.edit import CreateView
from django.urls import include, path, reverse_lazy


handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.internal_server_error'

