# -*- coding: utf-8 -*-
import json

from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import normalize_newlines
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import ModificationDateTimeField, CreationDateTimeField

from bearded_web.core.fields import Choice


class ServerManager(models.Manager):

    def get_by_user(self, user):
        return self.filter(user=user)

    def get_by_user_and_server(self, user, server_id):
        try:
            return self.get(user=user, id=server_id)
        except Server.DoesNotExist:
            return None


class Server(models.Model):
    host = models.CharField(_('host'), max_length=255, help_text=_('domain or ip address'))
    user = models.ForeignKey(to=get_user_model())

    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    objects = ServerManager()

    def __unicode__(self):
        return u'%s' % self.host

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)

    def get_absolute_url(self):
        return reverse('servers:server', kwargs={'server_id': self.pk})

    def get_last_scan(self):
        scans = ScanTask.objects.get_by_server(self)
        return scans[0] if scans else None


class ScanTaskManager(models.Manager):

    def get_by_user(self, user):
        return self.filter(user=user)

    def get_by_server(self, server):
        return self.filter(server=server)

    def get_by_id(self, id):
        try:
            return self.get(id=id)
        except ScanTask.DoesNotExist:
            return None


class ScanTask(models.Model):
    class STATUS(Choice):
        CREATED = 1, _('Created')
        WAITING = 2, _('Waiting')
        WORKING = 3, _('Working')
        COMPLETE = 8, _('Complete')
        FAIL = 9, _('Fail')

    server = models.ForeignKey(to='servers.Server')
    user = models.ForeignKey(to=get_user_model())
    status = models.PositiveSmallIntegerField(choices=STATUS, default=STATUS.CREATED)

    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    # эти поля мы потом удалим
    stdout = models.TextField(null=True, blank=True)

    objects = ScanTaskManager()

    @property
    def stdout_colored(self):
        stdout = self.stdout
        if stdout:
            stdout = normalize_newlines(stdout)
            stdout = stdout.replace('\n', '<br />')
            stdout = stdout.replace('[32m', '<span style="color:green" >')
            stdout = stdout.replace('[31m', '<span style="color:red" >')
            stdout = stdout.replace('[0m', '</span>')
        return stdout

    def __unicode__(self):
        return u'task [%s]' % self.pk

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)

    def get_absolute_url(self):
        return reverse('servers:scan', kwargs={'server_id': self.server_id, 'scan_id': self.pk})


class ScanContext(models.Model):
    task = models.ForeignKey('ScanTask')
    # пока сохраняется в виде строчки json, в дальнейшем нужно привести к бинарному виду и паковать msgpack
    data_char = models.TextField(blank=True, null=True)

    @property
    def data(self):
        return json.loads(self.data_char) if self.data_char else None

    @data.setter
    def data(self, value):
        self.data_char = json.dumps(value) if value else None