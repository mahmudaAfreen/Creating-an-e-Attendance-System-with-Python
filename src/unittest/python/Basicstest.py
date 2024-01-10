import cv2
import face_recognition

# Function to load and convert an image
def load_and_convert_image(file_path):
    image = face_recognition.load_image_file(file_path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Function to get face location and encoding from an image
def get_face_location_and_encoding(image):
    face_location = face_recognition.face_locations(image)[0]
    face_encoding = face_recognition.face_encodings(image)[0]
    return face_location, face_encoding

# Function to draw rectangles and text on an image
def draw_rectangle_and_text(image, face_location, color=(255, 0, 255)):
    cv2.rectangle(image, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color, 2)

def main():
    # Load and convert images
    imgElon = load_and_convert_image('ImagesBasic/Elon Musk.jpg')
    imgTest = load_and_convert_image('ImagesBasic/Elon Test.jpg')

    # Get face location and encoding for both images
    faceLocElon, encodeElon = get_face_location_and_encoding(imgElon)
    faceLocTest, encodeTest = get_face_location_and_encoding(imgTest)

    # Draw rectangles around faces on both images
    draw_rectangle_and_text(imgElon, faceLocElon)
    draw_rectangle_and_text(imgTest, faceLocTest)

    # Compare faces and get results
    results = face_recognition.compare_faces([encodeElon], encodeTest)
    faceDis = face_recognition.face_distance([encodeElon], encodeTest)
    
    # Add text with results on the test image
    result_text = f'{results} {round(faceDis[0], 2)}'
    cv2.putText(imgTest, result_text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    # Display images
    cv2.imshow('Elon Musk', imgElon)
    cv2.imshow('Elon Test', imgTest)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
