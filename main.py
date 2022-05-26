from flask import Response, Flask

app = Flask(__name__)

import endpoints


@app.route('/', methods=['GET'])
def home_page():
    output = """
        /vol?key={}&val={}<br>
        /mediaKey?key={}<br>
        /shut=key={}&type={}&val={}<br>
        /ping=range={}<br>
        /qrCode=type={}&val={}
        """
    return Response(output, status=418, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='192.168.0.150', port=8080)
