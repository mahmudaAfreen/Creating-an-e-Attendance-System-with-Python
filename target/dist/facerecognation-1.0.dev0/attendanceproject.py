
import cv2  # Import the OpenCV library
import numpy as np  # Import NumPy
import face_recognition  # Import the face_recognition library
import os  # Import the os library for file and directory management
from datetime import datetime  # Import the datetime module for time-related functions

# Set the path to the directory containing the known images
path = 'ImagesAttendance'

# Initialize empty lists for the known images and their corresponding class names
photos = []
classNames = []

# Get a list of all the files in the directory
myList = os.listdir(path)

# Iterate through the list of files
for cl in myList:
    # Read the current file as an image
    curImg = cv2.imread(f'{path}/{cl}')
    # Add the image to the list of known images
    photos.append(curImg)
    # Get the class name by removing the file extension from the file name
    classNames.append(os.path.splitext(cl)[0])

# Print the list of class names
print(classNames)

# Define a function to find the encodings for the known images
def findencodings(photos):
    # Initialize an empty list for the encodings
    cdata = []
    # Iterate through the list of images
    for i in photos:
        # Convert the image from BGR to RGB color space
        i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
        # Find the encoding for the image
        encode = face_recognition.face_encodings(i)[0]
        # Add the encoding to the list
        cdata.append(encode)
    # Return the list of encodings
    return cdata

# Define a function to mark attendance for a given name
def markattendance(name):
    # Open the attendance file in read/write mode
    with open('Attendance.csv', 'r+') as f:
        # Read the contents of the file
        mydata = f.readlines()
        # Initialize an empty list for the names in the file
        namelist = []
        # Iterate through the lines in the file
        for line in mydata:
            # Split the line by the comma separator
            entry = line.split(',')
            # Add the name to the list
            namelist.append(entry[0])
        # If the name is not in the list
        if name not in namelist:
            # Get the current time
            now = datetime.now()
            # Format the time as a string in the desired format
            show = now.strftime('%H:%M:%S')
            # Write the name and time to the file, with a newline character
            f.writelines(f'\n{name},{show}')

# Find the encodings for the known images
encodelistknown = findencodings(photos)
# Print a message indicating that the encoding is complete
print('Encoding Complete')

# Initialize the video capturer using the default webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    success, img = cap.read()
    # Resize the frame to a quarter of its original size
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    # Convert the frame from BGR to RGB color space
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Find the locations of faces in the frame
    facesCurFrame = face_recognition.face_locations(imgS)
    # Find the encodings of the faces in the frame
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    # Iterate through the encodings and locations of the faces in the frame
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        # Calculate the distance between the current face encoding and the known encodings
        faceDis = face_recognition.face_distance(encodelistknown, encodeFace)
        # Print the face distance
        print(faceDis)
        # Get the index of the closest matching encoding
        matchIndex = np.argmin(faceDis)

        # If the distance to the closest encoding is less than 0.6
        if faceDis[matchIndex] < 0.60:
            # Set the name to the corresponding class name
            name = classNames[matchIndex].upper()
            # Mark attendance for the name
            markattendance(name)
        else:
            # If the distance is greater than or equal to 0.6, set the name to "Unknown"
            name = 'Unknown'
        # Get the coordinates of the face location
        y1, x2, y2, x1 = faceLoc
        # Multiply the coordinates by 4 to scale them up from the resized frame
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        # Draw a rectangle around the face
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Draw a filled rectangle below the face
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        # Display the name of the person on the rectangle
        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    # Display the frame
    cv2.imshow('Webcam', img)
    cv2.waitKey(1)