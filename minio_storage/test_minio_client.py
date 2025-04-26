import os
import tempfile
import pytest
from minio.error import S3Error
from minio_storage import minio_client

# Настройки
BUCKET_NAME = "test-bucket"
OBJECT_NAME = "test-object.txt"
NEW_OBJECT_NAME = "updated-object.txt"

@pytest.fixture(scope="module")
def setup_bucket():
    """Ensure test bucket exists."""
    try:
        if not minio_client.minio_client.bucket_exists(BUCKET_NAME):
            minio_client.minio_client.make_bucket(BUCKET_NAME)
    except S3Error as e:
        print(f"Bucket setup error: {e}")
    yield
    try:
        minio_client.minio_client.remove_bucket(BUCKET_NAME)
    except:
        pass

def test_upload_file(setup_bucket):
    """Test file upload to bucket."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"Hello, MinIO!")
        tmp_path = tmp.name

    minio_client.upload_file(BUCKET_NAME, tmp_path, OBJECT_NAME)

    objects = list(minio_client.minio_client.list_objects(BUCKET_NAME))
    assert any(obj.object_name == OBJECT_NAME for obj in objects)

    os.remove(tmp_path)

def test_download_file(setup_bucket):
    """Test file download from bucket."""
    download_path = "downloaded_test_object.txt"

    minio_client.download_file(BUCKET_NAME, OBJECT_NAME, download_path)

    assert os.path.exists(download_path)

    os.remove(download_path)

def test_update_file(setup_bucket):
    """Test updating (overwriting) a file."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"Updated content!")
        tmp_path = tmp.name

    minio_client.update_file(BUCKET_NAME, OBJECT_NAME, tmp_path)

    os.remove(tmp_path)

def test_delete_file(setup_bucket):
    """Test deleting a file from bucket."""
    minio_client.delete_file(BUCKET_NAME, OBJECT_NAME)

    objects = list(minio_client.minio_client.list_objects(BUCKET_NAME))
    assert all(obj.object_name != OBJECT_NAME for obj in objects)
