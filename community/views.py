import json
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from community.models import Community
from community.serializers import CommunitySerializer, CommunityCreateSerializer


class CommunityPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    pagination_class = CommunityPagination

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query)

        return qs

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return CommunityCreateSerializer
        else:
            return CommunitySerializer


# def community_list(request):
#     qs1 = Community.objects.all()
#     data = [
#         {
#             "community_num": community.community_num,
#             "title": community.title,
#             "content": community.content,
#             "img1": community.img1,
#             "img2": community.img2,
#             "img3": community.img3,
#             "img4": community.img4,
#             "img5": community.img5,
#             "registration_date": community.registration_date,
#             "user_id": community.user_id,
#
#
#         }
#         for community in qs1
#     ]
#     json_string = json.dumps(data)
#     return HttpResponse(json_string)
