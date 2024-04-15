from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
from .models import Information, Feature, About, Call, SocialMedia, Footer
from .serializers import InformationSerializer, FeatureSerializer, AboutSerializer, CallSerializer, SocialMediaSerializer, FooterSerializer

# Create your views here.


@api_view(['GET'])
def information_view(request):
    information = get_object_or_404(Information)
    serializer = InformationSerializer(information)
    return Response(serializer.data)


@api_view(['GET'])
def feature_view(request):
    feature = Feature.objects.all()
    serializer = FeatureSerializer(feature,  many=True)
    return Response(serializer.data)


@api_view(['GET'])
def about_view(request):
    about = get_object_or_404(About)
    serializer = AboutSerializer(about)
    return Response(serializer.data)


@api_view(['GET'])
def call_view(request):
    call = get_object_or_404(Call)
    serializer = CallSerializer(call)
    return Response(serializer.data)


@api_view(['GET'])
def social_media_view(request):
    social_media = SocialMedia.objects.all()
    serializer = SocialMediaSerializer(social_media, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def footer_view(request):
    footer = get_object_or_404(Footer)
    serializer = FooterSerializer(footer)
    return Response(serializer.data)


def home(request):
    return render(request, 'home.html')
