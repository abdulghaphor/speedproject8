from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView,DestroyAPIView,CreateAPIView
from datetime import datetime
from .models import *
from .serializers import *


class HumanList(ListAPIView):
	queryset = Human.objects.all()
	serializer_class = HumanSerializer

class HumanCreate(CreateAPIView):
	queryset = Human.objects.all()
	serializer_class = HumanSerializer