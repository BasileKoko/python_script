### FavouriteLanguage

This is a command line script which allows users to enter a GitHub username, and to be presented with the GitHub user's favourite programming language.

**Project files**  
The project has 3 main files.

- favourite_language.py  
This is the main script file.

- run_script.py  
This is the file needed to run the script

- test_favourite_language.py  
This is the test file for the script.


**Setup**
```
$ git clone https://github.com/BasileKoko/python_script.git
$ cd python_script
$ sudo pip install dotenv
edit the file .env.example, replace 'xxxx' with your Github token and remove .example extension
```
[How to create Github Token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)

**To run the program**
```
$ python run_script.py
When prompt enter a Github username
```

**To run tests**
```
$ sudo pip install pytest
$ py.test -v -s
-v : for verbose output
-s : to disable all capturing
```
**Screenshots**

![](https://github.com/BasileKoko/python_script/blob/master/run_script_example.png)  
**_run_script_example_**


![](https://github.com/BasileKoko/python_script/blob/master/run_test_example.png)
**_run_test_example_**

**Modules used**
```
dotenv
requests
json
urllib2
Counter
pytest
sys
```
