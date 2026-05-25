[app]
title = أبو يحيى للتبريد والتكييف
package.name = aboyahiaapp
package.domain = com.aboyahia
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3
version = 1.0.0
requirements = python3, kivy, flask, sqlite3, pyjnius, android
orientation = portrait

[checkboxes]
fullscreen = 1

# حقن كافة الصلاحيات (الإنترنت، الاتصال، الإشعارات، الصور، الكاميرا، الصوت، والموقع)
android.permissions = INTERNET, CALL_PHONE, POST_NOTIFICATIONS, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, RECORD_AUDIO, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION

android.api = 31
android.minapi = 21
android.ndk = 25b
android.skip_update = False
android.accept_some_licenses = True
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
