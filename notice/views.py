from rest_framework import viewsets
from notice.models import Notice
from notice.serializers import NoticeSerializer, NoticeCreateSerializer
from rest_framework.pagination import PageNumberPagination


class NoticePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1


class NoticeCreateViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeCreateSerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    pagination_class = NoticePagination

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query)

        return qs





