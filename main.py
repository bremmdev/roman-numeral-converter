from flask import Flask, request, render_template, render_template_string
import convert_number
import validate
import hashlib

app = Flask(__name__)


def get_response_headers(template):
    content = render_template(template)
    etag = hashlib.sha256(content.encode('utf-8')).hexdigest()
    cache_control = 'no-cache' if (template == 'index.html' or template ==
                                   'index_roman.html') else 'public, max-age=86400'
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
    is_htmx_request = request.headers.get('Hx-Request')
    # diffentiate between htmx and normal request for different templates
    template = 'decimal.html' if is_htmx_request else 'index.html'
    etag, headers = get_response_headers(template)
    if request.headers.get('If-None-Match') == etag:
        return '', 304, headers  # Not Modified

    return render_template(template), 200, headers


@app.route('/roman')
def roman():
    is_htmx_request = request.headers.get('Hx-Request')
    # diffentiate between htmx and normal request for different templates
    template = 'roman.html' if is_htmx_request else 'index_roman.html'
    etag, headers = get_response_headers(template)
    if request.headers.get('If-None-Match') == etag:
        return '', 304, headers  # Not Modified

    return render_template(template), 200, headers


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
