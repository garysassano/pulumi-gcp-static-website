import pulumi
from pulumi_gcp import storage

bucket = storage.Bucket(
    "website-bucket",
    location="eu",
    website=storage.BucketWebsiteArgs(main_page_suffix="index.html"),
    uniform_bucket_level_access=True,
)

bucketIAMBinding = storage.BucketIAMBinding(
    "website-bucket-iam-binding",
    bucket=bucket.name,
    role="roles/storage.objectViewer",
    members=["allUsers"],
)

bucketObject = storage.BucketObject(
    "website-index-page",
    bucket=bucket.name,
    content_type="text/html",
    source=pulumi.FileAsset("index.html"),
)

pulumi.export(
    "website-bucket-endpoint",
    pulumi.Output.concat("http://storage.googleapis.com/", bucket.id, "/", bucketObject.name),
)
