from rest_framework import status
from rest_framework import generics
from user_app.serializers import *
from rest_framework.response import Response
from user_app.utils import Util
from rest_framework.permissions import IsAuthenticated

# View: Login
# ---------------------------------------------------------------------------------------------------------------
class LoginAPIView(generics.CreateAPIView):
    """
    API view for user login or registration.
    """
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.context.get("user")
        if not user:
            user = serializer.save()

        tokens = Util.get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_200_OK)
    
# View: Profile
# ---------------------------------------------------------------------------------------------------------------
class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile