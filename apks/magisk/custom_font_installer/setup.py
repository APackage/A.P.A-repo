import os
import shutil

APP_NAME = os.getenv('APP_NAME', "APP_NAME")

# Yeni ve mevcut APK sürümleri
apk_versions = [
    ("Universal", f"https://github.com/APackage/A.P.A-repo/releases/download/{APP_NAME}/{APP_NAME}.zip")
]

folder_name = os.environ.get("FOLDER_NAME", "apks/magisk/custom_font_installer/")
index_file_path = os.path.join(folder_name, "index.html")
index_template_path = os.path.join("index_template")

# Eğer index.html yoksa, index_template'i kopyala
if not os.path.exists(index_file_path):
    shutil.copy(index_template_path, index_file_path)

# index.html'i aç ve içeriğini oku
with open(index_file_path, 'r') as file:
    index_content = file.read()

# "cards" bölümünü bul
start_marker = '<div class="cards">'
end_marker = '</div>'

start_idx = index_content.find(start_marker)
end_idx = index_content.find(end_marker, start_idx)

if start_idx == -1 or end_idx == -1:
    print("Hata: 'cards' bölümü bulunamadı.")
else:
    # Mevcut içerik
    current_cards = index_content[start_idx + len(start_marker):end_idx].strip()

    # Yeni sürüm kartı oluştur
    new_version_card = f"""
        <div class="card">
            <h3 class="apk_name">{APP_NAME}</h3>
            <div class="buttons">
    """
    for version, url in apk_versions:
        new_version_card += f"""
                <a href="{url}" class="apk_file">{version}</a>
        """
    new_version_card += """
            </div>
        </div>
    """

    # Yeni kartı mevcut içeriğin en üstüne ekle
    updated_cards = new_version_card + current_cards

    # Güncellenmiş içeriği birleştir
    updated_content = (
        index_content[:start_idx + len(start_marker)] + updated_cards + index_content[end_idx:]
    )

    # Değişiklikleri index.html'e yaz
    with open(index_file_path, 'w') as file:
        file.write(updated_content)

    print(f"Yeni sürüm eklendi: {APP_NAME}")
