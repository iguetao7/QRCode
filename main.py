import qrcode
from qrcode.image.pure import PyPNGImage


#QRCode convencional
#link para o redirecionamento
imagem = qrcode.make('SEU LINK')

#salvando a imagem
imagem.save('qrcode.png')


#QRCode editavel
#Ajustando tamanho e erros
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

#Link de redirecionamento
qr.add_data('SEU LINK')
qr.make(fit=True)

#Cores do qrcode
img = qr.make_image(fill_color="black", back_color=(244, 236, 230))

#Salvando imagem
img.save('qrcode1.png')
