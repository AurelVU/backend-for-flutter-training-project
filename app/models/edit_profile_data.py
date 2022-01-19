from dataclasses import dataclass


@dataclass
class EditProfileData:
    firstname: str
    lastname: str
    website: str
    avatarUrl: str = None
