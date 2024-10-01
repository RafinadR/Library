from django.shortcuts import render
from authentication.models import CustomUser
from .decorators import librarian_required
# Create your views here.


@librarian_required       
def users_view(request):    
    users = CustomUser.objects.all()
    return render(request, "users/all_users.html", {
        "users" : users
    })

@librarian_required     
def user_by_id(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    return render(request, "users/user.html", {
        "user": user, 
        "role": user.get_role_name()
    })
         

