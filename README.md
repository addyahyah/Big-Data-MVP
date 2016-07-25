# Setting Up JupyterHub
This tutorial replicates and extends the information in the [JupyterHub PyData 2016](https://github.com/minrk/jupyterhub-pydata-2016/blob/master/JupyterHub.pdf) presentation.

This tutorial runs the server without ssl encryption. For more details on how to adde ssl, read the link above.

by [Runzhi Yang](https://github.com/RunZGit)

## Installation
JupyterHub requires Python 3.3+, so first download the Python 3.5 version of [Anaconda](https://www.continuum.io/downloads).

In this case, we installed Anaconda3 using root privilege.
'''
su
//enter your su password
'''
To set a password for su
'''
sudo passwrd
'''
To install anaconda do
'''
bash anaconda3xxxx.bash
'''
When asked, make sure the package will be installed to this directory:
```
/opt/anaconda3/
```
Open .bashrc and root user's .bashrc 
```{r, engine='bash', count_lines}
vi /home/your_directory/.bashrc
vi /root/.bashrc
```
Then add the bin file path to your in the command line:
```
export PATH=”$PATH:/opt/anaconda3/bin"
```
Type the following into the command line to install JupyterHub:
```
root: conda install -c conda-forge jupyterhub
```
This line adds the conda-forge channel for package management:
```
root: conda config --add channels conda-forge
```
In order to run Jupyterhub without ssl
```
root: mkdir /srv/jupyterhub
root: cd /srv/jupyterhub
root: jupyterhub --no-ssl
```
## Optional Steps
You do not have to install Jupyter Notebook if you are only running a server, but you could by typing the following:
```
root: conda install notebook
```
Using minrk's github repo will help you install oauthenticator, dockerspawner, and netifaces:
```
git clone https://github.com/minrk/jupyterhub-pydata-2016 /srv/jupyterhub
root: cd /srv/jupyterhub
root: conda env create -f environment.yml
```
### Installing Docker
Install Docker here: [Docker.io](https://docs.docker.com/engine/installation/linux/ubuntulinux/)

### Adding Python2 and R to your JupyerHub
Python2:
```
conda create -n py2 python=2 anaconda
source activate py2
ipython kernel install
```
R:
```
conda install -c r r-essentials
conda create -n my-r-env -c r r-essentials
```
For more in-depth information on using R in the Jupyter Notebook environment, check out Christine Doig's blog [Jupyter and Conda for R](https://www.continuum.io/blog/developer/jupyter-and-conda-r).
