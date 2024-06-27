# Python_Tkinter_GUIs
Python Tkinter GUI Araçları
Bu proje, Python'un Tkinter kütüphanesini kullanarak temel GUI bileşenleri ile nasıl çalışılacağını gösteren çeşitli örnekleri içermektedir. Bu bileşenler arasında butonlar, etiketler, comboboxlar ve daha fazlası bulunmaktadır.

Özellikler
Butonlar: Kullanıcı tıklamaları ile çeşitli olayları tetiklemek için kullanılan düğmeler.
Etiketler (Labels): Kullanıcılara bilgi sunmak veya metin göstermek için kullanılan statik metin alanları.
Giriş Alanları (Entry): Kullanıcıların veri girmesi için kullanılan metin kutuları.
Comboboxlar: Kullanıcının bir dizi önceden tanımlanmış seçenek arasından seçim yapmasını sağlayan açılır menüler.
Checkbutton ve Radiobutton: Kullanıcıların bir veya birden fazla seçeneği seçmelerine olanak tanıyan düğmeler.
Listboxlar: Kullanıcıların birden fazla öğeyi görüntülemesi ve seçmesi için kullanılan listeler.
Kullanılan Bileşenler

1. Buton (Button)
Tkinter'da bir buton, kullanıcı etkileşimi için bir düğmedir.

from tkinter import Button

button = Button(master, text="Tıkla", command=buton_olayı)
button.pack()

2. Etiket (Label)
Etiketler, kullanıcıya bilgi sağlamak için kullanılır.

from tkinter import Label

label = Label(master, text="Merhaba Dünya")
label.pack()

3. Giriş Alanı (Entry)
Giriş alanları, kullanıcıların metin girmesi için kullanılır.

from tkinter import Entry

entry = Entry(master)
entry.pack()

4. Combobox
Combobox, bir dizi seçenek arasından seçim yapmayı sağlar.

from tkinter.ttk import Combobox

combobox = Combobox(master, values=["Seçenek 1", "Seçenek 2", "Seçenek 3"])
combobox.pack()

5. Checkbutton
Birden fazla seçeneği seçmek için kullanılır.

from tkinter import Checkbutton

checkbutton = Checkbutton(master, text="Seçenek")
checkbutton.pack()

6. Radiobutton
Tek bir seçenek seçmek için kullanılır.

from tkinter import Radiobutton

radiobutton = Radiobutton(master, text="Seçenek", value=1)
radiobutton.pack()

7. Listbox
Birden fazla öğeyi listelemek ve seçmek için kullanılır.

from tkinter import Listbox

listbox = Listbox(master)
listbox.pack()

# Kurulum
Bu projeyi çalıştırmak için aşağıdaki adımları takip edin:

Python'u İndirin ve Kurun: Proje Python 3 gerektirir. Python web sitesinden en son sürümü indirin ve kurun.

Proje Dosyalarını İndirin: Bu projeyi kendi bilgisayarınıza klonlayın veya indirin.

git clone https://github.com/kullanici_adiniz/tkinter-gui-ornekleri.git

Gerekli Kütüphaneleri Kurun: Gerekli Python kütüphanelerini kurmak için aşağıdaki komutu çalıştırın:
pip install tk

Kullanım
Ana Python Dosyasını Çalıştırın: main.py dosyasını çalıştırarak GUI uygulamasını başlatın.
python main.py
Arayüzde Gezin: Uygulama açıldığında, farklı bileşenleri tıklayarak veya etkileşimde bulunarak özelliklerini keşfedin.

Örnekler
Aşağıda, projede yer alan örnek dosyaların kısa açıklamaları bulunmaktadır:

button_example.py: Tkinter buton bileşeninin nasıl kullanıldığını gösterir.
label_example.py: Etiketler ile metinlerin nasıl gösterileceğini açıklar.
combobox_example.py: Combobox kullanarak açılır menülerin nasıl oluşturulacağını gösterir.
entry_example.py: Kullanıcı girdisi almak için giriş alanlarının nasıl kullanılacağını gösterir.
checkbutton_example.py: Çoklu seçim yapma imkanı sunan checkbutton bileşeninin örneğini içerir.
radiobutton_example.py: Tekli seçim yapmayı sağlayan radiobutton bileşeninin kullanımını gösterir.
listbox_example.py: Listbox ile birden fazla öğeyi listeleme ve seçme işlemlerini açıklar.
Katkıda Bulunma
Katkıda bulunmak isterseniz aşağıdaki adımları takip edebilirsiniz:

1.Bu projeyi fork edin.
2.Kendi dalınızı (feature/harika-ozellik) oluşturun.
3.Yaptığınız değişiklikleri dalınıza (git checkout -b feature/harika-ozellik) ekleyin.
4.Değişikliklerinizi commitleyin (git commit -m 'Harika bir özellik ekledim').
5.Dalınıza pushlayın (git push origin feature/harika-ozellik).
6.Bir Pull Request oluşturun.
