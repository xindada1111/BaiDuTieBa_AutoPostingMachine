#coding:utf-8
#!/usr/bin/env python3
# @xindada
import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter import messagebox
import random
import os
from selenium.webdriver import ActionChains
import time
from selenium import webdriver
from lxml import etree



class UPGRANDE_ACCOUNT(object):
    '''
    百度账号升级,顶贴
    '''
    def __init__(self,tieba_name='',username="hemakeji4",password="hema6666",open_tieba_detail_liulan=False,open_send_tieba_name=True,min_page_num=2,max_page_num=5,proxy_server=None,open_set_headless=False,open_tieba_detail_liulan_num=3,open_post_bor_comments=False,content='', tieba_automatic_tipping_machine_url=None, tieba_automatic_tipping_machine_sendtimes=1, tieba_automatic_tipping_machine_min_waiting_time=1, tieba_automatic_tipping_machine_max_waiting_time=1):
        self.tieba_name=tieba_name
        self.driver=None
        self.username=username  #登陆用户名
        self.password=password  #登陆密码
        self.open_tieba_detail_liulan=open_tieba_detail_liulan    #控制是否打开贴吧中的帖子并浏览
        self.open_send_tieba_name=open_send_tieba_name   #控制是否打开tieba_liulan()中的输入贴吧名，仅用于测试时使用
        self.min_page_num=min_page_num   #浏览贴吧的最小页数
        self.max_page_num=max_page_num   #浏览贴吧的最大页数
        self.proxy_server=proxy_server   #代理服务器,默认为空
        self.open_set_headless=open_set_headless  #控制打开无头浏览器开关，默认关闭
        self.open_tieba_detail_liulan_num=open_tieba_detail_liulan_num  #贴吧中每一页的帖子浏览次数
        self.open_post_bor_comments=open_post_bor_comments   #控制帖子回复开关，默认关闭
        self.content=content  #帖子回复和顶贴的文本
        #顶贴函数使用参数
        self.tieba_automatic_tipping_machine_url=tieba_automatic_tipping_machine_url    #需要顶的帖子URL
        self.tieba_automatic_tipping_machine_sendtimes = tieba_automatic_tipping_machine_sendtimes  #顶贴的次数
        self.tieba_automatic_tipping_machine_min_waiting_time = tieba_automatic_tipping_machine_min_waiting_time   #顶贴等待最小时间，单位（分钟）
        self.tieba_automatic_tipping_machine_max_waiting_time=tieba_automatic_tipping_machine_max_waiting_time     #顶贴等待最大时间，单位（分钟）
    def tieba_login(self):
        '''
        自动登录4.0版本
        param username:
        param password:
        :return: driver  webdriver.Chrome()对象
        '''

        opt = webdriver.ChromeOptions()
        if self.open_set_headless:
            opt.add_argument('--headless')   #设置无头浏览器
        if self.proxy_server:
            opt.add_argument("–proxy-server={}".format(self.proxy_server))  # 设置代理ip
        filename=os.getcwd()+'\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=filename, options=opt)
        # 登录贴吧首页
        self.driver.implicitly_wait(20)  # 隐式等待
        self.driver.set_window_size(1000, 800)  # 设置浏览器长1000像素，宽800像素
        login_url = 'https://tieba.baidu.com/'
        self.driver.get(login_url)
        # 模拟人类行为改变浏览器大小
        time.sleep(random.randint(1, 5))  # 随机睡眠1-5秒
        self.driver.set_window_size(1920, 1080)
        time.sleep(random.randint(1, 5))
        self.driver.find_element_by_xpath('/html/body/div[1]/ul/li[4]/div/a').click()  # 点击登录用户的按钮，等待弹出登录框
        # selenium执行时并不会自动切换到新开的页签或者窗口上，还会停留在之前的窗口中，所以两次打印的句柄都一样。新开窗口后必须通过脚本来进行句柄切换，才能正确操作相应窗口中的元素
        time.sleep(random.randint(3, 5))
        search_window = self.driver.current_window_handle  # 获取当前窗口句柄集合
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()  # 点击账号登陆
        time.sleep(random.randint(3, 5))
        getUserPhoneDom = self.driver.find_element_by_id('TANGRAM__PSP_11__userName')  # 输入用户名
        getUserPassDom = self.driver.find_element_by_id('TANGRAM__PSP_11__password')  # 输入密码
        # 模拟人类输入用户名和密码
        for i in self.username:
            getUserPhoneDom.send_keys(i)
            time.sleep(random.uniform(0, 2))
        time.sleep(random.randint(1, 3))
        for j in self.password:
            getUserPassDom.send_keys(j)
            time.sleep(random.uniform(0, 2))

        time.sleep(random.randint(1, 3))
        action = ActionChains(self.driver)
        loginDom = self.driver.find_element_by_id('TANGRAM__PSP_11__submit')
        action.move_to_element(loginDom).click().perform()
        time.sleep(random.randint(1, 5))
        try:
            search_window = self.driver.current_window_handle
            errorData = self.driver.find_element_by_xpath('//p[@class="mod-page-tipInfo-gray2"]').text
            if errorData == "拖动滑块，使图片角度为正":
                time.sleep(10)
        except Exception as e:
            print(e)

    def tieba_automatic_tipping_machine(self):
        '''
        百度自动顶帖机
        :param url:        帖子链接
        :param sendtimes: 发送次数
        :param min_waiting_time: 随机最小等待时间
        :param max_waiting_time: 随机最大等待时间
        :return:
        '''

        try:
            for cc in range(self.tieba_automatic_tipping_machine_sendtimes):  # 设置循环次数
                if self.tieba_automatic_tipping_machine_sendtimes!=1 and self.tieba_automatic_tipping_machine_min_waiting_time!=1 and self.tieba_automatic_tipping_machine_max_waiting_time!=1:
                    self.tieba_liulan()
                time.sleep(random.randint(1, 5))
                self.driver.get(self.tieba_automatic_tipping_machine_url)
                search_window = self.driver.current_window_handle  # 获取当前窗口句柄集合
                time.sleep(random.randint(2, 6))
                search_window = self.driver.current_window_handle
                offset = 0
                height = self.driver.execute_script('return document.body.scrollHeight')
                for j in range(0, height, random.randint(500, 1000)):
                    for i in range(offset, j):
                        js = "window.scrollTo(0,{});".format(i, i + 6)
                        self.driver.execute_script(js)
                    offset = j
                    time.sleep(random.uniform(0, 1))
                str = ''
                for i in self.content:
                    str += i
                    js = 'document.getElementById("ueditor_replace").innerHTML="<p>{}</p>" '.format(str)
                    self.driver.execute_script(js)
                    time.sleep(random.uniform(0, 1))
                js1 = 'document.querySelectorAll(".ui_btn_m")[0].click()'
                self.driver.execute_script(js1)
                time.sleep(random.randint(self.tieba_automatic_tipping_machine_min_waiting_time*60, self.tieba_automatic_tipping_machine_max_waiting_time*60))  # 设置睡眠时间

        except Exception as e:
            print(e)

    def post_bor_comments(self):
        '''
        发送贴吧评论

        :return:
        '''
        try:
            time.sleep(random.randint(3, 5))
            try:
                js1 = 'document.evaluate(\'(//div[@id="j_p_postlist"]/div[@class="l_post l_post_bright j_l_post clearfix  "]//a[@class="lzl_link_unfold"])[1]\',document).iterateNext().click()  '
                self.driver.execute_script(js1)
                time.sleep(random.randint(1, 3))
                str = ''
                for i in self.content:
                    str += i
                    js = 'document.getElementById("j_editor_for_container").innerHTML="<p>{}</p>"  '.format(str)
                    self.driver.execute_script(js)
                    time.sleep(random.uniform(0, 1))
                js1 = 'document.querySelectorAll(".lzl_panel_submit")[0].click()'
                self.driver.execute_script(js1)
            except Exception as e:
                print(e)


        except Exception as e:
            print(e)

    def tieba_guanzhu(self):
        '''
           贴吧自动关注及浏览贴吧内容
           :param bro:
           :param content:
           :return:driver
           '''
        self.tieba_liulan()
        time.sleep(random.randint(1, 5))
        search_window = self.driver.current_window_handle  # 获取当前窗口句柄集合

        try:
            for i in range(0, 401):
                self.driver.execute_script("window.scrollTo(0,400-{});".format(i))
            self.driver.find_element_by_xpath('//a[@id="j_head_focus_btn"]').click()  # 点击关注
            time.sleep(random.randint(2, 5))
            search_window = self.driver.current_window_handle  # 获取当前窗口句柄集合
            try:
                self.driver.find_element_by_xpath('//a[@class="dialogJclose"]').click()  # 关闭关注成功界面
                time.sleep(random.randint(3, 5))
                search_window = self.driver.current_window_handle  # 获取当前窗口句柄集合
            except Exception as e:
                print(e)
            try:
                self.driver.find_element_by_xpath('//a[@id="cancel_focus_no"] | //a[@class="dialogJclose"]').click()  # 关闭取消关注页面
                time.sleep(random.randint(3, 5))
                search_window = self.driver.current_window_handle  # 获取当前窗口句柄集合
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)


    def tieba_qiandao(self):
        '''
           贴吧自动签到及浏览贴吧内容2.0

           '''
        self.tieba_liulan()
        time.sleep(random.randint(1, 5))
        search_window = self.driver.current_window_handle  # 获取当前窗口句柄集合

        try:
            for i in range(0, 401):
                self.driver.execute_script("window.scrollTo(0,400-{});".format(i))
            time.sleep(random.randint(1, 3))
            search_window = self.driver.current_window_handle  # 获取当前窗口句柄集合
            js = 'document.querySelectorAll(".j_signbtn")[0].click()'  # 签到
            self.driver.execute_script(js)
            self.driver.execute_script(js)
            #没有关注就点签到
            try:
                time.sleep(random.randint(2, 5))
                search_window = self.driver.current_window_handle
                errorData = self.driver.find_element_by_xpath('//div[@class="signmod_likeandsign_dialog"]').text
                if errorData == "您还未加入此吧或等级不够":
                    self.driver.find_element_by_xpath('//a[@class="dialogJclose"]').click()  #关闭签到失败弹窗
                    time.sleep(random.randint(2, 5))
                    search_window = self.driver.current_window_handle
                    self.driver.find_element_by_xpath('//a[@id="j_head_focus_btn"]').click()  # 点击关注
                    time.sleep(random.randint(2, 5))
                    self.driver.find_element_by_xpath('//a[@class="dialogJclose"]').click()  # 关闭关注成功界面
                    time.sleep(random.randint(3, 5))
                    search_window = self.driver.current_window_handle  # 获取当前窗口句柄集合
                    js = 'document.querySelectorAll(".j_signbtn")[0].click()'  # 签到
                    self.driver.execute_script(js)
                    self.driver.execute_script(js)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

    def func_liulan(self,first_height,height,control_the_number_of_stay=800,control_speed=10,):
        '''
        浏览函数
        :param first_height:开始的页面高度
        :param height:网页高度
        :param url_list:帖子链接列表
        :param control_the_number_of_stay: 控制下滑停留次数和打开帖子链接的频率，最小值不低于500，默认1000
        :param control_speed:  # 控制下滑速度 单位（ps） 默认10ps
        :return:
        '''
        offset=first_height

        if self.open_tieba_detail_liulan:
            counter = 0  # 计数器
            # 获取当前页贴吧中所有帖子链接
            html = etree.HTML(self.driver.page_source)
            url_list = html.xpath(
                '//div[@id="content"]//li[@class=" j_thread_list clearfix"]//a[@class="j_th_tit "]/@href')
            url_list = ['https://tieba.baidu.com' + i for i in url_list]
            # print(url_list)
            randint_list = [random.randint(1, len(url_list)) for i in range(self.open_tieba_detail_liulan_num)]
            randint_list.sort()
            button_height_lst = [self.driver.find_element_by_xpath(
                '//ul[@id="thread_list"]/li[@class=" j_thread_list clearfix"][{}]//a[@class="j_th_tit "]'.format(
                    i)).location['y'] - 200  for i in randint_list]
            button_height_lst.append('-1')   #防止计数器超出列表范围
            # print(randint_list)
            # print(button_height_lst)
        for j in range(first_height, height, random.randint(500, control_the_number_of_stay)):  # 控制下滑停留次数
            # 模拟鼠标在指定区域下滑，符合条件的情况下会随即打开帖子并浏览
            for i in range(offset, j):
                if self.open_tieba_detail_liulan:  # 打开贴吧帖子浏览开关时才会执行
                    if i == button_height_lst[counter]:  # 只有鼠标滑倒url所在高度才执行
                        time.sleep(random.randint(2,4))
                        self.tieba_detail_liulan(url_list[randint_list[counter] - 1])  # 随机打开贴吧中的帖子并浏览
                        counter+=1
                js = "window.scrollTo(0,{});".format(i, i + control_speed)  # 控制下滑速度
                self.driver.execute_script(js)

            offset = j
            time.sleep(random.uniform(0, 1))
    def tieba_liulan(self):
        '''
                  输入关键字搜索并自动浏览贴吧内容
                  :param driver:
                  :param open_send_tieba_name:   仅用于测试
                  :param min_page_num  最小浏览页数
                  :param max_page_num  最大浏览页数
                  :return:
                  '''
        try:
            if self.open_send_tieba_name:  #控制是否打开发送贴吧名，此过程默认打开，测试时可将关闭
                time.sleep(random.randint(1, 5))
                search_window = self.driver.current_window_handle  # 获取当前窗口句柄集合
                # self.driver.execute_script("window.scrollTo(0,0);")
                wd1 = self.driver.find_element_by_id('wd1')
                wd1.clear()
                time.sleep(random.randint(1, 3))
                # 模拟输入贴吧名
                for i in self.tieba_name:
                    wd1.send_keys(i)
                    time.sleep(random.uniform(0, 2))  # 控制输入速度
                time.sleep(random.randint(1, 3))
                self.driver.find_element_by_xpath('//a[@class="search_btn search_btn_enter_ba j_enter_ba"]').click()
            try:

                page_num = random.randint(self.min_page_num,self.max_page_num)  # 控制浏览的页数
                # 模拟鼠标滑动到页尾
                for k in range(page_num):
                    time.sleep(random.randint(1, 5))
                    search_window = self.driver.current_window_handle  # 获取当前窗口句柄集合
                    try:  #有下一页按钮的情况下，高度定位到下一页按钮的高度
                        height =self.driver.find_element_by_xpath('//div[@id="frs_list_pager"]/a[text()="下一页>"]').location['y']

                    except:  #没有下一页的情况，高度定位到底部
                        height=self.driver.execute_script('return document.body.scrollHeight')

                    if k == 0:  # 第一页时
                        self.func_liulan(0,height)
                    else:  # 当贴吧点击下一页时返回的页面不是回到顶部的，高度400像素
                        self.func_liulan(400, height)
                    time.sleep(random.randint(3, 5))
                    self.driver.find_element_by_xpath('//a[@class="next pagination-item "]').click()
            except Exception as e:
                print(e)
                print('模拟鼠标滑动网页时出现问题')
        except Exception as e:
            print(e)
            print("输入贴吧名时出现问题")

    def tieba_detail_liulan(self,url):
        '''
        随机打开贴吧中的帖子并浏览
        :param driver:
        :return: driver
        '''
        if random.randint(1, 1):
            self.driver.execute_script("window.open('{}')".format(url))   #打开新标签页
            time.sleep(random.randint(3, 5))
            # 当前打开的所有窗口
            windows = self.driver.window_handles
            # 转换到最新打开的窗口
            self.driver.switch_to.window(windows[-1])
            height = self.driver.execute_script('return document.body.scrollHeight')   #获取网页长度
            #二楼的回复按钮没定位到，就执行自动‘百度自动顶帖机’程序
            try:
                try:
                    if self.open_post_bor_comments:
                        button_height=self.driver.find_element_by_xpath('(//div[@id="j_p_postlist"]/div[@class="l_post l_post_bright j_l_post clearfix  "]//a[@class="lzl_link_unfold"])[1]').location['y'] - 200   #二楼‘回复’按钮y轴高度
                    offset = 0
                    for j in range(0, height, random.randint(500, 1000)):  # 控制下滑停留次数
                        for i in range(offset, j):
                            if self.open_post_bor_comments and i == button_height:  # 打开发送贴吧评论并且鼠标移动到‘回复’按钮
                                self.post_bor_comments()  # 发送贴吧评论函数
                            js = "window.scrollTo({},{});".format(i, i + 10)  # 控制下滑速度
                            self.driver.execute_script(js)

                        offset = j
                        time.sleep(random.uniform(0, 1))
                except:
                    self.tieba_automatic_tipping_machine_url=self.driver.current_url
                    self.tieba_automatic_tipping_machine()

                self.driver.close()  #关闭打开的新标签页
                time.sleep(random.randint(1, 5))
                search_window = self.driver.window_handles  # 获取窗口句柄集合
                self.driver.switch_to.window(search_window[0])  # 获取贴吧主页的句柄
            except Exception as e:
                print(e)


