import requests


def hava_durumu():
    url_link = "http://api.weatherapi.com/v1/current.json"
    access_key = "fe661b56017447dab3d24625220704"

    iller = [
        "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkâri", "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kırıkkale", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Şanlıurfa", "Siirt", "Sinop", "Sivas", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat", "Zonguldak"
    ]

    veriler = []

    for il in iller:
        respose = requests.get(url=url_link, params={
                               "key": access_key, "q": il}).json()
        try:
            if respose["current"]["temp_c"] > 13:

                deger = {
                    "il": respose["location"]["name"],
                    "sicaklik": respose["current"]["temp_c"],
                    "tarih": respose["location"]["localtime"][:-6]
                }
                veriler.append(deger)

            else:
                continue

        except:
            continue
    # print(veriler)


hava_durumu()
