# MY470 Computer Programming


### Michaelmas Term 2017

### Instructors

* [Milena Tsvetkova](m.tsvetkova@lse.ac.uk), *Office hours*: Mondays 15:00–17:00, COL 8.03
* [Kenneth Benoit](k.r.benoit@lse.ac.uk), *Office hours*: By appointment, COL 8.11
* [Kohei Watanabe](k.watanabe1@lse.ac.uk) (TA), *Office hours*: Thursdays 10:00-12:00, COL 7.04

### Course Information

* Lectures on Mondays 13:00–15:00 in KSW G.01
* Classes on:
  * Tuesdays 15:00–16:30 in TW2 4.03
  * Thursdays 14:30–16:00 in STC S018 (Weeks 1-5, 7, 11) and STC S08 (Weeks 8-10)

No lectures or classes will take place during School Reading Week 6.


### Course Description

This course introduces students to the fundamentals of computer programming as students design, write, and debug computer programs using the programming languages Python and R. The course will also cover the foundations of computer languages, algorithms, functions, variables, object orientation, scoping, and assignment.

### Organization

This course is an introduction to the fundamental concepts of programming for students who lack a formal background in the field, but will include more advanced problem-solving skills in the later stages of the course. Topics include algorithm design and program development; data types; control structures; functions and parameter passing; recursion; data structures; searching and sorting; and an introduction to the principles of object-oriented programming.

### Prerequisites

This is an introductory class and no prior experience with programming is required.

### Software

The course will use Python and R. We will use the Anaconda distribution to install the languages and manage packages and The Jupyter Notebook to write code. Lectures and assignments will be posted on Github, Students are expected to use Github also to submit problem sets and final exam.

### Materials

The main course texts will be:
*	Guttag, John V. *Introduction to Computation and Programming Using Python: With Application to Understanding Data*. MIT Press, 2016.
* Miller, Bradley N. and David L. Ranum. *Problem Solving with Algorithms and Data Structures Using Python*. Available online at http://interactivepython.org/runestone/static/pythonds/index.html.
*	Intermediate and advanced documentation at http://docs.python.org/3/.
*	Grolemund, Garrett and Hadley Wickham. *R for Data Science*. O’Reilly, 2016. http://r4ds.had.co.nz
*	Grolemund, Garrett. *Hands-On Programming with R*. O’Reilly, 2014.
* Matthes, Eric, *Python Crash Course*, Cheat Sheet at https://ehmatthes.github.io/pcc/cheatsheets/README.html.

### Assessment

Take home exam (50%) and in-class assessment (50%). Students will be expected to produce 10 problem sets in the MT. Student problem sets will be marked each week, and will provide 50% of the mark.

Problem sets will be distributed on Tuesdays and due at 12:00 noon on Mondays.

The take home exam will be distributed on Tuesday, December 12, 2017 and due at 12:00 noon on Monday, January 8, 2018.

**The deadlines are final. Late submissions will not be considered, except in the case of a valid documented legal or medical excuse.**

### Schedule

---
#### Week 1. What is Computation?

In the first week, we will introduce the basic concepts in computer programming: computers, algorithms, programming languages, and programs. We will then discuss the elements of programming languages: primitive constructs, syntax, static semantics, and semantics. We will further introduce the essential primitives for all programming languages: data types, operators, expressions, variables and values.

*Readings*:

