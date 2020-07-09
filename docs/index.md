Recently, I experienced unusual crashes with my old friend, Spyder IDE. It was a bit frustrated to restart anaconda and spyder. It is perhaps a sign to move on. Then, I turned to look for alternatives. Some fellows are using vscode and I am attracted by its convenience and endless extenstions at first sight. To get it seup, it takes some time, but it all worths it. 

Now let us dig into some of the issues that enable me to get started. First open the project root folder in vscode. Vscode is still an IDE, thus it does not manage the data science python or conda environment. The first thing we need is either a miniconda or conda environment so that we can manage all the packages. Let us assume that you have a anaconda distribution and some virtual environment is created. When you start vscode, you can see all the created and default environment. You can switch to the virtual environment that you would like to use.   

# .vscode folder
This is quite important for setting up the vscode. If you directly start from a new project from vscode, this folder is setup automatically. If you import some repos, then add this folder before doing anything. Two important files shall live in this folder are launch.json and settings.json. In launch.json, we adjust the configrations. In settings.json, we point the python path or tests framework etc. 

# run python interactive
This was one of the reasons that I did not want to giveup spyder, now vscode has it as well. The default way of running script set the path to where the script is. This can be inconvenient is we want to our path always start from project root, which is the case when you want to deploy your code somewhere, for example docker. To change this, a convenient way is to follow  File->preference->settings->workspace->extensions->python->Notebook File root, set to ${workspaceFolder} instead of ${fileDirname}. 

# parser.parse_args() does not work in python interactive

This is can be solved run sys.argv = [''] before running argpaser in python interactives. See, https://github.com/microsoft/vscode-python/issues/11206

# pytest discovery failed (exit code 2)

This can caused by that the folder and the test_**.py has the same name. If your test files are nested in a deep directory structure, try add a __init__.py file in the same folder. 

# Debugger issue

## 1) conda not found error or 'conda' command is not recognized, which causes the debugger could not work properly 

This results from installing anaconda process in which we did not select add conda to path. Thus, to fix this, we need to first find where we installed our conda and python. Then, add them to the environment variables path. Type in anaconda prompt. First, where python, keep the path info. Then type where conda, keep the path info. The order is not important. Then, type SETX PATH "%PATH%;C:\<path>\Anaconda3;C:\<path>\Anaconda3\Scripts;C:\<path>\Anaconda3\Library\bin" where you shall use the right path that you obtained previousely. Then in vscode powershell, type conda init 

Why this important? because vscode's debugger needs to find the right environment where you install you packages. Even through, you have set the enviroment in vscode, but it still need to run conda activate ** to switch to the right env before debugging. If the env is not right, some packages may not be setup correctly.  

# push docker: unauthentification issue.
This can be solved using az login in the powershell. Remember to switch to the right subscription. 
