from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    actions = ['delete_question']

    def delete_question(self, request, queryset):
        for question in queryset:
            Answer.objects.filter(question=question).delete()
            question.delete()

        self.message_user(request, "Selected question(s) and their answers have been deleted.")

    delete_question.short_description = "Delete selected questions and their answers"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'author', 'get_likes', 'get_unlikes']

    def get_likes(self, obj):
        return obj.likes.count()

    def get_unlikes(self, obj):
        return obj.unlikes.count()

    get_likes.short_description = 'Likes'
    get_unlikes.short_description = 'Unlikes'
