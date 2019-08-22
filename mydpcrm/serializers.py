from mydpcrm.models import User
from rest_framework import serializers
from .models import NewLeads, ColdLeads, InstalledLeads, ScheduledLeads,ConvertedLeads , LeadNotes, ReferralTbl, ReferralNotes

class NewLeadsSerializers(serializers.ModelSerializer):

    class Meta:
        model = NewLeads
        #fields = ('__all__')
        exclude = ('user','enquiryDate',)
        #read_only_fields = ('user',)

class NewColdLeadsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ColdLeads
        #fields = ('__all__')
        exclude = ('user','coldDate',)
        #read_only_fields = ('user',)

class ReferralLeadsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ReferralTbl
        exclude = ('user','enquiryDate',)

class ScheduledLeadsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ScheduledLeads
        exclude = ('user','scheduledDate',)

class InstalledLeadsSerializers(serializers.ModelSerializer):

    class Meta:
        model = InstalledLeads
        exclude = ('user','installationDate',)

class ConvertedLeadsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ConvertedLeads
        exclude = ('user','convertedDate',)

class LeadNotesSerializers(serializers.ModelSerializer):

    class Meta:
        model = LeadNotes
        exclude = ('DateTime','user',)

class ReferralNotesSerializers(serializers.ModelSerializer):

    class Meta:
        model = ReferralNotes
        exclude = ('user','timestamp',)