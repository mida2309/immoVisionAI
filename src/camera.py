import cv2
import os

def create_frames(image_path, output_folder, duration=5, fps=30):

    image = cv2.imread(image_path)

    if image is None:
        print("Erreur : image introuvable")
        return

    height, width = image.shape[:2]

    os.makedirs(output_folder, exist_ok=True)

    total_frames = duration * fps

    for i in range(total_frames):

        progress = i / total_frames

        zoom = 1 + (0.15 * progress)

        crop_w = int(width / zoom)
        crop_h = int(height / zoom)

        x = (width - crop_w) // 2
        y = (height - crop_h) // 2

        crop = image[y:y + crop_h, x:x + crop_w]

        frame = cv2.resize(crop, (width, height))

        filename = os.path.join(output_folder, f"frame_{i:04d}.jpg")

        cv2.imwrite(filename, frame)

    print(f"{total_frames} images créées.")