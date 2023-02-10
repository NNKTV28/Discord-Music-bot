# Setup
- Make sure to install git here:
https://git-scm.com/download/win
- If you dont have python installed make sure to install it here: https://www.python.org/downloads/
- Make sure when you are installing python u add python.exe to path on the installation process.
First:
- Make sure to install git ([Windows](https://git-scm.com/download/win), [Linux](https://git-scm.com/download/linux), [macOS](https://git-scm.com/download/mac))
- If you dont have python installed make sure to install it from [here](https://www.python.org/downloads)
- On Windows, make sure to add python.exe to your PATH during the installation.

Then, clone the repository:
```
git clone https://github.com/NNKTV28/Discord-Music-bot.git
cd Discord-Music-bot
pip install -r requirements.txt
```

Once installed, go to the folder and rename config.env to .env (i added the config because github didnt let me upload the .env file by itself)

Or Download it here (Zip download button):
https://github.com/NNKTV28/Discord-Music-bot/archive/refs/heads/main.zip

# Setup Lavalink
This bot is made so you can run it without having to modify anything apart from your bot token in config.env. In case you want to modify it you have 3 options

### 1- Host lavalink in your pc (only when running bot in the same pc)

- Run the lavalink.jar file in the lavalink folder, you can do this by doing: java jar lavalink.jar

### 2- Host lavalink in Replit

-  Go to: `repl.it/github/DarrenOfficial/lavalink-replit` and press import from Github
-  Run the replit
-  copy the replit url and put it to your bot
-  make sure you remove `https://` and always connect with the port 443

**The default port to connect is `443` and the default password is `maybeiwasboring`
You can’t change the lavalink port! it will default to 443 due to how replit work.**

### How to keep the replit on with [freshping](https://www.freshworks.com/website-monitoring/)
Go to [freshping](https://www.freshworks.com/website-monitoring/), and set HTTP request to your app I.e. `https://lavalink-replit.sexsells.repl.co/metrics`
and it should show that it's online. if it's show offline, go to your application.yml and make sure metrics is set to on
![freshpingisbetterthanuptimerobot](https://darrennathanael.com/cdn/873E3AB4-8862-49A2-B5F6-5A0B97E3BCF1.jpeg)
