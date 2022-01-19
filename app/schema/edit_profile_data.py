import marshmallow_dataclass

from app.models.edit_profile_data import EditProfileData

EditProfileDataSchema = marshmallow_dataclass.class_schema(EditProfileData)
