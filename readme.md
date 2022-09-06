# Basic Explanation Of What Was Done
I must admit I started this way too late on a week day and I was exhausted by the time I got here. That's on me.
However this lead me to think, "in  real life, what would be the easiest, fastest way to get this done?" and the answer is always python + Django

Now, at any time of day I would not bother making up an algorithm like this. There are innumerable [examples](https://www.c-sharpcorner.com/blogs/convert-number-to-words-in-c-sharp) and [tutorials](https://www.tutorialspoint.com/Number-to-word-conversion) that implement it and I would look for a good implementation and copy that as a starting point. This might require a bit of tweaking or error checking but it's really not something worth thinking about.

And in general there is a mantra that "if you need to do it in python there's a one-line library somewhere". 

One caveat is I *have been burned* by an over-reliance in Python on third party libraries (less of a problem in C# and Java) that end up not being maintained and become useless. So a good idea is to make sure you can [get the source](https://github.com/savoirfairelinux/num2words) if you need it and not rely on anything that is too fringe.

Improvements I could make if I spent more time and wasn't 75% asleep by now (really should have started this earlier but it's tough with kids and a full day job!):

 - Client-side (javascript) validation of data. Relying on input type to ensure integrity now
 - Real-time updates as you type (might be fun to watch) with ajax

Also Django might seem heavy-handed for something so simple compared to e.g. Flask but was looking for something good to go "out the box" with minimal configuration and sensible defaults.

After cloning this repository, I am not sure if you will have Python installed or not. It is easy to get an [installer](https://www.python.org/downloads/) for Windows but on Mac this is better done with [Homebrew](https://docs.python-guide.org/starting/install3/osx/)  and on something like Ubuntu either via snap or apt-installer. Please install Python version 3.6 or better just to make sure there are no hiccups with compatibility.

From a terminal in the project root then type (note I have not had time to test syntax cross platform, not sure what you work on):

```
python -m pip install — upgrade pip
virtualenv env
env\scripts\activate
pip install -r requirements.txt
python .\manage.py runserver
```

Note you don't necessarily need a virtual environment if you don't mind polluting your global python package list. 

> Written with [StackEdit](https://stackedit.io/).
