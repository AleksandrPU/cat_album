from datetime import datetime as dt

from django.db import transaction
from rest_framework import serializers

from cats.fields import Base64ImageField, Hex2NameColor
from cats.models import Achievement, Cat


class AchievementSerializer(serializers.ModelSerializer):
    achievement_name = serializers.CharField(source='name')

    class Meta:
        model = Achievement
        fields = ('id', 'achievement_name')


class CatSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(required=False, many=True)
    color = Hex2NameColor()
    age = serializers.SerializerMethodField()
    image = Base64ImageField(required=False, allow_null=True)
    image_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cat
        fields = (
            'id',
            'name',
            'color',
            'birth_year',
            'achievements',
            'owner',
            'age',
            'image',
            'image_url',
        )
        read_only_fields = ('owner',)

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def get_age(self, obj):
        return dt.now().year - obj.birth_year

    def add_achievements(self, cat, achievements):
        achievement_objects = []
        for achievement in achievements:
            current_achievement, status = Achievement.objects.get_or_create(
                **achievement
            )
            achievement_objects.append(current_achievement)

        cat.achievements.set(achievement_objects)

    @transaction.atomic
    def create(self, validated_data):
        achievements = []
        if 'achievements' in validated_data:
            achievements = validated_data.pop('achievements')

        cat = Cat.objects.create(**validated_data)

        self.add_achievements(cat, achievements)

        return cat

    @transaction.atomic
    def update(self, instance, validated_data):
        achievements = []
        if 'achievements' in validated_data:
            achievements = validated_data.pop('achievements')

        super().update(instance, validated_data)

        if achievements:
            instance.set_achievements.all().delete()

            self.add_achievements(instance, achievements)

        return instance
