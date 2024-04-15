from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from home.models import Information, About, Call, SocialMedia, Footer, Feature


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'title', 'description']


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['id', 'title', 'slogan', 'description', 'seo_content']


class AboutSerializer(serializers.ModelSerializer):
    content_html = SerializerMethodField()
    def get_content_html(self, instance):
        return str(instance.content.html)

    class Meta:
        model = About
        fields = ['id', 'title', 'content_html']




class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['id', 'name', 'icon_image', 'url']


class FooterSerializer(serializers.ModelSerializer):
    social_medias = SocialMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Footer
        fields = ['id', 'title', 'description', 'address', 'address_caption', 'email', 'email_caption',
                  'phone', 'phone_caption', 'social_medias']


class CallSerializer(serializers.ModelSerializer):
    social_medias = SocialMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Call
        fields = ['title', 'social_medias']


