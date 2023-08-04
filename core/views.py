from rest_framework.response import Response
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"