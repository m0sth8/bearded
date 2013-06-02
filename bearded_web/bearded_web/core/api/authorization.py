# -*- coding: utf-8 -*-

from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized


class NoUserField(object):
    pass


class UserObjectsOnlyAuthorization(Authorization):

    def __init__(self, user_field='user'):
        super(UserObjectsOnlyAuthorization, self).__init__()
        self.user_field = user_field

    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(**{self.user_field: bundle.request.user})

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return getattr(bundle.obj, self.user_field, NoUserField) == bundle.request.user

    def create_list(self, object_list, bundle):
        # Assuming their auto-assigned to ``user``.
        return object_list

    def create_detail(self, object_list, bundle):
        return True

    def update_list(self, object_list, bundle):
        allowed = []
        user = bundle.request.user
        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if getattr(obj, self.user_field, NoUserField) == user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return getattr(bundle.obj, self.user_field, NoUserField) == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        return getattr(bundle.obj, self.user_field, NoUserField) == bundle.request.user