from pathlib import Path
import pulumi
from pulumi import FileAsset, Output
from pulumi_gcp.storage import Bucket, BucketIAMBinding, BucketObject

website_bucket = Bucket(
    "website-bucket",
    location="eu",
    website={"main_page_suffix": "index.html"},
    uniform_bucket_level_access=True,
    force_destroy=True,
)

website_bucket_iam_binding = BucketIAMBinding(
    "website-bucket-iam-binding",
    bucket=website_bucket.name,
    role="roles/storage.objectViewer",
    members=["allUsers"],
)

website_index_page = BucketObject(
    "website-index-page",
    name="index.html",
    source=FileAsset(str(Path(__file__).parent / "public" / "index.html")),
    content_type="text/html",
    bucket=website_bucket.name,
)

pulumi.export(
    "website-endpoint",
    Output.concat(
        "http://storage.googleapis.com/",
        website_bucket.name,
        "/",
        website_index_page.output_name,
    ),
)
