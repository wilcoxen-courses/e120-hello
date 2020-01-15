# Exercise: Hello World

### Summary

This exercise goes over the basics of writing text from Python scripts. It also
goes over concatenating strings and how scripts can create Markdown files,
which can be convenient when preparing nicely-formatted output.

### Instructions

1. Please create a new script called `hello1.py` that uses the `print` function
to write the string "Hello, World!" Once the script is working properly, commit
it to the repository.

1. Create a new script called `hello2_file.py` that does the following.
    1. Sets a string called `author_name` to your name;
    1. Uses string concatenation to build a new string called `author_msg`
    that is glues together three parts: `"Author: *"`, `author_name`, and
    `"*\n"`;
    1. Opens a new file called `hello2_file.md` for writing;
    1. Writes three lines to the file: `# Hello, World!\n`, a blank line, and
    a line with `author_msg`;
    1. Closes the file.

1. If you aren't sure how to do one or more of these steps, have a look at the
accompanying `demo.py` file. It has some example code that may be useful.

1. When `hello2_file.py` is working properly, it should produce output
similar to `example.md`. Once you're happy with it, commit the finished
versions of `hello2_file.py` and `hello2_file.md` to the repository.

### Submitting

Once you're happy with everything and have committed all of the changes to
your local repository, please push the changes to GitHub. At that point,
you're done: you have submitted your answer.

### Notes

* Basing the name of a script's output file on the name of the script itself
can be very helpful in projects that involve a lot of files. It ensures that
the two are close to each other when someone looks through the directory.

* Having to include the `\n` explicitly at
the end of lines in write statements is very annoying at first because it's
easy to forget. However, it's actually a very useful feature because it allows
you to build up a long line with several write calls before adding the `\n`.
