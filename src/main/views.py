import json

from django.http import HttpResponse
from django.views import generic


class ApiListView(generic.ListView):
    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(json.dumps(self.response_data(), ensure_ascii=False), content_type='application/json')

    def response_data(self):
        return []
