from rest_framework.permissions import BasePermission


class IsUserInSaleGroup(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.groups.filter(name='sale').exists()


class CanSearch(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('ecommerce.search_car')
