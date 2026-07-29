import cv2
import os
import random


class Camera:

    def __init__(self, fps=30):
        self.fps = fps

    def zoom_in(self, image, progress):
        height, width = image.shape[:2]

        zoom = 1 + (0.15 * progress)

        crop_w = int(width / zoom)
        crop_h = int(height / zoom)

        x = (width - crop_w) // 2
        y = (height - crop_h) // 2

        crop = image[y:y + crop_h, x:x + crop_w]

        return cv2.resize(crop, (width, height))

    def pan_left_right(self, image, progress):
        height, width = image.shape[:2]

        crop_w = int(width * 0.85)

        x = int((width - crop_w) * progress)

        crop = image[:, x:x + crop_w]

        return cv2.resize(crop, (width, height))

    def pan_right_left(self, image, progress):
        height, width = image.shape[:2]

        crop_w = int(width * 0.85)

        x = int((width - crop_w) * (1 - progress))

        crop = image[:, x:x + crop_w]

        return cv2.resize(crop, (width, height))

    def create_frames(self, image_path, output_folder, duration=5):

        image = cv2.imread(str(image_path))

        if image is None:
            print(f"Impossible de lire {image_path}")
            return

        os.makedirs(output_folder, exist_ok=True)

        total_frames = duration * self.fps

        effect = random.choice([
            "zoom",
            "left",
            "right"
        ])

        for i in range(total_frames):

            progress = i / total_frames

            if effect == "zoom":
                frame = self.zoom_in(image, progress)

            elif effect == "left":
                frame = self.pan_left_right(image, progress)

            else:
                frame = self.pan_right_left(image, progress)

            filename = os.path.join(
                output_folder,
                f"frame_{i:04d}.jpg"
            )

            cv2.imwrite(filename, frame)

        print(f"{image_path.name} terminé ({effect})")