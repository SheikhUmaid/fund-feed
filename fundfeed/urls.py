from django.urls import path
from .views import PublicProfileCreateView, ProfileView

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
]