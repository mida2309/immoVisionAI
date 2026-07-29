from pathlib import Path
import subprocess


class Montage:

    def concat_clips(self, clips_folder, output_video):

        clips = sorted(Path(clips_folder).glob("*.mp4"))

        if not clips:
            print("Aucun clip trouvé.")
            return

        list_file = Path(clips_folder) / "clips.txt"

        with open(list_file, "w") as f:
            for clip in clips:
                f.write(f"file '{clip.resolve()}'\n")

        subprocess.run([
            "ffmpeg",
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(list_file),
            "-c", "copy",
            output_video
        ], check=True)

        print("Vidéo finale créée :", output_video)