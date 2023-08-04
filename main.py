from flask import Flask, request, render_template
import convert_number
import validate


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/decimal')
def decimal():
    return render_template('decimal.html')


@app.route('/roman')
def roman():
    return render_template('roman.html')


@app.route('/convert-decimal', methods=['POST'])
def convert_decimal():
    decimal = request.form['decimal']
    valid = validate.validate_decimal(decimal)
    if not valid:
        return render_template('decimal.html', decimal=decimal, error='No valid number between 1 and 3999 entered')
    result = convert_number.convert_decimal(int(decimal))
    return render_template('decimal.html', decimal=decimal, result=result)


@app.route('/convert-roman', methods=['POST'])
def convert_roman():
    roman = request.form['roman']
    valid = validate.validate_roman(roman)
    if not valid:
        return render_template('roman.html', roman=roman, error='Invalid roman number')

    result = convert_number.convert_roman(roman)
    return render_template('roman.html', roman=roman, result=str(result))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
