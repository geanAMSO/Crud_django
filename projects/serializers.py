from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        #escribe las columnas como estan en el modelo
        fields = ('id','title','description','technology','create_at')
        #no se puede rescribir 
        read_only_fields = ('create_at',)
