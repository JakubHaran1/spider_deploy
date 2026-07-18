from rest_framework import serializers

from spider_app.models import User, Tag, Spider, Spider_img


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        password_val = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password_val)
        user.save()
        return user

    def update(self, instance, validated_data):
        password_val = validated_data.pop("password")

        for atr, val in validated_data.items():
            setattr(instance, atr, val)

        if self.password:
            setattr(instance, "password", password_val)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["tag"]


class SpiderImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spider_img
        fields = ["img"]


class SpiderSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags_detail = TagSerializer(source="tags", many=True, read_only=True)
    spider_img_detail = SpiderImgSerializer(
        source="spiders_img", many=True, read_only=True)

    tags = serializers.CharField(
        write_only=True, required=False)

    spider_img = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Spider

        fields = ["id", "name", "author", "type", "description",
                  "tags", "date_created", "spider_img", "spider_img_detail", "tags_detail"]

    def create(self, validated_data):
        tags_data = validated_data.pop("tags")

        img_data = validated_data.pop("spider_img")
        spider_obj = Spider.objects.create(**validated_data)
        Spider_img.objects.create(spider=spider_obj, img=img_data)
        tags = []
        tags_arr = tags_data.split(",")
        for tag in tags_arr:
            name_clean = tag.strip().lower()
            tag_obj, _ = Tag.objects.get_or_create(
                tag=name_clean)
            tags.append(tag_obj)

        spider_obj.tags.set(tags)

        return spider_obj

    def update(self, instance, validated_data):
        tags_data = validated_data.pop("tags")

        img_data = validated_data.pop("spider_img")
        Spider_img.objects.create(spider=instance, img=img_data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        tags = []
        tags_arr = tags_data.split(",")

        for tag in tags_arr:
            name_clean = tag.strip().lower()

            tag_obj, _ = Tag.objects.get_or_create(
                tag=name_clean)
            tags.append(tag_obj)

        instance.tags.set(tags)

        return instance
