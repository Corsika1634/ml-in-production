from minio import Minio
from minio.error import S3Error

# Инициализация клиента MinIO
minio_client = Minio(
    "127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

def upload_file(bucket_name: str, file_path: str, object_name: str):
    """Upload a file to a bucket."""
    try:
        minio_client.fput_object(bucket_name, object_name, file_path)
        print(f"✅ Uploaded {file_path} to {bucket_name}/{object_name}")
    except S3Error as e:
        print(f"❌ Upload error: {e}")

def download_file(bucket_name: str, object_name: str, file_path: str):
    """Download a file from a bucket."""
    try:
        minio_client.fget_object(bucket_name, object_name, file_path)
        print(f"✅ Downloaded {object_name} from {bucket_name} to {file_path}")
    except S3Error as e:
        print(f"❌ Download error: {e}")

def update_file(bucket_name: str, object_name: str, new_file_path: str):
    """Update (overwrite) an object in a bucket."""
    try:
        minio_client.fput_object(bucket_name, object_name, new_file_path)
        print(f"✅ Updated {object_name} in {bucket_name}")
    except S3Error as e:
        print(f"❌ Update error: {e}")

def delete_file(bucket_name: str, object_name: str):
    """Delete a file from a bucket."""
    try:
        minio_client.remove_object(bucket_name, object_name)
        print(f"✅ Deleted {object_name} from {bucket_name}")
    except S3Error as e:
        print(f"❌ Delete error: {e}")
