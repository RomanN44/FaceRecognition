import face_recognition
import time

# Often instead of just checking if two faces match or not (True or False), it's helpful to see how similar they are.
# You can do that by using the face_distance function.

# The model was trained in a way that faces with a distance of 0.6 or less should be a match. But if you want to
# be more strict, you can look for a smaller face distance. For example, using a 0.55 cutoff would reduce false
# positive matches at the risk of more false negatives.

# Note: This isn't exactly the same as a "percent match". The scale isn't linear. But you can assume that images with a
# smaller distance are more similar to each other than ones with a larger distance.



# Load some images to compare against
known_obama_image = face_recognition.load_image_file("obama.jpg")
known_biden_image = face_recognition.load_image_file("biden.jpg")

# Get the face encodings for the known images
obama_face_encoding = face_recognition.face_encodings(known_obama_image)[0]
biden_face_encoding = face_recognition.face_encodings(known_biden_image)[0]

# known_encodings = [
#     obama_face_encoding,
#     biden_face_encoding
# ]

known_encodings = {"obama": obama_face_encoding, "biden": biden_face_encoding}

# Load a test image and get encondings for it
image_to_test = face_recognition.load_image_file("obama2.jpg")
image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

# See how far apart the test image is from the known faces
face_distances = face_recognition.face_distance(list(known_encodings.values()), image_to_test_encoding)

start_time = time.time()
for i, face_distance in enumerate(face_distances):
    print("Тестовое изображение находится на расстоянии {:.2} от известного изображения #{}".format(face_distance, list(known_encodings.keys())[i]))
    print("- При нормальном срезе 0,6 будет ли тестовое изображение соответствовать известному изображению? {}".format(face_distance < 0.6))
    print("- При очень строгом отсечении 0,5 будет ли тестовое изображение соответствовать известному изображению? {}".format(face_distance < 0.5))
    print()
print("--- %s seconds ---" % (time.time() - start_time))