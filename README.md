# Creating an e-Attendance System with Python

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python)](https://sonarcloud.io/summary/new_code?id=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python)


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
## 1. Git
To do frequent commits, push, merging, and other operations I used git. The record of my git activity can be found in the [git contribution](https://github.com/mahmudaAfreen). 
## 2. Unified Model Language(UML)
I can relate UML to building a house. The first thing will be explaining the ideas to different people—like architects, builders, and decorators. UML is like a set of drawings and symbols that make it easy for everyone to understand the ideas about how the house should look, what it should do, and how different parts will work together.

In the world of software, UML is like a universal language that developers, designers, and other people involved in building software can use to communicate and share their thoughts. It's a way to make sure everyone is on the same page when it comes to designing and talking about software.

#### UML Diagrams Presented in this Repository
2.1.	[**Activity Diagram:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Activity%20Diagram.png)
An activity diagram provides a comprehensive look at how a system behaves by illustrating the sequence of actions in a process. It helps us follow the flow and connections between activities, aiding in the understanding of activity order and dependencies. This diagram is a valuable tool for gaining insight into the dynamics of the system, contributing to a holistic understanding of how various activities interrelate. In simpler terms, it serves as a helpful guide for comprehending how different activities work together to make the system function cohesively.

2.2.	[**Sequence Diagram:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Sequence%20diagram.jpg)
In a sequence diagram, we witness a play-by-play conversation among different objects in a software system. Each object has a "lifeline," and this diagram acts like a visual script, revealing how these objects talk to each other over time. It's akin to observing a dynamic chat between various parts of the software, providing a clear view of when and how these exchanges happen.
Simply put, a sequence diagram is a visual story that unfolds the dialogue between software objects, giving us a snapshot of their interactions and timing.

2.3.	[**Use Case Diagram:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Use%20Case%20Diagram.jpg)
A use case diagram paints a broad picture of a system's major functions and what it aims to achieve. It acts like a map, highlighting the interactions between the system and the external players involved. By showcasing use cases (what the system does) and actors (external participants), it emphasizes the external interactions and functions rather than delving into the inner workings of the system. It's like a visual guide that outlines the system's goals and how outside elements connect with it.

2.4.	[**Component Diagram:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Component%20Diagram.jpg)
A component diagram is like a blueprint that reveals the different building blocks that make up a project. It showcases the various components that work together to create the entire system. Think of it as a visual guide highlighting the project's structural aspects. This diagram helps us understand how the different parts fit together to form a cohesive whole, making it particularly useful for visualizing the project's overall structure.

2.5. [**Future Work Component Diagram**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Component%20Diagram-Future%20work.jpg)
Consideration for future work includes the enhancement of the Component Diagram to showcase detailed components, providing a more nuanced insight into the system's architecture. Investment in this aspect would contribute to a more thorough understanding of the project's structure and interdependencies.


## 3. Domain-Driven Design(DDD)
I considered it as a strategy aimed at improving the quality of software by aligning it more closely with the business needs it serves. At its core, DDD is about navigating complexity by placing the focus of software development on the ‘domain’, or the specific business context within which the software operates. It advocates for the use of a ‘ubiquitous language’, a common language that is shared by both the software developers and the business stakeholders.

In the [**Domain Driven Design Diagram**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/DDD%20Diagram.jpg),[**Core domain chart**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Core%20domain%20chart.jpg), and [**Context mapping**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Context%20mapping%20ddd.jpg) with a future vision. I drew out all the important parts of the application's problems and goals. This is like the basic plan for what we want the software to do. Some parts are already done, and some are planned for the future, depending on getting funds. Here is the 

To make things easy to understand, I made a simple [**glossary**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Ubiquitous%20Language.pdf) or we can say ubiquitous language’, a common language that is shared by both the software developers and the business stakeholders. This helps everyone working on the project understand how the software is built and talk about it similarly. This way, everyone involved can communicate and work together more effectively.

## 4. Metrics
I prefer SonarCloud to analyze my code because it brings automated, thorough code reviews and early issue detection into my development process. It calculates technical debt, integrates seamlessly into my CI/CD workflow, and supports various languages. The convenience of a cloud-based platform, coupled with robust security features, makes SonarCloud my top choice. Its active community and SonarSource backing add valuable support that sets it apart from other platforms.

Here are all the calculated metrics for my project.

- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python&metric=bugs)](https://sonarcloud.io/summary/new_code?id=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=mahmudaAfreen_Creating-an-e-Attendance-System-with-Python)
## 5. Clean Code Development
Following clean code principles in software development is vital. Clean code is easier to read and understand, promoting collaboration and hassle-free maintenance. It enhances efficiency by simplifying issue identification and resolution, reducing the risk of introducing new errors. Importantly, it creates a positive work environment, making development more enjoyable and less stressful.
There are plenty of ways and principles one can follow in terms of writing code clean. Here are my top preferences that i used in my [main](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/src/main/python/AttendanceProject.py) , [basictest](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/src/unittest/python/Basicstest.py) , and in [unittest](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/src/unittest/python/projectunittest.py)

[**5.1. Descriptive names:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py#L46) The names of variables and classes should be descriptive. They should explain the intentions, inform the purpose they exist for, the role they play, and the way they should be used.

[**5.2. Names should describe side effects:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py#L35) The name you choose should describe what a given method, variable or class does. For example, if a function is created to search for an object and - in the case of not finding it - create a new one, it is better to use the name findOrCreate instead of just find.

[**5.3. Always delete commented-out code:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py) It's essential to delete commented-out code. Such code confuses readers, messes up the code, and disrupts understanding. Over time, it becomes outdated and loses meaning. Leaving it creates uncertainty, as future readers may hesitate to remove it without knowing its significance.

[**5.4. DRY - the “Don’t Repeat Yourself”:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py#L38#L52) It advises against repeating code in software development. Copy-pasting the same or similar code in different spots not only makes it longer but also means changing it in multiple places for updates, raising the chance of errors. The solution? Put duplicate code in a separate method, or consider using polymorphism or design patterns in specific situations.

[**5.5. Parameterization:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py#L74) It configures values or settings, such as file paths, encoding thresholds, or webcam indices, to make the code more flexible and adaptable to different environments or use cases.

[**5.6. Format and Syntax:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py#L1#L120) Overall, the entire code snippet adheres to consistent formatting and syntax conventions. Keeping the same look and style in the code is crucial for clean code. It makes the code easy to read and understand. Consistent formatting lets developers spot patterns, making it simpler to fix issues, keep things up-to-date, and handle the code over time. It also reduces mistakes because everyone follows the same rules.

[**5.7. Conciseness vs Clarity:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py#L1#L120) While it's important to keep code concise to improve its readability and maintainability, it's equally important to ensure that the code is clear and easy to understand. Writing overly concise code can lead to confusion and errors, and can make the code difficult to work with for other developers. Throughout the code snippet, there is a balance between conciseness and clarity, making it easy to understand.

[**5.8. Reusability:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py#L31) Code reusability is a fundamental concept in software engineering that refers to the ability of code to be used multiple times without modification. The importance of code reusability lies in the fact that it can greatly improve the efficiency and productivity of software development by reducing the amount of code that needs to be written and tested.

[**5.9. Clear Flow of Execution:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py#L1#L120) Having a clear flow of execution is essential for writing clean code because it makes the code easier to read, understand, and maintain. Code that follows a clear and logical structure is less prone to errors, easier to modify and extend, and more efficient in terms of time and resources.The code follows a clear flow of execution from top to bottom, with each section performing a specific task

[**5.10. Documentation:**](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Cheat%20Sheet.pdf) Documentation is an essential part of writing clean code. Proper documentation not only helps the developer who wrote the code understand it better in the future but also makes it easier for other developers to read and understand the codebase. When code is well-documented, it can save time and effort in debugging and maintaining the code.


## 6. Build Management
Build management is a critical aspect of modern software development, especially with the adoption of continuous integration and continuous delivery (CI/CD) practices. It involves collecting, compiling, testing, and deploying software assets to facilitate the release process.

Ever wondered how software is made and put together? For that one will have to know Build management and there is some amazing way to do so. For this work, I used a cool tool called PyBuilder to make this process super easy. PyBuilder stands out as a nifty tool for automating software builds. Crafted entirely in Python, it focuses on making life easier for Python developers. It plays with the concept of dependency-based programming but adds a cool twist – a powerful plugin system. This feature lets you build life-cycles that are as flexible and robust as those you might find in other big-name tools like Apache Maven and Gradle. It's like having a versatile toolbox for constructing your software in a way that suits you best.

If I describe it in simple words, it's like a helpful robot that takes care of all the steps – from collecting the pieces of the software to making sure everything works correctly. Or, you can think of it like baking a cake – PyBuilder is the chef who takes care of everything, from gathering ingredients to baking the cake (or in our case, compiling and testing the software).

1.  [build.py](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/build.py): This is the brain of our operation. It tells PyBuilder what to do – like which parts of the software to use and how to assemble them.
2.  [setup.py](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/setup.py): Think of this as a recipe card. It gives instructions on how the software should be packaged and shared with others.
3. [pyproject.toml](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/pyproject.toml): This is like a note to PyBuilder. It tells PyBuilder important details about our project, so it knows what tools to use.
   
To get started with the building management one can follow the first steps I described in [Software Dependencies](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/tree/main#software-dependencies). If everything is set up successfully one will see the [build](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Unittest.png) is successful once they run **pyb publish** in the cmd. 
## 7. Continuous Delivery
This [YAML](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/python-package.yml) file sets up a continuous delivery pipeline using GitHub Actions. It triggers on pushes to the main branch, and then runs a series of steps:

- Set up the Python environment.
- Check out the repository.
- Installs dependencies, including flake8 and pybuilder.
- Lints the code using flake8.
- Builds the project using PyBuilder.
- Executes any post-build actions.
- Completes the job with final actions or notifications.

One may need to adjust the Python version, branch name, and specific commands according to the project's requirements.

## 8. Unit Test
I was directly trying to do the unit test but it was going all wrong in the testing, the system was not identifying most of the faces of the same person from different angles. After doing some reading, I realized I should do a [basic test](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/src/unittest/python/Basicstest.py) to see what was going wrong. So, the basic test was giving me a higher True Value and I realized I should start from scratch there must be an error in my environment since I tried all possible ways to fix it.
For the test, I used images of different people but got Better results with the Images of Elon Musk. Because the good quality images of him in JPG/PNG format were freely available online. once I got a lower True value in the basic test then my unit tests were also working well. 

<img src="https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Train.png" width="400" height="300">      <img src="https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/test.png" width="400" height="300">

Secondly, I used [Unittest](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/src/unittest/python/projectunittest.py) to make sure everything was working fine. My way of doing that was pretty simple. 

**8.1. Setting Up for Testing:** First I set up my testing environment using the setup function. This function added a photo of a person I knew (let's call them 'Test Person') to a list, getting everything ready for my tests.

**8.2. Checked Attendance Marking:** Next, I wanted to ensure that my attendance marking was working. In the test_markattendance function, I took a picture (like using a webcam), marked the attendance for 'Test Person', and then checked the ['Attendance.csv'](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Attendance.csv) file. I verified that the file had two lines - one for the file header and one for the marked attendance of my known person.

**8.3. Tested Face Recognition:** My system was supposed to recognize faces, right? In the test_face_recognition function, I captured a frame from a webcam, looked for faces in that frame, and used some recognition magic. I made sure that when my system saw 'Test Person', it got it right - like saying, "Hey, I know you! You're 'Test Person'!"

**8.4. Used Modules and Functions:** I didn't build everything from scratch. I borrowed some useful tools from the 'AttendanceProject' module. It was like having a toolbox with some handy gadgets. I used functions like markattendance and variables like classNames from there to make my job easier.

**8.5. Ran the Tests:** Lastly, when I ran my script, it checked if everything I had written actually worked. It was like pushing a "test" button to ensure my code did what it was supposed to do. If all tests passed, I was in good shape!

In a nutshell, I made sure my attendance system recognized faces correctly, marked attendance properly, and all the tools I used did their jobs.

## 9. IDE
I used PyCharm 2022.2.4 (Community Edition) using Anaconda Python 3.9 as an interpreter. I find it very useful to use it this way for an easier environment and package management even if I decide to use other tools like Jupyter Notebook or Google Collab, Anaconda as an interpreter will save time not having to install save packages everywhere. The integration with Git using this IDE was straightforward forward and I was able to commit, pull, and push updates without facing an issue, it would be interesting to start trying it with multiple branches for more complex projects. Another feature I like very much about this IDE is the new package manager for PyCharm that allows you to install and update packages within a few clicks, no pip is needed. 

My most used shortcuts are:
1. Ctrl + K to show commit window
2. Ctrl + Shift + C to cpy document path
3. Alt + Shift + F9 to run selected
To explore all the shortcuts, we can check [here](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf).
## 10. DSL
DSLs, or special code languages, are like secret codes made for solving specific job-related puzzles. They are short, easy to read, and focus on the kind of problems we find at work. So, if we are used to the kind of stuff we deal with at our job, DSLs make coding feel like a breeze. They are great for making machines do repetitive tasks, sorting out complicated stuff, or letting non-coders use the computer without getting into the nitty-gritty of regular coding languages. 

I even made a cool [weekly routine tracker](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/daily_routine.dsl) using DSL. It's like jotting down what we do each day, and the DSL magic summarizes everything for us. Just run the DSL file with [Python](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/dsl_interpreter.py), and boom, it's done!

**Following cmd:** ```python dsl_interpreter.py daily_routine_tckr.dsl```

## 11. Functional Programming
Functional Programming benefits: Immutability, pure functions, readability, predictable code, easy debugging, and concurrency management, enhancing maintainability and reliability in face recognition. I have tried to use all the functions but I could not because of the structure of my project. However, I used most of them simply, these are:

[11.1. Final Data Structures:](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py#L69) `encodelistknown` This list holds the face encodings of known images.

```encodelistknown = findencodings(photos)  # List of face encodings for known images```

[11.2. (Mostly) Side-Effect-Free Functions:](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py#L31) ´findencodings:´ This function is a higher-order function since it takes a list (photos) and applies the face_recognition.face_encodings function to each element.

 ```
def findencodings(photos):
    # ... (unchanged code)
    return cdata  # List of face encodings for the provided images
```
 [11.3. Use of Higher-Order Functions:](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py#L31) `findencodings:` This function is mostly side-effect-free. It takes a list of images, processes each image to find face encodings, and returns a list of these encodings.
 
  ```
def findencodings(photos):
    # ... (unchanged code)
    encode = face_recognition.face_encodings(i)[0]  # Applying a function to each element
    # ... (unchanged code)

```
 
[11.4. Functions as Parameters and Return Values:](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/target/dist/facerecognation-1.0.dev0/attendanceproject.py#L69#L103)  ´findencodings:´ Takes a list of images as a parameter and returns a list of face encodings. ´markattendance:´ Takes a name as a parameter and marks attendance.

```
encodelistknown = findencodings(photos)  # Function returns a list of face encodings
markattendance(name)  # Function takes a name as a parameter

```
Since my main code does not contain all the functions, I wrote another example that showcases the flexibility and expressive power of the functions in performing different operations on a list of numbers.

- [Only final data structures](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/AllFunctions.py) 
- [(mostly) side effect free functions](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/AllFunctions.py#L5)  
- [Higher order function](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/AllFunctions.py#L9) 
- [Functions as parameters and return values](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/AllFunctions.py#L15) 
- [Use closures functions](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/AllFunctions.py#L23#L13)  
