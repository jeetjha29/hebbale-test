from rest_framework import serializers
from myapp.models import CategoryView

class AddCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryView
        fields = "__all__"

class ListCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryView
        fields = "__all__"