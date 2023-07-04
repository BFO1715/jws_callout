# JWS Callout Request

The JWS Callout Request website is designed to streamline the process of requesting callouts for malfunctioning weighing equipment. We understand the importance of accurate measurements in various industries, and our platform aims to minimize downtime and ensure efficient maintenance. With just a few clicks, you can submit a callout request, providing details about the specific equipment and issue. Our team of skilled technicians will promptly review your request and dispatch the nearest available expert to address the problem. Our goal is to provide a seamless user experience and ensure that your weighing machines are up and running in no time, minimizing any disruptions to your operations. Trust our JWS website to simplify the process of resolving issues with your weighing machines.

<img src="assets/images/website.png" alt="Website" width="350" height="200"> <img src="assets/images/request_callout.png" alt="Request Callout Test" width="350" height="200"> <img src="assets/images/comment.png" alt="Comment" width="350" height="200">

<strong><u>STRATEGY</u></strong>

Focus - What’s worth doing?<br>
The primary focus of creating a JWS website for requesting callouts for weighing machines not working is to streamline and optimize the maintenance process. The website aims to provide a centralized platform where users can easily submit their callout requests, eliminating the need for lengthy phone calls or paperwork. By digitizing the request process, the website improves efficiency and reduces response times.<br><br>
Value - Firstly, it provides a convenient and user-friendly platform where users can easily submit their callout requests, eliminating the need for lengthy phone calls or manual paperwork. This saves users time and effort in reporting issues and allows them to focus on their core tasks.

Secondly, the website ensures a prompt response and resolution to the reported problems. By connecting users with skilled technicians who specialize in weighing machine repairs, the website reduces downtime and minimizes the impact on operations. Users can have peace of mind knowing that their issues will be addressed quickly and effectively.

Additionally, the website offers transparency and visibility into the status of the callout requests. Users can track the progress of their requests, receive updates on technician assignments, and get estimated repair timelines. This transparency enhances communication and helps users plan their operations accordingly.

Overall, the value for users lies in the convenience, efficiency, and reliability of the JWS website. It simplifies the process of reporting and resolving weighing machine issues, ensuring minimal disruptions and enabling users to maintain accurate measurements for their businesses. 

<strong><u>SCOPE</u></strong>

What features will be available?<br>
The JWS website for requesting callouts for weighing machines not working will offer several key features to enhance user experience and streamline the maintenance process. Some of the features that users can expect include:

Callout Request Submission: Users will have a user-friendly interface to submit their callout requests online. They can provide details about the issue, such as the nature of the problem and specific machine details.

Technician Assignment: Once a callout request is submitted, JWS will assign the next available technician with the relevant expertise to address the issue. 

Communication Channel: The website include a commuents section, allowing users to communicate directly with our support team. This feature enables users to provide additional information or seek clarification about the reported issue.

Progress Tracking: Users will have the ability to track the progress of their callout requests. They can receive updates on the status of the repair process, including technician arrival, diagnostics, repairs performed, and estimated completion time. This feature enhances transparency and keeps users informed throughout the resolution process.

Service History: The website will maintain a service history for each user, keeping a record of past callout requests, repairs performed, and any additional notes or recommendations from the technicians. This information can be valuable for future reference and analysis.

Feedback and Rating: After the repair is completed, users may have the opportunity to provide feedback and rate the service received. This feature helps maintain service quality and enables continuous improvement.

These features aim to provide users with a seamless and efficient experience when requesting callouts for malfunctioning weighing machines, ensuring timely repairs and maximizing user satisfaction.

<strong><u>STRUCTURE</u></strong>

How is the user interaction designed?<br> 

Below is a flowchart of how a user will use the website and a Kanban board with milestones devolped using User stories:

<img src="assets/images/request_process.png" alt="Request Process" width="350" height="100"><br>

<img src="assets/images/user_story.png" alt="User Story" width="700" height="200"><br>

<strong><u>SURFACE</u></strong>

What will the visual design look like?<br>

Below is a wireframe for what the website will look like with the main body changing depending which section the user is interacting with:

<img src="assets/images/website_wireframe.png" alt="Website Wireframe" width="350" height="200"><br>

<strong><u>FUTURE RELEASES</u></strong>

