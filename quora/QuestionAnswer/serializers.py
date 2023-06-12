from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    unlikes = serializers.SerializerMethodField()

    def get_likes(self, obj):
        return obj.likes.count()

    def get_unlikes(self, obj):
        return obj.unlikes.count()

    class Meta:
        model = Answer
        fields = ['id', 'content', 'likes', 'unlikes']
