from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task.models import TodoTask
from task.api.serializers import TodoTaskSerializer



@api_view(['GET'])
def task_list(request):
    if request.method == "GET":
        query = TodoTask.objects.all()
        serializer = TodoTaskSerializer(query, many=True)
        return Response(serializer.data)