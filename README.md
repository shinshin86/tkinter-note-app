# tkinter-note-app

This is a GUI notebook application for tkinter created for learning.

## Screenshot

![Screenshot](./demo/screenshot.png)

## Python version etc...

```sh
python --version
# => Python 3.10.1

python -c "import tkinter;print(tkinter.TkVersion)"
# => 8.6
```

## Start GUI App

```sh
python main.py
```

## Build the executable file

Create an executable file using cx_Freeze.

### Mac

```sh
python setup.py bdist_mac
```

### Windows

```sh
python setup.py bdist_msi
```

## Licence

[MIT](https://github.com/shinshin86/tkinter-note-app/blob/main/LICENSE)

## Author

[Yuki Shindo](https://shinshin86.com/en)