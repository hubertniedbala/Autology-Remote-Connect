# Autology Remote Connect

Aplikacja kliencka dla systemu macOS umożliwiająca zdalne połączenie z serwerem Autology.

## 🌟 Główne funkcje

- 🖥️ Aplikacja w pasku menu macOS
- 🔗 Bezpieczne zdalne połączenie
- 🚀 Automatyczny start przy uruchomieniu systemu
- 🔒 Podpisana cyfrowo aplikacja
- 📦 Prosty instalator DMG

## 💻 Wymagania systemowe

- macOS 10.15 lub nowszy
- Python 3.11
- Połączenie internetowe
- Konto Autology

## 🛠️ Rozwój aplikacji

### Wymagane narzędzia
- Python 3.11
- Homebrew
- create-dmg
- fileicon

### Instalacja zależności
Instalacja narzędzi przez Homebrew
brew install create-dmg fileicon
Instalacja zależności Pythona
```pip3.11 install -r requirements.txt```

## Budowanie aplikacji

Nadaj uprawnienia wykonywania dla skryptu build
```chmod +x build.sh
Uruchom skrypt budujący
./build.sh
```

## 📦 Instalacja

1. Pobierz najnowszą wersję z zakładki [Releases](../../releases)
2. Otwórz pobrany plik DMG
3. Przeciągnij aplikację do folderu Applications
4. Uruchom aplikację z folderu Applications

## 🔧 Struktura projektu

- `menubar_app.py` - Główny plik aplikacji
- `setup.py` - Konfiguracja budowania
- `build.sh` - Skrypt budujący
- `entitlements.plist` - Uprawnienia aplikacji
- `requirements.txt` - Zależności Pythona

## 📝 Licencja

Copyright © 2024 Autology. Wszelkie prawa zastrzeżone.
