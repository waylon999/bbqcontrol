from rest_framework import generics
from bbq.models import Bbq
from bbq.serializers import BbqSerializer

class BbqList(generics.ListCreateAPIView):
    """
    List the bbq equipement
    """
    model = Bbq
    serializer_class = BbqSerializer

class BbqDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Bbq
    serializer_class = BbqSerializer

