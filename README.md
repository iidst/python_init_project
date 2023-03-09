# python_init_project
一个python项目的初始化目录 *借鉴https://kgithub.com/zhayujie/chatgpt-on-wechat* 
- cmd: 某个命令或程序的入口
- common: 共用的一些程序
- config: 配置文件对应，用于加载 conf.yaml
- pkg: 一些包的引入与工厂
- logs: 存入日志的地方
- settings.py 一些配置参数
- main.py 入口文件

其 `pkg` `cmd` 下面每个文件夹代表一个模块，如示例中的pkg/ex_bot解释:
- bot.py 具体对应这个模块下面的类该实现哪个方法，类似于定义Go语言的interface
- bot_factory 工厂函数，通过传入的参数，来判断应该给予对方哪具体哪个类
- bot1 | bot2 具体类的实现，比如基于mysql或mongdb实现


` pip freeze > requirements.txt` 导入安装文件