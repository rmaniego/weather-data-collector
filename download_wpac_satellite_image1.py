import os
from datetime import datetime
import requests

def main():
    
    print("\n[West Pacific Satellite Image Downloader]")
    
    if not os.path.exists("datasets/accuweather"):
        os.makedirs("datasets/accuweather")

    current_datetime = datetime.now().strftime("%Y-%m-%d")
    filepath = f"datasets/accuweather/{current_datetime}.jpg"
    
    if os.path.exists(filepath):
        print("\nThe file already exist, try again tomorrow.")
        return
    
    # ask the necessary data
    api_key = input("\nEnter your valid AccuWeather API key: ").strip()
    
    if not api_key:
        print(" - Sorry, go to AccuWeather.com to generate your API key.")
        return
    
    
    API_BASE_URL = "https://api.accuweather.com/maps/v1/radar/static/globalSIR/zxyuv/4/13/7/5/3.jpg"
    API_PARAMS = "imgwidth=768&imgheight=432&base_data=radar&language=en"
    
    try:
        # Get the content of the response
        URL = f"{API_BASE_URL}?{API_PARAMS}&apikey={api_key}"
        image = requests.get(URL).content
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