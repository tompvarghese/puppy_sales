from rest_framework import serializers
from .models import Puppy, PuppyImage
from django.conf import settings

class PuppyImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = PuppyImage
        fields = ['id', 'image_url']

    def get_image_url(self, obj):
        # Returns the full URL of the image
        return settings.BASE_URL + obj.image.url if obj.image else None

class PuppySerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()  # Main image should return a full absolute URL
    additional_images = PuppyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Puppy
        fields = ['id', 'name', 'age', 'breed', 'description', 'price', 'main_image', 'additional_images', 'video']
        
    def get_main_image(self, obj):
        # Return the absolute URL for the main image
        return settings.BASE_URL + obj.main_image.url if obj.main_image else None
