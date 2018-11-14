# fitz-meal-booking
Automate fitz meal booking to beat the queue. In python based on Selenium

Simply enter your crsID and password when the authentication is called. Enter dietary preferences and booking date at top and it will refresh every 10secs to ensure you are booked on to the meal

Based on website version 14/11/2018, testing reccomended. I accept no liability for missed bookings.

## Getting Started

Download python 3.7 [here](https://www.python.org/ftp/python/3.7.1/python-3.7.1-amd64.exe), (starts download automatically)

Install for all users -> Select destination -> ensure "add python.exe to Path" is checked -> advance and install.

Open up the Windows/Mac command prompt and type the following commands
```
pip install selenium chromedriver
```
Now [install Git](https://git-scm.com/downloads)

Back in command prompt, type:
```
git clone https://github.com/rsewell97/fitz-meal-booking.git
cd fitz-meal-booking 
```

Open the file in Notepad by simply typing `automateBook.py` into the command prompt. Edit all relevant parameters in lines 18-22. and save. Now finally type 
```
python automateBook.py
```
to run it.
This should open a new window and automate the process :) 
