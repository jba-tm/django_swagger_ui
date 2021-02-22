from django.views.generic import TemplateView


class DocsView(TemplateView):
    template_name = 'api/documentation.html'
    extra_context = {'schema_url': 'openapi-schema'}
