import time
import pickle
import selenium.webdriver 
from selenium.webdriver.support import expected_conditions as EC
import csv

from selenium.webdriver.common.keys import Keys
output_file = 'medical.csv'


def add_csv_head():
    with open(output_file, 'w', newline='',encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['الترميز', 'الاسم', 'التعبئة', 'التركيز', 'الوكيل', 'سعر _الصيدلي', 'سعر _الجمهور _الاردني','سعر _الجمهور _الضريبة'])

def add_csv_row(row1, row2, row3, row4, row5, row6, row7, row8):
    # print("-----33--------")
    # print(jobs_category)
    with open(output_file, 'a', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([row1, row2, row3, row4, row5, row6, row7, row8])
add_csv_head()

default_timeout = 100

driver = selenium.webdriver.Chrome()

driver.get("http://www.jfda.jo/Pages/viewpage.aspx?pageID=184")

driver.implicitly_wait(default_timeout)
# fr = driver.find_element('#ContentPlaceHolder1_tdPart4 frame')
iframe = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.frame(iframe)
aa=driver.find_element_by_xpath('//*[@id="DDtype"]/option[text()="Normal"]').click()
driver.find_element_by_xpath('//*[@id="BTNsearch"]').click()
driver.implicitly_wait(default_timeout)

page=1
while True:
    page+=1
    time.sleep(15)
    # task here
    trs=driver.find_elements_by_xpath('//tr[@class="GVdetails"]')
    for tr in trs:
        row1=tr.find_elements_by_tag_name("td")[0].text
        row2=tr.find_elements_by_tag_name("td")[1].text
        row3=tr.find_elements_by_tag_name("td")[2].text
        row4=tr.find_elements_by_tag_name("td")[3].text
        row5=tr.find_elements_by_tag_name("td")[4].text
        row6=tr.find_elements_by_tag_name("td")[5].text
        row7=tr.find_elements_by_tag_name("td")[6].text
        row8=tr.find_elements_by_tag_name("td")[7].text
        add_csv_row(row1, row2, row3, row4, row5, row6, row7, row8)
        

    # end of task

    # goto next
    driver.execute_script("__doPostBack('GridView1','Page${}')".format(page))
    


# bb=driver.find_elements_by_xpath('//a[@style="color:White;"]')
# print(bb)
# for ab in bb:
#     # time.sleep(8)
#     # print(ab.text)
#     time.sleep(2)
#     driver.execute_script("arguments[0].click();", ab)
#     # time.sleep(16)
#     # print(ab)
#     # print(i)
#     driver.implicitly_wait(50)
    
 


print("done")