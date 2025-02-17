import tempfile
from collections import namedtuple

from PIL import Image

from common import tostring

Resolution = namedtuple('Resolution', ['width', 'height'])


@tostring
class Photo:
    def __init__(self, source, resolution: Resolution, iso):
        self.source = source
        self.resolution = resolution
        self.iso = iso

    def resize(self, ratio, quality: int = 80):
        image = Image.open(self.source)
        new_resolution = Resolution(int(self.resolution.width * ratio), int(self.resolution.height * ratio))
        image_resized = image.resize(new_resolution, Image.ANTIALIAS)
        temp_file = tempfile.NamedTemporaryFile(mode="w+t", delete=False, suffix='.jpg')
        image_resized.save(temp_file.name, "JPEG", quality=quality)

        return Photo(temp_file.name, new_resolution, self.iso)
