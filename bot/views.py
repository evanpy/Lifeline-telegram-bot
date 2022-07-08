from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from bot.models import Session
from bot.serializers import Session_Serializer

@api_view(['GET'])
def all_sessions(request):
    sessions = Session.objects.all()
    serialized_sessions = Session_Serializer(sessions, many=True)
    return Response(serialized_sessions.data)

@api_view(['GET'])
def vacant_session(request):
    session = Session.objects.filter(vacant=True).order_by("-createdAt")
    if (len(session) == 0):
        return Response(session)
    serialized_session = Session_Serializer(session[0], many=False)
    return Response(serialized_session.data)

@api_view(['GET'])
def detail_session(request, pk):
    session = Session.objects.get(id=pk)
    serialized_session = Session_Serializer(session, many=False)
    return Response(serialized_session.data)

@api_view(['POST'])
def create_session(request):
    serialized_session = Session_Serializer(data=request.data)
    if serialized_session.is_valid(): serialized_session.save()
    return Response(serialized_session.data)

@api_view(['POST'])
def update_session(request, pk):
    sessionData = request.data
    session = Session.objects.get(id=pk)
    serialized_session = Session_Serializer(session, data=sessionData)
    if serialized_session.is_valid():
        serialized_session.save()
        return Response(serialized_session.data)
    return Response(serialized_session.errors, status=status.HTTP_400_BAD_REQUEST)
