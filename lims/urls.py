
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static


admin.site.name='GRIPCO LIMS'
admin.site.site_title='GRIPCO LIMS'
admin.site.site_header='GRIPCO LIMS'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  
    path('api/',include('test_methods.urls')),
    path('api/',include('compliance.urls')),
    path('api/',include('compliance.urls')),
    path('api/',include('proficiency_testing.urls')),
    path('api/',include('LabEquipments.urls')),
    path('api/',include('calibrationtesting.urls')),
    path('api/',include('attendancelisting.urls')),
    path('api/',include('leaveapplication.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
