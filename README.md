# Introduction
This is a very basic discord bot that can play music, it uses lavalink nodes to search and play the music

# Setup
* Make sure to install git here:
https://git-scm.com/download/win
* If you dont have python installed make sure to install it here: https://www.python.org/downloads/
* Make sure when you are installing python u add python.exe to path on the installation process.
First:
* Make sure to install git 
           [Windows](https://git-scm.com/download/win) [Linux](https://git-scm.com/download/linux) [MacOS](https://git-scm.com/download/mac)
* If you dont have python installed make sure to install it from [here](https://www.python.org/downloads)
* On Windows, make sure to add python.exe to your PATH during the installation.

Then, clone the repository:
```
git clone https://github.com/NNKTV28/Discord-Music-bot.git
cd Discord-Music-bot
pip install -r requirements.txt
python -m pip install --upgrade --force-reinstall discord.py
```

Once installed, go to the folder and rename config.env to .env (i added the config because github didnt let me upload the .env file by itself)

Or Download it here (Zip download button):
https://github.com/NNKTV28/Discord-Music-bot/archive/refs/heads/main.zip

# Setup Lavalink
This bot is made so you can run it without having to modify anything apart from your bot token in config.env. In case you want to modify it you have 3 options

### 1- Host lavalink in your pc (only when running bot in the same pc)

### Setup the enviroent

**To make a lavalink server, you will need a java 13 or greater, I recommend using Azul Zulu java 16 or 17**
You can download & setup java by going to here:
* [Linux](https://www.azul.com/downloads/?os=linux&package=jdk) Make sure to get `zulu16-jdk` or `zulu17-jdk`
            * [Ubuntu / Debian; APT Base](https://docs.azul.com/core/zulu-openjdk/install/debian)
            * [Rhel / CentOS / Oracle; RPM Base](https://docs.azul.com/core/zulu-openjdk/install/rpm-based-linux)
            * [Arch](https://aur.archlinux.org/packages/zulu-16-bin/)
* [MacOS](https://www.azul.com/downloads/?os=macos&package=jdk)
* [Windows](https://www.azul.com/downloads/?os=windows&package=jdk)
Once install you can verify it by doing `java -version`, the output should look something like this
```
openjdk version "16.0.2" 2021-07-20
OpenJDK Runtime Environment Zulu16.32+15-CA (build 16.0.2+7)
OpenJDK 64-Bit Server VM Zulu16.32+15-CA (build 16.0.2+7, mixed mode, sharing)
```
depending on your os, you may need to restart to for it to apply.

* Run the lavalink.jar file in the lavalink folder, you can do this by doing: `java jar lavalink.jar`
* Go to `music.py` in the cogs folder and go down to line 88 - 90. You will see this:
```
if not hasattr(bot, 'lavalink'):  # This ensures the client isn't overwritten during cog reloads.
            bot.lavalink = lavalink.Client(bot.user.id)
            bot.lavalink.add_node('lavalink1.albinhakanson.se', 1141, 'albinhakanson.se', 'eu', 'default-node')  # Host, Port, Password, Region, Name
```
* Apply these changes: 

```
 if not hasattr(bot, 'lavalink'):  # This ensures the client isn't overwritten during cog reloads.
            bot.lavalink = lavalink.Client(bot.user.id)
            bot.lavalink.add_node('localhost', 2333, 'youshallnotpass', 'eu', 'default-node')  # Host, Port, Password, Region, Name
```
* Run `Python bot.py`
### 2- Host lavalink in Replit

*  Go to: `repl.it/github/DarrenOfficial/lavalink-replit` and press import from Github
*  Run the replit
*  copy the replit url and put it to your bot
*  make sure you remove `https://` and always connect with the port 443

**The default port to connect is `443` and the default password is `maybeiwasboring`
You can’t change the lavalink port! it will default to 443 due to how replit work.**

### How to keep the replit on with [freshping](https://www.freshworks.com/website-monitoring/)
Go to [freshping](https://www.freshworks.com/website-monitoring/), and set HTTP request to your app I.e. `https://lavalink-replit.sexsells.repl.co/metrics`
and it should show that it's online. if it's show offline, go to your application.yml and make sure metrics is set to on
![freshpingisbetterthanuptimerobot](https://darrennathanael.com/cdn/873E3AB4-8862-49A2-B5F6-5A0B97E3BCF1.jpeg)

only needed if the run button doesnt work.
```bash
chmod +x start.sh
```
```bash
./start.sh
```

### 3- Using a public free node **(Recommended option)**
For this method, i posted a file called `Lavalink free nodes.txt`, in there you have a bunch of nodes that are available to use for anyone, they work Way better than Replit and than self hosting, althoug if the module you are using shuts down, in that file you have many more ones that you can use

* Go to the `music.py` file in the cogs folder
* From line 22 to line 34 **DO NOT TOUCH THAT**, that code block ensures to check if theres any nodes running already, and if not, it will start a node
Code to leave alone:
```
 # ensure a client already exists
        if hasattr(self.client, 'lavalink'):
            self.lavalink = self.client.lavalink
        else:
            self.client.lavalink = lavalink.Client(client.user.id)
            self.client.lavalink.add_node(
                'localhost',
                2333,
                'youshallnotpass',
                'us',
                'default-node'
            )
            self.lavalink = self.client.lavalink
```
- go to line 88 to line 80, thats where you should change the node you are using
```
        if not hasattr(bot, 'lavalink'):  # This ensures the client isn't overwritten during cog reloads.
            bot.lavalink = lavalink.Client(bot.user.id)
            bot.lavalink.add_node('Node link', port, 'Password', 'eu', 'default-node')  # Host, Port, Password, Region, Name

        lavalink.add_event_hook(self.track_hook)
```
        
# For any questions, DM me in discord -> `NNKtv28#7344` 
# Or join my discord server [Python Communists](https://discord.gg/9fQymyuF4c)

