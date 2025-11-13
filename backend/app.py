import os
import requests
from flask import Flask, jsonify, send_from_directory
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# --- CONFIGURATION ---
# Folder to store processed stickers
STICKER_FOLDER = 'stickers'
if not os.path.exists(STICKER_FOLDER):
    os.makedirs(STICKER_FOLDER)

# Mock data for testing (Use this until you get your real Pinterest API Key)
USE_MOCK_DATA = True 

def process_image(image_url, filename):
    """Downloads, resizes to 512x512, and saves as WebP"""
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    
    # Resize to exactly 512x512 (WhatsApp Requirement)
    img = img.resize((512, 512))
    
    # Save as WebP
    save_path = os.path.join(STICKER_FOLDER, filename)
    img.save(save_path, 'webp', quality=80)
    return filename

@app.route('/get-new-stickers', methods=['GET'])
def get_stickers():
    print("📱 App requested new stickers...")
    
    new_stickers = []
    
    if USE_MOCK_DATA:
        # These are just random images for testing
        mock_images = [
            ("https://images.unsplash.com/photo-1517849845537-4d257902454a", "sad_1.webp"),
            ("https://images.unsplash.com/photo-1595433707802-6b2626ef1c91", "joy_1.webp"),
            ("https://images.unsplash.com/photo-1472214103451-9374bd1c798e", "neutral_1.webp")
        ]
        
        for url, name in mock_images:
            try:
                # Process the image
                filename = process_image(url, name)
                
                # Create the full URL so the phone can download it
                # NOTE: '10.0.2.2' is a special code for Android Emulators to talk to Localhost
                # If testing on a REAL phone, this must be your computer's IP address (e.g., 192.168.1.X)
                full_url = f"http://10.0.2.2:5000/stickers/{filename}"
                
                new_stickers.append(full_url)
            except Exception as e:
                print(f"Error processing {name}: {e}")

    # Return the list of sticker URLs to the app
    return jsonify({
        "pack_name": "New Pinterest Pack",
        "stickers": new_stickers
    })

@app.route('/stickers/<path:filename>')
def serve_sticker(filename):
    """Allows the app to download the image file"""
    return send_from_directory(STICKER_FOLDER, filename)

if __name__ == '__main__':
    # Get the PORT from the environment (Cloud) or use 5001 (Local)
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)