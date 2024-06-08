from flask import Flask
from modules.index.IndexRoute import app_index
from modules.dosen.DosenRoute import app_dosen
from modules.mahasiswa.MahasiswaRoute import app_mahasiswa
from modules.fakultas.FakultasRoute import app_fakultas
from modules.prodi.ProdiRoute import app_prodi

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Dibutuhkan untuk menggunakan flash

# registrasi blueprint untuk rute index
app.register_blueprint(app_index, url_prefix='/')

# registrasi blueprint untuk rute mahasiswa dibawah blueprint dosen
app.register_blueprint(app_mahasiswa, url_prefix='/mahasiswa')

# registrasi blueprint untuk rute mahasiswa dibawah blueprint dosen
app.register_blueprint(app_fakultas, url_prefix='/fakultas')

# registrasi blueprint untuk rute dosen
app.register_blueprint(app_dosen, url_prefix='/dosen')

# registrasi blueprint untuk rute dosen
app.register_blueprint(app_prodi, url_prefix='/prodi')

if __name__ == '__main__':
    app.run(debug=True)
