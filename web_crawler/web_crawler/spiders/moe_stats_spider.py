import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from bs4 import BeautifulSoup
import csv


class MoeStatsSpiderSpider(scrapy.Spider):
    name = "moe_stats_spider"
    allowed_domains = ["stats.moe.gov.tw"]
    start_urls = ["https://stats.moe.gov.tw/bcode/"]

    def __init__(self):
        super(MoeStatsSpiderSpider, self).__init__()

        # 初始化Selenium WebDriver
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 不顯示瀏覽器視窗
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://stats.moe.gov.tw/bcode/")

        self.wait_time = 5
        self.max_data_page = 100

    def parse(self, response):
        self.setup_search_criteria()
        self.driver.find_element(By.ID, "Button1").click()

        # 等待網頁生成並獲取HTML內容
        WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "GridView1"))
        )

        # 使用BeautifulSoup來解析HTML
        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        # 取得表格標頭
        header_row = soup.find(
            "tr", {"style": "color:White;background-color:#C04000;font-weight:bold;"}
        )
        headers = [th.text.strip() for th in header_row.find_all("th")]

        # 將資料寫入CSV檔案
        with open("output.csv", "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=headers)
            csv_writer.writeheader()

            for page in range(self.max_data_page):
                # 取得表格資料
                data_rows = soup.find_all("tr", {"class": ["GridViewRowStyle"]})
                for row in data_rows:
                    values = [td.text.strip() for td in row.find_all("td")]
                    row_data = dict(zip(headers, values))
                    csv_writer.writerow(row_data)

                # 檢查是否有下一頁
                next_page_button = self.driver.find_element(By.ID, "BtnNext")
                if next_page_button.get_attribute("disabled"):
                    break
                else:
                    next_page_button.click()
                    sleep(0.5)

                    # 等待數據加載完成
                    WebDriverWait(self.driver, self.wait_time).until(
                        EC.staleness_of(next_page_button)
                    )

                    # 使用BeautifulSoup來解析HTML
                    soup = BeautifulSoup(self.driver.page_source, "html.parser")

    def setup_search_criteria(self):
        self.click_radio_button("RadioButtonList2_3")

        self.fill_text_field("minYear", "100")
        self.fill_text_field("maxYear", "110")

        checkbox_data = {
            "CheckBoxList1_0": True,
            "CheckBoxList1_1": False,
            "CheckBoxList1_2": False,
            "CheckBoxList2_0": True,
            "CheckBoxList2_1": False,
            "CheckBoxList3_0": True,
            "CheckBoxList3_1": False,
            "CheckBoxList4_0": True,
            "CheckBoxList4_1": True,
            "CheckBoxList4_2": True,
            "CheckBoxList4_3": False,
            "CheckBoxList4_4": False,
            "CheckBoxList4_5": False,
            "CheckBoxList4_6": False,
            "CheckBoxList4_7": False,
        }

        for id, is_checked in checkbox_data.items():
            self.set_checkbox_state(id, is_checked)

        self.set_dropdown_value("DropDownList1", "06")
        self.set_dropdown_value("DropDownList2", "-1")
        self.set_dropdown_value("DropDownList3", "-1")
        self.set_dropdown_value("DropDownList4", "-1")

    def click_radio_button(self, button_id):
        # 找到指定id的radio button並點擊
        radio_button = WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, button_id))
        )
        radio_button.click()

    def fill_text_field(self, field_id, text):
        # 找到指定id的text field，清空並填入文字
        text_field = WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        text_field.clear()
        text_field.send_keys(text)

    def set_checkbox_state(self, checkbox_id, is_checked):
        # 找到指定id的checkbox，並根據is_checked設置狀態
        checkbox = WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, checkbox_id))
        )

        if checkbox.is_selected() != is_checked:
            checkbox.click()

    def set_dropdown_value(self, dropdown_id, value):
        try:
            # 找到指定id的dropdown
            dropdown = WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located((By.ID, dropdown_id))
            )

            # 使用 Select 類別來處理下拉列表
            select = Select(dropdown)
            select.select_by_value(value)

        except NoSuchElementException:
            self.logger.error(
                f"Value {value} not found in dropdown with ID {dropdown_id}"
            )

    def closed(self, reason):
        # 確保在爬蟲結束後正確關閉Selenium WebDriver
        pass
        # self.driver.quit()
