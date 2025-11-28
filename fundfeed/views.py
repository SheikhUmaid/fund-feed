from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.



class PublicProfileCreateView(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        username = request.data.get("user")
        pwd = request.data.get("password")
        
        if username and pwd:
            user = authenticate(username=username, password=pwd)
            if user:
                serializer.initial_data['user'] = user.id
            else:
                user = User.objects.create_user(username=username, password=pwd)
                profile = Profile.objects.create(user=user, name=request.data.get("name"), role=request.data.get("role"), bio=request.data.get("bio"), location=request.data.get("location"))
                
                user.save()
                profile.save()
                serializer.initial_data['user'] = user.id
                
                return Response({"detail": "User and Profile created successfully."}, status=status.HTTP_201_CREATED)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class ProfileView(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.serializer_class(profile)
        return Response(serializer.data)
    
    
    
    



    
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsDeveloperUploader


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny, IsDeveloperUploader]
    