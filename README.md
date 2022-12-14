<h1 align="center">PyPhisher</h1>

[![Telegram](https://img.shields.io/badge/Join-Cyberide-green?style=for-the-badge&logo=telegram)](https://t.me/Cyberide)

<p align="center">
   <img src="[https://img.shields.io/badge/Join-Cyberide-green?style=for-the-badge&logo=telegram](t.me/cyberide)"
  <img src="https://img.shields.io/badge/Version-1.9-green?style=for-the-badge"
  <img src="https://img.shields.io/github/issues/KasRoudra/pyphisher?color=red&style=for-the-badge">
<br>
<br>
  <img src="https://img.shields.io/badge/Author-PravarNotFound-purple?style=flat-square">
  <img src="https://img.shields.io/badge/Open%20Source-80%25-cyan?style=flat-square">
  <img src="https://img.shields.io/badge/Made%20in-India-yellow?colorA=%23ff0000&colorB=%23017e40&style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python-blue?style=flat-square">
</p>


### [√] Description :

***Ultimate phishing tool in python. Includes popular websites like facebook, twitter, instagram, github, reddit, gmail and many others.***

### [+] Installation

##### Install primary dependencies (git, python, php)

 - For Debian (Ubuntu, Kali-Linux, Parrot)
    - ```sudo apt install git python php -y```
 - For Arch (Manjaro)
    - ```sudo pacman -S git python php```
 - For Redhat(Fedora)
    - ```sudo dnf install git python php -y```
 - For Termux
    - ```pkg install git python php -y```

##### Clone this repository

 - ```git clone https://github.com/PravarX/PyPhisher```

##### Enter the directory
 - ```cd PyPhisher```

##### Install all modoules
 - ```pip3 install -r requirements.txt```

##### Run the tool
 - ```python3 pyphisher.py```

#### Or, directly run
```
wget https://raw.githubusercontent.com/PravarX/PyPhisher/main/pyphisher.py && python3 pyphisher.py

```

### Pip
 - `pip3 install pyphisher` [For Termux]
 - `sudo pip3 install pyphisher` [For Linux]
 - `pyphisher`

### Docker

 - `sudo docker pull PravarX/pyphisher`
 - `sudo docker run --rm -it PravarX/pyphisher`

#### Options

```
usage: pyphisher.py [-h] [-p PORT] [-o OPTION] [-t TUNNELER] [--noupdate]

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  PyPhisher's server port [ Default : 8080 ]
  -o OPTION, --option OPTION
                        PyPhisher's template index [ Default : null ]
  -t TUNNELER, --tunneler TUNNELER
                        Tunneler to be chosen while url shortening
  --noupdate            Skip update checking
```

### Features:

 - Multi platform (Supports most linux)
 - 77 Website templates
 - Concurrent triple tunneling (Ngrok, Cloudflared and Loclx)
 - OTP Support
 - Credentials mailing
 - Easy to use
 - Possible error diagnoser
 - Built-in masking of URL
 - Custom masking of URL
 - URL Shadowing
 - Portable file (Can be run from any directory)
 - Get IP Address and many other details along with login credentials


### Requirements

 - `Python(3)`
   - `requests`
   - `bs4`
 - `PHP`
 - 200MB storage
 
If not found, php and python modoules will be installed on first run

#### Tested on

 - `Termux`
 - `Ubuntu`
 - `Kali-Linux`
 - `Arch`
 - `Fedora`
 - `Manjaro`

## Usage

1. Run the script
2. Choose a Website
3. Wait sometimes for setting up all
4. Send the generated link to victim
5. Wait for victim login. As soon as he/she logs in, credentials will be captured

<h1 align="center">Example</h1>

![PyPhisher](https://raw.githubusercontent.com/PravarX/PyPhisher/main/files/pyphisher.gif)

## Video Tutorial
<a href="https://rebrand.ly/pyphishervideo">PyPhisher Video</a>

## Whats new in 1.8?
 - *Mailing*
   - Now you can send credentials to any email. You just need a gmail and app password to use this feature. Edit the data in `files/email.json`
 - *Custom Preview*
   - Now you can set a custom social media preview of your link. Enter a website url when asked in `shadow url`. Your link will have same appearence as that website in whatsapp/messenger/telegram etc. Note this only works with Cloudflared urls
 - *OTP Support*
   - 20 templates will show an option to enable otp pages
 - *Saved*
   - An option to view all saved credentials just from PyPhisher. This credentials won't get deleted in PyPhisher update

## Whats new in 1.9?
 - *Loclx*
   - Introducing a new port forwarding/tunneling service named localxpose or loclx. It is quite slower but still usable
 - *Docker image*
   - A docker image is published which can be pulled and run
 - *PIP*
   - This project is now also available in PIP

## Solution of common issues
 - Some secured browsers like Firefox can warn for '@' prefixed links. You should use pure links or custom link to avoid it
 - Ngrok links require Ngrok token to work. Follow the instructions [here](https://github.com/KasRoudra/PyPhisher/issues/1) to set up ngrok token
 - Some android requires hotspot to start Ngrok or Cloudflared. If you face 'tunneling failed' in android, most probably your hotspot is turned off. Turn it on and keep it on untill you close PyPhisher
 - If you want mailing credentials then you need to use app password. Visit [here](https://myaccount.google.com/u/0/apppasswords) and generate an app password, put that in `files/email.json`. You may need to enable 2FA before it
 
## [!] Disclaimer
***This tool is developed for educational purposes. Here it demonstrates how phishing works. If anybody wants to gain unauthorized access to someones social media, he/she may try out this at his/her own risk. You have your own responsibilities and you are liable to any damage or violation of laws by this tool. The author is not responsible for any misuse of PyPhisher!***

### This repository is open source to help others. So if you wish to copy, consider giving credit!

## Credits:
Some base codes and templates are from [htr-tech](https://github.com/htr-tech/zphisher), otp templates are from [ignitech](https://guthub.com/ignitech/AdvPhishing) and url masking is inspired from [jaykali](https://github.com/jaykali/maskphish)

####  If this tool helped you, consider staring repository. Your stars encourage me a lot!

## [~] Find Me on :

- [![Github](https://img.shields.io/badge/Github-PravarX-green?style=for-the-badge&logo=github)](https://github.com/PravarX)

- [![Gmail](https://img.shields.io/badge/Gmail-PravarX-green?style=for-the-badge&logo=gmail)](mailto:PravarX@gmail.com)

- [![Telegram](https://img.shields.io/badge/Telegram-PravarNotFound-green?style=for-the-badge&logo=telegram)](https://t.me/PravarNotFound)

