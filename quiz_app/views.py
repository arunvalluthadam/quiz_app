from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.csrf import csrf_exempt
from .decorators import is_master, is_student
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from .models import *
from .forms import *

# Create your views here.
def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/?next=%s' % request.path)
	else:
		employee = get_object_or_404(User,email=request.user.email)


	variables = RequestContext(request, {
		'employee': employee,
	})
	return render_to_response('index.html', variables)


def show_questions(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/?next=%s' % request.path)
	else:
		employee = get_object_or_404(User,email=request.user.email)
	
	# show_questions = get_object_or_404(QuizQuestions,quiz=employee)
	show_questions = QuizQuestions.objects.filter(quiz=employee)
	print show_questions
	variables = RequestContext(request, {
		'show_questions': show_questions,
	})
	return render_to_response('show_questions.html', variables)


@csrf_exempt
def add_questions(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/?next=%s' % request.path)
	else:
		employee = get_object_or_404(Signup,email=request.user.email)
	print employee
	if request.method == "POST":
		print "This is POST"
		form = QuizQuestionsForm(request.POST)
		
		if form.is_valid():
			print "is_valid"
			service_form = form.save(commit=False)
			print "Good!!!!"
			print employee
			service_form.quiz = employee
			print service_form.quiz
			service_form.save()
			print 'service saved'
			return HttpResponseRedirect('/show-questions')
		else:
			print form.errors

	form = QuizQuestionsForm()
	variables = RequestContext(request, {
		'add_form': form,
		# 'success':success,
		# 'success_message':success_message
	})
	return render_to_response('add_questions.html', variables)

@csrf_exempt
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            # print username
            password = request.POST['password']
            # print password
            # author = Signup.objects.get(email=username)
            # print author.email
            # print author.check_password(password)
            user = auth.authenticate(username=username, password=password)
            # if author.email == username and author.check_password(password):
            #     user = True
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/') #redirect after POST
            else:
                return HttpResponseRedirect('/login')
    variables = RequestContext(request, {'form':form})

    return render_to_response('login.html', variables)

@csrf_exempt
def master_signup(request):
	form = SignupForm()
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			master = form.save(commit=False)
			master.is_master = True
			password1 = request.POST['password1']
			print password1
			password2 = request.POST['password2']
			print password2
			if password1 == password2:
				password = password1
			else:
				print "password is not Same ...."
			master.set_password(password)
			print master.password
			master.save()
			return HttpResponseRedirect('/login')
		else:
			print form.errors

	variables = RequestContext(request, {
        'master_form':form,
        })
	return render_to_response('master_signup.html', variables)

@csrf_exempt
def student_signup(request):
	form = SignupForm()
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			student = form.save(commit=False)
			student.is_student = True
			password1 = request.POST['password1']
			password2 = request.POST['password2']
			if password1 == password2:
				password = password1
			else:
				print "password is not Same ...."
			student.set_password(password)
			student.save()
			return HttpResponseRedirect('/')
		else:
			print form.errors

	variables = RequestContext(request, {
        'student_form':form,
        })
	return render_to_response('student_signup.html', variables)

# @is_student
def my_results(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/?next=%s' % request.path)
	else:
		employee = get_object_or_404(User,email=request.user.email)
	variables = RequestContext(request, {
		'employee': employee,
	})
	return render_to_response('my_result.html', variables)

def profile(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/?next=%s' % request.path)
	else:
		employee = get_object_or_404(User,email=request.user.email)
	profile = get_object_or_404(User,email=request.user.email)
	variables = RequestContext(request, {
		'employee': employee,
		'profile': profile,
	})
	return render_to_response('profile.html', variables)

def start_quiz_index(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/?next=%s' % request.path)
	else:
		employee = get_object_or_404(User,email=request.user.email)
		
	check_questions = QuizQuestions.objects.all() # filter(quiz=employee)

	variables = RequestContext(request, {
		'check_questions': check_questions,
	})
	return render_to_response('start_quiz_index.html', variables)

# @is_student
@csrf_exempt
def start_quiz(request, quiz_id=1):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/?next=%s' % request.path)
	else:
		employee = get_object_or_404(User,email=request.user.email)
	check_questions = QuizQuestions.objects.get(id=quiz_id)
	# seperate = []
	# for start in check_questions:
	# 	seperate.append(start)
	# print seperate
	variables = RequestContext(request, {
		'check_questions': check_questions,
		# 'seperate': seperate,
	})
	return render_to_response('start_quiz.html', variables)

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/login')
