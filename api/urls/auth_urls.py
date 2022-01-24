from django.urls import path

from api.views.auth_views import *
from api.utils.decorators import user_login_required


app_name = 'auth'

@api_view(['POST'])
@user_login_required
def logout(request):

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]

