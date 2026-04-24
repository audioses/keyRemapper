\# Key Remapper



\* Yazar: Ömer Yılmaz

\* Sürüm: 1.0.0

\* Minimum NVDA sürümü: 2023.1

\* Son test edilen NVDA sürümü: 2025.2

\* Lisans: GPL v2 veya sonrası

\* Kaynak: \[https://github.com/audioses/keyRemapper](https://github.com/audioses/keyRemapper)



\## Genel Bakış



Key Remapper, herhangi bir klavye tuşunu (veya tuş kombinasyonunu) başka bir tuşa eşlemenizi sağlayan bir NVDA eklentisidir. Özellikle fiziksel klavyenizde bazı tuşlar eksikse — örneğin fonksiyon tuşları, yön tuşları, `Insert`, `Applications`, sayısal tuş takımı (numpad) veya medya kontrolleri bulunmayan kompakt dizüstü klavye düzenlerinde — oldukça kullanışlıdır. Çünkü sahip olduğunuz bir tuşa, sahip olmadığınız bir tuşun işlevini atamanıza imkan verir.



Eşlemeler NVDA’nın yapılandırmasına kaydedilir ve bir sonraki başlatmada otomatik olarak geri yüklenir.



\## Komutlar



Eklenti iki komut sunar. Her ikisi de NVDA’nın \*\*Giriş Hareketleri\*\* iletişim kutusunda, \*\*Key Remapper\*\* kategorisi altında bulunur. Varsayılan kısayollar sisteminizde çakışıyorsa, buradan yeniden atayabilirsiniz.



\### Eşleme oluştur — `NVDA+Shift+X`



Eşleme modunu başlatır. Kısa bir bip sesi, eklentinin giriş beklediğini doğrular.



\* \*\*Tek basış (`NVDA+Shift+X`)\*\* — yeniden eşlemek istediğiniz kaynak tuşa basın, ardından üretmesini istediğiniz hedef tuşa basın. Daha yüksek bir bip sesi ve sesli onay, eşlemenin kaydedildiğini bildirir.

\* \*\*Çift basış (`NVDA+Shift+X` hızlıca iki kez)\*\* — önce kaynak tuşa basın, ardından hedefi arama yapılabilir bir iletişim kutusundan seçin. Hedef tuş fiziksel olarak klavyenizde yoksa bu yöntemi kullanın (zaten çoğu zaman eşlemenin amacı budur).



Kaynak ve hedef tuşlar değiştirici (modifier) içerebilir. Örneğin `F13` → `Alt+F4` veya `Caps Lock` → `Insert` şeklinde eşleme yapabilirsiniz.



\### Eşleme çalıştır — `NVDA+X`



Daha önce oluşturulmuş bir eşlemeyi tetikler.



\* \*\*Tek basış (`NVDA+X`)\*\* — kaynak tuşa basın; eklenti eşlenen hedef tuşu aktif uygulamaya gönderir.

\* \*\*Çift basış (`NVDA+X` hızlıca iki kez)\*\* — eklentinin bildiği tüm tuşları listeleyen bir iletişim kutusu açılır; böylece eşleme kullanmadan doğrudan bir tuş gönderebilirsiniz.



Eğer eşlemesi olmayan bir tuşa basarsanız, düşük bir hata bip sesi duyulur ve NVDA “Eşleme bulunamadı” der.



\## Tuş seçim iletişim kutusunun kullanımı



Çift basışta (her iki komut için de) açılan iletişim kutusu, tuşları kategorilere ayrılmış şekilde gösterir — Navigation, System, Function keys, Numpad, Media, Browser, Launch ve `Alt`, `Control`, `Windows` kombinasyon grupları. Kategori başlıkları seçilebilir değildir; yalnızca gezinmenize yardımcı olur.



\* \*\*Filtre alanı\*\* — listeyi daraltmak için bir tuş adının herhangi bir kısmını yazın (örneğin `f1` yazarsanız `f1` ile `f19` arası, `alt` yazarsanız tüm Alt kombinasyonları görünür). Filtre alanındayken `Aşağı Ok` tuşuna basarak doğrudan sonuç listesine geçebilirsiniz.

\* \*\*Tuş listesi\*\* — `Yukarı` / `Aşağı` ok tuşlarıyla gezinip `Enter` tuşuna basın veya \*\*Seç\*\* düğmesini etkinleştirin.

\* \*\*İptal\*\* — hiçbir şey seçmeden iletişim kutusunu kapatır.



\## Tipik kullanım senaryoları



\### `F13` tuşu olmayan kompakt dizüstü



1\. `NVDA+Shift+X` tuşlarına hızlıca iki kez basın.

2\. Feda etmek istediğiniz fiziksel tuşa basın (örneğin `ScrollLock`).

3\. İletişim kutusunda `f13` yazıp filtreleyin, seçin ve Enter’a basın.

4\. Bundan sonra `NVDA+X` ardından `ScrollLock` basarak `F13` gönderebilirsiniz.



\### Numpad’i olmayan dizüstü



Normal tuşların bir sırasını (örneğin `1`–`9`) `numpad1`–`numpad9` olarak eşleyin. Bunun için tek basış yöntemini kullanın: `NVDA+Shift+X` → kaynak tuş → hedef tuş.



\### `Insert` veya `Applications` tuşu olmayan klavye



İletişim kutusu yöntemini (`NVDA+Shift+X` iki kez) kullanarak \*\*Navigation\*\* kategorisinden `insert` veya `applications` seçin.



\## Notlar ve sınırlamalar



\* `NVDA+Shift+X` ve `NVDA+X` tuşları kaynak olarak kullanılamaz — eklenti kendi kısayollarını korur, böylece kendinizi kilitlemezsiniz.

\* Tek başına basılan değiştirici tuşlar (`Shift`, `Control`, `Alt`) yok sayılır; eklenti gerçek bir tuş bekler. Kombinasyon yakalamak için değiştiriciyi başka bir tuşla birlikte basın.

\* Hedef tuş, odaktaki uygulamaya simüle edilmiş tuş vuruşu olarak gönderilir. Donanım seviyesinde tuş olaylarını değiştirmez; yalnızca `NVDA+X` ile tetiklendiğinde çeviri yapar.

\* Eşlemeler geneldir — tüm uygulamalarda aynıdır.

\* Tüm mesajlar ve tuş seçim iletişim kutusu, NVDA’nın standart gettext çeviri sistemiyle tamamen çevrilebilir.



\## Depolama



Eşlemeler, NVDA yapılandırma dosyasında JSON olarak saklanır (`keyRemapper` bölümü, `mappings` anahtarı altında). Bu girdiyi silmek (veya NVDA yapılandırmasını sıfırlamak) tüm eşlemeleri temizler.



\## Değişiklik Günlüğü



\### 1.0



\* İlk sürüm.

\* Tuşları tuş basımıyla veya iletişim kutusundan seçerek eşleme.

\* Eşlemeleri tuş basımıyla çalıştırma veya doğrudan gönderilecek tuş seçimi.

\* Aranabilir, kategorilere ayrılmış tuş seçim iletişim kutusu.

\* Tam çeviri desteği.



