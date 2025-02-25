import json

from django.db import models


class Country(models.Model):
    """Note about the top_level_domain field:
    - In the API to ingest the data, the Top leve; domain is return as a list, that may contain more than one value.
     So, we need a way to store one or more values in the same field.
    - The standard approach would be to use the models.JSONField(), that exists in Django since version 3.1.
    - However, this project is using Django 2.2, that does not support this feature.
    - The proper approach to this task would be to upgrade Django to a newer version.
    - However, I'm assuming that this is part of the challenge - finding an alternative solution.
    - So, we went with the present solution:
        a TextField that stores serialized JSON, with the required helper functions.
    - Another alternative would be to create an additional table for TLDs with a relation to the Countries table.
        However, this would be more time consuming - and inefficient from the perspective of data management, once the TLDs are unique.
    """

    name = models.CharField(max_length=100)
    alpha2Code = models.CharField(max_length=2)
    alpha3Code = models.CharField(max_length=3)
    population = models.IntegerField()
    capital = models.CharField(max_length=100)
    top_level_domains = models.TextField()
    region = models.ForeignKey(
        "Region",
        on_delete=models.CASCADE,
        related_name="countries",
    )

    def set_top_level_domains(self, tld_list):
        try:
            self.values = json.dumps(tld_list)
        except (TypeError, ValueError) as e:
            raise ValueError(f"Error serializing Top Level Domain: {e}")

    def get_top_level_domains(self):
        try:
            return json.loads(self.top_level_domains)
        except (json.JSONDecodeError, ValueError) as e:
            raise ValueError(f"Error deserializing values for Top Level Domain: {e}")

    def save(self, *args, **kwargs):
        try:
            if isinstance(self.top_level_domains, list):
                self.set_top_level_domains(self.top_level_domains)
            super().save(*args, **kwargs)
        except ValueError as e:
            raise ValueError(f"Error saving Country instance: {e}")

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
