"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'ocms.dashboard.CustomIndexDashboard'
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
        self.children.append(modules.Group(
            _('Group: Administration'),
            column=1,
            collapsible=True,
            children = [
                modules.AppList(
                    _('Administration'),
                    column=1,
                    collapsible=False,
                    models=('django.contrib.*',),
                ),
                modules.AppList(
                    _('AppList: Aplicaciones'),
                    collapsible=True,
                    column=1,
                    css_classes=('collapse opened',),
                    exclude=('django.contrib.*','projectadmin.*'),
                ),
            ]
        ))
        
        
        # append an app list module for "Applications"
        self.children.append(modules.Group(
            _('Panel: Project Admin'),
            collapsible=True,
            column=1,
            css_classes=('collapse opened',),
            exclude=('django.contrib.*',),
            children = [
                modules.ModelList(
                    _('Proyectos'),
                    column=1,
                    models=('projectadmin.models.Proyecto',),
                ),
                modules.ModelList(
                    _('Recursos'),
                    column=1,
                    css_classes=('collapse opened',),
                    models=(
                        'projectadmin.models.Peticion',
                        'projectadmin.models.Wiki',
                        'projectadmin.models.Documento',
                        'projectadmin.models.Archivo',
                        'projectadmin.models.Comentario',
                        ),
                ),
                modules.LinkList(
                    _('Analisis'),
                    column=2,
                    children=[
                        {
                            'title': _(u'Calendario'),
                            'url': '/admin/projectadmin/show/calendar/',
                            'external': False,
                        },
                    ]
                ),
            ]
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Media Management'),
            column=2,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            column=2,
            children=[
                {
                    'title': _('Django Documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Documentation'),
                    'url': 'http://packages.python.org/django-grappelli/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Google-Code'),
                    'url': 'http://code.google.com/p/django-grappelli/',
                    'external': True,
                },
            ]
        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


