from .models import Trek,Itenary
from rest_framework import serializers

class TrekSerializer(serializers.ModelSerializer):
   class Meta:
      model=Trek
      fields='__all__'

class ItenarySerializer(serializers.ModelSerializer):
   class Meta:
      model=Itenary
      fields='__all__'