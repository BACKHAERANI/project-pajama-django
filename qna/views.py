import json
from django.http import HttpResponse
from rest_framework import viewsets
from qna.models import Qna
from qna.serializers import QnaSerializer


class QnaViewSet(viewsets.ModelViewSet):
    queryset = Qna.objects.all()
    serializer_class = QnaSerializer


def qna_list(request):
    qs = Qna.objects.all()
    data = [
        {
            "qna_num": qna.qna_num,
            "title": qna.title,
            "content": qna.content,
            "answer": qna.answer,
            "img": qna.img,
            "registration_date": qna.registration_date,
            "user_id": qna.user_id,
        }
        for qna in qs
    ]
    json_string = json.dumps(data)
    return HttpResponse(json_string)