* Guttag. Chapters 1-2.1, pp.1–15.
* Wing, Jeannette M. (2006). [Computational thinking](http://tech-insider.org/academia/research/acrobat/0603.pdf). *Communications of the ACM*, 49(3), 33–35.

*Lab*: **Anaconda, Jupyter, and GitHub**
* Installing Python with Anaconda
* Introduction to Jupyter and other IDEs
* Submitting assignments on GitHub

---
#### Week 2. Data Types in Python

In the next five weeks of the course, we will use Python to get familiar with the elements of programming languages. We will begin with scalar data types, operators, expressions, and value assignment to variables. We will also cover non-scalar, also known as compound or structured, data types (lists, tuples, sets, and dictionaries) and discuss the difference between mutable and immutable and ordered and unordered types. As lists are very commonly used, we will further overview the most common list operations, including indexing, slicing, appending, splitting, aliasing, and cloning.  

*Readings*:
* Guttag. Chapters 2.3, 5.1-5.3, 5.5-5.6, pp.18–21, 65–73, 77–84.

*Lab*: **Working with Strings and Lists in Python**
* Programing with simple statements, including `print()`, `len()`, `append()`, `extend()`, `pop()`, `remove()`, `split()`, `join()`, `sort()`, and `sorted()`

---
#### Week 3. Control Flow in Python

Control flow defines the order in which statements are evaluated and executed in a program. In Python, indentation plays a crucial role in determining the control flow. In this week, we will discuss branching and iteration and how to write these in Python using `if`-`else` statements, `while` loops, `for` loops, `range()`, `break`, and `continue`. We will also introduce the extremely useful concept of list comprehensions. To exemplify the use of conditional statements and iteration, we will go over several simple numerical search and approximation algorithms.

*Readings*:
* Guttag. Chapters 2.2, 2.4–3, pp.15–18, 22–38.

*Lab*: **For Loops and List Comprehensions in Python**
* Control flow best practices and pitfalls
* Nested dictionary and list comprehensions

---
#### Week 4. Functions in Python

Good programmers are not measured by the amount of code they write but by the amount of functionality in their code. Good programming relies on abstraction and decomposition. Decomposition creates structure while abstraction helps hide details. Decomposition and abstraction can be achieved with functions and classes and in this week, we will introduce functions. We will discuss function arguments and variable scope and by means of an example, we will introduce the concept of recursion.

*Readings*:
* Guttag. Chapter 4, pp.39–63.

*Lab*: **Writing and Calling Functions in Python**
* Function specification
* What are functions good for?

---
#### Week 5. Classes in Python

Object-oriented programming is a programming paradigm that helps increase modularity, reduce complexity, and foster code reuse. Objects are a data abstraction consisting of (1) an internal representation i.e. object attributes and (2) an interface for interacting with the objects through methods and functions. Objects are instances of classes and classes determine the type of an object. In this week, we will discuss how to define classes in Python and how to create instances of a class. We will also touch upon class inheritance and hierarchies, as well as generators.

*Readings*:
* Guttag. Chapter 8, pp.109–134.

*Lab*: **Programming in Teams**
* Using GitHub as a collaboration tool

---
#### Week 7. Testing and Debugging in Python

Writing computer programs is easy but making them work properly is hard. We test programs to check if they work as intended and we debug them when we find out that they don’t. In this lecture, we will discuss different ways to test and debug programs. We will cover common error messages and how to catch them with `try`, `except`, `raise`, and `assert`.

*Readings*:
* Guttag. Chapters 6–7, pp.85–108.

*Lab*: **Unit Testing, Exceptions, and Assertions in Python**
* Using .py files to structure programs and conduct testing
* Defensive programming with `try`, `except`, and `assert`

---
#### Week 8. The R Programming Language

In the next two weeks of the course, we will review the concepts learned until now by learning how they are implemented in the R programming language. We will start with basic data types in R (vectors, lists, matrices, factors, data frames) and object classes.

*Lecture Notes*:
* as [html slides](wk8/MY470_wk8_lecture.html)
* as [pdf slides](wk8/MY470_wk8_lecture.pdf)

*Readings*:
* Venables, W. N. et. al.  2017.  [_An Introduction to R_](https://cran.r-project.org/doc/manuals/r-release/R-intro.pdf).  Chapters 1-6.
* (optional, but recommended) Zuur, A., Ieno, E. N., & Meesters, E. (2009). _A Beginner's Guide to R_. Springer Science & Business Media.
* The [Introduction to R handout](wk8/Introductory_R.pdf).

*Lab*: **Introduction to R**
* Installing R and RStudio
* Introduction to RStudio and workflow
* Working with R objects

---
#### Week 9. (More) Advanced R

Continuing from the previous week, we will cover control flow (if-else statements, for and while loops, repeat, next, break), and vectorized operations in R, functions, and variable scoping.

*Readings*:
* Venables et. al., Chs. 9-10.
* (optional) Patrick Burns.  2011.  _The R Inferno_.  http://www.burns-stat.com/pages/Tutor/R_inferno.pdf

*Lecture Notes*:
* as [html slides](wk9/MY470_wk9_lecture.html)
* as [pdf slides](wk9/MY470_wk9_lecture.pdf)

*Lab*: **Working with lists and functions in R**

---
#### Week 10. Algorithms and Order of Growth

Algorithms are recipes that consist of a sequence of simple steps, control flow, and stopping rule. To evaluate the scalability of algorithms and to compare their efficiency, we use the abstraction “order of growth”. Order of growth expresses how the maximum amount of time needed grows as the size of the input grows. We will discuss different complexity classes and ways to analyze the complexity of programs.

*Readings*:
* Guttag. Chapter 9, pp.135–149.
* Bradley and Ranum. [Chapter 2](http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/toctree.html).

*Lab*: **Order of growth**
* Reading programs written in Python and R and evaluating their time complexity

---
#### Week 11. Searching and Sorting Algorithms

We will use the concepts and approaches introduced in the previous lecture to look at the complexity of several classic algorithms on searching and sorting. The goal is to get a better intuition of how to approach problems of efficiency. We will use examples written in both Python and R. The lecture will end with an overview of what we have learned in the course and possible steps you can take to further develop your programming skills.  

*Readings*:
* Guttag. Chapter 10.1–10.2, pp.151–164.
* Bradley and Ranum. [Chapter 5](http://interactivepython.org/runestone/static/pythonds/SortSearch/toctree.html).

*Lab*: **Preparation for the final assignment**
* Getting familiar with the data
* Understanding temporal motifs
