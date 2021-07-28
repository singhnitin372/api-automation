**Steps to Run**

1. Install the Nodejs and Python in your machine.
2. Install allure report using (npm install -g allure)
3. Create and activate the virtualenv   
4. Go to the root project root directory and run (pip3 install -r requirements.txt)
6. Run the command (pytest --alluredir=results)
7. Run the next command (allure serve results/)
8. Browser will open automatically, and you will be seeing a html report
9. You can see the logs in the 'api_automation.log' under the root directory of application

**Project Structure**

1. resource folder contains 'config.ini', which holds base url for the test
2. schemas folder contains schema for service schema validation
3. test folder contains all the test files
4. request folder contains individual service requests
5. utility folder contains all useful methods for test
6. Body folder contains all the post body for the test
