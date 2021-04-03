# Welcome to the Python Class Cookie Cutter

A cookie cutter is a template for creating a new project. This cookie cutter will be used to create a new Python project with all of the development tools and initial code preconfigured and ready for use with Visual Studio Code.

## Getting Started

To use this Cookie Cutter you will need Python and the Cookie Cutter package installed. Also, the files created with the Cookie Cutter project template are designed to work with 

### For Windows

1. Download the Windows Installer for Python from [python.org](https://www.python.org/)

1. On the first page of the installation wizard, check the box to add Python to the path. This will make it easier to run Python from the command prompt.

1. Complete the install as normal.

### For macOS or Linux

1. Install Homebrew from [brew.sh](https://brew.sh/)

1. Then, run:

```bash
brew install python
```

### For All Systems

1. To verify the Python installation, run the following command:

```bash
python -V
```

Ensure it outputs the version you just installed.

- If the version displayed is different from the version installed the most likely you will need to adjust your system paths to resolve to the new Python path. Configuring path environment variables is outside the scope of this document.

### Upgrade PIP and Install Cookie Cutter

With Python installed, let's ensure we have the latest PIP package manager.

```bash
python -m pip install --upgrade pip setuptools wheel
```

With PIP upgraded, now the Cookie Cutter package needs to be installed. From a terminal window, run the following command:

```bash
python -m pip install cookiecutter
```

### Create a new Project with Cookie Cutter

1. From a terminal window, change to the folder where you would like to store your new project.

2. To create the new project, run the following command:

```bash
cookiecutter https://github.com/t4d-starter-projects/cookiecutter-create-python-project
```

3. It will prompt you for a project name, type in a name. I recommended something with no spaces, allow lower case, and no special characters except for an underscore.

4. A new folder is created with the project name. The contents of the cookie cutter project template are copied into the folder.

### Get the Project Up and Running in Visual Studio Code

1. First, ensure you have Visual Studio Code installed. It can be downloaded from here [code.visualstudio.com](https://code.visualstudio.com/).

2. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for Visual Studio Code.

3. Start Visual Studio Code, and open the project folder created by Cookie Cutter.

4. Open a terminal window. Within the terminal session verify you are in the folder with the "requirements.txt" file.

5. Create a new virtual environment.

```bash
python -m venv venv
```

**Note:** On systems where you have Python 2 installed along with Python 3 you may need to use the `python3` command instead of the plain `python` command for this one step.

6. When the environment is created Visual Studio Code should detect it and asked you if you want to make this virtual environment the Python interpreter in Visual Studio, click "Yes".

7. Activate the environment in the terminal window.

**Windows with PowerShell**

```bash
.\venv\Scripts\Activate.ps1
```

**macOS, Linux, Bash/Zsh Shell**

```bash
source ./venv/bin/activate
```

8. Upgrade PIP for the virtual environment.

```bash
python -m pip install --upgrade pip setuptools wheel
```

9. Install the packages listed in the `requirements.txt` file.

```bash
python -m pip install -r requirements.txt
```

10. Congrats! You are all done!

To run the project in various ways, here are the commands:

**Run the Main Module**

```bash
python -m {{cookiecutter.package_name}}
```

**Run the Pylint Linter**

```bash
python -m pylint --max-line-length=79 --unsafe-load-any-extension=y --ignore=.git,venv,.vscode,__pycache__ {{cookiecutter.package_name}} tests
```

**Run the Flake8 Linter**

```bash
python -m flake8 --exclude=venv,.git,__pycache__
```

**Run the MyPy Linter**

```bash
python -m mypy --ignore-missing-imports --follow-imports=silent --show-column-numbers --strict --exclude venv .
```

**Run the Unit Tests with Code Coverage**

```bash
python -m coverage run -m unittest tests.__main__
```

**Generate Code Coverage Report**

```bash
python -m coverage report --omit="venv/*,tests/*,setup.py"
```

## Extra

- Included is an Azure Pipeline file that will validate the source code per the linting rules and run unit tests and code coverage when committed code to Azure Repos.

