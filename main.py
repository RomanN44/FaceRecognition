import face_recognition

find_face = face_recognition.load_image_file("photos/1.jpg") # Загружаем изображение нужного человека
face_encoding = face_recognition.face_encodings(find_face) # Кодируем уникальные черты лица, для того чтобы сравнивать с другими
print(face_encoding)

unknown_picture = face_recognition.load_image_file("roman.jpg") # Загружаем скачанное изображение
unknown_face_encoding = face_recognition.face_encodings(unknown_picture) # Кодируем уникальные черты лица
print(unknown_face_encoding)