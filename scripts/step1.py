import requests
import logging
import http.cookiejar
import sys

# 1. Setup Logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("log.txt", mode="w"),
        logging.StreamHandler(sys.stdout)
    ]
)

def fetch_watched_threads():
    url = "https://simpcity.cr/watched/threads"
    cookie_file = "cookies.txt"
    output_file = "fetched-links/A.txt"
    
    # Custom User-Agent to mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    try:
        logging.info("Starting Step 1: Fetching watched threads...")
        
        # 2. Load Netscape Cookies
        cookie_jar = http.cookiejar.MozillaCookieJar(cookie_file)
        try:
            cookie_jar.load(ignore_discard=True, ignore_expires=True)
            logging.info(f"Successfully loaded {cookie_file}")
        except FileNotFoundError:
            logging.error(f"Error: {cookie_file} not found. Please place it in the script directory.")
            return
        except Exception as e:
            logging.error(f"Failed to load cookies: {e}")
            return

        # 3. Create Session and Fetch Data
        session = requests.Session()
        session.cookies = cookie_jar
        
        logging.info(f"Requesting URL: {url}")
        response = session.get(url, headers=headers, timeout=15)
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # 4. Save to A.txt
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(response.text)
        
        logging.info(f"Successfully saved HTML content to {output_file}")
        logging.info("Step 1 complete.")

    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP Error occurred: {e}")
        if response.status_code == 403:
            logging.error("Access Denied (403). Your cookies might be expired or Cloudflare is blocking the request.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_watched_threads()
