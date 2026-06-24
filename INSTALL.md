# Development Setup
Installing the required Python libraries is mostly operating-system independent. However, the installation of some tools depends on the operating system.

- [Tool Installation](#tool-installation)
    - [Windows](#windows)
    - [Linux](#linux)
- [Library Installation](#library-installation)
    - [Python Libraries](#python-libraries)
    - [Webots Configuration](#webots-configuration)
- [Git (Optional)](#git-installation-optional)


# Tool-Installation
We need:
- Python
- pip
- virtualenv (or Python's built-in `venv` module)

## Windows
- **Python**:  
    Download Python from: https://www.python.org/downloads/
    1. Run the installer.  
        Important: enable “Add Python to PATH”
    2. Open PowerShell and check:  
        ```
        python -–version
        ```

- **pip**:  
    - Usually included with Python.

- **virtualenv**:  
    - Usually included with Python.


## Linux (Ubuntu/Debian)
- **Python**:
    ```
    sudo apt install python3
    ```
 
- **virtualenv**:  
    ```
    sudo apt install python3-venv
    ```

- **pip**:
    ```
    sudo apt install python3-pip
    ```
  

## Mac
1. Open Terminal.
2. Check whether Python 3 is already installed:
    ```
    python3 --version
    ```
4. If Python is missing, install it from:  https://www.python.org/downloads/

## Docker
> Not yet documented. Help welcome!



# Library Installation
## Python Libraries
### 1. Create a virtual environment
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
source ./at_venv/bin/activate
```

**Windows:**
```shell
.\at_venv\Scripts\activate
```

### 3. Install needed libraries
```
pip install -r requirements.txt
```

# Webots-Configuration
## Installation

- Go to the official Cyberbotics/Webots website: https://cyberbotics.com/
- Download the Webots installer for your operating system. The Webots website normally provides the correct
download for your operating system automatically.

### Windows
Download the Windows installer, e.g. `webots-..._setup.exe.`  
- Run the installer.
- Choose the default installation location unless you have a specific reason to change it.
- Start Webots from the Start Menu.

### Linux (Ubuntu/Debian)
1. Download the .deb package for your Ubuntu version.
2. Install it from the terminal, for example:
    ```
    sudo apt install ./webots_*.deb
    ```
3. Run Webots from the Start Menu or running
    ```
    webots
    ```

### macOS
Go to the official Cyberbotics/Webots website: https://cyberbotics.com/
1. Download the `.dmg` installer.
2. Open the `.dmg` file.
3. Drag Webots into the Applications folder.
4. Start Webots.  

## Configuration
Webots uses the system Python interpreter by default. Since the required libraries are installed in a virtual environment, Webots must be configured to use the Python interpreter from that environment.

First, activate the virtual environment and locate the Python executable.

Linux/macOS:
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

# Git installation (Optional)
Git is optional, but recommended for keeping track of changes in your Python/Webots controller code and for using version control in your project.  
1. Go to the official Git website: https://git-scm.com/
2. Download and install Git for your operating system. The official Git documentation provides installation instructions and installers for different systems.  
3. After installation, check that Git works:
    ```
    git --version
    ```
- Recommendation:  
Use Git together with GitHub, GitLab, or another remote repository to keep an online backup of your project.