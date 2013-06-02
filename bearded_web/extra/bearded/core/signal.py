# -*- coding: utf-8 -*-
from collections import namedtuple
from gevent import Greenlet, GreenletExit, sleep, spawn, joinall, spawn_later
from gevent.event import Event
from gevent.queue import Queue
from uuid import uuid4
from datetime import datetime
from inspect import ismethod
import logging
import random

EmitEvent = namedtuple('EmitEvent', 'name time args kwargs')
ConsumerEvent = namedtuple('ConsumerEvent', 'consumer event')


class Signal(object):

    def __init__(self):
        super(Signal, self).__init__()
        self._consumers = set()

    def __get_event_consumer(self, event, consumer):
        if not consumer and not event:
            return None, None
        if not isinstance(event, basestring):
            if ismethod(event) and event.im_func.func_name.startswith('on_'):
                consumer = event.im_self
                event = event.im_func.func_name.replace('on_', '', 1)
            else:
                return None, None
        if not consumer or not isinstance(consumer, Base):
            return None, None
        return event, consumer

    def connect(self, event=None, consumer=None):
        event, consumer = self.__get_event_consumer(event, consumer)
        if not event or not consumer:
            return False
        self._consumers.add(ConsumerEvent(consumer=consumer, event=event))
        return True

    def disconnect(self, event=None, consumer=None):
        event, consumer = self.__get_event_consumer(event, consumer)
        if not event or not consumer:
            return False
        self._consumers.remove(ConsumerEvent(consumer=consumer, event=event))
        return True

    def emit(self, silent=True, *args, **kwargs):
        for consumer, event in self._consumers.copy():
            if consumer.ready(): # удаляем подписчика, если его гринлет уже умер
                self._consumers.remove(consumer)
            else:
                try:
                    consumer.emit(event, *args, **kwargs)
                except:
                    if not silent:
                        raise

    def clear(self):
        self._consumers.clear()