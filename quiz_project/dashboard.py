"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'jewella.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        # append a group for "Administration" & "Applications"
        
        
        # # append an app list module for "Applications"
        # self.children.append(modules.ModelList(
        #     _('Home'),
        #     column=1,
        #     collapsible=True,
        #     models=(
        #         'apps.church.models.Slider',
        #         'apps.church.models.ChurchPeople',
        #         'apps.church.models.Trustee',
        #         'apps.church.models.HomeDetails',
        #         ),
        # ))


        # self.children.append(modules.ModelList(
        #     _('Add Quiz Question'),
        #     column=1,
        #     collapsible=True,
        #     models=(
        #         'quiz_app.models.QuizMaster',
        #         ),
        # ))
        
        self.children.append(modules.ModelList(
            _('SignUp for both Master and Student'),
            column=1,
            collapsible=True,
            models=(
                'quiz_app.models.Signup',
                ),
        ))

        # self.children.append(modules.ModelList(
        #     _('Associations & Gallery'),
        #     column=1,
        #     collapsible=True,
        #     models=(
        #         'apps.church.models.Associations',
        #         'apps.church.models.Gallery',
        #         ),
        # ))
        

        # self.children.append(modules.ModelList(
        #     _('History'),
        #     column=1,
        #     collapsible=True,
        #     models=(
        #         'apps.church.models.ChurchHistory',
        #         'apps.church.models.Vicars',
        #         ),
        # ))


        # self.children.append(modules.ModelList(
        #     _('Bullettin & Notifications'),
        #     column=1,
        #     collapsible=True,
        #     models=(
        #         # -------- bullettin is here ------------
        #         'apps.church.models.PreBullettin',
        #         'apps.church.models.Notifications',
        #         ),
        # ))


        # self.children.append(modules.ModelList(
        #     _('Contacts'),
        #     column=1,
        #     collapsible=True,
        #     models=(
        #         'apps.church.models.Sitemap',
        #         'apps.church.models.Address',
        #         'apps.church.models.Feedback',
        #         ),
        # ))

 #------------------------------------------------------------------------------

        self.children.append(modules.ModelList(
            _('Users'),
            column=1,
            collapsible=True,
            models=('django.contrib.auth.models.User',),
        ))
        # append an app list module for "Administration"
        
        
       
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            column=2,
            children=[
                {
                    'title': _('1800-2000-939'),
                    'url': 'http://simplans.in/',
                    'external': True,
                },
                {
                    'title': _('support@simplans.com'),
                    'url': 'mailto:support@simplans.com',
                    'external': True,
                },
                {
                    'title': _('Support Desk'),
                    'url': 'http://simplans.com/support/home',
                    'external': True,
                },
            ]
        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=2,
        ))


