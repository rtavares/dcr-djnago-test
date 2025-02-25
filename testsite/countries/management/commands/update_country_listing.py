import requests
from countries.models import Country, Region
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Loads country data from a JSON file."

    DATA_SOURCE_URL = "https://storage.googleapis.com/dcr-django-test/countries.json"

    def get_data(self):
        data = []
        try:
            response = requests.get(self.DATA_SOURCE_URL)
        except requests.exceptions.HTTPError as http_err:
            raise RuntimeError(f"HTTP error occurred: {http_err}") from http_err
        except requests.exceptions.ConnectionError as conn_err:
            raise RuntimeError("Failed to connect to the server.") from conn_err
        except requests.exceptions.Timeout as timeout_err:
            raise RuntimeError("The request timed out.") from timeout_err
        except requests.exceptions.RequestException as req_err:
            raise RuntimeError(f"An unexpected error occurred: {req_err}") from req_err
        else:
            data = response.json()

        return data

    def handle(self, *args, **options):
        data = self.get_data()
        for row in data:
            region, region_created = Region.objects.get_or_create(name=row["region"])
            if region_created:
                self.stdout.write(
                    self.style.SUCCESS("Region: {} - Created".format(region))
                )
            country, country_created = Country.objects.get_or_create(
                name=row["name"],
                defaults={
                    "alpha2Code": row["alpha2Code"],
                    "alpha3Code": row["alpha3Code"],
                    "population": row["population"],
                    "region": region,
                    "capital": row["capital"],
                    "top_level_domains": row["topLevelDomain"],
                },
            )

            self.stdout.write(
                self.style.SUCCESS(
                    "{} - {}".format(
                        country, "Created" if country_created else "Updated"
                    )
                )
            )
