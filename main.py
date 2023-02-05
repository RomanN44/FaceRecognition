import face_recognition
from PIL import Image # Библиотека для работы с изображениями

find_face = face_recognition.load_image_file("photos/0.jpg") # Загружаем изображение нужного человека
# find_face = face_recognition.load_image_file("face/sergey.jpg") # Загружаем изображение нужного человека
face_encoding = face_recognition.face_encodings(find_face)[0] # Кодируем уникальные черты лица, для того чтобы сравнивать с другими

i = 0 # Счётчик общего выполнения
done = 0 # Счётчик совпадений
numFiles = 12 # Тут указываем кол-во фото
while i != numFiles:
    i += 1 # Увеличиваем счётчик общего выполнения
    unknown_picture = face_recognition.load_image_file(f"photos/{i}.jpg") # Загружаем скачанное изображение
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture) # Кодируем уникальные черты лица

    pil_image = Image.fromarray(unknown_picture) # Записываем изображение в переменную

    # Проверяем нашла ли нейросеть лицо
    if len(unknown_face_encoding) > 0: # Если нашли лицо
        encoding = unknown_face_encoding[0] # Обращаемся к 0 элементу, чтобы сравнить
        results = face_recognition.compare_faces([face_encoding], encoding) # Сравниваем лица

        if results[0] == True: # Если нашли сходство
            done += 1 # Увеличиваем счётчик общего выполнения
            print(i,"-","Нашли нужного человека !")
            pil_image.save(f"done/{int(done)}.jpg") # Сохраняем фото с найденным человеком
        else: # Если не нашли сходство
            print(i,"-","Не нашли нужного человека!")
    else: # Если не нашли лицо
        print(i,"-","Лицо не найдено!")
