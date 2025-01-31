import asyncio
from google.cloud import storage as gcs
import os


class GCS:
    bucket_name = "hassaku-blog-contents"

    def __init__(self) -> None:
        self.client = gcs.Client(project=os.environ["PROJECT_ID"])
        self.bucket = self.client.get_bucket(self.bucket_name)

    async def write(self, blob_name: str, content: bytes, content_type: str | None = None, cache_control: str | None = None) -> None:
        """GCS にバイナリファイルを書き込む.

        Args:
            blob_name: GCS 上でのファイル名
            content: ファイルの内容 (bytes)
            content_type: Content-Type (オプション)
            cache_control: Cache-Control ヘッダー (オプション)
        """
        blob = self.bucket.blob(blob_name)
        if cache_control:
            blob.cache_control = cache_control
        await asyncio.to_thread(blob.upload_from_string, content, content_type=content_type)

    async def read(self, blob_name: str) -> bytes:
        """GCS からバイナリファイルを読み込む."""
        blob = self.bucket.blob(blob_name)
        return await asyncio.to_thread(blob.download_as_bytes)

    async def delete(self, blob_name: str) -> None:
        """GCS からファイルを削除する."""
        blob = self.bucket.blob(blob_name)
        await asyncio.to_thread(blob.delete)

    async def list_files(self, dir_path: str) -> list[str]:
        """GCS ディレクトリ内のファイルリストを取得する."""
        blobs = await asyncio.to_thread(self.bucket.list_blobs, prefix=dir_path)
        return [blob.name for blob in blobs]
