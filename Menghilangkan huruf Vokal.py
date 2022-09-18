Teks = input("\n masukkan kata yang anda inginkan: ").strip()
pengganti = ""
for huruf in 'aiueoAIUEO' :
    Teks = Teks.replace(huruf,pengganti)
print(Teks)