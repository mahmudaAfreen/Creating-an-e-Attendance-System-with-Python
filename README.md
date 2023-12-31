# Creating an e-Attendance System with Python


# Overview 

#### Introduction
Welcome to a fascinating project that involves creating a Face Recognition Attendance System using Python. In simple terms, we're building a system that can recognize and identify people based on their unique facial features. This project is especially exciting because it aims to upgrade the way organizations track attendance using advanced facial recognition technology.

#### Objective
The primary goal here is to improve the attendance tracking system in organizations. Traditional methods of taking attendance can be a bit tricky and time-consuming. So, we're turning to face recognition to make the process more efficient and accurate. The idea is to use the distinctive features of people's faces to take attendance automatically.

#### How It Works
Imagine taking a selfie, and the system automatically figures out who you are by comparing your face with faces it already knows. That's essentially how our attendance system works. It captures and analyzes facial features to confirm the identity of employees and record their attendance without any manual effort.

#### Benefits
The cool thing about this system is that it's super accurate. It reduces mistakes that can happen when humans manually track attendance. Plus, it's way faster! Another advantage is that it cuts down on the need for people to do the attendance work, letting the system handle the complicated parts.

#### Conditions for Optimal Performance
Here's a little tip for the system to work its best: make sure the area where employees are getting their pictures taken is well-lit. Good lighting helps the system see and understand facial features clearly, ensuring accurate identification.

#### Why Facial Recognition?
So, why go for facial recognition? Well, it solves problems we often face with traditional attendance methods. It's like upgrading from a manual typewriter to a fancy computer. Facial recognition not only saves time and effort but also makes the attendance process smoother and more reliable.

