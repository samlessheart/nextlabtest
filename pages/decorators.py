from django.core.exceptions import PermissionDenied


def staff_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_staff==True:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap