import os
import sqlite3
import threading
import time
from datetime import datetime, timedelta
from flask import Flask, render_template_string, request, redirect, send_file

# إعدادات واجهة Kivy والوقت للأندرويد
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

# استدعاء محرك الويب وأدوات التنبيهات وصلاحيات الأندرويد الرسمية
try:
    from jnius import autoclass
    from android.runnable import run_on_ui_thread
    from android.permissions import request_permissions, Permission
    
    AndroidWebView = autoclass('android.webkit.WebView')
    AndroidWebViewClient = autoclass('android.webkit.WebViewClient')
    Activity = autoclass('org.kivy.android.PythonActivity').mActivity
    
    # تحديد المسار الداخلي الآمن للأندرويد لحل مشكلة قراءة البيانات والصوت
    BASE_DIR = Activity.getFilesDir().getAbsolutePath()
    
    Context = autoclass('android.content.Context')
    NotificationBuilder = autoclass('android.app.Notification$Builder')
    NotificationManager = autoclass('android.app.NotificationManager')
    NotificationChannel = autoclass('android.app.NotificationChannel')
except ImportError:
    run_on_ui_thread = lambda x: x
    AndroidWebView = None
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    request_permissions = lambda x: None
    Permission = None

app = Flask(__name__)

# دمج المسارات داخل المجلد الآمن المسموح للتطبيق بالكتابة والقراءة منه
DB_FILE = os.path.join(BASE_DIR, "maintenance_pro.db")
AUDIO_FILE = os.path.join(BASE_DIR, "sound.mp3")

# نسخ ملف الصوت برمجياً للمجلد الآمن إذا كان متواجداً في مجلد التثبيت الرئيسي
if not os.path.exists(AUDIO_FILE) and os.path.exists("sound.mp3"):
    try:
        import shutil
        shutil.copy("sound.mp3", AUDIO_FILE)
    except:
        pass

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, phone TEXT, address TEXT, date_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# دالة إرسال التنبيهات الرسمية لشاشة الأندرويد
def send_android_notification(title, message):
    if not AndroidWebView:
        print(f"🖥️ تنبيه على الكمبيوتر: {title} - {message}")
        return
    try:
        notif_manager = Activity.getSystemService(Context.NOTIFICATION_SERVICE)
        channel_id = "yh_maintenance_channels"
        
        channel = NotificationChannel(channel_id, "مواعيد الصيانة", NotificationManager.IMPORTANCE_HIGH)
        notif_manager.createNotificationChannel(channel)
        
        builder = NotificationBuilder(Activity, channel_id)
        builder.setContentTitle(title)
        builder.setContentText(message)
        builder.setSmallIcon(Activity.getApplicationInfo().icon)
        builder.setAutoCancel(True)
        
        notif_manager.notify(int(time.time()), builder.build())
    except Exception as e:
        print(f"خطأ في إرسال التنبيه: {e}")

# خيط فحص المواعيد تلقائياً في الخلفية كل دقيقة
def check_appointments_worker():
    while True:
        try:
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT name, address FROM appointments WHERE date_time = ?", (now_str,))
            matches = cursor.fetchall()
            conn.close()
            
            for match in matches:
                send_android_notification(
                    f"⏰ بعد إذنك يا أبو يحيى: ميعاد صيانة", 
                    f"الزبون: {match[0]} | 📍 العنوان: {match[1]} - توكل على الله!"
                )
        except Exception as e:
            print(e)
        time.sleep(60)

# واجهة لوحة التحكم الاحترافية
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>أبو يحيى للتبريد والتكييف</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, sans-serif; background-color: #f1f5f9; margin: 0; padding: 0; color: #0f172a; }
        .marquee-container { background-color: #1e3a8a; color: white; padding: 10px; font-weight: bold; font-size: 16px; }
        .container { max-width: 600px; margin: 20px auto; padding: 15px; }
        .header { background-color: #1e3a8a; padding: 20px; border-radius: 12px; text-align: center; color: white; margin-bottom: 25px; }
        .header h1 { margin: 0; font-size: 24px; }
        .header p { margin: 5px 0 0 0; color: #93c5fd; font-weight: bold; }
        .form-card { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 25px; }
        .form-card h3 { margin-top: 0; color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }
        .form-group { margin-bottom: 15px; text-align: right; }
        .form-group label { display: block; font-weight: bold; margin-bottom: 5px; color: #334155; }
        .form-group input { width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 8px; box-sizing: border-box; font-size: 15px; font-weight: bold; text-align: right; }
        .btn-submit { background-color: #2563eb; color: white; border: none; width: 100%; padding: 12px; border-radius: 8px; font-size: 16px; font-weight: bold; cursor: pointer; }
        .appt-card { background-color: white; padding: 15px; border-radius: 12px; margin-bottom: 15px; border-right: 6px solid #2563eb; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        .appt-card h4 { margin: 0; color: #1e3a8a; font-size: 18px; }
        .appt-card p { margin: 6px 0; color: #475569; font-size: 14px; }
        .appt-card .time { color: #dc2626; font-weight: bold; }
        .btn-container { display: flex; gap: 8px; margin-top: 10px; flex-wrap: wrap; }
        .btn { flex: 1; min-width: 100px; padding: 8px; border: none; border-radius: 6px; font-weight: bold; text-align: center; text-decoration: none; color: white; font-size: 13px; cursor: pointer; }
        .btn-call { background-color: #10b981; }
        .btn-map { background-color: #3b82f6; }
        .btn-snooze { background-color: #f59e0b; }
        .btn-del { background-color: #ef4444; }
    </style>
</head>
<body>

    {% if audio_exists %}
    <audio autoplay loop style="display:none;"><source src="/get_audio" type="audio/mpeg"></audio>
    {% endif %}

    <div class="marquee-container">
        <marquee direction="right" scrollamount="5">
            ❄️ أبو يحيى للتبريد والتكييف .. صيانة وتركيب بأعلى جودة وضمان 🛠️
        </marquee>
    </div>

    <div class="container">
        <div class="header">
            <h1>🛠️ لوحة تحكم البشمهندس يحيى 🛠️</h1>
            <p>نظام إدارة وصيانة عملاء التبريد والتكييف الذكي</p>
        </div>

        <div class="form-card">
            <h3>📝 سجل حجز جديد هنا</h3>
            <form action="/add" method="POST">
                <div class="form-group"><label>اسم الزبون كاملاً</label><input type="text" name="name" required></div>
                <div class="form-group"><label>رقم تليفونه للتواصل</label><input type="text" name="phone" required></div>
                <div class="form-group"><label>عنوانه فين بالظبط؟</label><input type="text" name="address" required></div>
                <div class="form-group"><label>الميعاد بالتفصيل</label><input type="text" name="date_time" placeholder="مثال: 2026-05-25 14:30" required></div>
                <button type="submit" class="btn-submit">🚀 احفظ الميعاد وجدول الشغل</button>
            </form>
        </div>

        <h3 style="text-align: right; color: #475569;">📋 قائمة المواعيد والعملاء الحالية</h3>
        
        {% if not rows %}
            <p style="text-align: center; color: #64748b;">مفيش أي مواعيد صيانة متسجلة دلوقتي، جدولك رايق!</p>
        {% else %}
            {% for row in rows %}
            <div class="appt-card">
                <h4>👤 : {{ row[1] }}</h4>
                <p><b>📞 تليفون:</b> {{ row[2] }} &nbsp;|&nbsp; <b>📍 عنوان:</b> {{ row[3] }}</p>
                <p class="time"><b>⏰ ميعاد الزيارة:</b> {{ row[4] }}</p>
                
                <div class="btn-container">
                    <a href="tel:{{ row[2] }}" class="btn btn-call">📞 اتصل</a>
                    <a href="https://google.com{{ row[3] }}" target="_blank" class="btn btn-map">📍 مكان الخريطة</a>
                    <a href="/snooze/{{ row[0] }}" class="btn btn-snooze">⏳ تأجيل ربع ساعة</a>
                    <a href="/delete/{{ row[0] }}" class="btn btn-del">❌ مسح الموعد</a>
                </div>
            </div>
            {% endfor %}
        {% endif %}
    </div>

</body>
</html>
'''

@app.route('/')
def index():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone, address, date_time FROM appointments ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    audio_exists = os.path.exists(AUDIO_FILE)
    return render_template_string(HTML_TEMPLATE, rows=rows, audio_exists=audio_exists)

@app.route('/get_audio')
def get_audio():
    if os.path.exists(AUDIO_FILE): return send_file(AUDIO_FILE, mimetype="audio/mpeg")
    return "No audio file", 404

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    phone = request.form['phone']
    address = request.form['address']
    date_time = request.form['date_time']
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO appointments (name, phone, address, date_time) VALUES (?, ?, ?, ?)', (name, phone, address, date_time))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/snooze/<int:appt_id>')
def snooze(appt_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT date_time FROM appointments WHERE id = ?", (appt_id,))
    row = cursor.fetchone()
    if row:
        try:
