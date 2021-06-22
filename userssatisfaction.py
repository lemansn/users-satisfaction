sonraki_kullanici = 'e'
say = 0                 #toplam kullanıcı sayısı
ios = 0                 #IOS kullanıcı sayısı
android = 0             #ANDROİD kulanıcı sayısı
memnun_ios = 0          #İOS kullanıcılarının memnuniyet düzeyi
memnun_android = 0      #ANDROİD kullanıcılarının memnuniyet düzeyi
memnun_olm_sure = 0     #memnun olmayan kullanıcıların uygulamayı kullanma süresi
memnuniyet1 = 0         #memnun olmayan kullanıcıların sayısı
memnuniyet2 = 0         #ne memnun ne memnun değil olan kullanıcıların sayısı
memnuniyet3 = 0         #memnun olan kullanıcıların sayısı
biryildan_fazla_sure= 0 #1 yıldan daha uzun kullanılan toplam süre
bir_yildan_cok = 0      #1 yıldan daha uzun kullanan kullanıcı sayısı
bir_aydan_az = 0        #kullanım süresi dolmadan silen kullanıcıların sayı
toplam_mem_1yil = 0     #1 yıldan daha uzun süre kullanan kullanıcıların toplam memnuniyet düzeyi
toplam = 0              #genel mmemnuniyet düzeyi

while sonraki_kullanici != 'h':
    sistem_turu = input('Kullanıcının cihazındaki işletim sistemini giriniz (i: ios, a: android): ')
    kullanilan_sure= int(input('Kullanıcının uygulamayı kullandığı süreyi giriniz (ay sayısı): '))
    memnuniyet_duzeyi = input('Kullanıcının uygulamadan memnuniyet düzeyini giriniz (1: memnun değil, 2: ne memnun ne memnun değil, 3: memnun): ')
    sonraki_kullanici = input('Başka kullanıcı var mı? (e/h): ')

    if sistem_turu == 'i':
        ios += 1
        memnun_ios += int(memnuniyet_duzeyi)
    else:
        android += 1
        memnun_android += int(memnuniyet_duzeyi)

    if memnuniyet_duzeyi == '1':
        memnuniyet1 += 1
        memnun_olm_sure += kullanilan_sure

    elif memnuniyet_duzeyi == '2':
        memnuniyet2 += 1
    else:
        memnuniyet3 += 1

    if kullanilan_sure > 12:
        bir_yildan_cok += 1
        biryildan_fazla_sure += kullanilan_sure
        toplam_mem_1yil += int(memnuniyet_duzeyi)

    elif kullanilan_sure < 1:
        bir_aydan_az += 1

    say += 1

toplam = memnun_ios + memnun_android

print('Uygulamadan memnun olan kullanıcıların sayısı:', memnuniyet3, f"ve yüzdesi: %{format(((memnuniyet3 / say) * 100), '.2f')}")

print('Uygulamadan ne memnun ne memnun değil olan kullanıcıların sayısı:', memnuniyet2, f"ve yüzdesi: %{format(((memnuniyet2 / say) * 100), '.2f')}")

print('Uygulamadan memnun olmayan kullanıcıların sayısı:', memnuniyet1, f"ve yüzdesi: %{format(((memnuniyet1 / say) * 100), '.2f')}")

print(f"IOS kullanıcılarının oranı: %{format(((ios / say) * 100), '.2f')} ",'ve memnuniyet düzeyi ortalaması:', round((memnun_ios/ios),2))

print(f"Android kullanıcılarının oranı: %{format(((android / say) * 100), '.2f')}",'ve memnuniyet düzeyi ortalaması:', round(( memnun_android/android),2))

print('Uygulamanın genel memnuniyet düzeyi ortalaması:', round((toplam/say),2))

print('Uygulamayı 1 yıldan daha uzun süre kullanan kullanıcıların sayısı:', f'{bir_yildan_cok},',
      'kullandıkları ortalama süre:',round((biryildan_fazla_sure/bir_yildan_cok),2),"ay",
      've memnuniyet düzeyi ortalaması:',round((toplam_mem_1yil/bir_yildan_cok),2))

print('Uygulamadan memnun olmayan kullanıcıların uygulamayı kullandıkları ortalama süre:',round(( memnun_olm_sure/memnuniyet1),2),'ay')

print( f"Uygulamanın ücretsiz kullanım süresi dolmadan silen kullanıcıların tüm kullanıcılar içindeki oranı: %{format(((bir_aydan_az / say) * 100), '.2f')}")
