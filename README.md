# enrollme
Alerts NYU Tandon students when the course they're looking for is available

## Requirements
python 3.6

## Instructions
1. Install the [cookies.txt](https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg?utm_source=chrome-ntp-icon) plugin for chrome
2. Log into Albert
3. Download cookies.txt file using the plugin and place it in the repository directory
4. In the course shopping cart, find the id of the status column of the course you want to take up using "Inspect Element"
5. In `properties.py`, add your email address, password and the course id.
6. Install the requirements using `pip install -r requirements.txt`
7. Run the application using `python main.py`
