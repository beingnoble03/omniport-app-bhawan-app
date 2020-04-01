from rest_framework import permissions
from bhawan_app.managers.services import is_hostel_admin
from bhawan_app.constants import designations

class IsSupervisor(permissions.BasePermission):
    """
    Object-level permission to only allow admin of an object to edit
    it.
    """

    def has_permission(self, request, view):
        """
        Returns if the authenticated user has the permissions to access a
        particular object
        :param obj: an instance of the bhawan app models whose permissions is
        checked
        :return: if the the person is allowed or not
        """
        person = request.person
        if is_hostel_admin(person):
            return person.hosteladmin.designation == designations.SUPERVISOR
        return False