class MAKE_GUI(object):
    def __init__(self):
        self.upgrande =UPGRANDE_ACCOUNT()

        # 第1步，实例化object，建立窗口window
        self.window = tk.Tk()
        # 第2步，给窗口的可视化起名字
        self.window.title('百度贴吧自动发贴机1.0---试用版')
        # 第3步，设定窗口的大小(长 * 宽)
        self.window.geometry('500x600')  # 这里的乘是小x
        self.gongneng_var = tk.StringVar()   #功能参数，qiandao,guanzhu,dingtie
        self.tiezi_liulan_switch_var=tk.IntVar()   #帖子浏览开关参数
        self.tiezi_pinglun_switch_var=tk.IntVar()  #帖子评论开关参数
        self.min_page_num_var=tk.IntVar()   #贴吧浏览的最小页数
        self.min_page_num_var.set(2)
        self.max_page_num_var=tk.IntVar()   #贴吧浏览的最大页数
        self.max_page_num_var.set(5)
        self.proxy_swich_var=tk.IntVar()   #代理IP开关参数
        self.headless_switch_var=tk.IntVar()   #无头浏览器开关参数
        self.open_tieba_detail_liulan_num=tk.IntVar()   #每页贴吧中浏览的帖子数量
        self.open_tieba_detail_liulan_num.set(3)
        self.tieba_automatic_tipping_machine_url=tk.StringVar()   #顶贴URL，只在顶贴功能中使用
        self.tieba_automatic_tipping_machine_url.set('顶贴URL')
        self.tieba_automatic_tipping_machine_sendtimes=tk.IntVar()   #顶贴的次数，只在顶贴功能中使用
        self.tieba_automatic_tipping_machine_sendtimes.set(3)
        self.tieba_automatic_tipping_machine_min_waiting_time=tk.IntVar()   #顶贴等待的最小时间，单位（分钟），只在顶贴功能中使用
        self.tieba_automatic_tipping_machine_min_waiting_time.set(5)
        self.tieba_automatic_tipping_machine_max_waiting_time=tk.IntVar()   #顶贴等待的最大时间，单位（分钟），只在顶贴功能中使用
        self.tieba_automatic_tipping_machine_max_waiting_time.set(15)
        tk.Radiobutton(self.window,variable=self.gongneng_var,value='guanzhu', text='贴吧关注').place(x=50,y=50)
        tk.Radiobutton(self.window,variable=self.gongneng_var,value='qiandao', text='贴吧签到').place(x=250,y=50)
        tk.Radiobutton(self.window,variable=self.gongneng_var,value='dingtie', text='贴吧顶贴').place(x=50,y=100)
        tk.Entry(self.window,textvariable=self.tieba_automatic_tipping_machine_url).place(x=200,y=100)
        tk.Checkbutton(self.window,variable=self.tiezi_liulan_switch_var,onvalue=1,offvalue=0,text='帖子浏览开关').place(x=50,y=150)
        tk.Checkbutton(self.window,variable=self.tiezi_pinglun_switch_var,onvalue=1,offvalue=0,text='帖子评论开关').place(x=250,y=150)
        tk.Checkbutton(self.window,variable=self.proxy_swich_var,onvalue=1,offvalue=0,text='代理IP(待测试)').place(x=50,y=200)
        tk.Checkbutton(self.window,variable=self.headless_switch_var,onvalue=1,offvalue=0,text='无头浏览器开关(待测试)').place(x=250,y=200)
        tk.Label(self.window, text='顶贴次数(仅贴吧顶贴使用)').place(x=50, y=250)
        tk.Label(self.window, text='顶贴等待最小时间(仅贴吧顶贴使用)').place(x=50, y=300)
        tk.Label(self.window, text='顶贴等待最大时间(仅贴吧顶贴使用)').place(x=50, y=350)
        tk.Entry(self.window, textvariable=self.tieba_automatic_tipping_machine_sendtimes).place(x=200, y=250)
        tk.Entry(self.window, textvariable=self.tieba_automatic_tipping_machine_min_waiting_time).place(x=250, y=300)
        tk.Entry(self.window, textvariable=self.tieba_automatic_tipping_machine_max_waiting_time).place(x=250, y=350)
        tk.Label(self.window,text='贴吧最小浏览页数').place(x=50,y=400)
        tk.Label(self.window,text='贴吧最大浏览页数').place(x=50,y=450)
        tk.Label(self.window, text='贴吧每页中的帖子浏览次数').place(x=50, y=500)
        tk.Entry(self.window,textvariable=self.min_page_num_var).place(x=150,y=400)
        tk.Entry(self.window,textvariable=self.max_page_num_var).place(x=150,y=450)
        tk.Entry(self.window, textvariable=self.open_tieba_detail_liulan_num).place(x=150, y=500)
        tk.Button(self.window,text='攻击',command=self.relation_func).place(x=250,y=550)
        self.window.mainloop()
    def sub_relation_func(self,func):
        filename = os.getcwd() + '\贴吧账号.txt'
        with open(filename, 'r', encoding='utf-8') as fp:
            tieba_zhanghao_list = fp.readlines()
        if len(tieba_zhanghao_list)==0:
            print('贴吧账号.txt为空')
            exit()
        filename1 = os.getcwd() + '\贴吧.txt'
        with open(filename1, 'r', encoding='utf-8') as fp:
            tieba_name_list = fp.readlines()
        if len(tieba_name_list)==0:
            print('贴吧.txt为空')
            exit()
        if self.tiezi_pinglun_switch_var.get() or self.gongneng_var.get() =='dingtie':
            filename3 = os.getcwd() + '\广告话术.txt'
            with open(filename3, 'r', encoding='utf-8') as fp:
                content_list = fp.readlines()
                content_list = [i.strip() for i in content_list]
            if len(content_list)==0:
                print('广告话术.txt为空')
                exit()

        if self.proxy_swich_var.get():
            filename2 = os.getcwd() + '\代理IP.txt'
            with open(filename2, 'r', encoding='utf-8') as fp:
                proxy_list = fp.readlines()
            proxy_list=[i.strip() for i in proxy_list]
            if len(proxy_list)==0:
                print('代理ip.txt为空')
                exit()

        if self.gongneng_var.get()=='dingtie':   #功能选择了贴吧顶贴
            self.upgrande.tieba_automatic_tipping_machine_url=self.tieba_automatic_tipping_machine_url.get()
            self.upgrande.tieba_automatic_tipping_machine_sendtimes=self.tieba_automatic_tipping_machine_sendtimes.get()
            self.upgrande.tieba_automatic_tipping_machine_min_waiting_time=self.tieba_automatic_tipping_machine_min_waiting_time.get()
            self.upgrande.tieba_automatic_tipping_machine_max_waiting_time = self.tieba_automatic_tipping_machine_max_waiting_time.get()
        if self.tiezi_liulan_switch_var.get():   #贴吧浏览开关打开
            self.upgrande.open_tieba_detail_liulan_num = self.open_tieba_detail_liulan_num.get()
            self.upgrande.open_post_bor_comments = self.tiezi_pinglun_switch_var.get()
            self.upgrande.open_tieba_detail_liulan = self.tiezi_liulan_switch_var.get()
        self.upgrande.min_page_num = self.min_page_num_var.get()
        self.upgrande.max_page_num = self.max_page_num_var.get()
        self.upgrande.open_set_headless = self.headless_switch_var.get()

        for tieba_zhanghao in tieba_zhanghao_list:
            username = tieba_zhanghao.split(' ')[0]
            password = tieba_zhanghao.split(' ')[1].strip()
            self.upgrande.username = username
            self.upgrande.password = password
            if self.proxy_swich_var.get():
                self.upgrande.proxy_server = random.choice(proxy_list)
            self.upgrande.tieba_login()
            for tieba_name in tieba_name_list:
                self.upgrande.tieba_name = tieba_name.strip()
                if self.tiezi_pinglun_switch_var.get() or self.gongneng_var.get() =='dingtie':  #帖子评论开关打开或者选择贴吧顶贴功能
                    self.upgrande.content = random.choice(content_list)
                func()



    def relation_func(self):
        if self.gongneng_var.get() =='guanzhu':
            self.sub_relation_func(self.upgrande.tieba_guanzhu)
        elif self.gongneng_var.get() =='qiandao':
            self.sub_relation_func(self.upgrande.tieba_qiandao)
        elif self.gongneng_var.get()=='dingtie':
            self.sub_relation_func(self.upgrande.tieba_automatic_tipping_machine)
        else:
            messagebox.showwarning('Error','没有选择功能')



if __name__ == '__main__':

    make=MAKE_GUI()
