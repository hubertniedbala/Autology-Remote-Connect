#!/bin/bash

# 0. Zainstaluj wymagane narzędzia
if ! command -v create-dmg &> /dev/null; then
    brew install create-dmg
fi
if ! command -v fileicon &> /dev/null; then
    brew install fileicon
fi

# 1. Wyczyść poprzednie buildy
rm -rf build dist
rm -f "Autology Remote Connect.dmg"

# 2. Konwertuj PNG na ICNS dla ikony instalatora DMG
mkdir -p icon.iconset
sips -z 1024 1024 icons/Autology_icon.png --out icons/temp_icon.png
sips -z 16 16     icons/temp_icon.png --out icon.iconset/icon_16x16.png
sips -z 32 32     icons/temp_icon.png --out icon.iconset/icon_16x16@2x.png
sips -z 32 32     icons/temp_icon.png --out icon.iconset/icon_32x32.png
sips -z 64 64     icons/temp_icon.png --out icon.iconset/icon_32x32@2x.png
sips -z 128 128   icons/temp_icon.png --out icon.iconset/icon_128x128.png
sips -z 256 256   icons/temp_icon.png --out icon.iconset/icon_128x128@2x.png
sips -z 256 256   icons/temp_icon.png --out icon.iconset/icon_256x256.png
sips -z 512 512   icons/temp_icon.png --out icon.iconset/icon_256x256@2x.png
sips -z 512 512   icons/temp_icon.png --out icon.iconset/icon_512x512.png
sips -z 1024 1024 icons/temp_icon.png --out icon.iconset/icon_512x512@2x.png
iconutil -c icns icon.iconset -o icons/Autology_icon.icns
rm icons/temp_icon.png

# 3. Konwertuj PNG na ICNS dla ikony aplikacji
mkdir -p app_icon.iconset
sips -z 1024 1024 icons/icon.png --out icons/temp_app_icon.png
sips -z 16 16     icons/temp_app_icon.png --out app_icon.iconset/icon_16x16.png
sips -z 32 32     icons/temp_app_icon.png --out app_icon.iconset/icon_16x16@2x.png
sips -z 32 32     icons/temp_app_icon.png --out app_icon.iconset/icon_32x32.png
sips -z 64 64     icons/temp_app_icon.png --out app_icon.iconset/icon_32x32@2x.png
sips -z 128 128   icons/temp_app_icon.png --out app_icon.iconset/icon_128x128.png
sips -z 256 256   icons/temp_app_icon.png --out app_icon.iconset/icon_128x128@2x.png
sips -z 256 256   icons/temp_app_icon.png --out app_icon.iconset/icon_256x256.png
sips -z 512 512   icons/temp_app_icon.png --out app_icon.iconset/icon_256x256@2x.png
sips -z 512 512   icons/temp_app_icon.png --out app_icon.iconset/icon_512x512.png
sips -z 1024 1024 icons/temp_app_icon.png --out app_icon.iconset/icon_512x512@2x.png
iconutil -c icns app_icon.iconset -o icons/icon.icns
rm icons/temp_app_icon.png

# 4. Zbuduj aplikację
python3.11 setup.py py2app

# 5. Podpisz aplikację z uprawnieniami
codesign --force --deep --sign - --entitlements entitlements.plist "dist/Autology Remote Connect.app"

# 6. Utwórz DMG
create-dmg \
  --volname "Autology Remote Connect" \
  --volicon "icons/Autology_icon.icns" \
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon-size 100 \
  --icon "Autology Remote Connect.app" 200 190 \
  --hide-extension "Autology Remote Connect.app" \
  --app-drop-link 600 185 \
  "Autology Remote Connect.dmg" \
  "dist/Autology Remote Connect.app"

# 7. Ustaw ikonę dla pliku DMG
fileicon set "Autology Remote Connect.dmg" icons/Autology_icon.icns

# 8. Wyczyść tymczasowe pliki
rm -rf icon.iconset app_icon.iconset 