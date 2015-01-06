my_blog
=======

基于Django的个人博客，实现了基本的发博、分页功能，需要更多功能可自行扩展。

SAE部署：http://livevilwt.me/blog/

### 初始化
`
pip install taggit
`

`
pip install bootstrap_admin_bootstrapped
`

### 自定义配置
    blog/setting.py

### 同步数据库
    python manage.py syncdb

### 运行
    python manage.py runserver
