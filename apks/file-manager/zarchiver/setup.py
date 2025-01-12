import os
import shutil

APP_NAME = os.getenv('APP_NAME')

apk_versions = [
    ("arm64-v8a", f"https://github.com/APackage/A.P.A-repo/releases/download/{APP_NAME}/{APP_NAME}_arm64-v8a_release.apk"),
    ("armeabi-v7a", f"https://github.com/APackage/A.P.A-repo/releases/download/{APP_NAME}/{APP_NAME}_armeabi-v7a_release.apk"),
    ("x86", f"https://github.com/APackage/A.P.A-repo/releases/download/{APP_NAME}/{APP_NAME}_x86_release.apk")
]

folder_name = os.environ.get("FOLDER_NAME", "apks/file-manager/zarchiver/")
index_file_path = os.path.join(folder_name, "index.html")
index_template_path = os.path.join("index_template")

# Eğer index.html yoksa, index_template'i kopyala
if not os.path.exists(index_file_path):
    shutil.copy(index_template_path, index_file_path)

# index.html'i aç ve içeriği düzenle
with open(index_file_path, 'r') as file:
    index_content = file.read()

# APK sürümlerini HTML içine eklemek için "versions" bölümünü bul
versions_section = '<section id="services">\n    <h2>Versions</h2>\n    <div class="cards">\n'

# APK sürümlerini dinamik olarak ekle
for version, url in apk_versions:
    version_card = f"""
        <div class="card">
            <h3 class="apk_name">{APP_NAME}</h3>
            <a href="{url}" class="apk_file">{version}</a>
        </div>
    """
    versions_section += version_card

versions_section += "    </div>\n</section>"

# "services" bölümünü bulup yerine yeni sürüm kısmını ekle
index_content = index_content.replace('<section id="services">', versions_section)

# Değiştirilen içeriği tekrar index.html'e yaz
with open(index_file_path, 'w') as file:
    file.write(index_content)

print(f"index.html güncellendi: {index_file_path}")
