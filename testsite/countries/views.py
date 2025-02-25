from django.db.models import Count, Sum
from django.http import JsonResponse

from .models import Region

def stats(request):
    """ Return stats by region """
    regions_stats = Region.objects.annotate(
        number_countries=Count('countries'),
        total_population=Sum('countries__population'),
    ).values('name', 'number_countries', 'total_population')

    return JsonResponse({'regions': list(regions_stats)})