from django.db.models import Count, Sum
from django.http import JsonResponse

from .models import Country, Region


def stats(request):
    """Return stats by region"""
    regions_stats = Region.objects.annotate(
        number_countries=Count("countries"),
        total_population=Sum("countries__population"),
    ).values("name", "number_countries", "total_population")

    return JsonResponse({"regions": list(regions_stats)})


def get_countries(request):
    """Return a list of countries"""
    # TBD: Get the region description
    # We have to be careful when using .all() in a real scenario
    # Pagination would be a good first approach.
    countries = Country.objects.all()

    return JsonResponse({"countries": list(countries.values())})
