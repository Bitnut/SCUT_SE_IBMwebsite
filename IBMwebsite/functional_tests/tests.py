# 功能测试 python3 manage.py test functional_tests
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_rul = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_rul = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_rul == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        # 加入隐式等待
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_finish_table_and_submit(self):
        self.browser.get(self.server_url)

        # 输入一个代办事项
        name_inputbox = self.browser.find_element_by_id('name_input')
        sex_inputbox = self.browser.find_element_by_id('sex_input')
        nation_inputbox = self.browser.find_element_by_id('nation_input')
        address_inputbox = self.browser.find_element_by_id('address_input')
        email_inputbox = self.browser.find_element_by_id('email_input')
        QQ_inputbox = self.browser.find_element_by_id('QQ_input')
        phone_inputbox = self.browser.find_element_by_id('phone_input')
        hobby_inputbox = self.browser.find_element_by_id('hobby_input')
        organization_inputbox = self.browser.find_element_by_id('organization_input')
        apartment_inputbox = self.browser.find_element_by_id('apartment_input')
        agree_inputbox = self.browser.find_element_by_id('agree_to_allocation_input')
        tech_inputbox = self.browser.find_element_by_id('tech_input')
        await_inputbox = self.browser.find_element_by_id('await_input')
        plan_inputbox = self.browser.find_element_by_id('plan_input')
        assess_inputbox = self.browser.find_element_by_id('assess_input')

        name_inputbox.send_keys('蛤蛤蛤')
        nation_inputbox.send_keys('汉')
        address_inputbox.send_keys('')

        # # 在文本框中输入"Buy peacock feathers"
        # inputbox.send_keys('Buy peacock feathers')
        #
        # # 按下回车后重定向到一个新的url
        # # 代办事项表格中显示了"1: Buy peacock feathers"
        # inputbox.send_keys(Keys.ENTER)
        # edith_list_url = self.browser.current_url
        # self.assertRegex(edith_list_url, '/lists/.+')
        # self.check_for_row_in_list_table('1: Buy peacock feathers')
        #
        # # 页面中还有一个文本框 可以输入其他待办事项
        # # 输入"Use peacock feathers to make a fly"
        # inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys('Use peacock feathers to make a fly')
        # inputbox.send_keys(Keys.ENTER)
        #
        # # 页面再次更新,清单中显示了这两个待办事项
        # self.check_for_row_in_list_table('1: Buy peacock feathers')
        # self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        #
        # # 现在francis访问网站
        #
        # # 使用新的浏览器
        # self.browser.quit()
        # self.browser = webdriver.Firefox()
        #
        # # francis访问首页 看不到其他人的清单
        # self.browser.get(self.server_url)
        # page_text = self.browser.find_element_by_tag_name('body').text
        # self.assertNotIn('Buy peacock feathers', page_text)
        # self.assertNotIn('make a fly', page_text)
        #
        # # francis新建一个清单
        # inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys('Buy milk')
        # inputbox.send_keys(Keys.ENTER)
        #
        # # francis获得了一个唯一的url
        # francis_list_url = self.browser.current_url
        # self.assertRegex(francis_list_url, '/lists/.+')
        # self.assertNotEqual(francis_list_url, edith_list_url)
        #
        # # 这个页面没有edith的清单
        # page_text = self.browser.find_element_by_tag_name('body').text
        # self.assertNotIn('Buy peacock feathers', page_text)
        # self.assertIn('Buy milk', page_text)
        #
        # #
        # # self.fail('Finish the test!')





