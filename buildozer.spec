[app]

# (str) Title of your application
title = Elyor AI

# (str) Package name
package.name = elyorai

# (str) Package domain (needed for android/ios packaging)
package.domain = com.elyor

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.2.1,urllib3

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API
android.api = 33

# (int) Minimum API support
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Accept SDK license
android.accept_sdk_license = True

# (list) Permissions
android.permissions = INTERNET

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (1 = display, 0 = hide)
warn_on_root = 1

