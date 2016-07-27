# Rose-Hulman Big Data Website

To run this web app, you need to install flask in your python environment. In this project, "screen" was used to have the app run in the background.  

Special step needed for Jupyterflow machine  
```
source activate py2
```

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
In order to have d3 to display the graph, the data has to be passed in the following format, the number of rows are arbitrary:

![Image of data format](https://github.com/shibberu/Big-Data-MVP/blob/master/Website/data/Required%20Data%20format.png)
