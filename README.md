# TestGenerator
unit test generation tool.

Intellij setup:
-

### **1. Download IntelliJ IDEA**
- Go to the [official JetBrains website](https://www.jetbrains.com/help/idea/installation-guide.html) and download IntelliJ IDEA.
- Choose between:
  - **Community Edition** (Free, for Java and Android development).
  - **Ultimate Edition** (Paid, with advanced features for web and enterprise development).

### **2. Install IntelliJ IDEA**
- Run the downloaded installer (`.exe` for Windows).
- Follow the installation wizard:
  - Select installation location.
  - Choose additional components (like JetBrains Toolbox).
  - Click **Install** and wait for the process to complete.

### **3. Configure IntelliJ IDEA**
- Launch IntelliJ IDEA.
- Configure the **JDK** (Java Development Kit):
  - If you don’t have one, IntelliJ will prompt you to download it.
- Set up **plugins** if needed.


_For a more detailed guide, check out [JetBrains' official documentation](https://www.jetbrains.com/help/idea/installation-guide.html) or this [step-by-step tutorial](https://www.geeksforgeeks.org/step-by-step-guide-to-install-intellij-idea/)._

Python 3 setup:
-

#### **1. Download Python 3**
- Visit the [official Python website](https://www.python.org/downloads/) and download the latest **Python 3** version.
- Select the appropriate installer:
  - **Windows:** `.exe` installer.
  - **Mac/Linux:** `.pkg` or `.tar.gz` file.

#### **2. Install Python 3**
- Run the installer.
- **Important:** Check the box **"Add Python to PATH"** before clicking **Install Now**.
Follow the installation wizard until it is completed.

#### **3. Verify Installation**
- Open **Command Prompt (`cmd`)** or **Terminal** and run:
  - **On Windows:**  
    ```
    python --version
    ```
  - **On macOS/Linux:**  
    ```
    python3 --version
    ```

✅ If the command displays Python 3.x, the installation is successful.  

_For a more detailed guide, check out [this tutorial](https://www.geeksforgeeks.org/how-to-install-python-on-windows/)._


Plugin setup -
-

_with git installation

Git installation
### **1. Download Git**
- Visit the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) and download the latest version for your operating system.
- Choose the appropriate installer:
  - **Windows:** `.exe` installer
  - **Mac/Linux:** `.pkg` or `.tar.gz` file

### **2. Install Git**
- Run the installer and follow the setup wizard.
- **Windows Users:**  
  - During installation, select **Git Bash** as your default terminal (recommended).
  - Choose the default editor (VS Code, Vim, Nano, etc.).
  - Ensure **"Use Git from the Windows Command Prompt"** is selected.

### **3. Verify Installation**
- Open **Command Prompt (`cmd`)** or **Git Bash** and run:
  ```
  git --version
  ```
- If Git is installed correctly, it will display the version number.

### **4. Clone the Repository**
Clone the repository to the relevant path on your pc, according to your operating system-
 - Find your path by your operating system:
   - **Windows** -
     ```
     C:\\Program Files
     ```
   - **Mac** - 
     ```
     /User
     ```
   - **Linux/Unix** - 
     ```
     /home
     ```
 - Open your terminal and insert the following commands:

  ```
  cd <path>
  git clone https://github.com/orerez1/TestGenerator.git
  ```

For more details, check out [Git’s official setup guide](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) or [GitHub’s documentation](https://docs.github.com/en/get-started/git-basics/set-up-git).
