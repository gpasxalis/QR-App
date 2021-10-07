from flask import Blueprint, render_template, request, url_for, send_file
import qrcode, os, sys, io, uuid, base64
import flask 


qr_main = Blueprint('qr_main',__name__)


def random_qr(text):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=12,
                       border=2)

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    return img


@qr_main.route('/')
def index_page():
	return render_template("index_page.html")

@qr_main.route('/result', methods = ["POST", "GET"])
def result():
	global text_input
	text_input = request.values.get('text_input')
	if text_input == None:
		return render_template("index_page.html")
	temp_data = io.BytesIO()
	
	img = random_qr(text_input)

	img.save(temp_data, "PNG")
	endoded_img_data = base64.b64encode(temp_data.getvalue())
	
	return render_template("result_page.html", img = endoded_img_data.decode('utf-8'))

@qr_main.route('/download', methods = ["POST", "GET"])	
def download():
	global text_input
	randomUUID = uuid.uuid1()
	path = f"myapp/static/images/{randomUUID}.png"
	
	dl_temp = io.BytesIO()
	img = random_qr(text_input)

	img.save(path)
	
	with open(path, 'rb') as png:
		dl_temp.write(png.read())
	
	dl_temp.seek(0)
	os.remove(path)
	
	return send_file(dl_temp, as_attachment=True, attachment_filename=f'{randomUUID}.png')
	
