[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,jpeg,mp3,wav
version = 0.1
requirements = python3,kivy,android
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.ndk = 25b
android.private_storage = True
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET
android.archs = armeabi-v7a, arm64-v8a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
