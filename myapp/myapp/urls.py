
from django.contrib import admin
from django.urls import path
from home.views import home
from vegetable.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),
    path('', login_page, name='login_page'),
    path('recipes/', recipes, name='recipes'),
    path('update_recipes/<id>/', update_recipes, name='update_recipes'),
    path('delete_recipes/<id>/', delete_recipes, name='delete_recipes'),
    # path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', logout_page, name='logout_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()