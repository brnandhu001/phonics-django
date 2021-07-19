from import_export import resources
from .models import word

class WordResource(resources.ModelResource):
    class Meta:
        model =word