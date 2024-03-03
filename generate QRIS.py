import qrcode

# Fungsi untuk membuat QR kode QRIS
def generate_qris_qrcode(merchant_name, mid, output_file):
    qris_payload = (
        "00020101021126730008ID.CO.GPN.WWW01189360010232957655650303"
        + mid
        + "IDN0605Jakarta0705"
        + merchant_name
    )
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qris_payload)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

# Contoh penggunaan
merchant_name = "ARDI DIGITAL SHOP"
mid = "ID1023295765565"
output_file = "qris_qrcode1.png"

generate_qris_qrcode(merchant_name, mid, output_file)
print("QR kode QRIS telah berhasil dibuat.")
