meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            

}
for i in range(5):
    word = input("Введите непонятное слово : ")
    word = word.upper()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Такого слова нет")
