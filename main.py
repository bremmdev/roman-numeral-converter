from flask import Flask, request, render_template, render_template_string
import convert_number
import validate
import hashlib

app = Flask(__name__)


def get_response_headers(template):
    content = render_template(template)
    etag = hashlib.sha256(content.encode('utf-8')).hexdigest()
    cache_control = 'no-cache' if template == 'index.html' else 'public, max-age=86400'
    headers = {'cache-control': cache_control, 'Etag': etag}
    return etag, headers


@app.route('/')
def index():
    etag, headers = get_response_headers('index.html')
    if request.headers.get('If-None-Match') == etag:
        return '', 304, headers  # Not Modified
    return render_template('index.html'), 200, headers


@app.route('/decimal')
def decimal():
    etag, headers = get_response_headers('decimal.html')
    if request.headers.get('If-None-Match') == etag:
        return '', 304, headers  # Not Modified
    return render_template('decimal.html'), 200, headers


@app.route('/roman')
def roman():
    etag, headers = get_response_headers('roman.html')
    if request.headers.get('If-None-Match') == etag:
        return '', 304, headers  # Not Modified
    return render_template('roman.html'), 200, headers


@app.route('/convert-decimal', methods=['POST'])
def convert_decimal():
    decimal = request.form['decimal']
    valid = validate.validate_decimal(decimal)

    if not valid:
        return render_template_string("<span class='error'>Invalid number</span>")
    result = convert_number.convert_decimal(int(decimal))
    return render_template_string("<span>{{ decimal }} to roman is {{ result }}</span>", decimal=decimal, result=result)


@app.route('/convert-roman', methods=['POST'])
def convert_roman():
    roman = request.form['roman']
    valid = validate.validate_roman(roman)
    if not valid:
        return render_template_string("<span class='error'>Invalid number</span>")

    result = convert_number.convert_roman(roman)
    return render_template_string("<span>{{ roman }} to decimal is {{ result }}</span>", roman=roman, result=result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
