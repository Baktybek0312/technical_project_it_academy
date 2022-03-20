from rest_framework import serializers

from .models import InfoHabrs


class InfoHabrSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfoHabrs
        fields = (
            'title',
            'url'
        )

    def create(self, validated_data):
        return InfoHabrs.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.save()
        return instance
