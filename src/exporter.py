import subprocess
from pathlib import Path


class Exporter:

    def create_video(self, frames_folder, output_video, fps=30):

        command = [
            "ffmpeg",
            "-y",
            "-framerate", str(fps),
            "-i", f"{frames_folder}/frame_%04d.jpg",
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            output_video
        ]

        subprocess.run(command, check=True)

        print("Vidéo créée :", output_video)