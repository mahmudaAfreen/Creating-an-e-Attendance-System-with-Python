import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

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
def find_encodings(photos):
    # Initialize an empty list for the encodings
    encodings_list = []
    # Iterate through the list of images
    for img in photos:
        # Convert the image from BGR to RGB color space
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Find the encoding for the image
        encode = face_recognition.face_encodings(rgb_img)[0]
        # Add the encoding to the list
        encodings_list.append(encode)
    # Return the list of encodings
    return encodings_list

# Define a function to mark attendance for a given name
def mark_attendance(name):
    # Open the attendance file in read/write mode
    with open('Attendance.csv', 'r+') as f:
        # Read the contents of the file
        attendance_data = f.readlines()
        # Initialize an empty list for the names in the file
        name_list = []
        # Iterate through the lines in the file
        for line in attendance_data:
            # Split the line by the comma separator
            entry = line.split(',')
            # Add the name to the list
            name_list.append(entry[0])
        # If the name is not in the list
        if name not in name_list:
            # Get the current time
            now = datetime.now()
            # Format the time as a string in the desired format
            time_str = now.strftime('%H:%M:%S')
            # Write the name and time to the file, with a newline character
            f.writelines(f'\n{name},{time_str}')

# Find the encodings for the known images
encodings_known = find_encodings(photos)
# Print a message indicating that the encoding is complete
print('Encoding Complete')

# Initialize the video capturer using the default webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    success, img = cap.read()
    # Resize the frame to a quarter of its original size
    img_small = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    # Convert the frame from BGR to RGB color space
    rgb_frame = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

    # Find the locations of faces in the frame
    faces_cur_frame = face_recognition.face_locations(rgb_frame)
    # Find the encodings of the faces in the frame
    encodes_cur_frame = face_recognition.face_encodings(rgb_frame, faces_cur_frame)

    # Iterate through the encodings and locations of the faces in the frame
    for encode_face, face_loc in zip(encodes_cur_frame, faces_cur_frame):
        # Calculate the distance between the current face encoding and the known encodings
        face_distances = face_recognition.face_distance(encodings_known, encode_face)
        # Print the face distance
        print(face_distances)
        # Get the index of the closest matching encoding
        match_index = np.argmin(face_distances)

        # If the distance to the closest encoding is less than 0.6
        if face_distances[match_index] < 0.60:
            # Set the name to the corresponding class name
            name = classNames[match_index].upper()
            # Mark attendance for the name
            mark_attendance(name)
        else:
            # If the distance is greater than or equal to 0.6, set the name to "Unknown"
            name = 'Unknown'
        
        # Get the coordinates of the face location
        y1, x2, y2, x1 = face_loc
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
