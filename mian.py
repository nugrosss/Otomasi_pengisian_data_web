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
        page6_value = data.loc[i,'page6']
        page7_value = data.loc[i,'page7']
        page8_value = data.loc[i,'page8']
        page9_value = data.loc[i,'page9']
        page10_value = data.loc[i,'page10']
        page11_value = data.loc[i,'page11']
        page12_value = data.loc[i,'page12']
        



        
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
        time.sleep(2) 
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
        time.sleep(2)

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

        time.sleep(2)

        botton3_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[2]/div/div[3]/ul/li[2]/span')
        botton3_next.click()
        time.sleep(2)

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
        time.sleep(2)

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

        botton5_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[4]/div/div[3]/ul/li[2]/span')
        botton5_next.click()
        time.sleep(2)
        
         ##page 6
        if page6_value == 1:
            page6A = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[5]/div/div[1]/div[2]/div/div[2]/ul/li[1]/label')
            page6A.click()  # Centang radio button untuk opsi A
            print("Berhasil memilih opsi A di halaman kedua")
        elif page6_value == 2:
            page6B = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[5]/div/div[1]/div[2]/div/div[2]/ul/li[2]/label')
            page6B.click()  # Centang radio button untuk opsi B
            print("Berhasil memilih opsi B di halaman kedua")
        elif page6_value == 3:
            page6C = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[5]/div/div[1]/div[2]/div/div[2]/ul/li[3]/label')
            page6C.click()  # Centang radio button untuk opsi C
            print("Berhasil memilih opsi C di halaman kedua")
        elif page6_value == 4:
            page6D = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[5]/div/div[1]/div[2]/div/div[2]/ul/li[4]/label')
            page6D.click()  # Centang radio button untuk opsi D
            print("Berhasil memilih opsi D di halaman kedua")

        botton6_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[5]/div/div[3]/ul/li[2]/span')
        botton6_next.click()
        time.sleep(2)

        ##page 7
        if page7_value == 1:
            page7A = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[6]/div/div[1]/div[2]/div/div[2]/ul/li[1]/label')
            page7A.click()  # Centang radio button untuk opsi A
            print("Berhasil memilih opsi A di halaman kedua")
        elif page7_value == 2:
            page7B = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[6]/div/div[1]/div[2]/div/div[2]/ul/li[2]/label')
            page7B.click()  # Centang radio button untuk opsi B
            print("Berhasil memilih opsi B di halaman kedua")
        elif page7_value == 3:
            page7C = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[6]/div/div[1]/div[2]/div/div[2]/ul/li[3]/label')
            page7C.click()  # Centang radio button untuk opsi C
            print("Berhasil memilih opsi C di halaman kedua")
        elif page7_value == 4:
            page7D = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[6]/div/div[1]/div[2]/div/div[2]/ul/li[4]/label')
            page7D.click()  # Centang radio button untuk opsi D
            print("Berhasil memilih opsi D di halaman kedua")

        botton7_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[6]/div/div[3]/ul/li[2]/span')
        botton7_next.click()
        time.sleep(2)


        if page8_value == 1:
            page8A = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[7]/div/div[1]/div[2]/div/div[2]/ul/li[1]/label')
            page8A.click()  # Centang radio button untuk opsi A
            print("Berhasil memilih opsi A di halaman kedua")
        elif page8_value == 2:
            page8B = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[7]/div/div[1]/div[2]/div/div[2]/ul/li[2]/label')
            page8B.click()  # Centang radio button untuk opsi B
            print("Berhasil memilih opsi B di halaman kedua")
        elif page8_value == 3:
            page8C = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[7]/div/div[1]/div[2]/div/div[2]/ul/li[3]/label')
            page8C.click()  # Centang radio button untuk opsi C
            print("Berhasil memilih opsi C di halaman kedua")
        elif page8_value == 4:
            page8D = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[7]/div/div[1]/div[2]/div/div[2]/ul/li[4]/label')
            page8D.click()  # Centang radio button untuk opsi D
            print("Berhasil memilih opsi D di halaman kedua")

        botton8_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[7]/div/div[3]/ul/li[2]/span')
        botton8_next.click()
        time.sleep(2)
        

        if page9_value == 1:
            page9A = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[8]/div/div[1]/div[2]/div/div[2]/ul/li[1]/label')
            page9A.click()  # Centang radio button untuk opsi A
            print("Berhasil memilih opsi A di halaman kedua")
        elif page9_value == 2:
            page9B = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[8]/div/div[1]/div[2]/div/div[2]/ul/li[2]/label')
            page9B.click()  # Centang radio button untuk opsi B
            print("Berhasil memilih opsi B di halaman kedua")
        elif page9_value == 3:
            page9C = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[8]/div/div[1]/div[2]/div/div[2]/ul/li[3]/label')
            page9C.click()  # Centang radio button untuk opsi C
            print("Berhasil memilih opsi C di halaman kedua")
        elif page9_value == 4:
            page9D = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[8]/div/div[1]/div[2]/div/div[2]/ul/li[4]/label')
            page9D.click()  # Centang radio button untuk opsi D
            print("Berhasil memilih opsi D di halaman kedua")

        botton9_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[8]/div/div[3]/ul/li[2]/span')
        botton9_next.click()
        time.sleep(2)

        if page10_value == 1:
            page10A = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[9]/div/div[1]/div[2]/div/div[2]/ul/li[1]/label')
            page10A.click()  # Centang radio button untuk opsi A
            print("Berhasil memilih opsi A di halaman kedua")
        elif page10_value == 2:
            page10B = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[9]/div/div[1]/div[2]/div/div[2]/ul/li[2]/label')
            page10B.click()  # Centang radio button untuk opsi B
            print("Berhasil memilih opsi B di halaman kedua")
        elif page10_value == 3:
            page10C = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[9]/div/div[1]/div[2]/div/div[2]/ul/li[3]/label')
            page10C.click()  # Centang radio button untuk opsi C
            print("Berhasil memilih opsi C di halaman kedua")
        elif page10_value == 4:
            page10D = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[9]/div/div[1]/div[2]/div/div[2]/ul/li[4]/label')
            page10D.click()  # Centang radio button untuk opsi D
            print("Berhasil memilih opsi D di halaman kedua")

        botton10_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[9]/div/div[3]/ul/li[2]/span')
        botton10_next.click()
        time.sleep(2)

        if page11_value == 1:
            page11A = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[10]/div/div[1]/div[2]/div/div/ul/li[1]/label')
            page11A.click()  # Centang radio button untuk opsi A
            print("Berhasil memilih opsi A di halaman kedua")
        elif page11_value == 2:
            page11B = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[10]/div/div[1]/div[2]/div/div/ul/li[2]/label')
            page11B.click()  # Centang radio button untuk opsi B
            print("Berhasil memilih opsi B di halaman kedua")
        elif page11_value == 3:
            page11C = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[10]/div/div[1]/div[2]/div/div/ul/li[3]/label')
            page11C.click()  # Centang radio button untuk opsi C
            print("Berhasil memilih opsi C di halaman kedua")
        elif page11_value == 4:
            page11D = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[10]/div/div[1]/div[2]/div/div/ul/li[4]/label')
            page11D.click()  # Centang radio button untuk opsi D
            print("Berhasil memilih opsi D di halaman kedua")

        botton10_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[10]/div/div[3]/ul/li[2]/span')
        botton10_next.click()
        time.sleep(2)

        if page11_value == 1:
            page11A = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[11]/div/div[1]/div[2]/div/div/ul/li[1]/label')
            page11A.click()  # Centang radio button untuk opsi A
            print("Berhasil memilih opsi A di halaman kedua")
        elif page11_value == 2:
            page11B = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[11]/div/div[1]/div[2]/div/div/ul/li[2]/label')
            page11B.click()  # Centang radio button untuk opsi B
            print("Berhasil memilih opsi B di halaman kedua")
        elif page11_value == 3:
            page11C = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[11]/div/div[1]/div[2]/div/div/ul/li[3]/label')
            page11C.click()  # Centang radio button untuk opsi C
            print("Berhasil memilih opsi C di halaman kedua")
        elif page11_value == 4:
            page11D = driver.find_element(By.XPATH, '//*[@id="wizard"]/div/div[11]/div/div[1]/div[2]/div/div/ul/li[4]/label')
            page11D.click()  # Centang radio button untuk opsi D
            print("Berhasil memilih opsi D di halaman kedua")

        botton10_next = driver.find_element(By.XPATH,'//*[@id="wizard"]/div/div[11]/div/div[3]/ul/li[2]/button')
        botton10_next.click()
        time.sleep(2)
        

        
    # Tutup browser setelah selesai mengisi data
    driver.quit()

# Panggil fungsi untuk menjalankan program
fill_form()
