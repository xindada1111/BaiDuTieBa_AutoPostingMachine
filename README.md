## 百度贴吧自动发贴机源码介绍



tieba_func.py是主要的工具源码。

    1.UPGRANDE_ACCOUNT模块主要使用了python浏览器自动化技术selenium完成了模拟人进行百度贴吧的登录，贴吧浏览，贴吧关注，贴吧签到，贴吧顶贴的功能；
    2.MAKE_GUI模块主要使用了tkinter将代码制作成了GUI图形界面，方便用户使用。


## 百度自动顶贴机1.0---试用版软件使用说明


  功能：
  
    养号功能：贴吧关注，贴吧签到
    顶贴功能：贴吧顶贴（使用此功能时需要输入顶贴URL）
  选项：
  
    帖子浏览开关：
        功能描述：控制贴吧中帖子的浏览开关
        使用场景：贴吧关注，贴吧签到，贴吧顶贴
    帖子评论开关：
        功能描述：控制贴吧中帖子的评论开关
        使用场景：勾选帖子浏览后使用
    代理ip：
        功能描述：控制代理ip的开关（代理ip地址在同一目录下的代理IP.txt中），该功能没有测试手头上的免费代理ip资源不好用，建议使用此功能去网上购买代理ip
        使用场景：贴吧关注，贴吧签到，贴吧顶贴
    无头浏览器开关：
        功能描述：控制是否显示浏览器的开关，不建议启动，因为百度登陆时有时需要手动绕过图片验证码，关闭可能使程序错误
        使用场景：贴吧关注，贴吧签到，贴吧顶贴
 输入框：
 
    顶贴次数：
        功能描述：控制顶贴的次数，默认是3次
        使用场景：贴吧顶贴
    顶贴等待最小时间：
        功能描述：控制顶贴后需要等待最小的时间，单位（分钟），默认是5分钟
        使用场景：贴吧顶贴
    顶贴等待最大时间：
    功能描述：控制顶贴后需要等待最大的时间，单位（分钟），默认是15分钟
        使用场景：贴吧顶贴
    贴吧最小浏览页数：
        功能描述：控制每次打开新的贴吧最小需要浏览的页面数，默认是2页
        使用场景：贴吧关注，贴吧签到，贴吧顶贴
    贴吧最大浏览页数：
        功能描述：控制每次打开新的贴吧最大需要浏览的页面数，默认是5页
        使用场景：贴吧关注，贴吧签到，贴吧顶贴
    贴吧每页中的帖子浏览次数：
        功能描述：控制每页中帖子的浏览次数，默认是3次
        使用场景：勾选帖子浏览开关后使用

（相关文件说明）

    代理ip.txt   代理ip存放文件            格式：  http://47.56.9.58:3128   http://IP地址:端口号
    广告话术.txt    发送的广告的存放文件     格式，一行一个广告语，不宜过长
    贴吧.txt     需要攻击的相关贴吧名存放文件    格式：一行一个贴吧名
    贴吧账号.txt   百度贴吧账号存放文件   格式：用户名(空格)密码   例如：username passwd 

软件剖析：

    1.    没有实现多线程的功能，目前只能单线程使用
    2.	没有绕过百度的图片验证码
    3.	没有实现分布式爬取
    4.	代理ip功能目前只能调用本地保存的代理ip（这些代理ip是免费的代理IP质量不高），可以在网上买代理IP然后写接口连接
    5.	软件没有经过软件系统测试，可能存在小bug（但整体功能可以实现）
    6.	有些贴吧评论需要输入验证码（字符验证码），可以将验证码图片下载下来，交给打码平台识别，但这块功能没有写



