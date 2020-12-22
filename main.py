import sys
from jd_mask_spider_requests import Jd_Mask_Spider
from QR_Login import JDLogin
import  os

if __name__ == '__main__':

    #删除cookies
    cookiePath = './cookies'
    isexits = os.path.exists(cookiePath)
    if isexits:
        print("存在")
        for root, dirs, files in os.walk(cookiePath):
            print(files);
            for fileName in files:
                del_file = os.path.join(root, fileName)
                os.remove(del_file)
    login = JDLogin();
    if login.JD_RQ_login():
        print("登录完成~")

    a = """
    ==========================
    1.预约商品
    2.秒杀抢购商品
    ==========================
    """
    start_tool = Jd_Mask_Spider()
    print(a)
    choice_function = input('选择功能:')
    if choice_function == '1':
        start_tool.login()
        start_tool.make_reserve()
    elif choice_function == '2':
        start_tool.request_seckill_url()
        start_tool.request_seckill_checkout_page()
        start_tool.submit_seckill_order()
    else:
        print('没有此功能')
        sys.exit(1)

     
     
