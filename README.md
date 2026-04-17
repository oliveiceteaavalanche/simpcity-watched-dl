# simpcity-watched-dl 

SimpCity Watched Forum/Threads Today or Yesterday Posted Videos Downloader. Think of a script that run and download all* the videos from your watched forums on simpcity website. Run it at the end of the day (with Today keyword) or next day (with Yesterday keyword) and download latest uploaded videos from external links. 

It does not download images, posts which has written *mirror* word, and embedded videos from turbo. It is created to downlaod only videos with external links. 

It requires 
- Python3.10 or newer 
- SimpCity 
    - account 
    - added forums or threads to watched 
    - Netscape HTTP Cookie 
- gallery-dl 

# How To

**Clone Repository**

```bash
git clone https://github.com/oliveiceteaavalanche/simpcity-watched-dl.git

cd simpcity-watched-dl
```

**Python Setup**

```bash
python3.10 -m venv .venv 

source .venv/bin/activate

pip install -r requirements.txt
```

**Cookies**

Add an extention for `Netscape HTTP Cookie` in your browser (Firefox extensions works good).

Login to your SimpCity account (make sure you have added forums to your wached list and they have latest post with urls in it) 

From the extension, copy cookies and paste it into `cookies.txt` file present in the current directory.

**Customize**

Customize today's post or yesterday's post from `scripts` > `step2.py` and find `target_day = "Today"`. Change it to Yesterday if you want yesterdays posted videos. 

**Run**

```bash
python3 main.py
```

**Find Logs**

```bash
cat log.txt
```

## Issues

- Report issue in GitHub Issues > New issue

## Contributing

1. Fork the repository.  
2. Create a feature branch (`git checkout -b feature-name`).  
3. Commit your changes and push (`git push origin feature-name`).  
4. Open a Pull Request describing the improvement.

## License

This project is licensed under the **MIT License** 