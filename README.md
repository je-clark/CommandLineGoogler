# Command Line Utilities

This is a collection of Python-based command line utilities. Installation guidelines are below:

When you stick it in the Scripts folder within your Python installation (for me, it's C:\Python\Scripts) and associate the .py extension with python.exe. This folder is automatically added to your system's PATH variable during Python's installation, which is how pip can execute by just calling "pip".

Once this is done, all you need to do is type "google <search terms>" in any command line utility (in Windows, this works for command prompt and Powershell) and it runs the script.

One modification that may be required is to modify the PATHEXT variable in your environment variables by appending ";.PY"
