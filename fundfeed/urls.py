from django.urls import path
from .views import PublicProfileCreateView, ProfileView, PostCreateView, RandomVideoListView

urlpatterns = [
# {
#   "user": 3,
#   "name": "Sheikh",
#   "role": "developer",
#   "bio": "AI developer & tinkerer",
#   "location": "Bengaluru",
#   "interest_ids": [1, 2, 3]
# }
    path("profile/create/", PublicProfileCreateView.as_view(), name="profile-create"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("posts/random/", RandomVideoListView.as_view(), name="random-videos"),
]