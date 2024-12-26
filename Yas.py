from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def install_browser():
    options = Options()
    options.add_argument("--headless")  # لتشغيل المتصفح بدون واجهة رسومية
    options.add_argument("--no-sandbox")  # لمنع المشاكل المتعلقة بالأمان
    options.add_argument("--disable-dev-shm-usage")  # لتقليل مشاكل الذاكرة

    # تحديد مسار ChromeDriver
    chrome_driver_path = '/path/to/chromedriver'  # قم بتحديد المسار الصحيح إلى ChromeDriver

    # استخدام Service لتحديد مسار ChromeDriver
    service = Service(executable_path=chrome_driver_path)

    # تشغيل المتصفح
    driver = webdriver.Chrome(service=service, options=options)

    driver.get('http://www.google.com')
    print(driver.title)

if __name__ == "__main__":
    install_browser()
