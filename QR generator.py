import qrcode
from PIL import Image

# QR kodun içeriği
data = ""# QR kodun içeriğini buraya yaz

# QR kodu oluştur
qr = qrcode.QRCode(
    version=5,  # QR kodun detay seviyesi
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Yüksek hata toleransı
    box_size=15,
    border=0,
)
qr.add_data(data)
qr.make(fit=True)

# QR kodu oluştur ve PIL ile aç
qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")  # RGB formatına çevir

# Logoyu yükle (JPG formatında olduğu için direk açabiliriz)
logo = Image.open("logo.jpg")  # Logo dosyanı buraya koy

# Logo boyutunu ayarla
qr_width, qr_height = qr_img.size
logo_size = qr_width // 4  # Logoyu QR kodun %25 boyutuna ayarla
logo = logo.resize((logo_size, 105))

# Logoyu QR kodun ortasına yerleştir
pos = ((qr_width - logo_size) // 2, (qr_height - 105) // 2)
qr_img.paste(logo, pos)  # JPG dosyası olduğu için mask kullanmaya gerek yok

# Sonucu göster ve kaydet
qr_img.show()
qr_img.save("QR.jpg")