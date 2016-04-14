
### 开始
```shell
  virtualenv .
  Scripts\activate
  pip install flask
  python runproxy.py
```


### 当后面更新了包以后需要更新require 文件

``` shell
  pip freeze > requirements.txt
```