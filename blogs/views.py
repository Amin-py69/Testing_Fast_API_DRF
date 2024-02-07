from .serializers import BlogSerializer, CommentSerializer
from rest_framework import status
from .models import Blogs
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class BlogShowView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Blogs.objects.all()
        paginator = PageNumberPagination()
        result = paginator.paginate_queryset(queryset=queryset, request=request)
        serializer = BlogSerializer(instance=result, many=True)
        return Response(data=serializer.data)


class BlogDetailView(APIView):
    def post(self, request, pk):
        queryset = Blogs.objects.get(id=pk)
        serializer = BlogSerializer(instance=queryset)
        return Response(data=serializer.data)


class BlogAddView(APIView):
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.validated_data['user'] = request.user
            serializer.save()
            return Response({'message': 'added'})
        return Response(serializer.errors)


class BlogUpdateView(APIView):
    def put(self, request, pk):
        queryset = Blogs.objects.get(id=pk)
        serializer = BlogSerializer(instance=queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'updated'})
        return Response(serializer.errors)


class BlogDeleteView(APIView):
    def delete(self, request, pk):
        queryset = Blogs.objects.get(id=pk)
        queryset.delete()
        return Response({'message': 'delete'})


class CheckToken(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        user = request.user
        return Response({'user': user.username})


class ShowCommentView(APIView):
    def get(self, request):
        queryset = Blogs.objects.all()
        serializer = CommentSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
