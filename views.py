from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sample
from .serializers import SampleSerializer

class SampleView(APIView):
    def get(self, request):
        data = Sample.objects.all()
        serializer = SampleSerializer(data, many=True)
        return Response(serializer.data)
