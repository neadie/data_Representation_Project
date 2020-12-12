# data_Representation_Project


### Steps to run the application

1. Connect to mysql server via xammp click on start for both apache and MySql and click on
   Admin for mySql to open up phpMyAdmin.
2. Click on the databases tab enter data_representation_project in Database name and click on create to create database.
3. To create tables and load the data, Click on the Import tab. Browse to  data_representation_project.sql file by clicking on the ‘Choose File’ option that you wish to import. And then click on the ‘Go’ button at the bottom.
4. Create virtual enviroment .on git bash or cmd do the following **python -m venv c:\path\to\myenv** . Make sure path is a parent of the data_Representation_Project
5. Activate virtual enviroment by running Scripts/activate 
6. For the external API with authenication part of the project you will have to create a credentials.json so you can see your own files
   in google drive. Steps below
    - Login to google drive with your own google credentials
    - Go to https://developers.google.com/drive/api/v3/quickstart/python
	- On Step 1 Turn on the Drive API Click on the Enable the Drive API button. 
	 - Leave project name as quickstart and accepts terms of services 
	 - On the Configure your OAuth client leave it as Desktop app and click on create
	 - Click on download client configuration to download the credentails.json file , once
	   downloaded move the credentails.json from downloads to the data_Representation_Project
	 - Install the Google Client Library
        Run the following command to install the library using pip:
          **pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib**
7. Start the app via python app  the localhost:5000/ will be the launched showing the login page as 
   user hasnt loged in yet.
   **username =  admin** 
   **password** = admin ** .
   
8. For my Google Files page 
    If you are not already logged into your Google account, you will be prompted to log in. If you are logged into multiple Google accounts, you will be asked to select one account to use for the authorization.
    Click the Accept button.
	You get message app if not authorized so click on advanced and 
	**message grant Quickstart permission View metadata for your google Drive , and click allow to proceed . **#
	
    The sample will proceed automatically, and you may close the window/tab.
   
   