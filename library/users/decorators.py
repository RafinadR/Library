

from functools import wraps
from django.shortcuts import redirect

def librarian_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is a librarian (customize this based on your user model)
        if request.user.is_authenticated and request.user.role == 1:
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to a permission denied page or login page
            return redirect("authentication:index")  # Update 'permission_denied' to your desired URL

    return _wrapped_view
