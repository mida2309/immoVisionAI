from pathlib import Path

# Chemin vers le dossier des photos
photos_folder = Path("photos")

# Récupère tous les fichiers images
images = []
for extension in ("*.jpg", "*.jpeg", "*.png"):
    images.extend(photos_folder.glob(extension))

print(f"{len(images)} photo(s) trouvée(s) :\n")

for image in images:
    print(image.name)