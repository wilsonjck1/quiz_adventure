# Quiz Adventure!

This project consists of two problems:

  * [ ] Write a quiz.
  * [ ] Write a small, text-based adventure.

You are free to do as you wish with these, there are no tests to satisfy,
and the complexity of your solution is up to you.  We will be sharing and
presenting the best quizzes/games in a later lesson.


## Printing

Some quick printing techniques that might be useful:

``` python

    name = "John"

    print("Hello", name)
    print("Hello " + name)

```

Printing multiple things, separated by commas will print each item with a space in between.
Adding the strings together before printing will just stick them together and then print.


## Getting User input

These problems will require you to get some user input and do things with
it.  To do this, we use the `input` keyword:

``` python

    print("Some question")
    answer = input("Answer: ")

    if answer == "The right answer":
        ... do something

```

`input` takes a prompt (in the example above, this was "Answer: "), and
then waits for the user to enter something. We can then assign this to
a variable.


`input` will always return a string, so if you need a number - you need
to turn it into one.  This is done like so:

``` python

    text_answer = input("Guess your number: ")
    num_answer = int(text_answer)

```



