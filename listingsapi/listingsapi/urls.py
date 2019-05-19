from django.conf.urls import url
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from listings_api import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"^$", views.api_root),
    url(r"^listings/$", views.ListingsView.as_view(), name="listings-view"),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
