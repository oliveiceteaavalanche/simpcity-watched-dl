import requests
import logging
import http.cookiejar
import sys
import os
from bs4 import BeautifulSoup

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(sys.stdout)
    ]
)

def extract_content_links():
    input_file = "fetched-links/B.txt"
    output_file = "fetched-links/C.txt"
    cookie_file = "cookies.txt"
    
    if not os.path.exists(input_file):
        logging.error(f"{input_file} not found. Please run Step 2 first.")
        return

    # Load Cookies & Session
    cookie_jar = http.cookiejar.MozillaCookieJar(cookie_file)
    try:
        cookie_jar.load(ignore_discard=True, ignore_expires=True)
    except Exception as e:
        logging.error(f"Cookie load failed: {e}")
        return

    session = requests.Session()
    session.cookies = cookie_jar
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0"
    })

    try:
        with open(input_file, "r") as f:
            thread_urls = [line.strip() for line in f if line.strip()]

        final_links = []
        
        # --- CONFIGURATION FOR FILTERS ---
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')
        ignore_text_keywords = ["mirror", "mirrors"]
        blocked_site_keywords = ["jpg6", "turbo"]

        for thread_url in thread_urls:
            logging.info(f"Processing thread: {thread_url}")
            try:
                response = session.get(thread_url, timeout=15)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')

                # Remove iframes entirely
                for iframe in soup.find_all("iframe"):
                    iframe.decompose()

                # Target the post content
                posts = soup.find_all("div", class_="bbWrapper")
                
                for post in posts:
                    links = post.find_all("a", href=True)
                    
                    for link in links:
                        href = link['href']
                        href_lower = href.lower()
                        link_text = link.get_text(strip=True).lower()
                        parent_text = link.parent.get_text().lower()

                        # --- FILTERS ---

                        # 1. Internal Links or Fragments (#)
                        # We ignore anything with # and anything pointing back to the site
                        if "#" in href or "simpcity.cr" in href_lower or href.startswith("/"):
                            logging.debug(f"Filtered (Internal/Anchor): {href}")
                            continue
                        
                        # 2. Image Extensions
                        if any(href_lower.endswith(ext) for ext in image_extensions):
                            logging.debug(f"Filtered (Image Extension): {href}")
                            continue

                        # 3. Blocked Sites (jpg6, turbo)
                        if any(site in href_lower for site in blocked_site_keywords):
                            logging.info(f"Filtered (Blocked Site): {href}")
                            continue

                        # 4. Mirror Keywords in Text
                        if any(kw in link_text for kw in ignore_text_keywords) or \
                           any(kw in parent_text for kw in ignore_text_keywords):
                            logging.info(f"Filtered (Mirror keyword): {href}")
                            continue

                        # If it passes everything, add the original URL
                        final_links.append(href)
                        logging.info(f"Found valid URL: {href}")

            except Exception as e:
                logging.error(f"Failed to process {thread_url}: {e}")

        # Save unique links to C.txt
        unique_final_links = list(dict.fromkeys(final_links))
        if unique_final_links:
            with open(output_file, "w") as f:
                for link in unique_final_links:
                    f.write(link + "\n")
            logging.info(f"Step 3 Complete. {len(unique_final_links)} links saved to {output_file}")
        else:
            logging.warning("No valid content links found. C.txt is empty.")

    except Exception as e:
        logging.error(f"An error occurred in Step 3: {e}")

if __name__ == "__main__":
    extract_content_links()
