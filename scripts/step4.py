import subprocess
import logging
import os
import sys

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(sys.stdout)
    ]
)

def run_gallery_dl_verbose():
    input_file = "fetched-links/C.txt"
    download_dir = "../city_videos"
    
    # 1. Validation
    if not os.path.exists(input_file) or os.path.getsize(input_file) == 0:
        logging.error(f"{input_file} is missing or empty. Run Step 3 first.")
        return

    # 2. Ensure download directory exists
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        logging.info(f"Created directory: {download_dir}")

    logging.info(f"Starting gallery-dl in VERBOSE mode for {input_file}...")

    # 3. Construct the command
    # -v: Verbose mode (shows internal logic and extractor details)
    # -i: Input file
    # -o: Base directory for output
    command = [
        "gallery-dl",
        "-v", 
        "--input-file", input_file,
        "-o", f"base-directory={download_dir}"
    ]

    try:
        # 4. Execute and stream output
        # We redirect stderr to stdout so we catch both normal logs and errors
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        # 5. Log everything gallery-dl spits out
        for line in process.stdout:
            clean_line = line.strip()
            if clean_line:
                # This will now include the verbose [gallery-dl] logs
                logging.info(f"[gallery-dl] {clean_line}")

        process.wait()

        if process.returncode == 0:
            logging.info("Step 4 Complete: Downloads finished successfully.")
        else:
            logging.error(f"gallery-dl exited with code {process.returncode}. Check log.txt for details.")

    except FileNotFoundError:
        logging.error("gallery-dl not found. Ensure it is installed in your .venv.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_gallery_dl_verbose()
