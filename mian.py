import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def fill_form():
    # Baca data dari file Excel
    data = pd.read_excel('data.xlsx')

    # Menampilkan nama kolom untuk debugging
    # print(data.columns)  # Menampilkan nama kolom
    data.columns = data.columns.str.strip()  # Menghapus spasi di awal dan akhir

    recycle = data.shape[0]  # Jumlah baris dalam file Excel

    # Konfigurasi Chrome dengan WebDriver Manager
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())

    # print(data.head())  # Tampilkan beberapa baris pertama dari DataFrame

    driver = webdriver.Chrome(service=service, options=chrome_options)  # Pindahkan di luar loop

    for i in range(recycle):
        print(f"Mengisi form untuk baris {i+1}")
        driver.get('https://sukma.jatimprov.go.id/fe/survey?idUser=236')  # Ganti URL form jika perlu
        time.sleep(2)  # Beri jeda untuk memuat halaman

        # Ambil data nama dari Excel
        nama_value = data.loc[i, 'nama']  # Mengambil nilai di kolom 'nama'
        # print(f"Nama yang diisi: {nama_value}")  # Debug print
        umur_value = data.loc[i, 'umur']
        tlp_value = data.loc[i, 'No.telp']
        sex_value = data.loc[i,'sex']
        page2_value = data.loc[i,'page2']
        page3_value = data.loc[i,'page3']
        page4_value = data.loc[i,'page4']
        page5_value = data.loc[i,'page5']
        
        



        
        # Isi kolom nama pada form
        nama_field = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
        nama_field.send_keys(nama_value)
        time.sleep(1)
        umur_field = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div[1]/input')
        umur_field.send_keys(str(umur_value))
        time.sleep(1)
        tlp_field = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div[2]/input')
        tlp_field.send_keys(str(tlp_value))
        time.sleep(1)

        sex = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/select')
        sex.click()
        time.sleep(1)
        if sex_value == 1 :
            sex_cowo = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/select/option[1]')
            sex_cowo.click()
            print('cowo')
        elif sex_value == 0 :
            sex_cewe = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/select/option[2]')
            sex_cewe.click()
            print('cewe')
        time.sleep(1)

        botton1_mulai = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div/div/div[2]/ul/li/button')
        botton1_mulai.click()
        time.sleep(1)
        
        #page2 
       # Misalnya, menambahkan bagian untuk mencentang radio button
    # Cek apakah page2_value bukan NaN
        time.sleep(1) 
        if page2_value == 1:
            page2A = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[1]/label')
            page2A.click()  # Centang radio button untuk opsi A
            print("Berhasil memilih opsi A di halaman kedua")
        elif page2_value == 2:
            page2B = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[2]/label')
            page2B.click()  # Centang radio button untuk opsi B
            print("Berhasil memilih opsi B di halaman kedua")
        elif page2_value == 3:
            page2C = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[3]/label')
            page2C.click()  # Centang radio button untuk opsi C
            print("Berhasil memilih opsi C di halaman kedua")
        elif page2_value == 4:
            page2D = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[4]/label')
            page2D.click()  # Centang radio button untuk opsi D
            print("Berhasil memilih opsi D di halaman kedua")
      
        botton2_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[1]/div/div[3]/ul/li/span')
        botton2_next.click()
        time.sleep(1)

        ##page 3

        if page3_value == 1:
            page3A = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[1]/label')
            page3A.click()  # Centang radio button untuk opsi A
            print("Berhasil memilih opsi A di halaman kedua")
        elif page3_value == 2:
            page3B = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[2]/label')
            page3B.click()  # Centang radio button untuk opsi B
            print("Berhasil memilih opsi B di halaman kedua")
        elif page3_value == 3:
            page3C = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[3]/label')
            page3C.click()  # Centang radio button untuk opsi C
            print("Berhasil memilih opsi C di halaman kedua")
        elif page3_value == 4:
            page3D = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[4]/label')
            page3D.click()  # Centang radio button untuk opsi D
            print("Berhasil memilih opsi D di halaman kedua")

        time.sleep(1)

        botton3_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[2]/div/div[3]/ul/li[2]/span')
        botton3_next.click()
        time.sleep(1)

        ##page 4
        if page4_value == 1:
            page4A = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[3]/div/div[1]/div[2]/div/div[2]/ul/li[1]/label')
            page4A.click()  # Centang radio button untuk opsi A
            print("Berhasil memilih opsi A di halaman kedua")
        elif page4_value == 2:
            page4B = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[3]/div/div[1]/div[2]/div/div[2]/ul/li[2]/label')
            page4B.click()  # Centang radio button untuk opsi B
            print("Berhasil memilih opsi B di halaman kedua")
        elif page4_value == 3:
            page4C = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[3]/div/div[1]/div[2]/div/div[2]/ul/li[4]/label')
            page4C.click()  # Centang radio button untuk opsi C
            print("Berhasil memilih opsi C di halaman kedua")
        elif page4_value == 4:
            page4D = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[3]/div/div[1]/div[2]/div/div[2]/ul/li[4]/label')
            page4D.click()  # Centang radio button untuk opsi D
            print("Berhasil memilih opsi D di halaman kedua")

        botton4_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[3]/div/div[3]/ul/li[2]/span')
        botton4_next.click()
        time.sleep(1)

        ##page 5
        if page5_value == 1:
            page5A = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[4]/div/div[1]/div[2]/div/div[2]/ul/li[1]/label')
            page5A.click()  # Centang radio button untuk opsi A
            print("Berhasil memilih opsi A di halaman kedua")
        elif page5_value == 2:
            page5B = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[4]/div/div[1]/div[2]/div/div[2]/ul/li[2]/label')
            page5B.click()  # Centang radio button untuk opsi B
            print("Berhasil memilih opsi B di halaman kedua")
        elif page5_value == 3:
            page5C = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[4]/div/div[1]/div[2]/div/div[2]/ul/li[3]/label')
            page5C.click()  # Centang radio button untuk opsi C
            print("Berhasil memilih opsi C di halaman kedua")
        elif page5_value == 4:
            page5D = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[4]/div/div[1]/div[2]/div/div[2]/ul/li[4]/label')
            page5D.click()  # Centang radio button untuk opsi D
            print("Berhasil memilih opsi D di halaman kedua")

        botton4_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[4]/div/div[3]/ul/li[2]/span')
        botton4_next.click()
        time.sleep(1)
        
        


        
    # Tutup browser setelah selesai mengisi data
    driver.quit()

# Panggil fungsi untuk menjalankan program
fill_form()
