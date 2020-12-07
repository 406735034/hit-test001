
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from test001.views import ChartWeekData

urlpatterns = [
    path('', include('test001.urls')),
    path('admin/', admin.site.urls),
    path(r'api/chart/weekdata/', ChartWeekData.as_view(), name='chart-data'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('question1/',
         TemplateView.as_view(template_name='questions/q1try.html'))

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = urlpatterns + \
#     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [re_path(r'^.*',
#                         TemplateView.as_view(template_name='index.html'))]
