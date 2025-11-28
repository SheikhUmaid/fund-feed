from rest_framework.permissions import BasePermission
from .models import Profile


class IsDeveloperUploader(BasePermission):
    """Allows only developer profiles to upload posts."""

    def has_permission(self, request, view):
        # uploader is passed inside POST body
        uploader_id = request.data.get("uploader")

        if uploader_id is None:
            return False  # uploader required

        try:
            profile = Profile.objects.get(id=uploader_id)
        except Profile.DoesNotExist:
            return False  # invalid ID

        return profile.role == "developer"

