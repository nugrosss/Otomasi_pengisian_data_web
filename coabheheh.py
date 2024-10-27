import os
from PIL import ImageGrab
import datetime

def take_screenshot():
    # Buat folder 'screenshots' jika belum ada
    folder_name = 'screenshots'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Ambil screenshot
    screenshot = ImageGrab.grab()

    # Dapatkan nama file dengan timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"screenshot_{timestamp}.png"

    # Tentukan path lengkap untuk menyimpan screenshot
    file_path = os.path.join(folder_name, file_name)

    # Simpan screenshot
    screenshot.save(file_path)
    print(f"Screenshot disimpan sebagai: {file_path}")

if __name__ == "__main__":
    take_screenshot()
