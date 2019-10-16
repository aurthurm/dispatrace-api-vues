from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

# Serve Vue Application
IndexView = never_cache(TemplateView.as_view(template_name='index.html'))

# Hnadle 404
def bad_request(request, exception): return redirect(reverse('index2'))