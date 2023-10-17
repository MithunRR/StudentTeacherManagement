# StudentTeacherManagement

# Setup Virtual Environment
* Create a project directory
* Create a virtual environment using `virtualenv env`
* If you don't have 'virtualenv' then install using `pip install vertualenv`
* Activate Virtual Env using `.\env\Scripts\activate`
* If get access restrictions Error on Windows. Run this cmd `Set-ExecutionPolicy Unrestricted -Scope Process` The try again to activate Env

# Setup Project
* Clone git repo `git clone https://github.com/MithunRR/StudentTeacherManagement.git`
* Change directory `cd StudentTeacherManagement`
* Install dependencies from requirements.txt
* `pip install -r requirements.txt`

# Run Project
* Run Project using `python manage.py runserver`
* Open browser and goto to `http://localhost:8000`

# To verify certificate 
* Goto `http://localhost:8000/verify-certificate/[VERIFICATION-TOKEN]`

# Additional Information
* To access admin dashboard got to `http://localhost:8000/admin`
* Username: `admin`
* Password: `pass`
    
