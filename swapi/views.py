from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.core.cache import cache

from resources.utils import get_resource_stats

DEFAULT_HITS = 50000


def index(request):
    data = cache.get('resource_data')
    if not data:
        data = get_resource_stats()
        cache.set('resource_data', data, 10000)
    return render_to_response(
        'index.html',
        data
    )


def documentation(request):
    return render_to_response("documentation.html")

