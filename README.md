# MY470 Computer Programming


### Michaelmas Term 2017

### Instructors

* [Milena Tsvetkova](m.tsvetkova@lse.ac.uk), *Office hours*: Mondays 15:00–17:00, COL 8.03
* [Kenneth Benoit](k.r.benoit@lse.ac.uk), *Office hours*: By appointment, COL 8.11
* [Kohei Watanabe](K.Watanabe1@lse.ac.uk) (GTA), *Office hours*: TIME, BLDG

### Course Information

* Lectures on Mondays 13:00–15:00 in KSW G.01
* Classes on:
  * Tuesdays 15:00–16:30 in TW2 4.03
  * Thursdays 14:30–16:00 in STC S018
  * Fridays 15:00–16:30 in STC S018

No lectures or classes will take place during School Reading Week 6.


### Course Description

This course introduces students to the fundamentals of computer programming as students design, write, and debug computer programs using the programing languages Python and R. The course will also cover the foundations of computer languages, algorithms, functions, variables, object orientation, scoping, and assignment.

### Organization

This course is an introduction to the fundamental concepts of programming for students who lack a formal background in the field, but will include more advanced problem-solving skills in the later stages of the course. Topics include algorithm design and program development; data types; control structures; functions and parameter passing; recursion; data structures; searching and sorting; and an introduction to the principles of object-oriented programming.

### Prerequisites

This is an introductory class and no prior experience with programming is required.

### Software

The course will use Python and R. We will use the Anaconda distribution to install the languages and manage packages and The Jupyter Notebook to write code. Lectures and assignments will be posted on Github, Students are expected to use Github also to submit problem sets and final exam.

### Materials

The main course texts will be:
*	Guttag, John V. *Introduction to Computation and Programming Using Python: With Application to Understanding Data*. MIT Press, 2016.
*	Intermediate and advanced documentation at http://docs.python.org/3/.
*	Grolemund, Garrett and Hadley Wickham. *R for Data Science*. O’Reilly, 2016. http://r4ds.had.co.nz
*	Grolemund, Garrett. *Hands-On Programming with R*. O’Reilly, 2014.

### Assessment

Take home exam (50%) and in-class assessment (50%). Students will be expected to produce 10 problem sets in the MT. Student problem sets will be marked each week, and will provide 50% of the mark.

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

Control flow defines the order in which statements are evaluated and executed in a program. In Python, indentation plays a crucial role in determining the control flow. In this week, we will discuss branching and iteration and how to write these in Python using `if`-`else` statements, `while` loops, `for` loops, `range()`, `break`, and `continue`. We will also introduce the extremely useful concept of list comprehensions.

*Readings*:
* Guttag. Chapters 2.2, 2.4–3.2, pp.15–18, 22–30.

*Lab*: **For Loops and List Comprehensions in Python**
* Control flow best practices and pitfalls
* Nested dictionary and list comprehensions

---
#### Week 4. Functions in Python

Good programmers are not measured by the amount of code they write but by the amount of functionality in their code. Good programming relies on abstraction and decomposition. Decomposition creates structure while abstraction helps hide details. Decomposition and abstraction can be achieved with functions and classes and in this week, we will introduce functions. We will discuss function arguments and variable scope and by means of an example, we will introduce the concept of recursion.

*Readings*:
* Guttag. Chapter 4, pp.39–63.

*Lab*: **Writing and Calling Functions in Python**

---
#### Week 5. Classes in Python

Object-oriented programming is a programming paradigm that helps increase modularity, reduce complexity, and foster code reuse. Objects are a data abstraction consisting of (1) an internal representation i.e. object attributes and (2) an interface for interacting with the objects through methods and functions. Objects are instances of classes and classes determine the type of an object. In this week, we will discuss how to define classes in Python and how to create instances of a class. We will also touch upon class inheritance and hierarchies.

*Readings*:
* Guttag. Chapter 8, pp.109–134.

*Lab*: **Programming in Teams**
* Programming in teams
* Commenting code

---
#### Week 7. Testing and Debugging in Python

Writing computer programs is easy but making them work properly is hard. We test programs to check if they work as intended and we debug them when we find out that they don’t. In this lecture, we will discuss different ways to test and debug programs. We will cover common error messages and how to catch them with `try`, `except`, `raise`, and `assert`.

*Readings*:
* Guttag. Chapters 6–7, pp.85–108.

*Lab*: **Exceptions and Assertions in Python**

---
#### Week 8. Data Types and Control Flow in R

In the next two weeks of the course, we will review the concepts learned until now by learning how they are implemented in the R programming language. We will start with basic data types in R (vectors, lists, matrices, factors, data frames) and control flow (if-else statements, for and while loops, repeat, next, break).

*Readings*:

*Lab*: **Introduction to R**
* Installing R with Anaconda
* Introduction to RStudio and workflow
* Practicing simple statements and control flow

---
#### Week 9. Functions and Debugging in R

Continuing from the previous week, we will cover vectorized operations in R (including `lapply`, `mapply`, `tapply`, `split`), functions, and variable scoping.

*Readings*:


*Lab*: **Writing Functions in R**

---
#### Week 10. Algorithms and Order of Growth

Algorithms are recipes that consist of a sequence of simple steps, control flow, and stopping rule. To evaluate the scalability of algorithms and to compare their efficiency, we use the abstraction “order of growth”. Order of growth expresses how the maximum amount of time needed grows as the size of the input grows. We will discuss different complexity classes and ways to analyze the complexity of programs.

*Readings*:
* Guttag. Chapter 9, pp.135–149.

*Lab*: **Order of Growth**
* Reading and evaluating order of growth of programs written in Python and R

---
#### Week 11. Searching and Sorting Algorithms

We will use the concepts and approaches introduced in the previous lecture to look at the complexity of several classic algorithms on searching and sorting. The goal is to get a better intuition of how to approach problems of efficiency. We will use examples written in both Python and R. The lecture will end with an overview of Python modules and R packages that are useful for data manipulation, analysis, and visualization.  

*Readings*:
* Guttag. Chapter 10.1–10.2, pp.151–164.

*Lab*: **Course Summary**
* Writing programs in Python and R
* Useful libraries for data science
