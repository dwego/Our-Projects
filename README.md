# Speech Recognition and Web Browsing
This is a simple Python program that allows you to open websites in your default browser by speaking their names. It uses speech recognition to listen to your voice commands, and the webbrowser module to open the desired website.

# Installation
Before running the program, make sure you have the necessary dependencies installed. You can install them using the following command:

```python
pip install speechrecognition
pip install pyaudio
```
# Usage
To use the program, simply run the main.py file:

```python
python main.py
```
The program will start listening to your voice commands. You can say things like:

- "Open Google"
- "Open Facebook"
- "Open YouTube"
The program will then open the corresponding website in your default browser.

# Customization
You can customize the program by adding new voice commands and websites. To do this, edit the main.py file and add a new entry to the WEBSITES dictionary. For example, to add a command for opening Wikipedia, you can add the following line:

```python
WEBSITES = {
    "google": "https://www.google.com",
    "facebook": "https://www.facebook.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://en.wikipedia.org",
}
```
You can also modify the trigger words that the program listens for by changing the start variable in main.py.

# License
This project is licensed under the MIT License. See the LICENSE file for more information.

Feel free to contribute to this project by submitting pull requests or reporting issues on GitHub.
