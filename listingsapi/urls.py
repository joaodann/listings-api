import requests
import asyncio
import json
import threading
from django.conf.urls import url
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from listings_api import views
from listings_api import cache
from listings_api import models
from django.conf import settings


def loop_in_thread(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(json_load())


@asyncio.coroutine
def json_load():
    print("start jsonload")
    decoded_json = ""
    json_data = requests.get(
        settings.LISTINGS_URL, verify=False, timeout=30, stream=True
    )
    for line in json_data.iter_lines():
        if line:
            decoded_line = line.decode("utf-8")
            decoded_json += decoded_line
            print("loop jsonload")

    json_decoded = json.loads(
        decoded_json, object_hook=models.Listing.from_dict
    )
    cache.create_cache(json_decoded)


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
# thread do get json data
loop = asyncio.get_event_loop()
t = threading.Thread(target=loop_in_thread, args=(loop,))
t.start()