## Software Dependencies
**Step 1: Install C++ Compiler (Visual Studio)**
1. [Download](https://visualstudio.microsoft.com/downloads/) the Visual Studio Community Edition.
2. Run the installer and select 'Desktop development with C++'.
3. Allow the installer to download and install the necessary components (This may take some time).
4. After installation, restart your computer.

**Step 2: Set Up Python Environment (PyCharm)**
1. Open your PyCharm project.
2. Install the required Python packages using the following commands
```
pip install cmake
pip install dlib
pip install face_recognition
pip install numpy opencv-python
```
**Step 3: Install PyBuilder**
1. Install PyBuilder using the following command:
```
python -m venv venv
.\venv\Scripts\activate
pip install pybuilder
pyb
pyb --start-project
```
2. Build the project using:
```
pyb publish
```
***You must install it using a virtual environment***

Begin with the basic requirements, then make sure to meet all the other [needs](https://pages.github.com/](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/src/main/python/requirement.txt)https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/src/main/python/requirement.txt) to finish the project successfully.

# Documentation 
## Git

## Unified Model Language(UML)
I can relate UML to building a house. The first thing will be explaining the ideas to different people—like architects, builders, and decorators. UML is like a set of drawings and symbols that make it easy for everyone to understand the ideas about how the house should look, what it should do, and how different parts will work together.

In the world of software, UML is like a universal language that developers, designers, and other people involved in building software can use to communicate and share their thoughts. It's a way to make sure everyone is on the same page when it comes to designing and talking about software.

#### UML Diagrams Presented in this Repository
1.	[**Activity Diagram:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Activity%20Diagram.png)
An activity diagram provides a comprehensive look at how a system behaves by illustrating the sequence of actions in a process. It helps us follow the flow and connections between activities, aiding in the understanding of activity order and dependencies. This diagram is a valuable tool for gaining insight into the dynamics of the system, contributing to a holistic understanding of how various activities interrelate. In simpler terms, it serves as a helpful guide for comprehending how different activities work together to make the system function cohesively.

2.	[**Sequence Diagram:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Sequence%20diagram.jpg)
In a sequence diagram, we witness a play-by-play conversation among different objects in a software system. Each object has a "lifeline," and this diagram acts like a visual script, revealing how these objects talk to each other over time. It's akin to observing a dynamic chat between various parts of the software, providing a clear view of when and how these exchanges happen.
Simply put, a sequence diagram is a visual story that unfolds the dialogue between software objects, giving us a snapshot of their interactions and timing.

3.	[**Use Case Diagram:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Use%20Case%20Diagram.jpg)
A use case diagram paints a broad picture of a system's major functions and what it aims to achieve. It acts like a map, highlighting the interactions between the system and the external players involved. By showcasing use cases (what the system does) and actors (external participants), it emphasizes the external interactions and functions rather than delving into the inner workings of the system. It's like a visual guide that outlines the system's goals and how outside elements connect with it.

4.	[**Component Diagram:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Component%20Diagram.jpg)
A component diagram is like a blueprint that reveals the different building blocks that make up a project. It showcases the various components that work together to create the entire system. Think of it as a visual guide highlighting the project's structural aspects. This diagram helps us understand how the different parts fit together to form a cohesive whole, making it particularly useful for visualizing the project's overall structure.

5. [**Future Work Component Diagram**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Component%20Diagram-Future%20work.jpg)
Consideration for future work includes the enhancement of the Component Diagram to showcase detailed components, providing a more nuanced insight into the system's architecture. Investment in this aspect would contribute to a more thorough understanding of the project's structure and interdependencies.


## Domain-Driven Design(DDD)
I considered it as a strategy aimed at improving the quality of software by aligning it more closely with the business needs it serves. At its core, DDD is about navigating complexity by placing the focus of software development on the ‘domain’, or the specific business context within which the software operates. It advocates for the use of a ‘ubiquitous language’, a common language that is shared by both the software developers and the business stakeholders.

In the [**Domain Driven Design Diagram**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/DDD%20Diagram.jpg), I drew out all the important parts of the application's problems and goals. This is like the basic plan for what we want the software to do. Some parts are already done, and some are planned for the future, depending on getting funds.

To make things easy to understand, I made a simple [**glossary**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Ubiquitous%20Language.pdf) or we can say ubiquitous language’, a common language that is shared by both the software developers and the business stakeholders. This helps everyone working on the project understand how the software is built and talk about it similarly. This way, everyone involved can communicate and work together more effectively.

## Metrics

## Clean Code Development
Following clean code principles in software development is vital. Clean code is easier to read and understand, promoting collaboration and hassle-free maintenance. It enhances efficiency by simplifying issue identification and resolution, reducing the risk of introducing new errors. Importantly, it creates a positive work environment, making development more enjoyable and less stressful.
There are plenty of ways and principles one can follow in terms of writing code clean. Here are my top preference, 
1. **Descriptive names:** The names of variables and classes should be descriptive. They should explain the intentions, inform the purpose they exist for, the role they play, and the way they should be used.
2. **Names should describe side effects:** The name you choose should describe what a given method, variable or class does. For example, if a function is created to search for an object and - in the case of not finding it - create a new one, it is better to use the name findOrCreate instead of just find.
3. **Always delete commented-out code:** It's essential to delete commented-out code. Such code confuses readers, messes up the code, and disrupts understanding. Over time, it becomes outdated and loses meaning. Leaving it creates uncertainty, as future readers may hesitate to remove it without knowing its significance.
4. **DRY - the “Don’t Repeat Yourself”:** It advises against repeating code in software development. Copy-pasting the same or similar code in different spots not only makes it longer but also means changing it in multiple places for updates, raising the chance of errors. The solution? Put duplicate code in a separate method, or consider using polymorphism or design patterns in specific situations.
5. **Code classes should have a single responsibility:** If a class is responsible for more than one area in the application, it can lead to problems in the future, e.i. when introducing changes in one area, we may mess up something in another, seemingly unrelated one.
6. **Format and Syntax:** Keeping the same look and style in the code is crucial for clean code. It makes the code easy to read and understand. Consistent formatting lets developers spot patterns, making it simpler to fix issues, keep things up-to-date, and handle the code over time. It also reduces mistakes because everyone follows the same rules.
7. **Conciseness vs Clarity:** While it's important to keep code concise to improve its readability and maintainability, it's equally important to ensure that the code is clear and easy to understand. Writing overly concise code can lead to confusion and errors, and can make the code difficult to work with for other developers.
8. **Reusability:** Code reusability is a fundamental concept in software engineering that refers to the ability of code to be used multiple times without modification. The importance of code reusability lies in the fact that it can greatly improve the efficiency and productivity of software development by reducing the amount of code that needs to be written and tested.
9. **Clear Flow of Execution:** Having a clear flow of execution is essential for writing clean code because it makes the code easier to read, understand, and maintain. Code that follows a clear and logical structure is less prone to errors, easier to modify and extend, and more efficient in terms of time and resources.
10. **Documentation:** Documentation is an essential part of writing clean code. Proper documentation not only helps the developer who wrote the code understand it better in the future but also makes it easier for other developers to read and understand the codebase. When code is well-documented, it can save time and effort in debugging and maintaining the code.

This is my [**cheat sheet**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Cheat%20Sheet.pdf) for important code descriptions in Python. It's detailed to ensure better understanding since the entire project is written in Python.

## Build Management
Build management is a critical aspect of modern software development, especially with the adoption of continuous integration and continuous delivery (CI/CD) practices. It involves collecting, compiling, testing, and deploying software assets to facilitate the release process.

Ever wondered how software is made and put together? For that one will have to know Build management and there is some amazing way to do so. For this work, I used a cool tool called PyBuilder to make this process super easy. PyBuilder stands out as a nifty tool for automating software builds. Crafted entirely in Python, it focuses on making life easier for Python developers. It plays with the concept of dependency-based programming but adds a cool twist – a powerful plugin system. This feature lets you build life-cycles that are as flexible and robust as those you might find in other big-name tools like Apache Maven and Gradle. It's like having a versatile toolbox for constructing your software in a way that suits you best.

If I describe it in simple words, it's like a helpful robot that takes care of all the steps – from collecting the pieces of the software to making sure everything works correctly. Or, you can think of it like baking a cake – PyBuilder is the chef who takes care of everything, from gathering ingredients to baking the cake (or in our case, compiling and testing the software).

1.  [build.py](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/build.py): This is the brain of our operation. It tells PyBuilder what to do – like which parts of the software to use and how to assemble them.
2.  [setup.py](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/setup.py): Think of this as a recipe card. It gives instructions on how the software should be packaged and shared with others.
3. [pyproject.toml](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/pyproject.toml): This is like a note to PyBuilder. It tells PyBuilder important details about our project, so it knows what tools to use.
   
To get started with the building management one can follow the first steps I described in [Software Dependencies](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/tree/main#software-dependencies). If everything is set up successfully one will see the [build](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Unittest.png) is successful once they run **pyb publish** in the cmd. 
## Continuous Delivery

## Unit Test

## IDE
I used PyCharm 2022.2.4 (Community Edition) using Anaconda Python 3.9 as an interpreter. I find it very useful to use it this way for an easier environment and package management even if I decide to use other tools like Jupyter Notebook or Google Collab, Anaconda as an interpreter will save time not having to install save packages everywhere. The integration with Git using this IDE was straightforward forward and I was able to commit, pull, and push updates without facing an issue, would be interesting to start trying it with multiple branches for more complex projects. Another feature I like very much about this IDE is the new package manager for PyCharm that allows you to install and update packages within a few clicks, no pip is needed. 

My most used shortcuts are:
1. Ctrl + K to show commit window
2. Ctrl + Shift + C to cpy document path
3. Alt + Shift + F9 to run selected
To explore all the shortcuts, we can check [here](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf).
## DSL
DSLs, or special code languages, are like secret codes made for solving specific job-related puzzles. They are short, easy to read, and focus on the kind of problems we find at work. So, if we are used to the kind of stuff we deal with at our job, DSLs make coding feel like a breeze. They are great for making machines do repetitive tasks, sorting out complicated stuff, or letting non-coders use the computer without getting into the nitty-gritty of regular coding languages. 

I even made a cool [weekly routine tracker](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/daily_routine.dsl) using DSL. It's like jotting down what we do each day, and the DSL magic summarizes everything for us. Just run the DSL file with [Python](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/dsl_interpreter.py), and boom, it's done!

**Following cmd:** ```python dsl_interpreter.py daily_routine_tckr.dsl```
## Functional Programming
