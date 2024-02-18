from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Other Django URLs

    # Add this catch-all route to serve the React app
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
