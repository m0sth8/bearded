# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from time import sleep
from servers.models import ScanTask
import pexpect


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        while True:
            tasks = ScanTask.objects.filter(status__in=(ScanTask.STATUS.CREATED, ))
            for task in tasks:
                task.status = ScanTask.STATUS.WORKING
                task.save()
                spn = pexpect.spawn('/home/vagrant/tools/wpscan/wpscan.rb --url %s' % task.server.host,
                                    timeout=1000)
                for txt in spn:
                    if task.stdout:
                        task.stdout += txt
                    else:
                        task.stdout = txt
                    task.save()
                    print(txt)
                task.status = ScanTask.STATUS.COMPLETE
                task.save()
            sleep(1)