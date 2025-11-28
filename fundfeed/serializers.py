from rest_framework import serializers
from .models import Profile, Interest


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ["id", "name"]


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    interests = InterestSerializer(many=True, read_only=True)
    interest_ids = serializers.PrimaryKeyRelatedField(
        queryset=Interest.objects.all(), many=True, write_only=True, required=False
    )

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "name",
            "role",
            "bio",
            "location",
            "profile_picture",
            "interests",
            "interest_ids",
            "created_at",
        ]
        read_only_fields = ["created_at"]

    def update(self, instance, validated_data):
        interest_ids = validated_data.pop("interest_ids", None)

        profile = super().update(instance, validated_data)

        if interest_ids is not None:
            profile.interests.set(interest_ids)

        return profile




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        write_only=True,
        required=False
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "uploader",
            "video_file",
            "description",
            "tags",
            "tag_ids",
            "created_at",
        ]
        read_only_fields = ["created_at"]

    def create(self, validated_data):
        tag_ids = validated_data.pop("tag_ids", [])
        post = Post.objects.create(**validated_data)
        post.tags.set(tag_ids)
        return post