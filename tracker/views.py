from django.shortcuts import render
from rest_framework import viewsets
from .models import CivicIssue
from .serializers import CivicIssueSerializer
import math

# Existing API ViewSet
class CivicIssueViewSet(viewsets.ModelViewSet):
    queryset = CivicIssue.objects.all()
    serializer_class = CivicIssueSerializer

    def get_queryset(self):
        lat = self.request.query_params.get('lat')
        lng = self.request.query_params.get('lng')
        radius = self.request.query_params.get('radius', 5)
        queryset = super().get_queryset()

        if lat and lng:
            lat = float(lat)
            lng = float(lng)
            radius = float(radius)

            def haversine(lat1, lon1, lat2, lon2):
                R = 6371  
                dlat = math.radians(lat2 - lat1)
                dlon = math.radians(lon2 - lon1)
                a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                return R * c

            queryset = [issue for issue in queryset if haversine(lat, lng, issue.latitude, issue.longitude) <= radius]

        return queryset

# New Form View
def report_form(request):
    return render(request, 'report_form.html')
