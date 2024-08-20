from rest_framework import status as http_status
from rest_framework.response import Response
from rest_framework.views import APIView
from portal.models import User  # Adjust the import according to your project structure
from .serializers import UserSerializer

class ChangeUserStatusView(APIView):
    def post(self, request, user_id, new_status):
        try:
            user = User.objects.get(id=user_id)
            
            # Validate new_status is either 0 or 1
            if new_status not in [0, 1]:
                return Response({"error": "Invalid status value. Must be 0 or 1."}, status=http_status.HTTP_400_BAD_REQUEST)
            
            # Update the user's status
            user.status = new_status
            user.save()
            
            # Serialize and return the updated user data
            serializer = UserSerializer(user)
            return Response(serializer.data, status=http_status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=http_status.HTTP_404_NOT_FOUND)
