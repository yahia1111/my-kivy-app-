[app]

# (str) Title of your application
title = أبو يحيى للتبريد والتكييف

# (str) Package name
package.name = aboyahiaapp

# (str) Package domain (needed for android packaging)
package.domain = com.aboyahia

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,mp3

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# تم إضافة flask, sqlite3, pyjnius, android لضمان تشغيل السيرفر الداخلي بنجاح
requirements = python3, kivy, flask, sqlite3, pyjnius, android

# (str) Custom source folders for requirements
# comma separated list of folders, directory name must be the project name
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid values are: landscape, portrait, portrait-reverse, landscape-reverse
orientation = portrait

# =============================================================================
# Android specific
# =============================================================================

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
# تم إضافة أذونات الإنترنت والاتصال الهاتفي المباشر لخدمة عملائك
android.permissions = INTERNET, CALL_PHONE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid any jnlp error or value error
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only.
android.accept_some_licenses = True

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (str) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so

# (list) Android architectures to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = armeabi-v7a, arm64-v8a

# (bool) enables Android auto backup feature (requires API >= 23)
android.allow_backup = True

# (str) The Android arch to build for (e.g. armeabi-v7a, arm64-v8a, x86)
# android.arch = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
