[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,jpeg,mp3,wav
version = 0.1
requirements = python3,kivy,android
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 0
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.private_storage = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
