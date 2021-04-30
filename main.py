from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import yaml
import keyboard


class Bot:

    def __init__(self):
        self.options = Options()
        self.options.binary_location = "C:\Program Files\BraveSoftware\Brave-Browser\Application/brave.exe"
        self.driver_path = "D:\College\PYTHON PROGRAMS\chromedriver.exe"
        self.driver = webdriver.Chrome(options=self.options, executable_path=self.driver_path)

        with open('credentials.yaml', 'r') as credentials:
            self.login_data = yaml.safe_load(credentials)
        username = self.login_data['credentials']['username']
        password = self.login_data['credentials']['password']

        self.login(username, password)
        self.send_message(self.login_data['recepient']['username'])
        self.replies()
        # self.chat_loop()

    def login(self, user, passwd):
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        username_field = self.driver.find_element_by_xpath("//input[@name='username']")
        username_field.send_keys(user)
        password_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(passwd)
        login_btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()
        sleep(5)
        not_now_1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_1.click()
        sleep(2)
        not_now_2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now_2.click()

    def send_message(self, recepient):
        messages_btn = self.driver.find_element_by_class_name('xWeGp')
        messages_btn.click()
        sleep(2)
        Find_recepient = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button')
        Find_recepient.click()
        sleep(1)
        search_user_field = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')
        search_user_field.send_keys(recepient)
        sleep(3)
        user_profile = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[2]')
        user_profile.click()
        sleep(2)
        next_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button')
        next_btn.click()
        sleep(3)


    def chat_loop(self):
        message_field = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

        while not keyboard.is_pressed('q'):
            message_field.send_keys("HI bot Speaking, Don't reply bot under testing")
            sleep(2)
            send_btn = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]')
            send_btn.click()
            sleep()

    def replies(self):
        reply = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[15]/div[2]/div/div/div/div/div/div/div/div')
        print(reply.text)


def main():
    bot_instance = Bot()


if __name__ == '__main__':
    main()
