# -*- coding: utf-8 -*-

import subprocess
import tempfile
import os

from celery import task

from target.models import Target


@task()
def analize(target_id):
    print('TARGET!! %s' % target_id)
    target = Target.objects.get(pk=target_id)
    if not target:
        return
    try:
        log_verbose_file, log_verbose_path = tempfile.mkstemp(text=True)
        log_xml_file, log_xml_path = tempfile.mkstemp(text=True)
        command = '/home/vagrant/tools/WhatWeb/whatweb --log-verbose=%s --log-xml=%s  %s' % (log_verbose_path, log_xml_path, target.host)
        subprocess.call(command, shell=True)
        target.info_raw = open(log_verbose_path).read()
        target.save()
    finally:
        if os.path.exists(log_xml_path):
            os.unlink(log_xml_path)
        if os.path.exists(log_verbose_path):
            os.unlink(log_verbose_path)
