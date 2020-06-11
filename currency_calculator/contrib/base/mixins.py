from django.http import HttpResponseBadRequest


class AjaxRequestMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest('Bad Request')

        return super().dispatch(request, *args, **kwargs)
