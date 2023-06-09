from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from ecommerce import documents


class CarSerializer(DocumentSerializer):
    class Meta:
        document = documents.CarDocument
        fields = (
            'id',
            'name',
            'price',
            'cylinder_count',
            'passenger_count',
            'color',
            'cylinder_volume',
            'owner_name',
        )
