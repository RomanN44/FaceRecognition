import face_recognition
from PIL import Image, ImageDraw


#лицо
# roman_picture = face_recognition.load_image_file("roman.jpg") # Загружаем скачанное изображение
# roman_face_encoding = face_recognition.face_encodings(roman_picture) # Кодируем уникальные черты лица
# print(roman_face_encoding)


# черты лица
# roman_img = face_recognition.load_image_file("roman.jpg")
# roman_face = face_recognition.face_landmarks(roman_img)
# print(roman_face)

# два лица
# two_face = face_recognition.load_image_file("two_face.jpg") # Загружаем изображение нужного человека
# two_face_encoding = face_recognition.face_encodings(two_face) # Кодируем уникальные черты лица, для того чтобы сравнивать с другими
# print(two_face_encoding)

# roman_img = face_recognition.load_image_file("roman.jpg")
# result = face_recognition.batch_face_locations(roman_img)
# print(result)


#сравнение двух лиц
# roman_picture = face_recognition.load_image_file("roman.jpg") # Загружаем скачанное изображение
# roman_face_encoding = face_recognition.face_encodings(roman_picture) # Кодируем уникальные черты лица
# unknown_picture = face_recognition.load_image_file("photos/11.jpg") # Загружаем скачанное изображение
# unknown_face_encoding = face_recognition.face_encodings(unknown_picture) # Кодируем уникальные черты лица
#
# results = face_recognition.compare_faces([roman_face_encoding], unknown_face_encoding[0])
# print(results)

# image = face_recognition.load_image_file("photos/6.jpg")
# face_landmarks_list = face_recognition.face_landmarks(image)
# pil_image = Image.fromarray(image)
# pil_image = Image.new("RGB", (image.shape[0],image.shape[1]), (255, 255, 255))
# for face_landmarks in face_landmarks_list:
#     d = ImageDraw.Draw(pil_image, 'RGBA')
#     # Make the eyebrows into a nightmare
#
#     # d.point(face_landmarks['chin'], fill=(0,0,0))
#     # d.point(face_landmarks['left_eyebrow'], fill=(0,0,0))
#     # d.point(face_landmarks['right_eyebrow'], fill=(0,0,0))
#     # d.point(face_landmarks['nose_bridge'], fill=(0,0,0))
#     # d.point(face_landmarks['nose_tip'], fill=(0,0,0))
#     # d.point(face_landmarks['left_eye'], fill=(0,0,0))
#     # d.point(face_landmarks['right_eye'], fill=(0,0,0))
#     # d.point(face_landmarks['top_lip'], fill=(0,0,0))
#     # d.point(face_landmarks['bottom_lip'], fill=(0,0,0))
#
#     d.line(face_landmarks['chin'], fill=(0,0,0))
#     d.line(face_landmarks['left_eyebrow'], fill=(0,0,0))
#     d.line(face_landmarks['right_eyebrow'], fill=(0,0,0))
#     d.line(face_landmarks['nose_bridge'], fill=(0,0,0))
#     d.line(face_landmarks['nose_tip'], fill=(0,0,0))
#     d.line(face_landmarks['left_eye'], fill=(0,0,0))
#     d.line(face_landmarks['right_eye'], fill=(0,0,0))
#     d.line(face_landmarks['top_lip'], fill=(0,0,0))
#     d.line(face_landmarks['bottom_lip'], fill=(0,0,0))
#
#     pil_image.show()

image = face_recognition.load_image_file("photos/6.jpg")
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()