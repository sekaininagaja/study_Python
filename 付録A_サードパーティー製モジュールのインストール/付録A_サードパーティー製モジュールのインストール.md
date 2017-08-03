Appendix A. Installing Third-Party Modules
https://automatetheboringstuff.com/appendixa/


Pythonのpipツールを使用し、サードパーティのモジュールをインストールする。  

- Python Software Foundation (PyPI(Python Package Index)は、Pythonモジュールのための無料のApp Storeの一種)
  https://pypi.python.org/

※ Linux
```bash
#  pipがインストールされてい場合はインストールする。
$ sudo yum install python3-pip

# モジュールをインストールする場合
$ sudo pip3 install ModuleName

# モジュールをアップデートする場合
$ pip install –U ModuleName

# インストールしたモジュールの一覧表示
$ pip list --format=columns
```
