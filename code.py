import requests
import time
import csv

data = [
#  {
#    "nama": "ACEH",
#    "id": 100054,
#    "kode": "11",
#    "tingkat": 1
#  },
  {
    "nama": "BALI",
    "id": 191103,
    "kode": "51",
    "tingkat": 1
  },
  {
    "nama": "BANTEN",
    "id": 191100,
    "kode": "36",
    "tingkat": 1
  },
  {
    "nama": "BENGKULU",
    "id": 191092,
    "kode": "17",
    "tingkat": 1
  },
  {
    "nama": "DAERAH ISTIMEWA YOGYAKARTA",
    "id": 191098,
    "kode": "34",
    "tingkat": 1
  },
  {
    "nama": "DKI JAKARTA",
    "id": 191095,
    "kode": "31",
    "tingkat": 1
  },
  {
    "nama": "GORONTALO",
    "id": 191053,
    "kode": "75",
    "tingkat": 1
  },
  {
    "nama": "JAMBI",
    "id": 191089,
    "kode": "15",
    "tingkat": 1
  },
  {
    "nama": "JAWA BARAT",
    "id": 191096,
    "kode": "32",
    "tingkat": 1
  },
  {
    "nama": "JAWA TENGAH",
    "id": 191097,
    "kode": "33",
    "tingkat": 1
  },
  {
    "nama": "JAWA TIMUR",
    "id": 191099,
    "kode": "35",
    "tingkat": 1
  },
  {
    "nama": "KALIMANTAN BARAT",
    "id": 191101,
    "kode": "61",
    "tingkat": 1
  },
  {
    "nama": "KALIMANTAN SELATAN",
    "id": 191106,
    "kode": "63",
    "tingkat": 1
  },
  {
    "nama": "KALIMANTAN TENGAH",
    "id": 191102,
    "kode": "62",
    "tingkat": 1
  },
  {
    "nama": "KALIMANTAN TIMUR",
    "id": 191107,
    "kode": "64",
    "tingkat": 1
  },
  {
    "nama": "KALIMANTAN UTARA",
    "id": 191108,
    "kode": "65",
    "tingkat": 1
  },
  {
    "nama": "KEPULAUAN BANGKA BELITUNG",
    "id": 191094,
    "kode": "19",
    "tingkat": 1
  },
  {
    "nama": "KEPULAUAN RIAU",
    "id": 191091,
    "kode": "21",
    "tingkat": 1
  },
  {
    "nama": "LAMPUNG",
    "id": 191093,
    "kode": "18",
    "tingkat": 1
  },
  {
    "nama": "Luar Negeri",
    "id": 200001,
    "kode": "99",
    "tingkat": 1
  },
  {
    "nama": "MALUKU",
    "id": 191115,
    "kode": "81",
    "tingkat": 1
  },
  {
    "nama": "MALUKU UTARA",
    "id": 191116,
    "kode": "82",
    "tingkat": 1
  },
  {
    "nama": "NUSA TENGGARA BARAT",
    "id": 191104,
    "kode": "52",
    "tingkat": 1
  },
  {
    "nama": "NUSA TENGGARA TIMUR",
    "id": 191105,
    "kode": "53",
    "tingkat": 1
  },
  {
    "nama": "P A P U A",
    "id": 191117,
    "kode": "91",
    "tingkat": 1
  },
  {
    "nama": "PAPUA BARAT",
    "id": 191118,
    "kode": "92",
    "tingkat": 1
  },
  {
    "nama": "PAPUA BARAT DAYA",
    "id": 191121,
    "kode": "96",
    "tingkat": 1
  },
  {
    "nama": "PAPUA PEGUNUNGAN",
    "id": 191120,
    "kode": "95",
    "tingkat": 1
  },
  {
    "nama": "PAPUA SELATAN",
    "id": 191114,
    "kode": "93",
    "tingkat": 1
  },
  {
    "nama": "PAPUA TENGAH",
    "id": 191119,
    "kode": "94",
    "tingkat": 1
  },
  {
    "nama": "RIAU",
    "id": 191088,
    "kode": "14",
    "tingkat": 1
  },
  {
    "nama": "SULAWESI BARAT",
    "id": 191113,
    "kode": "76",
    "tingkat": 1
  },
  {
    "nama": "SULAWESI SELATAN",
    "id": 191111,
    "kode": "73",
    "tingkat": 1
  },
  {
    "nama": "SULAWESI TENGAH",
    "id": 191110,
    "kode": "72",
    "tingkat": 1
  },
  {
    "nama": "SULAWESI TENGGARA",
    "id": 191112,
    "kode": "74",
    "tingkat": 1
  },
  {
    "nama": "SULAWESI UTARA",
    "id": 191109,
    "kode": "71",
    "tingkat": 1
  },
  {
    "nama": "SUMATERA BARAT",
    "id": 191087,
    "kode": "13",
    "tingkat": 1
  },
  {
    "nama": "SUMATERA SELATAN",
    "id": 191090,
    "kode": "16",
    "tingkat": 1
  },
  {
    "nama": "SUMATERA UTARA",
    "id": 191086,
    "kode": "12",
    "tingkat": 1
  }
]

