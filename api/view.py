from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from oauth2_provider.models import Application
from .models import SuperUsers
# Create your views here.
@api_view(["GET"])
def adduser(request):
    """
    添加那个
    """
    SuperUsers.objects.create(username="root")
    app = Application(
    name='root',
    redirect_uris='https://your-redirect-uri.com/',
    user=SuperUsers.objects.get(username='root'),
    client_type=Application.CLIENT_CONFIDENTIAL,
    authorization_grant_type=Application.GRANT_CLIENT_CREDENTIALS,
    )
    app.save()
    return Response({client_id : app.client_id,client_secret : app.client_secret})
