Merhaba ben DE-Şubat grubundan Furkan Beyaz."EndtoEnd_Dataflow_Project" isimli projemi açıklamak istiyorum.

1)InvokeHTTP işlemcisiyle ilgili api'ye get isteği attım.
2)SplitJson işlemcisiyle gelen veriyi "$" property'si ekleyerek splitlemiş oldum.
3)JoltTransformationJSON işlemcisiyle birçok key ve value çiftinden oluşan veriyi istediğim verileri alacak şekilde istediğim formata göre düzenledim.
4)EvaluateJSONPath işlemcisiyle  gelen verileri istediğim değişkenlere atadım.
5)RouteOnAttribute işlemcisiyle gelen verinin "name" kolonundaki veriler içinde, "Istanbul" bulunan verileri alacak şekilde koşullama sağladım. ("contains" expression language kullandım.)
6)ConvertJSONToSQL işlemcisiyle, database bağlantısı için gereken bilgileri girdim.
7)PutSQL işlemcisiyle, bilgileri girilen db'ye verileri aktarmış oldum.

Benim için çok faydalı bir projeydi, teşekkürler. 