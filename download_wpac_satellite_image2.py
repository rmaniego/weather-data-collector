import os
from datetime import datetime
import requests

def main():
    
    print("\n[West Pacific Satellite Image Downloader (Himawari)]")

    current_datetime = datetime.now().strftime("%Y-%m-%d_%H")
    filepath = f"datasets/{current_datetime}-himawari.gif"
    
    if os.path.exists(filepath):
        print("\nThe file already exist, try again tomorrow.")
        return
    
    try:
        # Get the content of the response
        API_URL = "https://www.ssd.noaa.gov/jma/wpac/vis-l.gif"
        image = requests.get(API_URL).content
    except Exception as e:
        print("Error encountered during the download.\n", e)
        return
    
    # Save the image data into file
    with open(filepath, "wb") as file:
        file.write(image)

    root_path = os.getcwd().replace("\\", "/")
    print(f"\nOpen satellite image: {root_path}/{filepath}")

if __name__ == "__main__":
    main()