from pathlib import Path
from camera import Camera
from exporter import Exporter
from montage import Montage


class Project:

    def __init__(self, photos_folder):

        self.photos_folder = Path(photos_folder)

    def get_images(self):

        extensions = [".jpg", ".jpeg", ".png"]

        images = []

        for ext in extensions:
            images.extend(self.photos_folder.glob(f"*{ext}"))
            images.extend(self.photos_folder.glob(f"*{ext.upper()}"))

        return sorted(images)
    def generate(self):
        camera = Camera()

        for image in self.get_images():
            output = f"../frames/{image.stem}"

            camera.create_frames(
                image,
                output
            )
        exporter = Exporter()

        for image in self.get_images():

            frames = f"../temp/frames/{image.stem}"

            camera.create_frames(image, frames)

            clip = f"../temp/clips/{image.stem}.mp4"

            exporter.create_video(
                frames,
                clip
            )
        montage = Montage()

        montage.concat_clips(
            "../temp/clips",
            "../videos/visite_complete.mp4"
)