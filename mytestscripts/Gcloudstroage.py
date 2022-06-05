from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/johnchen/gcloudkey.json"

def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
    """Uploads a file to the bucket."""

    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The contents to upload to the file
    # contents = "these are my contents"

    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(contents)

    print(
        f"{destination_blob_name} with contents {contents} uploaded to {bucket_name}."
    )
def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    print(f"Blob {blob_name} deleted.")
def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )



# delete_blob('humorbucket','tfrecords/')
# delete_blob('humorbucket','tfrecords/train/train_16.tfrecords')
# delete_blob('humorbucket','tfrecords/test/test_1.tfrecords')



upload_blob('humorbucket','../dataset/tfrecords/train/train_1845.tfrecords','tfrecords/train/train_1845.tfrecords')
upload_blob('humorbucket','../dataset/tfrecords/val/val_529.tfrecords','tfrecords/val/val_529.tfrecords')
# upload_blob_from_memory('humorbucket','dataset/tfrecords/...','tfrecords/val/')
# upload_blob_from_memory('humorbucket','dataset/tfrecords/...','tfrecords/test/')

# gcloud compute scp humorTPU:~/myhumorSP/dataset/test_user_result.txt /Users/johnchen/Desktop/SP/myhumorSP/dataset
# gcloud alpha compute tpus tpu-vm scp humorTPU:~/myhumorSP/dataset/test_user_result.txt /Users/johnchen/Desktop/SP/myhumorSP/dataset --zone=europe-west4-a