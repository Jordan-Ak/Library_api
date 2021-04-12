from rest_framework.pagination import LimitOffsetPagination
from .ad_variables import pagination_max_limit

class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
    # Set the maximum limit value to settings value
    max_limit = pagination_max_limit