from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from .models import NewLeads,ColdLeads,InstalledLeads,ScheduledLeads,ReferralNotes,ReferralTbl,LeadNotes, ConvertedLeads
from .serializers import NewLeadsSerializers,NewColdLeadsSerializers,ReferralLeadsSerializers,ScheduledLeadsSerializers, ConvertedLeadsSerializers, LeadNotesSerializers, ReferralNotesSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
# Create your views here.

class NewLeadsCreateOrGet(APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        nl = NewLeads.objects.all()
        serializer = NewLeadsSerializers(nl, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewLeadsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateLeadsOrGet(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, pk):
        try:
            return NewLeads.objects.get(pk=pk)
        except NewLeads.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ul = self.get_object(pk)
        serializer = NewLeadsSerializers(ul)
        #return Response({"message":"success","Result":serializer.data})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ul = self.get_object(pk)
        #ul.leadSource = "Cold"
        serializer = NewLeadsSerializers(ul, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewColdLeadsCreateOrGet(APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        nl = ColdLeads.objects.all()
        serializer = NewColdLeadsSerializers(nl, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewColdLeadsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateColdLeadsOrGet(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, pk):
        try:
            return ColdLeads.objects.get(pk=pk)
        except ColdLeads.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ul = self.get_object(pk)
        serializer = NewColdLeadsSerializers(ul)
        #return Response({"message":"success","Result":serializer.data})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ul = self.get_object(pk)
        #ul.leadSource = "Cold"
        serializer = NewColdLeadsSerializers(ul, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReferralLeadsCreateOrGet(APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        nl = ReferralTbl.objects.all()
        serializer = ReferralLeadsSerializers(nl, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReferralLeadsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateReferralLeadsOrGet(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, pk):
        try:
            return ReferralTbl.objects.get(pk=pk)
        except ReferralTbl.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ul = self.get_object(pk)
        serializer = ReferralLeadsSerializers(ul)
        #return Response({"message":"success","Result":serializer.data})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ul = self.get_object(pk)
        #ul.leadSource = "Cold"
        serializer = ReferralLeadsSerializers(ul, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduledLeadsCreateOrGet(APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        nl = ScheduledLeads.objects.all()
        serializer = ScheduledLeadsSerializers(nl, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScheduledLeadsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateScheduledLeadsOrGet(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, pk):
        try:
            return ScheduledLeads.objects.get(pk=pk)
        except ScheduledLeads.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ul = self.get_object(pk)
        serializer = ScheduledLeadsSerializers(ul)
        #return Response({"message":"success","Result":serializer.data})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ul = self.get_object(pk)
        #ul.leadSource = "Cold"
        serializer = ScheduledLeadsSerializers(ul, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConvertedLeadsCreateOrGet(APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        nl = ConvertedLeads.objects.all()
        serializer = ConvertedLeadsSerializers(nl, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ConvertedLeadsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateConvertedLeadsOrGet(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, pk):
        try:
            return ConvertedLeads.objects.get(pk=pk)
        except ConvertedLeads.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ul = self.get_object(pk)
        serializer = ConvertedLeadsSerializers(ul)
        #return Response({"message":"success","Result":serializer.data})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ul = self.get_object(pk)
        #ul.leadSource = "Cold"
        serializer = ConvertedLeadsSerializers(ul, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeadNotesCreateOrGet(APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        nl = LeadNotes.objects.all()
        serializer = LeadNotesSerializers(nl, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LeadNotesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateLeadNotesOrGet(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, pk):
        try:
            return LeadNotes.objects.get(pk=pk)
        except LeadNotes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ul = self.get_object(pk)
        serializer = LeadNotesSerializers(ul)
        #return Response({"message":"success","Result":serializer.data})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ul = self.get_object(pk)
        #ul.leadSource = "Cold"
        serializer = LeadNotesSerializers(ul, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReferralNotesCreateOrGet(APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        nl = ReferralNotes.objects.all()
        serializer = ReferralNotesSerializers(nl, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReferralNotesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateReferralNotesOrGet(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, pk):
        try:
            return ReferralNotes.objects.get(pk=pk)
        except ReferralNotes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ul = self.get_object(pk)
        serializer = ReferralNotesSerializers(ul)
        #return Response({"message":"success","Result":serializer.data})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ul = self.get_object(pk)
        #ul.leadSource = "Cold"
        serializer = ReferralNotesSerializers(ul, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
