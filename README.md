# Object Oriented Programming in Python 🐍

Bu repo, Python'da **Nesne Yönelimli Programlama (OOP)** temel kavramlarını ve örnek uygulamalarını içerir.

---

## İçerik ve Dosya Yapısı

## 1. `Class car.py` - Temel Sınıf (Class) ve Nesne Yapısı
* **Açıklama:** Sınıf tanımlama, `__init__` yapıcı metodu (constructor), nesne örnekleme (instantiation) ve durum yönetimi.
* **Öne Çıkan Kavramlar:** `self` kullanımı, durum değişkenleri (`speed`, `Car_is_moving`), metotlar ve `time.sleep` ile canlı simülasyon.

---

## 2. `Super() #1.py` - Kalıtım (Inheritance) ve `super()`
* **Açıklama:** Üst sınıftan (parent class) alt sınıflara (child class) özellik aktarımı ve metot genişletme.
* **Öne Çıkan Kavramlar:** `Shape` ana sınıfından türeyen `Circle`, `Square` ve `Triangle` sınıfları. `super().__init__()` ile kod tekrarını önleme ve `super().describe()` ile metot ezme (override).
* **Override:** 'Shape' ana sınıfında yazılan fonksiyonun 'Child' bir classda tekrar definition yapıldığında child kodun yapısını algılıyor. Child-to-parent mantığına dayanmaktadır.

---

### 3. `Abstract method.py` - Soyutlama (Abstraction)
* **Açıklama:** `abc` modülü kullanarak soyut sınıflar (Abstract Base Class) ve soyut metotlar (`@abstractmethod`) tanımlama.
* **Öne Çıkan Kavramlar:** Alt sınıfların uygulamak zorunda olduğu şablon yapılar oluşturma ve arayüz (interface) tasarımı.

---

##  Nasıl Çalıştırılır?

Projeyi bilgisayarınıza klonlayıp herhangi bir Python dosyasını çalıştırabilirsiniz:

```bash
git clone [https://github.com/hamzaseriat/Object_Orianted_Programming-In-Python.git](https://github.com/hamzaseriat/Object_Orianted_Programming-In-Python.git)
cd Object_Orianted_Programming-In-Python
python "Super() #1.py"
