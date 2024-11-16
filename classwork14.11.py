from flask import Flask, request

app = Flask(__name__)

@app.route('/sum')
def sum():
    args = request.args
    try:
        number1 = float(args.get('number1', 0))
        number2 = float(args.get('number2', 0))
        total = number1 + number2
        return str(total)
    except(TypeError, ValueError):
        return 'Invalid Input'
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True, use_reloader=False)
