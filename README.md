# simpcity-watched-dl 

SimpCity Watched Forum/Threads Today or Yesterday Posted Videos Downloader. Think of a script that run and download all* the videos from your watched forums on simpcity website. Run it at the end of the day (with Today keyword) or default- previous day (with Yesterday keyword) and download latest uploaded videos from external links. 

It does not download images, posts which has written *mirror* word, and embedded videos from turbo. It is created to downlaod only videos with external links. 

It requires 
- Python3 
- SimpCity 
    - account 
    - added forums or threads to watched 
    - Netscape HTTP Cookie 

It uses [gallery-dl](https://github.com/mikf/gallery-dl) to download videos.

# How To

**Clone Repository**

```bash
git clone https://github.com/oliveiceteaavalanche/simpcity-watched-dl.git

cd simpcity-watched-dl
```

### Linux

**Python Setup**

```bash
python3 -m venv .venv 

source .venv/bin/activate

pip install -r requirements.txt
```

Next refer to [Download](#Download) steps

### Windows

```cmd
python -m venv .venv

.venv\Scripts\activate.bat

pip install -r requirements.txt
```

Next refer to [Download](#Download) steps

### Download

#### Cookies

Add an extention for `Netscape HTTP Cookie` in your browser (Firefox extensions works good).

Login to your SimpCity account (make sure you have added forums to your wached list). 

From the extension, copy cookies and paste it into `cookies.txt` file present in the current directory.

#### Customize

Customize today's post or yesterday's post from `scripts` > `step2.py` and find `target_day = "Yesterday"`

Default is set to `Yesterday`. You can change it to `Today`, if you want today's posted videos. 

#### Run

**Automatic Run**

```bash
python3 main.py
```

**Custom Run**

```bash
cd scripts

python3 step1.py

python3 step2.py

python3 step3.py
```

Check which urls going to be downloaded in `fetched-links/C.txt`  

You can remove or add links from the `C.txt` file and then run the next step. 

```bash
python3 step4.py
```


#### Find Logs

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