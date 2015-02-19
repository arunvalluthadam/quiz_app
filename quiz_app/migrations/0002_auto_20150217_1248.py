# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
                ('correct_answer', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Quiz Question',
                'verbose_name_plural': 'Quiz Questions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_master', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.DeleteModel(
            name='QuizQuestion',
        ),
        migrations.AddField(
            model_name='quizquestions',
            name='quiz',
            field=models.ForeignKey(blank=True, to='quiz_app.Signup', null=True),
            preserve_default=True,
        ),
    ]
