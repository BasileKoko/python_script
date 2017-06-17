### FavouriteLanguage Script

This is a command line script which allows users to enter a GitHub username, and to be presented with the GitHub user's favourite programming language.

**Project Merit**  
I believe that this script is well structured. The logic to retrieve the user favourite language is organised in a way which allows changes easily. I have separate each task with its own method and I think I have implemented a good design.

**Flaws**  
I feel that the script is a bit long and I could refactor better.
I also think some of my variables names are a bit long which seems to clutter the script.

**Improvement**  
As improvement, I would like to refactor my script a bit more, change some of the current variables names to shorter ones, and write more tests.

**Setup**
```
$ git clone https://github.com/BasileKoko/python_script.git
$ cd python_script
$ sudo pip install dotenv
edit the file .env.example, replace 'xxxx' with your Github token and remove .example extension
```
[How to generate Github Token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)

**To run the program**
```
$ python favourite_language.py
When prompt enter a Github username
```

**To run**
```
$ py.test -v -s
when prompt please press enter
```
