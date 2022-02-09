import json
from django.http import HttpResponse
from rest_framework import viewsets
from community.models import Community
from community.serializers import CommunitySerializer


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


def community_list(request):
    qs = Community.objects.all()
    data = [
        {
            "community_num": community.community_num,
            "title": community.title,
            "content": community.content,
            "img1": community.img1,
            "img2": community.img2,
            "img3": community.img3,
            "img4": community.img4,
            "img5": community.img5,
            "registration_date": community.registration_date,
            "user_id": community.user_id,


        }
        for community in qs
    ]
    json_string = json.dumps(data)
    return HttpResponse(json_string)
