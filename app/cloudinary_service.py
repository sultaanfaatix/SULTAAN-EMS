import cloudinary
import cloudinary.uploader
from flask import current_app


def upload_image(file, folder):
    """Upload file to Cloudinary with error handling"""
    try:
        # Check if Cloudinary is configured
        if not current_app.config.get("CLOUDINARY_CLOUD_NAME"):
            raise ValueError("Cloudinary is not configured")
        
        cloudinary.config(
            cloud_name=current_app.config["CLOUDINARY_CLOUD_NAME"],
            api_key=current_app.config["CLOUDINARY_API_KEY"],
            api_secret=current_app.config["CLOUDINARY_API_SECRET"],
            secure=True,
        )

        # Determine resource type based on file content type
        content_type = getattr(file, 'content_type', 'application/octet-stream')
        if content_type.startswith('image'):
            resource_type = 'image'
        elif content_type.startswith('video'):
            resource_type = 'video'
        elif content_type.startswith('audio'):
            resource_type = 'video'  # Cloudinary uses 'video' for audio too
        else:
            resource_type = 'auto'  # Let Cloudinary auto-detect

        result = cloudinary.uploader.upload(
            file,
            folder=folder,
            resource_type=resource_type
        )

        return result["secure_url"]
    except Exception as e:
        # Log the error but don't crash the application
        current_app.logger.error(f"Cloudinary upload failed: {str(e)}")
        raise