from rest_framework import serializers
from .models import Lead, LeadPhoto

class LeadPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadPhoto
        fields = ('id', 'image', 'uploaded_at')

class LeadSerializer(serializers.ModelSerializer):
    """Public serializer - used for creating leads from the website form."""
    photos = LeadPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Lead
        fields = '__all__'
        read_only_fields = ('status', 'created_at', 'photos')


class LeadAdminSerializer(serializers.ModelSerializer):
    """Admin serializer - allows updating status and all fields."""
    service_title = serializers.CharField(source='service.title', read_only=True)
    photos = LeadPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Lead
        fields = '__all__'
        read_only_fields = ('created_at', 'photos')
