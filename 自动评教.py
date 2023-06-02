import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def iselement(browser, id):  # 判断页面是不是有这个元素
    try:
        browser.find_element(By.ID, id)
        return True
    except:
        return False
def send(j=False):#一键提交已经保存的评教
    if j :
        l_bc1=[]
        for i in range(s):  # 遍历评教列表
            txt = driver.find_element(By.ID, str(i + 1)).text  # 遍历评教列表
            print(txt)
            if "已评完" in txt:  # 已评完/保存的id加入列表
                l_bc1.append(i + 1)
        for i in l_bc1:
            driver.find_element(By.ID, str(i)).click()
            time.sleep(0.7)
            driver.find_element(By.ID, "btn_xspj_tj").click()
            time.sleep(0.3)
            driver.find_element(By.ID, "btn_ok").click()
            time.sleep(0.8)
def operate(c,l_wp,t1,t2,t3,t4,j=False):# 对未评的教师进行评价并保存，不提交
    if j :
        for i in l_wp:  # 对未评的教师进行评价并保存，不提交
            driver.find_element(By.ID, str(i)).click()
            time.sleep(0.7)
            a = 0
            for i1 in driver.find_elements(By.XPATH, "//*/input[@type='radio']"):  # 实现遍历点击所有的radio
                a = a + 1
                if a in c:
                    i1.click()
            b = 0
            for i in driver.find_elements(By.XPATH, '//*/textarea[@placeholder="请至少输入0个字，至多输入500个字"]'):  # 实现遍历请留下你宝贵的意见
                b = b + 1
                i.clear()
                if b == 1:  # *你对本课程老师的意见与建议。
                    i.send_keys(t1)
                if b == 2:  # 你是否愿意向其他同学推荐该课程？
                    i.send_keys(t2)
                if b == 3:  # 你学习该课程课外花费的学时数是？（含作业、习题、小论文、报告、设计等，按学时来计，45分钟计作1学时）
                    i.send_keys(t3)

            driver.find_element(By.XPATH, '//*/textarea[@placeholder="请输入评语(500字以内)"]').clear()  # 清空最后的评语
            driver.find_element(By.XPATH, '//*/textarea[@placeholder="请输入评语(500字以内)"]').send_keys(t4)  # 最后的评语
            time.sleep(0.2)  # 让电脑缓一下
            driver.find_element(By.ID, "btn_xspj_bc").click()  # 点击保存按钮
            time.sleep(0.3)
            driver.find_element(By.ID, "btn_ok").click()
            time.sleep(0.8)


if __name__ == '__main__':
    t1 = "无"  # *你对本课程老师的意见与建议。
    t2 = "愿意"  # 你是否愿意向其他同学推荐该课程？
    t3 = "16"  # 你学习该课程课外花费的学时数是？（含作业、习题、小论文、报告、设计等，按学时来计，45分钟计作1学时）
    t4 = "好"  # 最后的评语
    c = [2, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56]  # 按顺序点的radio位置，当前分数为96.40
    j1 = True
    j2 = False

    driver = webdriver.Chrome()  # Chrome浏览器
    driver.maximize_window()  # 窗口最大化
    driver.get("https://jwxt.zafu.edu.cn/jwglxt/xtgl/login_slogin.html")  # 打开网页

    id = input("输入学号（必填）：")
    pw = input("输入密码（如果浏览器输入请直接回车）：")

    driver.find_element(By.ID, "yhm").send_keys(id)
    driver.find_element(By.ID, "mm").send_keys(pw)
    input("请输入账号密码，并验证后按下回车键继续：")
    driver.maximize_window()  # 窗口最大化
    if iselement(driver, "dl"):  # 判断页面是不是有登录按钮
        driver.find_element(By.ID, "dl").click()  # 点击登录按钮

    url1 = "https://jwxt.zafu.edu.cn/jwglxt/xspjgl/xspj_cxXspjIndex.html?doType=details&gnmkdm=N401605&layout=default&su=" + id  # 评教界面网址
    driver.get(url1)  # 转到评教界面

    p = driver.find_element(By.ID, "sp_1_pager").text  # 检查当前页数
    if p != "1":  # 当前页数不是1，切换一页显示数量为1000
        ele = driver.find_element(By.NAME, "currentPage")
        select_ele = Select(ele)
        select_ele.select_by_value("1000")

    wp = driver.find_element(By.ID, "wp").text  # 未评数量
    bc = driver.find_element(By.ID, "bc").text  # 保存数量
    tj = driver.find_element(By.ID, "tj").text  # 提交数量
    s = int(wp) + int(bc) + int(tj)  # 总共的数量

    time.sleep(0.2)  # 让电脑缓一下

    l_wp = []  # 存未评id
    l_tj = []  # 存提交id
    l_bc = []  # 存已评完/保存id
    for i in range(s):  # 遍历评教列表
        txt = driver.find_element(By.ID, str(i + 1)).text  # 遍历评教列表
        print(txt)
        if "未评" in txt:  # 未评id加入列表
            l_wp.append(i + 1)
        if "提交" in txt:  # 提交id加入列表
            l_tj.append(i + 1)
        if "已评完" in txt:  # 已评完/保存的id加入列表
            l_bc.append(i + 1)

    time.sleep(0.5)  # 让电脑缓一下

    operate(c, l_wp, t1, t2, t3, t4, j1)

    send(j2)
