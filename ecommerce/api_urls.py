from rest_framework.routers import SimpleRouter

from ecommerce import api_views

router = SimpleRouter()

router.register('cars', api_views.CarViewSet, 'cars')
router.register('search/cars', api_views.CarSearchViewSet, 'cars_search')

urlpatterns = router.urls
