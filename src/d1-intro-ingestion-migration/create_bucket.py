# load library
from google.cloud import storage


# define creation function
def create_bucket_class_location(bucket_name):
    """
    create a new bucket in the US region with
    the coldline storage class
    """

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print("created bucket {} in {} with storage class {}".format(new_bucket.name, new_bucket.location, new_bucket.storage_class))
    return new_bucket


def delete_bucket(bucket_name):
    """Deletes a bucket. The bucket must be empty."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()

    print(f"bucket {bucket.name} deleted")


# create bucket
# create_bucket_class_location(bucket_name='owshq-py-landing-zone')

# delete bucket
# delete_bucket(bucket_name='owshq-py-landing-zone')