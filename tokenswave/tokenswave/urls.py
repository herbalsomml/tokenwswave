from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from website.views import MainView, custom_400, custom_403, custom_404, custom_500, robots_txt, sitemap_xml
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path("robots.txt/",robots_txt,),
    path("sitemap.xml/",sitemap_xml,),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Используйте i18n_patterns для добавления поддержки языков
urlpatterns += i18n_patterns(
    path('', MainView.as_view(), name='home'),  # Главная страница с поддержкой локализации
)

handler404 = 'website.views.custom_404'
handler500 = 'website.views.custom_500'
handler403 = 'website.views.custom_403'
handler400 = 'website.views.custom_400'