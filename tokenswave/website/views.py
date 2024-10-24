from django.views.generic import TemplateView
from tokenswave.settings import domain, sitename, twitter, telegram, snapchat, google_analytics
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET

robots_txt_content = f"""\
User-agent: *
Sitemap: {domain}/sitemap.xml

#Template Files
Allow: /static/*

#Languages
Allow: /en/
Allow: /id/
Allow: /de/
Allow: /es/
Allow: /fr/
Allow: /hi/
Allow: /it/
Allow: /cs/
Allow: /lv/
Allow: /hu/
Allow: /ko/
Allow: /ru/
Allow: /ja/
Allow: /pl/
Allow: /uk/
"""

sitemap_xml_content = f"""\
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url>
<loc>{domain}</loc>
</url>
<url>
<loc>{domain}/en</loc>
</url>
<url>
<loc>{domain}/id</loc>
</url>
<url>
<loc>{domain}/de</loc>
</url>
<url>
<loc>{domain}/es</loc>
</url>
<url>
<loc>{domain}/fr</loc>
</url>
<url>
<loc>{domain}/hi</loc>
</url>
<url>
<loc>{domain}/it</loc>
</url>
<url>
<loc>{domain}/cs</loc>
</url>
<url>
<loc>{domain}/lv</loc>
</url>
<url>
<loc>{domain}/hu</loc>
</url>
<url>
<loc>{domain}/ko</loc>
</url>
<url>
<loc>{domain}/ru</loc>
</url>
<url>
<loc>{domain}/ja</loc>
</url>
<url>
<loc>{domain}/pl</loc>
</url>
<url>
<loc>{domain}/uk</loc>
</url>
</urlset>
"""

@require_GET
def robots_txt(request):
    return HttpResponse(robots_txt_content, content_type="text/plain")

@require_GET
def sitemap_xml(request):
    return HttpResponse(sitemap_xml_content, content_type="text/xml")


def custom_404(request, exception):
    context = {}
    context['sitename'] = sitename
    return render(request, '404.html', status=404, context=context)

def custom_500(request):
    context = {}
    context['sitename'] = sitename
    return render(request, '500.html', status=500, context=context)

def custom_403(request, exception):
    context = {}
    context['sitename'] = sitename
    return render(request, '403.html', status=403, context=context)

def custom_400(request, exception):
    context = {}
    context['sitename'] = sitename
    return render(request, '400.html', status=400, context=context)


class MainView(TemplateView):
    template_name = 'index.html'
    
    language_flags = {
        'en': 'gb', 
        'id': 'id',
        'de': 'de',
        'es': 'es',
        'fr': 'fr',
        'hi': 'in',
        'it': 'it',
        'cs': 'cz',
        'lv': 'lv',
        'hu': 'hu',
        'ko': 'kr',
        'ru': 'ru',
        'ja': 'jp',
        'pl': 'pl',
        'uk': 'ua'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language_flags'] = self.language_flags
        context['domain'] = domain
        context['sitename'] = sitename
        context['twitter'] = twitter
        context['telegram'] = telegram
        context['snapchat'] = snapchat
        context['google_analytics'] = google_analytics
        return context
