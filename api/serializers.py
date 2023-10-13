from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    body = serializers.CharField()
    author = serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Post.objects.create(**validated_data)  
    
    def update(self,instance,validated_data):
        print(instance.title)
        instance.title=validated_data.get('title',instance.title)
        print(instance.title)
        instance.body=validated_data.get('body',instance.body)
        instance.author=validated_data.get('author',instance.author)
        instance.save()
        return instance