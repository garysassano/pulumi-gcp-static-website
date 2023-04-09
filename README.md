# pulumi-gcp-static-website

Pulumi project that deploys a static website to GCP using Cloud Storage.

## Resources Deployed

```sh
     Type                             Name                           Plan       
 +   pulumi:pulumi:Stack              pulumi-gcp-static-website-dev  create     
 +   ├─ gcp:storage:Bucket            website-bucket                 create     
 +   ├─ gcp:storage:BucketIAMBinding  website-bucket-iam-binding     create     
 +   └─ gcp:storage:BucketObject      website-index-page             create   
 ```
