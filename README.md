# simpcity-watched-dl 

SimpCity Watched Threads Video Downloader

This script downloads video linked in the threads you've added to Watched on SimpCity.

- Use the "Today" keyword to fetch videos posted during the current day.
- Use the "Yesterday" keyword (default) to retrieve videos from the previous day (No need to change anything in code).

Run the script at the end of the day to automatically collect the latest or run at any time for previous day uploaded external‑link videos from your Watched threads.

Tip: Add the file `main.py` in cron job for Linux/MacOS or Scheduled Task for Windows to run python script daily at 12:01 AM or at your time and *ENJOY!*

Note: It does not download images, posts which has written *mirror* word, and embedded videos from turbo. It is created to downlaod only videos with external links. 

It requires 
- Python3.10 or newer 
- SimpCity 
    - account 
    - added thread(s) to Watched 
    - Netscape HTTP Cookie 

Thanks: It uses [gallery-dl](https://github.com/mikf/gallery-dl) to download videos.

# How To

- [Clone Repository](#clone-repository) 
- [Python Setup](#python-setup) 
- [Cookies Setup](#cookies-setup)
- [Customization (optional)](#customization-optional)
- [Run](#run)

## Clone Repository

```bash
git clone https://github.com/oliveiceteaavalanche/simpcity-watched-dl.git

cd simpcity-watched-dl
```

## Python Setup

**Linux / MacOS**

```bash
python3 -m venv .venv 

source .venv/bin/activate

pip install -r requirements.txt
```

**Windows**

```powershell
python -m venv .venv

.venv\Scripts\activate.bat

pip install -r requirements.txt
```

## Cookies Setup

Add an extention for `Netscape HTTP Cookie` in your browser (Firefox browser Add-ons works great). Tested with [Cookies-txt](https://addons.mozilla.org/en-CA/firefox/addon/cookies-txt/).

Login to your SimpCity account (make sure you have added threads to your wached list). 

From the extension, copy cookies for this site and paste it into `cookies.txt` file present in the current directory.

## Customization (Optional)

Default is set to `Yesterday`. Will fetch and download from Yesterday posted content.
 
Replace "Yesterday" with "Today" for today's posts.

Change needs to be done at `scripts` > `step2.py` and find `target_day = "Yesterday"`

## Run

**Automatic Run**

```bash
python main.py
```

Once it starts downloading videos from link, the terminal will feel stuck but it is working in background. 

Downlaoded videos will be stored outside of the current directory- `cd ../city_videos`. Find folder name `city_videos`.

**Custom Run**

```bash
cd scripts

python step1.py

python step2.py

python step3.py
```

You can check which urls are going to be downloaded in the file: 
- `../fetched-links/C.txt`  

You can remove or add links from the `C.txt` file and then run the next step. 

```bash
python step4.py
```

**OR** you can run step 4 directly using *gallery-dl*:
```
gallery-dl -v -i ../fetched-links/C.txt -d ../city_videos
```
Running the above command will provide you progress for each video download.

## Find Logs

- `log.txt`
- Logs reset at every run.

# License

This project is licensed under the **MIT License** 