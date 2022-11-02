import requests


source = "https://everyayah.com/data/"
reciter = "Husary_128kbps/"

surah_index = int(input("Surah index:\n>>> "))
start = int(input("Start\n>>> "))
end = int(input("End\n>>> "))

def get_intro(index):
    if index == 1:
        return requests.get(source + reciter + "audhubillah.mp3")
    else:
        audio1 = requests.get(source + reciter + "audhubillah.mp3")
        audio2 = requests.get(source + reciter + "bismillah.mp3")
        return (audio1, audio2)

for i in range(start, end+1):
    
    surah_index = (3 - len(str(surah_index))) * '0' + str(surah_index)
    i = (3 - len(str(i))) * '0' + str(i)

    url = source + reciter + surah_index + i + '.mp3'
    print(i, url)

    response = requests.get(url)
    with open("audio.mp3", "ab") as file:
        file.write(response.content)

