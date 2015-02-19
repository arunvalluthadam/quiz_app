from django.http import HttpResponseRedirect
from quiz_app.models import Signup




def is_master(f):
	def wrap(request, *args, **kwargs):
		try:
			userdetail=Signup.objects.get(email= request.user)
			if not userdetail.is_master:
				return HttpResponseRedirect("/logout")
		except:
			return HttpResponseRedirect("/logout")
		return f(request, *args, **kwargs)
	wrap.__doc__=f.__doc__
	wrap.__name__=f.__name__
	return wrap
	
def is_student(f):
	def wrap(request, *args, **kwargs):
		try:
			userdetail=Signup.objects.get(email= request.user)
			if not userdetail.is_student:
				return HttpResponseRedirect("/logout")
		except:
			return HttpResponseRedirect("/logout")
		return f(request, *args, **kwargs)
	wrap.__doc__=f.__doc__
	wrap.__name__=f.__name__
	return wrap

