[app]
title = MyApp
package.name = mycustomapp
package.domain = com.yourname
source.dir = .
source.include_exts = py,png,jpg,jpeg,mp3,wav
version = 0.1
requirements = python3,kivy,android
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.private_storage = True
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET
android.archs = armeabi-v7a, arm64-v8a
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
