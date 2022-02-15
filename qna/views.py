from rest_framework import viewsets
from qna.models import Qna
from qna.serializers import QnaSerializer, QnaCreateSerializer


class QnaViewSet(viewsets.ModelViewSet):
    queryset = Qna.objects.all()
    serializer_class = QnaSerializer

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return QnaCreateSerializer
        else:
            return QnaSerializer