What features would you like to have in the future?<br>
Building a comprehensive knowledge base and resource section on the website could provide users with informative articles, FAQs, troubleshooting guides, and maintenance tips. This would empower users to resolve common issues on their own and enhance their understanding of weighing machine maintenance.

<strong><u>TECHNOLOGY</u></strong>

What technology was used?<br>
<ul>
<li>Gitpod - writing code on workspace.</li>
<li>Github - hosting repository.</li>
<li>Python - programming language used to write code.</li>
<li>Django - framework used to build website.</li>
<li>ElephantSQL - install and manage PostgreSQL database.</li>
<li>Bootstrap - HTML, CSS and Javascript library.</li>
<li>Heroku - platform used to deploy the app.</li>
</ul>

<strong><u>TESTING</u></strong>

<u>Manual Testing</u>

I created a set of test scenarios covering different aspects of the system, such as admin panel, register, login, callout request creation, editing, deleting, comments approval/submission and authorization.

Admin/Weigh1715<br>
WeighingCompany/Weigh1715<br>
OtherWeighingCompany/Weigh1715<br>

Homepage:

<img src="assets/images/homepage.png" alt="Homepage Test" width="350" height="200"><br>

Request detail:

<img src="assets/images/request_detail.png" alt="Request Detail Test" width="350" height="200"><br>

Admin:

<img src="assets/images/admin.png" alt="Admin Test" width="350" height="200"><br>

Register:

<img src="assets/images/register.png" alt="Register Test" width="350" height="200"><br>

Sign In:

<img src="assets/images/sign_in.png" alt="Sign In Test" width="350" height="200"><br>

When signed in can edit, delete and comment own request:

<img src="assets/images/own_request.png" alt="Own Request Test" width="700" height="200"><br>

Sign out:

<img src="assets/images/sign_out.png" alt="Sign Out Test" width="350" height="200"><br>

Request Callout:

<img src="assets/images/request_callout.png" alt="Request Callout Test" width="350" height="200"><br>

Adding comment for approval:

<img src="assets/images/comment_approval.png" alt="Comment Approval Test" width="700" height="200"><br>

Edit Request:

<img src="assets/images/edit_request.png" alt="Edit Request Test" width="350" height="200"><br>

Delete Request:

<img src="assets/images/delete_request.png" alt="Delete Request Test" width="350" height="200"><br>

User can only edit or delete their own requests unless they are Admin:

<img src="assets/images/auth.png" alt="Auth Test" width="1200" height="200"><br>

Tested Python code Snyx on https://snyk.io/code-checker/python/ and passed with one minor issue found which was a duplicate import:

<img src="assets/images/python_test.png" alt="Python Test" width="350" height="200"><br>

Tested HTML code on W3C https://validator.w3.org/ and passed with 1 warning and 3 infos:

<img src="assets/images/html_test.png" alt="HTML Test" width="350" height="200"><br>

Tested CSS code on Jigsaw https://jigsaw.w3.org/css-validator/ and passed with 2 warnings:

<img src="assets/images/css_test.png" alt="CSS Test" width="350" height="200"><br>

Bug found where non logged in users could access create, edit, delete and logged in users could edit and delete other users' posts by accessing urls directly via:

https://jws-callout.herokuapp.com/add_request/
https://jws-callout.herokuapp.com/edit/test-callout-request/
https://jws-callout.herokuapp.com/delete/test-callout-request/

<img src="assets/images/access_error.png" alt="Access Error" width="700" height="200"><br>

Bug fixed by adding LoginRequiredMixin to rectify non logged in users issue and PermissionDenied for logged in user restriction:

<img src="assets/images/access_fix.png" alt="Access Fix" width="700" height="200"><br>

<strong><u>DEPLOYMENT</u></strong>

How was the project deployed?<br>
The project was deployed using Github, Gitpod and Heroku. The steps to deploy are as follows:<br>
<ul>
<li>Open Gitpod via Github repository</li>
<li>Run python3 manage.py runserver to test program</li>
<li>Link Heroku to Githib and create new app</li>
<li>Link Heroku app to repository</li>
<li>Select Deploy</li>
</ul>

The live link can be found here https://jws-callout.herokuapp.com/

<strong><u>CREDITS</u></strong>

Code Institute - https://codeinstitute.net/<br>
Stack Overflow - https://stackoverflow.com/