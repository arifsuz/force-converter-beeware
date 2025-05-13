# **Force Converter Project Documentation**

## **Introduction**

The **Force Converter** project is a cross-platform application designed to convert various units of force. Built using the **BeeWare** framework, this project allows developers to create applications that run seamlessly on multiple platforms, including:

- **Desktop**: Windows, macOS, and Linux.
- **Mobile**: Android and iOS.
- **Web**: Through WebAssembly.

This documentation provides a comprehensive guide to setting up, running, customizing, and contributing to the project.

---

## **1. Cloning the Project**

To begin, clone the repository to your local machine.

### **Steps:**
1. Ensure **Git** is installed on your system.
2. Open a terminal or command prompt and run the following command:
   ```bash
   git clone https://github.com/arifsuz/force-converter.git
   ```
3. Navigate to the project directory:
   ```bash
   cd force-converter
   ```

---

## **2. Setting Up the Project**

### **Prerequisites:**
Before setting up the project, ensure the following tools are installed:
- **Python** (version 3.8 or later).
- **pip** (Python package manager).
- **virtualenv** (for managing Python virtual environments).
- **BeeWare Briefcase** (for building and running cross-platform applications).

### **Setup Steps:**
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install BeeWare Briefcase:
   ```bash
   pip install briefcase
   ```

---

## **3. Running the Project**

The project can be run on various platforms. Below are the instructions for each platform:

### **3.1 Running on Desktop (Windows, macOS, Linux)**
1. Run the application in development mode:
   ```bash
   briefcase dev
   ```
2. Create the application for desktop:
   ```bash
   briefcase create
   ```
3. Build the application for desktop:
   ```bash
   briefcase build
   ```
4. Run the built application:
   ```bash
   briefcase run
   ```

### **3.2 Running on Android**
1. Ensure **Android Studio** is installed and the Android SDK is configured.
2. Create the application for Android:
   ```bash
   briefcase create android
   ```
3. Build the application for Android:
   ```bash
   briefcase build android
   ```
4. Run the application on an emulator or Android device:
   ```bash
   briefcase run android
   ```

### **3.3 Running on iOS**
1. Use a macOS system with **Xcode** installed.
2. Create the application for iOS:
   ```bash
   briefcase create iOS
   ```
3. Build the application for iOS:
   ```bash
   briefcase build iOS
   ```
4. Run the application on a simulator or iOS device:
   ```bash
   briefcase run iOS
   ```

### **3.4 Running on Web (WebAssembly)**
1. Install **Emscripten** to enable WebAssembly support.
2. Create the application for the web:
   ```bash
   briefcase create web
   ```
3. Build the application for the web:
   ```bash
   briefcase build web
   ```
4. Run the application in a browser:
   ```bash
   briefcase run web
   ```
---

## **4. Customizing the Project**

### **4.1 Changing the Application Name**
1. Open the pyproject.toml file.
2. Modify the following fields:
   ```toml
   [tool.briefcase]
   name = "force-converter"
   formal_name = "Force Converter"
   ```

### **4.2 Adding New Features**
1. Create a new Python module in the src directory.
2. Import the new module into the main application file (`main.py`).

### **4.3 Customizing the User Interface**
1. Open the `main.py` file in the src directory.
2. Use the **Toga** library (part of BeeWare) to modify the UI. Example:
   ```python
   import toga
   from toga.style import Pack
   from toga.style.pack import COLUMN

   class ForceConverterApp(toga.App):
       def startup(self):
           main_box = toga.Box(style=Pack(direction=COLUMN))
           self.main_window = toga.MainWindow(title=self.formal_name)
           self.main_window.content = main_box
           self.main_window.show()
   ```

---

## **5. Contributing**

We welcome contributions to improve this project. Follow these steps to contribute:

### **Steps:**
1. Fork this repository to your GitHub account.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b new-feature
   ```
3. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Add new feature"
   ```
4. Push your branch to your forked repository:
   ```bash
   git push origin new-feature
   ```
5. Open a Pull Request (PR) to the main repository.

---

## **6. Project Directory Structure**

```
force-converter/
├── .gitignore
├── pyproject.toml
├── README.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── ...
├── tests/
│   ├── test_main.py
│   └── ...
├── build/
│   ├── force-converter/
│   └── ...
```

---

## **Authors**
**Developed by :**
**Muhamad Nur Arif**
**(41523010147)**

### **🔗 Link**
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://arifsuz.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/arifsuz)
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marif8/)
[![instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ariftsx/)