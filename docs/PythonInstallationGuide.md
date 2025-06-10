# **Python 3.6+ Setup Guide**
### **1. Download Python 3.6 or Later**
- Visit the [official Python website](https://www.python.org/downloads/) and download the latest **Python 3** version.
- Select the appropriate installer:
  - **Windows:** `.exe` installer
  - **Mac/Linux:** `.pkg` or `.tar.gz` file

### **2. Install Python**
- Run the installer.
- **Important:** Check the box **"Add Python to PATH"** before clicking **Install Now**.
- Follow the installation wizard until it completes.

### **3. Verify Installation**
- Open **Command Prompt (`cmd`)** or **Terminal**, then run:
  - **On Windows:**
    ```sh
    python --version
    ```
  - **On macOS/Linux:**  
    ```sh
    python3 --version
    ```

✅ **If the output displays Python 3.6 or higher, the installation is successful.**  
❌ **If `python3` doesn’t work on Windows, use `python` instead.**  
💡 **Windows typically recognizes Python using `python`, while macOS/Linux often differentiate versions using `python3`.**

### **4. Upgrade Python (If Needed)**
- If your version is **below 3.6**, download a newer version from the [official Python downloads page](https://www.python.org/downloads/).
- On Windows, check if `python` correctly points to Python 3:
  ```sh
  python --version
  ```
- If Python 2 appears instead, update the system PATH or reinstall Python.

_For a more detailed guide, check out [this tutorial](https://www.geeksforgeeks.org/how-to-install-python-on-windows/)._  

