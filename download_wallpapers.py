import requests
import time
import os
import re

# Configuration
SAVE_DIR = r"D:\File\Dev\Blog\Applied-Energetic.github.io\static\picture"
API_URL = "https://wallhaven.cc/api/v1"
LIMIT = 50
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

def get_top_wallpapers(limit=50):
    wallpapers = []
    page = 1
    while len(wallpapers) < limit:
        print(f"Fetching page {page}...")
        try:
            # sorting=toplist, purity=100 (SFW), topRange=1M (Last Month - popular)
            # You can change topRange to '1y' or 'all' for all-time top.
            url = f"{API_URL}/search?sorting=toplist&purity=100&topRange=1M&page={page}"
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            data = response.json().get('data', [])
            
            if not data:
                break
                
            for item in data:
                if len(wallpapers) >= limit:
                    break
                wallpapers.append(item)
            
            page += 1
            time.sleep(1) # Be nice to the API
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            break
    return wallpapers

def get_wallpaper_tags(wallpaper_id):
    try:
        url = f"{API_URL}/w/{wallpaper_id}"
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code == 429: # Rate limit
            print("Rate limit hit, sleeping for 5 seconds...")
            time.sleep(5)
            response = requests.get(url, headers=HEADERS) # Retry once
            
        if response.status_code == 200:
            data = response.json().get('data', {})
            tags = [tag['name'] for tag in data.get('tags', [])]
            return tags
    except Exception as e:
        print(f"Error fetching tags for {wallpaper_id}: {e}")
    return []

def download_image(url, filepath):
    try:
        response = requests.get(url, headers=HEADERS, stream=True)
        response.raise_for_status()
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def main():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
        print(f"Created directory: {SAVE_DIR}")

    print(f"Getting top {LIMIT} wallpapers...")
    wallpapers = get_top_wallpapers(LIMIT)
    print(f"Found {len(wallpapers)} wallpapers. Starting download...")

    for i, wp in enumerate(wallpapers):
        wp_id = wp['id']
        wp_url = wp['path']
        ext = os.path.splitext(wp_url)[1]
        
        # Get tags only if we need to name by tags
        # Rate limiting: 45 req/min. We have 50 items. This will take >1 min.
        print(f"[{i+1}/{len(wallpapers)}] Fetching details for {wp_id}...")
        tags = get_wallpaper_tags(wp_id)
        
        # Construct filename
        if tags:
            # Use top 3 tags, replace spaces with hyphens
            tag_str = "-".join([t.replace(" ", "") for t in tags[:3]])
            filename = f"{tag_str}-{wp_id}{ext}"
        else:
            filename = f"wallhaven-{wp_id}{ext}"
            
        filename = sanitize_filename(filename)
        filepath = os.path.join(SAVE_DIR, filename)

        if os.path.exists(filepath):
            print(f"Skipping {filename}, already exists.")
            continue

        print(f"Downloading to {filename}...")
        if download_image(wp_url, filepath):
            print("Done.")
        
        # throttle to avoid 429 Too Many Requests
        time.sleep(1.5)

if __name__ == "__main__":
    main()