def saveData(writer, wilayah, data):
    chart = data["chart"]
    paslon1 = chart.get("100025", 0)
    paslon2 = chart.get("100026", 0)
    paslon3 = chart.get("100027", 0)
    totalPaslon = paslon1 + paslon2 + paslon3
    if totalPaslon != data["administrasi"]["suara_sah"]:
        print(wilayah["prov"], ">",
            wilayah["kota"], ">",
            wilayah["kec"], ">",
            wilayah["kel"], ">",
            wilayah["tps"], "Is Invalid. Suara Sah: ", data["administrasi"]["suara_sah"], "Total Paslon: ", totalPaslon
        )
        writer.writerow([
            wilayah["prov"],
            wilayah["kota"],
            wilayah["kec"],
            wilayah["kel"],
            wilayah["tps"],
            data["administrasi"]["suara_sah"],
            data["administrasi"]["suara_total"],
            paslon1, paslon2, paslon3,
            data["images"][1]
        ])

with open("sirekap.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Prov", "Kota", "Kec", "Kel", "TPS", "Suara Sah", "Total Suara", "Paslon 1", "Paslon 2", "Paslon 3", "Link Dokumen"])
    
    for prov in data:
        print(prov['nama'])
        urlKota = "https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/{}.json".format(prov["kode"])
        kotas = requests.get(urlKota).json()
        for kota in kotas:
            # print(prov['nama'], " > ", kota['nama'])
            urlKec = "https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/{}/{}.json".format(prov["kode"], kota["kode"])
            kecs = requests.get(urlKec).json()
            for kec in kecs:
                print(prov['nama'], ">", kota['nama'], ">", kec["nama"])
                urlKel = "https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/{}/{}/{}.json".format(prov["kode"], kota["kode"], kec["kode"])
                kels = requests.get(urlKel).json()
                for kel in kels:
                    # print(prov['nama'], " > ", kota['nama'], " > ", kec["nama"], kel["nama"])
                    urlTps = "https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/{}/{}/{}/{}.json".format(prov["kode"], kota["kode"], kec["kode"], kel["kode"])
                    tpss = requests.get(urlTps).json()
                    for tps in tpss:
                        # print(prov['nama'], " > ", kota['nama'], " > ", kec["nama"], kel["nama"], tps["nama"])
                        urlTps = "https://sirekap-obj-data.kpu.go.id/pemilu/hhcw/ppwp/{}/{}/{}/{}/{}.json".format(prov["kode"], kota["kode"], kec["kode"], kel["kode"], tps["kode"])
                        dataTps = requests.get(urlTps).json()
                        if dataTps is not None and dataTps["administrasi"] is not None and dataTps["chart"] is not None:
                            # print("Saving data")
                            wilayah = {
                                "prov": prov["nama"],
                                "kota": kota["nama"],
                                "kec": kec["nama"],
                                "kel": kel["nama"],
                                "tps": tps["nama"]
                            }
                            saveData(writer,wilayah, dataTps)
                        # time.sleep(0.25)
