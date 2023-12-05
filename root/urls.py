from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'A Tale Galore'
admin.site.index_title = 'A Tale Galore - Admin'
admin.site.site_title = 'A Tale Galore - Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),

    path('api/account/', include('root.modules.accounts.urls')),
    path('api/main/', include('root.modules.main.urls'))
]
