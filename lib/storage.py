from google.cloud import storage as gcs
import os


class GCS:
    bucket_name = "hassaku-blog-contents"

    def __init__(self) -> None:
        client = gcs.Client(project=os.environ["PROJECT_ID"])
        self.bucket = client.get_bucket(self.bucket_name)

    def write(self, blob_name: str, content: bytes):
        """GCS にバイナリファイルを書き込む."""
        blob = self.bucket.blob(blob_name)
        blob.upload_from_string(content)

    def read(self, blob_name: str) -> bytes:
        """GCS からバイナリファイルを読み込む."""
        blob = self.bucket.blob(blob_name)
        return blob.download_as_bytes()

    def delete(self, blob_name: str):
        """GCS からファイルを削除する."""
        blob = self.bucket.blob(blob_name)
        blob.delete()

    def list_files(self, dir_path: str) -> list[str]:
        """GCS ディレクトリ内のファイルリストを取得する."""
        blobs = self.bucket.list_blobs(prefix=dir_path)
        return [blob.name for blob in blobs]
