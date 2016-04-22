from rest_framework import serializers
from .models import Vote, PollSubject, Poll

class VoteSerializer(serializers.ModelSerializer):
    class Meta:

        model = PollSubject
        fields = ('id', 'name', 'votes', 'total_votes')


class PollSubjectSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True)

    class Meta:
        model = PollSubject
        fields = ('id', 'name', 'votes', 'total_votes')
