import logging
import sys
from bs4 import BeautifulSoup

# Setup Logging (matching your previous style)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(sys.stdout)
    ]
)

def extract_target_links():
    target_day = "Today"  # Just change this to "Yesterday" when needed
    input_file = "fetched-links/A.txt"
    output_file = "fetched-links/B.txt"
    base_url = "https://simpcity.cr"
    
    try:
        logging.info(f"Starting Step 2: Extracting {target_day} links...")
        
        # 1. Read the HTML file
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                html_content = f.read()
        except FileNotFoundError:
            logging.error(f"{input_file} not found. Please run Step 1 first.")
            return

        # 2. Parse HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 3. Find all <time> tags containing target_day
        # We look for the text taget_day variable inside the tag
        target_tags = soup.find_all("time", string=lambda text: text and target_day in text)
        
        if not target_tags:
            logging.warning(f"No {target_day} keywords found in <time> tags. Exiting safely.")
            sys.exit(0)

        links = []
        for time_tag in target_tags:
            # Navigate to the parent <a> tag
            parent_a = time_tag.find_parent("a")
            
            if parent_a and 'href' in parent_a.attrs:
                href = parent_a['href']
                
                # Ensure it matches the /threads/.../latest pattern
                if "/threads/" in href and "/latest" in href:
                    full_url = base_url + href if href.startswith("/") else href
                    links.append(full_url)
                    logging.debug(f"Found match: {full_url}")

        # 4. Save to B.txt (using a set to ensure unique URLs)
        unique_links = list(dict.fromkeys(links)) # Preserves order while removing duplicates
        
        if unique_links:
            with open(output_file, "w", encoding="utf-8") as f:
                for link in unique_links:
                    f.write(link + "\n")
            logging.info(f"Successfully extracted {len(unique_links)} unique links to {output_file}")
        else:
            logging.warning(f"Found {target_day} text, but no valid thread links were associated with them.")
            sys.exit(0)

    except Exception as e:
        logging.error(f"An error occurred during extraction: {e}")

if __name__ == "__main__":
    extract_target_links()
