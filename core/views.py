from rest_framework.response import Response
from django.views.generic import TemplateView
from rest_framework.views import APIView

from .utils import populate_db, populate_devices

class HomePageView(TemplateView):
    template_name = "index.html"


class PopulateDB(APIView):
    def post(self, request):
        populate_db()
        return Response()


class PopulateDevices(APIView):
    def post(self, request):
        populate_devices()
        return Response()



