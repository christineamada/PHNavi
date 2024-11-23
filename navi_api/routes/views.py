from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Route
from .serializers import RouteSerializer

class RouteListView(APIView):
    def get(self, request):
        serializer = RouteSerializer(data=routes, many=True)
        serializer.is_valid()
        return Response(serializer.data)