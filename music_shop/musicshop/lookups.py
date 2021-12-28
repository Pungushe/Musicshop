from ajax_select import register, LookupChannel
from .models import Artist


class CustomLookupChannel(LookupChannel):
    min_length = 3

    def check_auth(self, request):
        return None


@register('artist')
class ArtistLookup(LookupChannel):
    model = Artist


def get_query(self, q, request):
    return self.model.objects.filter(name__icontains=q).order_by('name')[:10]


