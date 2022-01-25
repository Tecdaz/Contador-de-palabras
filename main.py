def normalize(text):
# Signos de puntuacion comunes y caracteres que no forman una palabra
    punctuation_marks = list(".,:;?¿()'><")
# reemplaza los signos de puntuacion por espacios, solo por si no hay buena gramatica en el texto

    words = [word.lower() for word in text.split()]

    for index, word in enumerate(words):
        for mark in punctuation_marks:
            word = word.replace(mark, "")
        words[index] = word
    return words

def run():
    total_count = 0
    res = {}

    with open("./data.txt", "r") as text:

        for line in text:
            for word in normalize(line):
                count = res.get(word, 0)
                count += 1
                total_count += 1
                res[word] = count
    
    print(res)
        
    


if __name__ == '__main__':
    run()