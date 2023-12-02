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

## Domain-Driven Design(DDD)

## Metrics

## Clean Code Development

## Build Management
Build management is a critical aspect of modern software development, especially with the adoption of continuous integration and continuous delivery (CI/CD) practices. It involves collecting, compiling, testing, and deploying software assets to facilitate the release process.
Ever wondered how software is made and put together? For that one will have to know Build management and there is some amazing way to do so. For this work, I used a cool tool called PyBuilder to make this process super easy. PyBuilder stands out as a nifty tool for automating software builds. Crafted entirely in Python, it focuses on making life easier for Python developers. It plays with the concept of dependency-based programming but adds a cool twist – a powerful plugin system. This feature lets you build life-cycles that are as flexible and robust as those you might find in other big-name tools like Apache Maven and Gradle. It's like having a versatile toolbox for constructing your software in a way that suits you best.
If I describe it in simple words, it's like a helpful robot that takes care of all the steps – from collecting the pieces of the software to making sure everything works correctly. Or, you can think of it like baking a cake – PyBuilder is the chef who takes care of everything, from gathering ingredients to baking the cake (or in our case, compiling and testing the software).

1.  [build.py](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/build.py): This is the brain of our operation. It tells PyBuilder what to do – like which parts of the software to use and how to assemble them.
2.  [setup.py](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/setup.py): Think of this as a recipe card. It gives instructions on how the software should be packaged and shared with others.
3. [pyproject.toml](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/pyproject.toml): This is like a note to PyBuilder. It tells PyBuilder important details about our project, so it knows what tools to use.
To get started with the building management you can follow the first steps I described in [Software Dependencies](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/tree/main#software-dependencies). If everything is set up successfully one will see the [build](https://github.com/mahmudaAfreen/Creating-an-e-Attendance-System-with-Python/blob/main/Work%20process/Unittest.png) is successful once they run **pyb publish** in the cmd. 
## Continuous Delivery

## Unit Test

## IDE

## DSL

## Functional Programming
