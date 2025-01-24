#! /usr/bin/env python3

import glob
import os

from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

image_ext = {
    "jpg",
    "jpeg",
    "png",
    "heic",
}

convert_image = {
    1: lambda img: img,
    2: lambda img: img.transpose(Image.Transpose.FLIP_LEFT_RIGHT),  # 左右反転
    3: lambda img: img.transpose(Image.Transpose.ROTATE_180),  # 180度回転
    4: lambda img: img.transpose(Image.Transpose.FLIP_TOP_BOTTOM),  # 上下反転
    5: lambda img: img.transpose(Image.Transpose.FLIP_LEFT_RIGHT).transpose(Image.Transpose.ROTATE_90),  # 左右反転＆反時計回りに90度回転
    6: lambda img: img.transpose(Image.Transpose.ROTATE_270),  # 反時計回りに270度回転
    7: lambda img: img.transpose(Image.Transpose.FLIP_LEFT_RIGHT).transpose(Image.Transpose.ROTATE_270),  # 左右反転＆反時計回りに270度回転
    8: lambda img: img.transpose(Image.Transpose.ROTATE_90),  # 反時計回りに90度回転
}


def convert(image: str):
    format = "webp"
    image_no_ext, _ = os.path.splitext(image)
    new_image = f"{image_no_ext}.{format}"
    if image != new_image:
        try:
            img = Image.open(image)
            exif = img.getexif()
            orientation = exif.get(0x112, 1)
            img = convert_image[orientation](img)  # 画像の向きを修正
            img.save(new_image)
            basename = os.path.basename(image)
            print(f"{basename} converted to {format}")
            os.remove(image)
        except Exception:
            print(f"Cannot convert {image}")
            return None
    return new_image


def convert_directory(directory: str):
    image_files = [f for f in glob.glob(os.path.join(directory, "assets/*.*")) if f.split(".")[-1] in image_ext]
    new_images: list[str | None] = []
    for image_file in image_files:
        new_images.append(convert(image_file))
    md_text = open(os.path.join(directory, "page.md"), "r").read()
    for new_image, old_image in zip(new_images, image_files):
        if not new_image:
            continue
        new_basename = os.path.basename(new_image)
        old_basename = os.path.basename(old_image)
        md_text = md_text.replace(old_basename, new_basename)
    with open(os.path.join(directory, "page.md"), "w") as f:
        f.write(md_text)


def main(args: list[str]):
    for directory in args:
        if not os.path.isdir(directory):
            print(f"{directory} is not a directory")
            continue
        convert_directory(directory)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: to_webp.py ...<directory>")
        sys.exit(1)

    main(sys.argv[1:])
