from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile
from .permissions import CustomReadOnly
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer


# http://127.0.0.1:8000/users/register/
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# http://127.0.0.1:8000/users/login/
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)

# http://127.0.0.1:8000/users/profile/1
class ProfileView(generics.GenericAPIView):
    serializer_class = ProfileSerializer

    def patch(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        profile.nickname = data['nickname']
        profile.position = data['position']
        profile.subjects = data['subjects']
        if request.data['image']:
            profile.image = request.data['image']
        profile.save()
        return Response({"result": "ok"},
                        status=status.HTTP_206_PARTIAL_CONTENT)

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

