
import cv2



# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed
# taken from face_recognition and repurposed for cv2 ONLY
# misses features like naming people

# Get a reference to webcam (0 if you want that) or link to a video saved
video_capture = cv2.VideoCapture("./downloads/pew.mp4")





# Initialize some variables
face_locations = []

process_this_frame = True
face_cascade = cv2.CascadeClassifier('frontalface.xml')
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        #detect face from frame
        faces = face_cascade.detectMultiScale(rgb_small_frame, 1.2, 5)
        print(faces)
        
        #set name(can leave blank)
        name="PEWDS"
        

    process_this_frame = not process_this_frame


    # Display the results
    for (x,y,w,h) in faces:
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        y *= 4
        w *= 4
        h *= 4
        x *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 0, 255), 2)
        
        # Draw a label with a name below the face
        
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (x + 6, y - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#End stream/program
video_capture.release()
cv2.destroyAllWindows()
