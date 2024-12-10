# 🔐 Password Manager
## Description
This project is a tool for storing account credentials of various websites and securely saving them on local device.  
**It was created as part of the [100 Days of Code](https://www.udemy.com/course/100-days-of-code) bootcamp.**
## Features
💾 **Store Credentials**: Storing website name, username and password inside data.txt  
✨ **Random Password Generator**: Creates a random password between 18 to 22 characters and automatically **copies to clipboard**

## Prerequisites
``tkinter``  
Python includes `tkinter` module by default but if you get an error on Linux-based systems, make sure you install it.

## How It Works:
🪟 Creates a window of 200x200 with 20 pixels padding on each side.  
⏺ Creates interactive texts, buttons, entries with `tkinter` instances: label, button and entry.   
📋 Utilizes built in tkinter function `clipboard.append` to copy password to clipboard

## Installation

```bash
sudo apt-get install python3-tk
```
**1. Clone the repository:**
```bash
git clone https://github.com/AlparslanCelik/password_manager/
cd password_manager
```
**2. Execute main.py with:**
```bash
python main.py
```

## Usage
-**Type down your credentials in correspondant boxes.**  
-**For password, you can generate a password with "Generate Password" button**  
-**Click on "Add" to save your information**  

