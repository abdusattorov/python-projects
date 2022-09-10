import requests


source = "https://everyayah.com/data/"
reciter = "Husary_128kbps/"

input_reciter = input()
surah_index = int(input("Surah index:\n>>> "))
start = int(input("Start\n>>> "))
end = int(input("End\n>>> "))

for i in range(start, end+1):
    
    surah_index = (3 - len(str(surah_index))) * '0' + str(surah_index)
    i = (3 - len(str(i))) * '0' + str(i)

    url = source + reciter + surah_index + i + '.mp3'
    print(i, url)

    response = requests.get(url)
    with open("audio.mp3", "ab") as file:
        file.write(response.content)

