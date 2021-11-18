from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = [
    # 'pub_date',
    # 'question_text'
    # ]

    inlines = [ChoiceInline]

    list_display = (
        'question_text',
        'pub_date',
        'was_published_recently'
    )


admin.site.register(Question, QuestionAdmin)
