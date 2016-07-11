
#JupyterHub Setup for Rose-Hulman   
This tutorial replicates and extends from the [JupyterHub Pydata 2016](https://github.com/minrk/jupyterhub-pydata-2016/blob/master/JupyterHub.pdf)
###Installing Anaconda Package   
Jupyterhub requires python3, therefore we will use [Anaconda3 package](https://www.continuum.io/downloads) in this tutorial.
Make sure you installed the package in this repository. 
```
/opt/anaconda3/
```
Then add the bin file path to your .bashrc and root user's .bashrc
```{r, engine='bash', count_lines}
export PATH=”$PATH:/opt/anaconda3/bin"
```
###Installing JupyterHub
To do so use type in the following
```
conda install -c conda-forge jupyterhub
```
You do not have to install notebook if you only run a server, but you could by typing the following:
```
conda install notebook
```
Using minrk's github repo which will help you install oauthenticator, dockerspawner and netifaces
```
git clone https://github.com/minrk/jupyterhub-pydata-2016 /srv/jupyterhub
cd /srv/jupyterhub
conda env create -f environment.yml

```
Then add the conda-forge channel for have it manage packages for you
```
conda config --add channels conda-forge
```

###Installing Docker(Optional)
Follow this link to instal docker  
[Docker.io](https://docs.docker.com/engine/installation/linux/ubuntulinux/)

###Adding Python2 and R to your Jupyerhub
For Python2
```
conda create -n py2 python=2 anaconda
source activate py2
ipython kernel install
```
For R
```
conda install -c r r-essentials
conda create -n my-r-env -c r r-essentials
```
For more in depth on R package, your could checkout Christine Doig's blog [Jupyter and Conda for R](https://www.continuum.io/blog/developer/jupyter-and-conda-r)



