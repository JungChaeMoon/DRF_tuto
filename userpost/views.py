from django.shortcuts import render
from rest_framework.filters import SearchFilter

from .models import UserPost
from .serializer import UserPostSerializer
from rest_framework import viewsets
# Create your views here.


# class UserPostViewSet(viewsets.ModelViewSet):
#     queryset = UserPost.objects.all()
#     serializer_class = UserPostSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         if self.request.user.is_authenticated:
#             qs = qs.filter(author=self.request.user)
#         else:
#             qs = qs.none()
#
#         return qs


class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer

    filter_backends = [SearchFilter]
    search_fields = (
        'title',
    )
