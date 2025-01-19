# Autology Remote Connect

Aplikacja proxy dla systemu macOS umożliwiająca bezpieczną komunikację między aplikacją chmurową Autology Pilot App a dronem Parrot Anafi.

## 🌟 Główne funkcje

- 🔄 Serwer proxy dla komunikacji z dronem
- 🔒 Bezpieczna autoryzacja przez JWT
- ☁️ Automatyczna konfiguracja tunelu Cloudflared
- 📊 Monitorowanie stanu połączenia
- 📝 System logowania i eksportu logów

## 💻 Wymagania systemowe

- macOS 10.15 lub nowszy
- Python 3.11
- Połączenie internetowe
- Dron Parrot Anafi w sieci lokalnej

## 🛠️ Instalacja

1. Pobierz najnowszą wersję aplikacji z sekcji [Releases](../../releases)
2. Otwórz plik DMG
3. Przeciągnij aplikację do folderu Applications
4. Uruchom aplikację

## 📋 Użytkowanie

### Menu aplikacji
- **Start Server** - Uruchamia serwer proxy i tunel Cloudflared
- **Stop Server** - Zatrzymuje serwer i tunel
- **Check Status** - Sprawdza stan serwera
- **Start/Stop Monitoring** - Zarządza automatycznym monitorowaniem
- **Export Logs** - Eksportuje logi (ZIP/TXT)

### API Endpoints
- `/start-server` - Uruchamia serwer (POST)
- `/stop-server` - Zatrzymuje serwer (POST)
- `/proxy/<path>` - Endpoint proxy dla żądań do drona
- `/status` - Sprawdza stan serwera (GET)
- `/check-drone` - Sprawdza połączenie z dronem (GET)
- `/logs` - Pobiera logi (GET)
- `/logs/export` - Eksportuje logi do ZIP (GET)
- `/logs/export/txt` - Eksportuje logi do TXT (GET)

## 🔒 Bezpieczeństwo

- Wszystkie endpointy wymagają autoryzacji JWT
- Automatyczne czyszczenie starych logów
- Bezpieczny tunel Cloudflared

## 📝 Logi

Logi są przechowywane w:
```
~/Library/Logs/AutologyRemoteConnect/
```
- Automatyczna rotacja przy 10MB
- Maksymalnie 5 plików logów
- Automatyczne czyszczenie po 30 dniach
- Eksporty są czyszczone po 7 dniach

## 🛠️ Rozwój

### Wymagane narzędzia

## Instalacja zależności
```
pip install -r requirements.txt
```
## Nadaj uprawnienia wykonywania dla skryptu build
```
chmod +x build.sh
```
## Zbuduj aplikację
```
./build.sh
```

## 📝 Licencja

Copyright © 2024 Autology. Wszelkie prawa zastrzeżone.
