# Development Setup
Installing the required Python libraries is mostly operating-system independent. However, the installation of some tools depends on the operating system.

- [Tool Installation](#tool-installations)
    - [Windows](#windows)
    - [Linux](#linux)
- [Library Installation](#library-installation)
    - [Python Libraries](#python-libs)
    - [Webots Configuration](#webot-configuration)

# Tool-Installations
We need:
- Python
- pip
- virtualenv (or Pythons build-in `venv` module)

## Windows
- Python:
    - Download the installer and allow `Add to Path`: [Python Installer Webpage](https://www.python.org/downloads/windows/)

- pip:  
    - should be included

- virtualenv:  
    - should be included



## Linux

- virtualenv:  
    - ubuntu/debian: [wiki.ubuntuusers.de](https://wiki.ubuntuusers.de/venv/)  
    - fedora: [unix.stackexchange.de](https://unix.stackexchange.com/questions/27877/install-virtualenv-on-fedora-16)

- pip:
    > should be preinstalled on all current OS's  

    - ubuntu/Debian: [wiki.ubuntuusers.de](https://wiki.ubuntuusers.de/pip/)  
    - fedora: should be preinstalled

## Mac
> I dont know, help needed

## Docker
> I dont know, help needed



# Library Installation
## Python Libs
### 1. Create virtual environment
```
python -m venv at_venv
```

<details>
<summary>Why use a virtualenv?</summary>
The best practise is using pip in the virtual environment. It will keep all modules for one project at one place and it will not break your local system. Another advantage is that you can have more versions of the same module in different virtual environments.

[From PyPi - Fedora](https://developer.fedoraproject.org/tech/languages/python/pypi-installation.html)
</details>

### 2. Activate the virtual env
**Linux/macOS:**
```bash
source /at_venv/bin/activate
```

**Windows:**
```shell
.\at_venv\Scripts\activate
```

### 3. Install needed libs
```
pip install -r requirements.txt
```

## Webot-Configuration
Webots uses the system Python interpreter by default. Since the required libraries are installed in a virtual environment, Webots must be configured to use the Python interpreter from that environment.

First, activate the virtual environment and locate the Python executable.

Linux:
```
which python
```

Windows:
```
Get-Command python
``` 
Copy the displayed path and configure Webots to use it:  
`Tools -> Preferences -> Python executable`  
Paste your copied path here.