# TestGenerator
unit test generation tool.

The following guide assumes that you already have Python 3.6 or later and IntelliJ installed.
If you don't then follow these guides first to install them:
[Python setup guide](https://github.com/orerez1/TestGenerator/blob/20-installation-guide/docs/PythonInstallationGuide.md), 
[IntelliJ setup guide](https://github.com/orerez1/TestGenerator/blob/20-installation-guide/docs/IntelliJ%20installation%20guide.md)


Plugin setup -
-
_Here's a guide for [git setup](https://github.com/orerez1/TestGenerator/blob/20-installation-guide/docs/git%20setup%20guide.md) for easier future setup_


### **1. Clone the Repository**

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
  _With git installation_
 - Open your terminal and insert the following commands:

  ```
  cd <path>
  git clone https://github.com/orerez1/TestGenerator.git
  ```
_Without git installation_

 - Go to the [main page of the project](https://github.com/orerez1/TestGenerator)
 - Click on the "Code" button to open a dropdown menu
 - Click on "Download ZIP"
 - Download it to <path> if possible
 - If you can't download it directly to the path, download it to somewhere you can, extract it, and move it to the right path
 - Might need admin permissions


### **2. Install the Plugin in IntelliJ IDEA**  
Now that you have cloned the `TestGenerator` repository to the appropriate path, follow these steps to install the plugin:

1. **Open IntelliJ IDEA**  
   Launch IntelliJ IDEA on your computer.

2. **Navigate to the Plugins Menu**  
   - Click on **File > Settings** (or **Preferences** on macOS).  
   - Open the **Plugins** tab.

3. **Install the Plugin from Disk**  
   - Click the gear icon ⚙️ at the top right corner.  
   - Select **Install Plugin from Disk...**  
   - Browse to the cloned repository location:  
     - **Windows:** `C:\Program Files\TestGenerator\Plugin\Plugin for installation\TestGeneratorPlugin-1.0-SNAPSHOT.zip`  
     - **Mac:** `/User/TestGenerator/Plugin/Plugin for installation/TestGeneratorPlugin-1.0-SNAPSHOT.zip`  
     - **Linux/Unix:** `/home/TestGenerator/Plugin/Plugin for installation/TestGeneratorPlugin-1.0-SNAPSHOT.zip`  
   - Select the file and click **OK** to install it.

4. **Apply Changes and Restart IntelliJ IDEA**  
   - Click **Apply** or **OK** to confirm the installation.  
   - Restart IntelliJ IDEA to activate the plugin.

### **3. Verify Installation**  
Once IntelliJ IDEA restarts, follow these steps to verify that the plugin is installed correctly:

- Go to **File > Settings > Plugins** and search for "TestGenerator."
- Ensure that it is listed and enabled.
- Open a test file and try generating unit tests using the plugin to confirm it’s functioning properly.

### **4. Troubleshooting**  
If you run into issues:  
- Double-check that you cloned the repository to the correct path.  
- Ensure you have the correct IntelliJ IDEA version.  
- Verify that your Python environment is set up correctly.  
- Check IntelliJ's log files (**Help > Show Log in Explorer**) for possible error messages.  
- Try reinstalling the plugin using the steps above.  


