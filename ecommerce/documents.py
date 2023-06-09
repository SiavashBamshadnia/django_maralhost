from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from ecommerce import models


@registry.register_document
class CarDocument(Document):
    id = fields.IntegerField()
    name = fields.TextField()
    price = fields.FloatField()
    cylinder_count = fields.IntegerField()
    passenger_count = fields.IntegerField()
    color = fields.TextField()
    cylinder_volume = fields.FloatField()
    owner_name = fields.TextField()

    class Index:
        name = 'cars'

    class Django:
        model = models.Car
