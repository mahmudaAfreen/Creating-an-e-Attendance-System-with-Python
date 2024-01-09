import unittest
import cv2
import numpy as np
import face_recognition

# Import functions and variables from the AttendanceProject module
from src.main.python.AttendanceProject import markattendance, cap, classNames, photos, findencodings
import src.main.python.AttendanceProject

class TestAttendanceMarking(unittest.TestCase):
    def setUp(self):
        # Set up test data by adding a known face to the list of photos
        self.test_image = cv2.imread('test.jpg')
        photos.append(self.test_image)
        classNames.append('Test Person')
        self.encodelist_known = findencodings(photos)

    def test_markattendance(self):
        # Test that the markattendance function adds an entry to the Attendance.csv file
        markattendance('Test Person')
        with open('Attendance.csv', 'r') as file:
            lines = file.readlines()
            # Verify that there are 2 lines in the file (1 header, 1 entry)
            self.assertEqual(len(lines), 2)
            # Verify that the first field in the second line is 'Test Person'
            self.assertEqual(lines[1].split(',')[0], 'Test Person')

    def test_face_recognition(self):
        # Test that the face recognition correctly identifies the known face
        success, img = cap.read()
        img_resized = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

        # Get face locations and encodings using face_recognition library
        faces_cur_frame = face_recognition.face_locations(img_rgb)
        encodes_cur_frame = face_recognition.face_encodings(img_rgb, faces_cur_frame)

        for encode_face, face_loc in zip(encodes_cur_frame, faces_cur_frame):
            # Compare the face with known faces
            matches = face_recognition.compare_faces(self.encodelist_known, encode_face)
            face_dis = face_recognition.face_distance(self.encodelist_known, encode_face)
            match_index = np.argmin(face_dis)
            
            # Assert that the distance is less than 0.60 and the name matches 'Test Person'
            self.assertLess(face_dis[match_index], 0.60)
            self.assertEqual(classNames[match_index], 'Test Person')

if __name__ == '__main__':
    unittest.main()
