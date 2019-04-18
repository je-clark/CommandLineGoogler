# CommandLineGoogler

Very simple script that takes in search terms and opens a Google search in your default web browser. The really nice part of this is when you stick it in the Scripts folder within your Python installation (for me, it's C:\Python\Scripts) and associate the .py extension with python.exe. This folder is automatically added to your system's PATH variable during Python's installation, which is how pip can execute by just calling "pip".

Once this is done, all you need to do is type "google <search terms>" in any command line utility (in Windows, this works for command prompt and Powershell) and it runs the script.

One modification that may be required is to modify the PATHEXT variable in your environment variables by appending ";.PY"
