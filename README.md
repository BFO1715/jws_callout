# JWS Callout Request

npm install -g heroku<br>
heroku login -i<br>
check env.py

Admin/WeighingCompany<br>
Weigh1715<br>
bethan@johnwhiteandson.com<br>
APi Key

python3 manage.py makemigrations<br>
python3 manage.py migrate<br>
python3 manage.py runserver

jws-callout.heroku.com

import os

os.environ["DATABASE_URL"]="postgres://altiihsq:Vecuor_Jvir81c122tOv3w-qRkmRBnXN@lucky.db.elephantsql.com/altiihsq"
os.environ["SECRET_KEY"]="my-jws-secret-key"
os.environ["CLOUDINARY_URL"]="cloudinary://798566658129613:ExOirMglR8aUVwNJdFs86BDFk6U@diplwfbus"



Weighing Data System is a terminal application that allows the user to input the inweight of vehicles that coming into a site and input the outweights of vehicles leaving site. The system then calculates the netweight of each vehicle and the total load of vehicles that have been in and out of site for that period (this system is based on 5 vehicles per period weighing a minimum of 7,500kg). The data logged for inweight, outweight and netweight is then parsed to google sheets for record keeping and further analysis. 

<img src="assets/images/app_multi_device.png" alt="App Multi Device" width="405" height="250"><img src="assets/images/inweight_data.png" alt="Inweight Data" width="135" height="250"><img src="assets/images/outweight_data.png" alt="Outweight Data" width="135" height="250"><img src="assets/images/netweight_data.png" alt="Netweight Data" width="135" height="250">

<strong><u>STRATEGY</u></strong>

Focus - What’s worth doing?<br>
Creating an app that allows a user to input weight of vehicles arriving and leaving sites, automatically calculate netweight and total load then upload the data for record keeping and further analysis.<br><br>
Definition - What are we creating?<br>
A terminal application that allows the user to address a real-life need – inputting and analyzing data in the weighing industry.<br><br>
Value - What value does it provide?<br>
It allows a user to log known weights of vehicles arriving and leaving site and calculates netweights which can then be exported into a format that can then be fed into their own internal system. 

<strong><u>SCOPE</u></strong>

What features will be available?<br>
There will be two input requests for the user asking for 5 inweights as the vehicles are arriving onsite and 5 outweights as the vehicles are leaving site. The user will then be able to upload the data to google sheets and will be notified of total load.

<strong><u>STRUCTURE</u></strong>

How is the user interaction designed?<br>
At the top of the terminal will be the title of the application Weighing Data System. The user will then be asked to input the 5 inweights which will give an error if the values entered aren’t integers, over required weight or in the correct format. The user will then be notified if the inweight data has been successfully uploaded to google sheets. Next, the user will be asked to input 5 outweights which will also give an error if the values entered aren’t integers, over required weight or in the correct format. The user will then be notified if the outweight data has been successfully uploaded to google sheets. The app will then calculate netweight from outweights minus inweights and notify the user when the netweight data has been successfully uploaded to google sheets. The app will then calculate total load by adding the 5 netweights then printing each of the outweights, inweights, netweights and finally total load. 

<img src="assets/images/process_flowchart.png" alt="Process Flowchart" width="500" height="200"><br>

<strong><u>SKELETON</u></strong>

How will the interface be laid out?<br>
Command-line interface with step by step instructions for user to follow and notifications of outputs.<br>

<img src="assets/images/python_terminal_app.png" alt="Terminal Screenshot" width="400" height="225"><br>

<strong><u>SURFACE</u></strong>

What will the visual design look like?<br>
Heroku app with step by step instructions for user to follow and notifications of outputs.<br>

<img src="assets/images/app_demo.png" alt="App Demo" width="400" height="225"><br>

<strong><u>FUTURE RELEASES</u></strong>

What features would you like to have in the future?<br>
Allow the user to select how many vehicles they will have coming to and leaving site for the given period and select the minimum weight for the vehicle.

<strong><u>TECHNOLOGY</u></strong>

What technology was used?<br>
<ul>
<li>Gitpod - writing code on workspace.</li>
<li>Github - hosting repository.</li>
<li>Python - programming language used to write code.</li>
<li>Google API - interface used to allow integration between google sheets and program.</li>
<li>Heroku - platform used to deploy the app.</li>
</ul>

<strong><u>TESTING</u></strong>

How was the app tested and are there any bugs that have not been addressed?<br>
Tested code PEP8 on https://www.pythonchecker.com/ with no major errors and a 96% mark. 6 minor issues are no whitespaces around operators. Also tested code by running pylint run.py on the terminal with the following results:

<img src="assets/images/pylint_test.png" alt="Pylint Test" width="1000" height="225"><br>

Reviewed app on Heroku dashboard and zero errors found as per below:

<img src="assets/images/heroku_test.png" alt="Heroku Testing" width="400" height="225">

Tested app is working correctly by following the step by step instructions in order to spot errors or inconsistencies - none found as per below:

<img src="assets/images/app_first_test.png" alt="App First Test" width="400" height="225"><img src="assets/images/app_second_test.png" alt="App Second Test" width="400" height="225"><img src="assets/images/app_final_test.png" alt="App Final Test" width="400" height="225"><br>
<img src="assets/images/sheets_first_test.png" alt="Sheets First Test" width="400" height="225"><img src="assets/images/sheets_second_test.png" alt="Sheets Second Test" width="400" height="225"><img src="assets/images/sheets_final_test.png" alt="Sheets Final Test" width="400" height="225">

Tested possible common errors such as inputting a string instead of integer, not inputting 5 values and inputting values less than 7,500kg:

<img src="assets/images/app_str_error.png" alt="String Error Testing" width="400" height="225"><img src="assets/images/app_count_error.png" alt="Count Error Testing" width="400" height="225"><img src="assets/images/app_value_error.png" alt="Value Error Testing" width="400" height="225">


Bug was found upon opening workspace on different device after a previously successful test, commit and push.  Error messages - Unable to import gspread and Unable to import google.oauth2.service_account.<br>

<img src="assets/images/gspread_bug.png" alt="Gspread Bug" width="400" height="225"><img src="assets/images/google_oauth2_bug.png" alt="Google Auth Bug" width="400" height="225"><br>

Investigated on stack overflow and ran:
<ul>
<li>pip install --upgrade google-auth google-auth-httplib2 google-api-python-client</li>
<li>pip install gspread</li>
<li>uploaded creds.json </li>
</ul>

Program tested fine afterwards though this bug kept happening upon opening workspace on different devices . 

<img src="assets/images/bugs_fixed.png" alt="Bugs Fixed" width="400" height="225"><img src="assets/images/bug_fixed_testing.png" alt="Bug Fixed Testing" width="400" height="225"><br>

Program still requires the pip install gspread and creds.json upload upon opening workspace on new device.

<strong><u>DEPLOYMENT</u></strong>

How was the project deployed?<br>
The project was deployed using Github, Gitpod and Heroku. The steps to deploy are as follows:<br>
<ul>
<li>Open Gitpod via Github repository</li>
<li>Run python3 run.py to test program</li>
<li>Link Heroku to Githib and create new app</li>
<li>Add creds.json config</li>
<li>Add python buildpack</li>
<li>Add node.js buildpack</li>
<li>Link Heroku app to repository</li>
<li>Select Deploy</li>
</ul>

The live link can be found here https://weighing-data.herokuapp.com/

<strong><u>CREDITS</u></strong>

Code Institute - https://codeinstitute.net/<br>
Stack Overflow - https://stackoverflow.com/