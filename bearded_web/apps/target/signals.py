# -*- coding: utf-8 -*-

from django.db.models.signals import post_save
from django.dispatch import receiver

from target.models import Target
from target.tasks import analize


@receiver(post_save, sender=Target, dispatch_uid='target_analyze_signal')
def target_analyze(sender, instance, **kwargs):
    if not instance.info_raw:
        analize.delay(instance.pk)
