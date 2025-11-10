# Pinicker

Pins to Stickers - A simple project that fetches new images from your specified Pinterest boards and bundles them into new WhatsApp sticker packs.

This project uses a manual-check approach. It does not remove image backgrounds and instead creates new, temporary sticker packs each time you check, rather than trying to update old ones.

## <img src="https://img.shields.io/badge/How_It_Works-FF69B4?style=for-the-badge" alt="How It Works" />

This project is split into two parts: a simple Python backend and a lightweight mobile app.

### 1. Backend (Server)

* A Python script (using Flask) waits for a request from your mobile app.
* When triggered, it polls your Pinterest boards ('sad', 'neutral', 'joy') using the Pinterest API.
* It checks a local database (SQLite) to see which pins it has already processed.
* For any new pins, it downloads the image, resizes it to 512x512, and converts it to `.webp` format (under 100 KB).
* It then sends a list of these new sticker files back to your mobile app.

### 2. Mobile App (Client)

* You open the app and press a "Check for New Stickers" button.
* The app calls your backend server.
* It receives the list of new `.webp` stickers.
* It then dynamically groups these stickers into a new pack (e.g., "New Sad Stickers 11-10-2025").
* The app displays an "Add to WhatsApp" button for this new pack.
* You tap the button, WhatsApp opens, and you confirm the import.

## <img src="https://img.shields.io/badge/Tech_Stack-FF69B4?style=for-the-badge" alt="Tech Stack" />

### Backend

* **Language:** Python 3
* **API Framework:** Flask (or FastAPI) to create a simple API endpoint for the mobile app to call
* **API Client:** Requests library to communicate with the Pinterest API
* **Image Processing:** Pillow (PIL) for resizing images and converting them to `.webp` format
* **Database:** SQLite to keep a simple list of processed pin IDs, so you don't get duplicates
* **API:** Pinterest API v5

### Mobile App (Client)

* **Framework:** Flutter (or React Native) to build a simple, cross-platform (Android/iOS) app
* **HTTP Client:** `http` package (for Flutter) to call your backend API
* **Sticker Integration:** A platform-specific sticker pack library (like `whatsapp_stickers_plus` for Flutter) that can call the native WhatsApp intent to add a sticker pack

## <img src="https://img.shields.io/badge/Setup_and_Installation-FF69B4?style=for-the-badge" alt="Setup and Installation" />

### 1. Backend Server

1. **Get Pinterest API Key:** Go to the Pinterest Developer site, create an app, and get your API access token.

2. **Configure Boards:** Edit `config.py` (or similar) and add your specific Pinterest Board IDs for 'sad', 'neutral', and 'joy'.

3. **Install Dependencies:**
```bash
pip install Flask requests Pillow
```

4. **Run Server:**
```bash
python app.py
```

### 2. Mobile App

1. **Clone the Repo:**
```bash
git clone https://github.com/yourusername/pinicker.git
```

2. **Set Server URL:** In the app's configuration (e.g., `lib/constants.dart`), change the `API_URL` to point to your backend server's address (e.g., `http://192.168.1.10:5000`).

3. **Build the App:**
```bash
flutter pub get
flutter run
```

4. **Run:** Open the app and tap the "Check" button.

## <img src="https://img.shields.io/badge/Known_Limitations-FF69B4?style=for-the-badge" alt="Known Limitations" />

* **Manual Action Required:** You must open the app and manually tap "Add to WhatsApp" every time. This is a security feature of WhatsApp.
* **No Background Removal:** This version uses the raw Pinterest image as the sticker.
* **Multiple Packs:** This approach will create many new sticker packs in your WhatsApp (e.g., "New Joy Stickers 1", "New Joy Stickers 2"). You will need to manually delete old packs from WhatsApp if your list gets too cluttered.
* **3-Sticker Minimum:** WhatsApp requires a minimum of 3 stickers per pack. If the script only finds 1 or 2 new pins, it may need to wait or add placeholders (not currently implemented).

## <img src="https://img.shields.io/badge/Future_Ideas-FF69B4?style=for-the-badge" alt="Future Ideas" />

* Implement a "placeholder" system to fill packs that have fewer than 3 new stickers.
* Add an optional toggle to use an AI background removal library (like `rembg`).
* Create a "cleanup" function to merge multiple small packs.

## <img src="https://img.shields.io/badge/License-FF69B4?style=for-the-badge" alt="License" />

It is licensed under [MIT License](https://github.com/Sentinel-Y/Pinicker/blob/main/LICENSE).

## <img src="https://img.shields.io/badge/Contributing-FF69B4?style=for-the-badge" alt="Contributing" />

Fork and start contributing for any discrepencies or new features.
