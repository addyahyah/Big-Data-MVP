# Rose-Hulman Big Data Website

To run this web app, you need to install flask in your python environment. In this project, "screen" was used to have the app run in the background.  
To serve the website, type the following in the command line:
```
screen
python app.py
```
Then type Ctrl+a then Ctrl+d to detach the process

To kill the website, search for the process first, then kill it
```
lsof -i tcp:80
kill #app.py pid#
```
