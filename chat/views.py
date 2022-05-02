from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment
from .serializers import CommentSerializer


class CommentView(APIView):
    def get(self, request, comment_id=""):
        comment = Comment.objects.all()

        serializer = CommentSerializer(comment, many=True)

        if comment_id:
            try:
                comment = Comment.objects.get(id=comment_id)
                serializer = CommentSerializer(comment)
            except ObjectDoesNotExist:
                return Response(
                    {"errors": "invalid comment_id"}, status=status.HTTP_404_NOT_FOUND
                )

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        comment = Comment.objects.create(**serializer.validated_data)
        serializer = CommentSerializer(comment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
