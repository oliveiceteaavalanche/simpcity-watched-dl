import logging
import sys

# Import functions from your existing files
# Note: Ensure your step files are named exactly like this or rename imports

from scripts.step1 import fetch_watched_threads
from scripts.step2 import extract_target_links
from scripts.step3 import extract_content_links
from scripts.step4 import run_gallery_dl_verbose

def run_pipeline():
    # Setup central logging for the whole process
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("log.txt"),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logging.info("=== STARTING DOWNLOAD PIPELINE ===")

    # Step 1: Fetch HTML
    fetch_watched_threads()

    # Step 2: Extract Target Day Threads
    extract_target_links()

    # Step 3: Extract Content Links
    extract_content_links()

    # Step 4: Download
    run_gallery_dl_verbose()

    logging.info("=== PIPELINE FINISHED ===")

if __name__ == "__main__":
    run_pipeline()
