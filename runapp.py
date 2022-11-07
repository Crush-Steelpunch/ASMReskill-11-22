from application import app
from application.route import read

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)