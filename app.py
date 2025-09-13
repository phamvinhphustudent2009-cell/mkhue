# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Thay đổi ngày kỷ niệm của bạn ở đây
# Định dạng: (năm, tháng, ngày, giờ, phút, giây)
anniversary_date = "2025-08-13T00:00:00" 

# Danh sách nhạc (tên file không bao gồm phần mở rộng .mp3)
music_list = ['ido', 'noinaycoanh', 'nguoiamphu']

@app.route('/')
def home():
    return render_template('index.html', 
                           anniversary_date=anniversary_date,
                           music_list=music_list)

if __name__ == '__main__':
    app.run(debug=True)