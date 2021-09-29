# GitHub: Command Line Interface

In August 2021, GitHub rolled out it's own command line interface (CLI) that can be used in any terminal or command line.  
When we use GitHub CLI, we use ```gh``` instead of ```git```. This means that we don't need an extra step in using git to connect our computers to GitHub. 
It brings pull requests, issues, and other GitHub concepts to the terminal next to where you are already working with git and your code. 
In this guide, we will focus on installing GitHub CLI using Anaconda Prompt, as the steps you need to this will be the same across all machines. 

To open Anaconda Prompt (anaconda3), simply search for it as you would any other program using the Windows Menu or Spotlight on Mac.

If you're cloning (downloading) GitHub repositories using HTTPS, you can use GitHub CLI. 
This means that when we are cloning a repo we need to use the "HTTPS" option as shown below, if we are not using the GitHub CLI shortcut (more on this later).

<img src="Images/download_ssh.PNG" height=300>

What we will go over in this tutorial is the bascis needed for the course, with addtional resources provided at the end.

1. Getting Started with GitHub CLI
2. Accessing Lectures
3. Working on Assignments

## Getting Started with GitHub CLI
The steps needed to clone a repo using HTTPS, is outlined in the next section, but first we need to download and install the CLI tools, as well as let GitHub know who we are.

If you are interested in other methods of installing GitHub CLI, [more information can be found on the Installation page of the CLI repo](https://github.com/cli/cli#installation)

**Step 1: Download and Install GitHub CLI**

Open Anaconda Prompt and copy and paste (left click) or type the line below into the terminal. Press return/enter.
```
conda install gh --channel conda-forge	
```
NOTE: If you need to update GitHub CLI use ```conda update gh --channel conda-forge```
After a few seconds you will be asked if you wish to proceed with installing ```gh```. Type ```y``` and press enter to install. 


**Step 2: Configuring GitHub CLI**

When the install is finished, we can begin setting up GitHub CLI to work on our computer. Don’t worry if you’ve closed the Anaconda Prompt, just open in again and carry on with these steps – you don’t need to install again. 

Still in the Anaconda Prompt, type ``` gh auth login``` and press enter. You will now be presented with a series of questions to set up GitHub CLI on your computer, as shown below.

```
(base) C:\Users\BrookeSJ> gh auth login

? What account do you want to log into?  [Use arrows to move, type to filter]
> GitHub.com
  GitHub Enterprise Server
```
We can use the cursor (```>```) to select the option that we want. We will use GitHub.com, so we can just press enter to select this. Next, we will be asked what our preferred protocol is, meaning the set of rules, conventions, and data structures that dictate how devices exchange data across networks. Again, the option we want (HTTPS) is already selected, so we can just press enter.

```
? What is your preferred protocol for Git operations?  [Use arrows to move, type to filter]
> HTTPS
  SSH
```
You will be asked if you would like to authenticate Git with your GitHub credentials. Type ```Y``` and press enter.

```
? Authenticate Git with your GitHub credentials? (Y/n)
```
You will then choose how you would like to authenticate (log in with) GitHub CLI. The easiest way is with the web browser option. To choose this, just press enter.
```
? How would you like to authenticate GitHub CLI?  [Use arrows to move, type to filter]
> Login with a web browser
  Paste an authentication token
```
You will then be shown the massage below. Follow the instructions and copy to code. You then to enter. you may need to press it twice before a GitHub “device activation” window opens in your browser.
```
! First copy your one-time code: D67B-2FSF
- Press Enter to open github.com in your browser...
```
If you can’t copy the one-time code, you can just type it in the GitHub device activation window directly (but remember to use caps).

<img src="Images/githubcli_device_activation.png" height=400>


You will then be asked to authorise the application.
 
Click the “Authorize github” button and then enter your password. Note that if you are prompted to log into you GitHub account, then do so. You will then be shown a screen that says “Congratulations, you're all set!” and confirms that your device is now connected to GitHub. 

<img src="Images/githubcli_authorize.png" height=400>

Returning to your Anaconda Prompt window, you should now see a message that confirms you are logged in. Note that the output will display your own username.
```
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as SianJMBrooke
```
To check GitHub CLI has been installed successfully, you can type ```gh``` in Anaconda prompt to see information on usage and commands. You can do this at any point to see what you can do with GitHub CLI.

## 2. Cloning a Existing Repository
**Read: Downloading Github Repo to my Computer**

Cloning a repository pulls down a full copy of all the repository data that GitHub has at that point in time, including all versions of every file and folder for the project. At any point, you can push your changes to the remote repository on GitHub, or pull other people's changes from GitHub. For more information, see "Working From Your Local Computer" below.

On GitHub, navigate to the main page of the repository. 

Above the list of files, click "⬇️ Code".

<img src="Images/download_code.PNG" height=150>

To clone the repository using HTTPS, under "Clone with HTTPS", click 📋. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click **Use SSH**, then click 📋.

<img src="Images/download_ssh.PNG" height=300>

Open Git Bash or your terminal (command line) and change the current working directory to the location where you want the cloned directory (**cd**).

Type```git clone```, and then paste the URL you copied earlier. Then press Enter to create your local clone.

<img src="Images/git_clone.PNG" height=200>

These files should now be copied to your local directory (folder).

To summarise, the code you would need to download the lectures repo for this course, is shown below.

``` bash
git clone https://github.com/lse-my470/lectures.git
```
And you would see a output that looks something like:
```
Cloning into 'lectures'...
remote: Enumerating objects: 1353, done.
remote: Counting objects: 100% (74/74), done.
remote: Compressing objects: 100% (57/57), done.
Receiving objects:  32% (433/1353), 10.23 MiB | 2.23 MiB/s
```
That's it! All of the lecture files are now avaliable on your personal computer.

**August 2021: Using GitHub CLI**
If you have chosen to use GitHub CLI, you can use the command below to download the lectures in Anaconda Prompt.
```
gh repo clone https://github.com/lse-my470/lectures.git
```

This document lays out the main ways that GitHub can be used.
