from django_elasticsearch_dsl_drf.filter_backends import FilteringFilterBackend, CompoundSearchFilterBackend
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination as RestPageNumberPagination

from ecommerce import models, api_serializers, documents, document_serializers, permissions


class RestPagination(RestPageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CarViewSet(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = api_serializers.CarSerializer
    permission_classes = [permissions.IsUserInSaleGroup]
    pagination_class = RestPagination

    class Meta:
        ordering = ['-id']


class DocumentPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CarSearchViewSet(DocumentViewSet):
    document = documents.CarDocument
    serializer_class = document_serializers.CarSerializer
    lookup_field = 'id'
    permission_classes = [permissions.CanSearch]
    pagination_class = DocumentPagination
    filter_backends = [FilteringFilterBackend, CompoundSearchFilterBackend]
    search_fields = ('name', 'owner_name', 'color')
    multi_match_search_fields = ('name', 'owner_name', 'color')
    filter_fields = {
        'cylinder_count': 'cylinder_count',
        'passenger_count': 'passenger_count',
        'color': 'color',
        'cylinder_volume': 'cylinder_volume'
    }

    class Meta:
        ordering = ['-id']
