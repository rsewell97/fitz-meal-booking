# fitz-meal-booking
Automate [fitz meal booking](https://collegebills.fitz.cam.ac.uk/collegebill/Main.aspx) to beat the queue. In python based on Selenium

Simply enter your crsID and password when the authentication is called. Enter dietary preferences and booking date at top and it will refresh every 10secs to ensure you are booked on to the meal

Based on website version 14/11/2018, testing recommended. I accept no liability for missed bookings.

## Getting Started

Download python 3.7 [here](https://www.python.org/ftp/python/3.7.1/python-3.7.1-amd64.exe), (starts download automatically)

Install for all users -> Select destination -> ensure "add python.exe to Path" is checked -> advance and install.

Open up the Windows/Mac command prompt and type the following command
```
pip install selenium
```
Now depending on what browser you want to use - moral of the story, use Chrome:
#### Chrome
run `pip install chromedriver`
#### Safari
To find the develop menu, go to Safari's advanced settings and enable it. Under the Develop menu, check the 'Allow Remote Automation'
Run `safaridriver -p 5555` in the command prompt
#### Edge
V quick download [here](https://download.microsoft.com/download/F/8/A/F8AF50AB-3C3A-4BC4-8773-DC27B32988DD/MicrosoftWebDriver.exe)
Then run `DISM.exe /Online /Add-Capability /CapabilityName:Microsoft.WebDriver~~~~0.0.1.0` as administrator
#### Firefox
Don't even try


### Either (recommended):
Download ZIP file (by clicking the green button in the top right) and extract file.

### Or:
[install Git](https://git-scm.com/downloads)

Then, back in command prompt, type:
```
git clone https://github.com/rsewell97/fitz-meal-booking.git
cd fitz-meal-booking 
```

### To Run
Open the file in Notepad by simply typing `automateBook.py` into the command prompt. Edit all relevant parameters in lines 18-22. and save. Now finally type 
```
python automateBook.py
```
to run it.
This should open a new window and automate the process :) 
