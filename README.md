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
Unified Modeling Language (UML) acts like a special language for drawing pictures that help us understand and explain how software is designed. It's like a set of tools that everyone can use to create a common understanding of how a piece of software works.

Imagine you're building a house, and you want to explain your ideas to different people—like architects, builders, and decorators. UML is like a set of drawings and symbols that make it easy for everyone to understand your ideas about how the house should look, what it should do, and how different parts will work together.

In the world of software, UML is like a universal language that developers, designers, and other people involved in building software can use to communicate and share their thoughts. It's a way to make sure everyone is on the same page when it comes to designing and talking about software.

So, in simpler terms, UML is like a toolbox for creating visual guides that help us all understand and discuss how software is put together and how it behaves.

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
