# Sauce Automation

This is a UI + API test automation framework using:

-  Selenium & Pytest for UI testing
-  Requests for REST API testing
-  Pytest-HTML reports
-  POM structure


Steps on how to run this automation.

1. clone the project
 - git clone 
 - cd sauce
 
2. Install the dependancies required. 
  - pip install -r requirements.txt
  
3. Run the automation
 - For the API tests use command:
    pytest -m api
    
 - For the UI tests use command
     pytest -m "not api"  
     
 - For both API and UI use command to run
     pytest
     
4. View Test Report use commands
   open tests/reports/report.html         # Mac
   
   start tests/reports\report.html        # Windows   
   
   
6. To view failure screenshots go to directory
    tests/screenshots
    

