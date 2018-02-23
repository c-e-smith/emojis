## Emoji Maker

Now you can _litter_ your commit messages with emojis!!

![makin mojis yo](/assets/screenshot.png "Recommended Usage")

### Installation steps:
* Copy emojis.py into ~/bin and remove .py extension
  * `mkdir ~/bin && mv emojis.py ~/bin/emojis.py`
* Make executable
  * `mv chmod +x ~/bin/emojis`
* Add `~/bin` to your system path
  * `echo $PATH:~/bin >> ~/.bashrc`

### Usage instructions:

* `emojis [n_emojis]`
* Copy the returned emojis tag into the commit messages
* Have fun! :trollface:
