import json

from django.http import HttpResponse


def json_response(x):
    return HttpResponse(json.dumps(x, indent=2), content_type='application/json; charset=UTF-8')
