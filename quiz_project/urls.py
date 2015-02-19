from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quiz_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'quiz_app.views.home', name='home'),
    url(r'^add-questions/$', 'quiz_app.views.add_questions', name='add_questions'),
    url(r'^login/$', 'quiz_app.views.login', name='login'),
    url(r'^logout/$', 'quiz_app.views.logout', name='logout'),
    url(r'^master-signup/$', 'quiz_app.views.master_signup', name='master_signup'),
    url(r'^my-results/$', 'quiz_app.views.my_results', name='my_results'),
    url(r'^profile/$', 'quiz_app.views.profile', name='profile'),
    url(r'^show-questions/$', 'quiz_app.views.show_questions', name='show_questions'),
    url(r'^start-quiz-index/$', 'quiz_app.views.start_quiz_index', name='start_quiz_index'),
    url(r'^start-quiz/(?P<quiz_id>\d+)/$', 'quiz_app.views.start_quiz', name='start_quiz'),
    url(r'^student-signup/$', 'quiz_app.views.student_signup', name='student_signup'),

    # grappelli url
    url(r'^grappelli/', include('grappelli.urls')),
    # Admin url
    url(r'^admin/', include(admin.site.urls)),
)
