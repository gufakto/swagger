from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.schemas import SchemaGenerator
from rest_framework.permissions import AllowAny
from rest_framework_swagger import renderers

# Create your views here.

class Home(APIView):
    def get(self, request, format=None):
        # generator = SchemaGenerator()
        # schema = generator.get_schema(data={status:200, message: "Donal Siagian"})
        return Response(data="Donal Siagian", status=200)

# class Docs(APIView):
#     permission_classes = [AllowAny]
#     renderer_classes = [
#         renderers.OpenAPIRenderer,
#         renderers.SwaggerUIRenderer
#     ]
#     def get(self, request, format=None):
#         generator = SchemaGenerator()
#         schema = generator.get_schema(data={status:200, message: "Donal Siagian"})
#         return Response(schema)