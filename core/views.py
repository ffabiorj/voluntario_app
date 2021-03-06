from core.models import Voluntario, Acao
from core.serializers import VoluntarioSerializer, AcaoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


class VoluntarioLista(APIView):
    """
    Uma simples viewset para listar todos voluntarios
    ou criar um novo.
    """

    def get(self, request, format=None):
        queryset = Voluntario.objects.all()
        serializer = VoluntarioSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = VoluntarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoluntarioDetalhe(APIView):
    """
    Recupera, atualizar ou deleta um voluntário.
    """

    def get_object(self, pk):
        try:
            return Voluntario.objects.get(pk=pk)
        except Voluntario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        voluntario = self.get_object(pk)
        serializer = VoluntarioSerializer(voluntario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        voluntario = self.get_object(pk)
        serializer = VoluntarioSerializer(voluntario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        voluntario = self.get_object(pk)
        voluntario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AcaoLista(APIView):
    """
    Uma simples viewset para listar todas ações
    ou criar uma nova.
    """

    def get(self, request, format=None):
        queryset = Acao.objects.all()
        serializer = AcaoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = AcaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AcaoDetalhe(APIView):
    """
    Recupera, atualizar ou deleta um ação.
    """

    def get_object(self, pk):
        try:
            return Acao.objects.get(pk=pk)
        except Acao.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        acao = self.get_object(pk)
        serializer = AcaoSerializer(acao)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        acao = self.get_object(pk)
        serializer = AcaoSerializer(acao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        acao = self.get_object(pk)
        acao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
