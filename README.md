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


**Project Merit**  
I believe that this script is well structured. The logic to retrieve the user favourite language is following a step by step process. I separate each task with its own method and I think I have implemented a good design.

**Project Flaws**  
I feel that the script is not DRY enough  and I could refactor better.
I also think some of my method names are a bit long and this appears to clutter the script.

**Improvement**  
As improvement, I would like to refactor my script a bit more, change some of the current method names and add more tests.

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
run_script_example


![](https://github.com/BasileKoko/python_script/blob/master/run_test_example.png)
run_test_example

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
