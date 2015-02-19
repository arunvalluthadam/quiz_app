from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .unique_slugify import unique_slugify

# Create your models here.

# ============================== Start signup ============================================

class Signup(User):
    is_master = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):  
        return self.first_name + " " + self.last_name

	class Meta:
		verbose_name = _("Signup")
		verbose_name_plural = _("Signup")



class QuizQuestions(models.Model):
	quiz = models.ForeignKey(Signup, null=True, blank=True)
	question = models.TextField()
	option1 = models.CharField(max_length=200)
	option2 = models.CharField(max_length=200)
	option3 = models.CharField(max_length=200)
	option4 = models.CharField(max_length=200)
	correct_answer = models.CharField(max_length=200)

	def __unicode__(self):
		return self.option1

	class Meta:
		verbose_name = ("Quiz Question")
		verbose_name_plural = ("Quiz Questions")


# # ============================== end signup ============================================



#  # ============================== question field =======================================
# class QuizMaster(models.Model):
# 	quiz_id =  models.CharField(verbose_name=_('Quiz ID'), max_length=100,null=True,blank=True)
# 	quiz_master = models.ForeignKey(User)

# 	def __unicode__(self):
# 		return "No. " + str(self.id)

# 	# def save(self, *args, **kwargs):
# 	# 	if not self.id:
# 	# 		unique_slugify(self,self.username)
# 	# 	super(QuizMaster, self).save(*args, **kwargs)

# 	def review_average(self):
# 		total = 0
# 		if self.employerfeedback_set.all():
# 			for review in self.employerfeedback_set.all():
# 				print review
# 				total +=  review.average()
# 			return int(total)/self.employerfeedback_set.all().count()
# 		else:
# 			return 0

# 	class Meta:
# 		verbose_name = ("Quiz Details")
# 		verbose_name_plural = ("Quiz Details")


# class QuizQuestions(models.Model):
# 	quiz = models.ForeignKey(QuizMaster, null=True, blank=True)
# 	question = models.TextField()
# 	option1 = models.CharField(max_length=200)
# 	option2 = models.CharField(max_length=200)
# 	option3 = models.CharField(max_length=200)
# 	option4 = models.CharField(max_length=200)
# 	correct_answer = models.CharField(max_length=200)

# 	def __unicode__(self):
# 		return self.option1

# 	class Meta:
# 		verbose_name = ("Quiz Question")
# 		verbose_name_plural = ("Quiz Questions")

# # ================================ End question field ===================================