from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Footer


class FooterModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Footer
        fields = [
            'contact_details',
            'copyright',
            ]