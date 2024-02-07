from django.shortcuts import get_object_or_404
from .models import RichMans
from .serializers import RichManSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class RichManViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = RichMans.objects.all()
        paginator = PageNumberPagination()
        result = paginator.paginate_queryset(queryset=queryset, request=request)
        serializer = RichManSerializer(instance=result, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = RichMans.objects.get(id=pk)
        serializer = RichManSerializer(instance=queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = RichManSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages('you can not creating'))

    def update(self, request, pk:None):
        queryset = RichMans.objects.all()
        rich_man = get_object_or_404(queryset, id=pk)
        serializer = RichManSerializer(instance=rich_man, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'updated'}, status=status.HTTP_200_OK)
        return Response(serializer.error_messages('you can not updated'))

    def destroy(self, request, pk:None):
        queryset = RichMans.objects.get(id=pk)
        queryset.delete()
        return Response({'message': 'deleted'})

