from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """ Check user trying to edit their own profile """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id #return True or False


class PostOwnStatus(permissions.BasePermission):
    """Allow user to POST their own status """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id