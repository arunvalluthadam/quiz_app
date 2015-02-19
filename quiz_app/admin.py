from django.contrib import admin
from .models import QuizQuestions, Signup #  QuizMaster,

# Register your models here.
class QuizQuestionsInline(admin.StackedInline):
	model = QuizQuestions
	extra = 1

# class QuizMasterAdmin(admin.ModelAdmin):
# 	model = QuizMaster
# 	list_display = ('quiz_master',)
# 	search_fields = ['quiz_master']
# 	inlines = [QuizQuestionsInline]

# admin.site.register(QuizMaster, QuizMasterAdmin)


class SignupAdmin(admin.ModelAdmin):
	model = Signup
	list_display = ('first_name','last_name','email','username')
	# search_fields = ['first_name','last_name','email','username',]
	inlines = [QuizQuestionsInline]

admin.site.register(Signup,SignupAdmin)