from rest_framework import serializers
from bbq.models import Bbq

class BbqSerializer(serializers.HyperlinkedModelSerializer):
    api_url = serializers.SerializerMethodField('get_api_url')
    class Meta:
        model = Bbq
        fields = ('id', 'name', 'description', 'created_on')

    def get_api_url(self, obj):
        return '#/bbq/%s' % obj.id

