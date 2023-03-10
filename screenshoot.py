# Import Package Selenium dan memanggil module webdriver ==========================================
from selenium import webdriver #Webdriver untuk Chrome
from selenium.webdriver.common.keys import Keys #Di Gunakan untuk Keys.ENTER
from selenium.webdriver.common.by import By #Di Gunakan untuk By.CSS_SELECTOR/XPATH
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import datetime

# Ini adalah Dictionary dengan satu Key dan banyak Value (Database) ==============================
interface = {
        "BCALC1" : ['10.68.68.2','10.68.68.2%2F19','./Capture link IP Sec/BCALC1/','BCALC1'],
        "BCALC1_2" : ['10.68.68.3','10.68.68.3%2F19','./Capture link IP Sec/BCALC1/','BCALC1'],
        "BSD" : ['10.63.140.3','10.63.140.3%2F14','./Capture link IP Sec/BSD/','BSD'],
        "BSD_2" : ['10.63.140.4','10.63.140.4%2F14','./Capture link IP Sec/BSD/','BSD'],
        "CPC" : ['10.64.0.29','10.64.0.29%2F14','./Capture link IP Sec/CPC/','CPC'],
        "CPC_2" : ['10.64.0.30','10.64.0.30%2F14','./Capture link IP Sec/CPC/','CPC'],
        "FOR" : ['10.61.0.1','10.61.0.1%2F14','./Capture link IP Sec/FOR/','FOR'],
        "FOR_2" : ['10.61.0.2','10.61.0.2%2F14','./Capture link IP Sec/FOR/','FOR'],
        "GSW" : ['10.70.4.1','10.70.4.1%2F11','./Capture link IP Sec/GSW/','GSW'],
        "GSW_2" : ['10.70.4.2','10.70.4.2%2F11','./Capture link IP Sec/GSW/','GSW'],
        "HSB" : ['10.66.128.1','10.66.128.1%2F13','./Capture link IP Sec/HSB/','HSB'],
        "HSB_2" : ['10.66.128.2','10.66.128.2%2F13','./Capture link IP Sec/HSB/','HSB'],
        "JDL" : ['10.70.0.1','10.70.0.1%2F11','./Capture link IP Sec/JDL/','JDL'],
        "JLD_2" : ['10.70.0.2','10.70.0.2%2F11','./Capture link IP Sec/JDL/','JDL'],
        "LMP" : ['10.69.0.29','10.69.0.29%2F12','./Capture link IP Sec/LMP/','LMP'],
        "LMP_2" : ['10.69.0.30','10.69.0.30%2F13','./Capture link IP Sec/LMP/','LMP'],
        "MJP" : ['10.66.64.1','10.66.64.1%2F0','./Capture link IP Sec/MJP/','MJP'],
        "MJP_2" : ['10.66.64.2','10.66.64.2%2F0','./Capture link IP Sec/MJP/','MJP'],
        "SMG2" : ['10.65.0.1','10.65.0.1%2F3','./Capture link IP Sec/SMG2/','SMG2'],
        "SMG2_2" : ['10.65.0.2','10.65.0.2%2F3','./Capture link IP Sec/SMG2/','SMG2'],
        "TCM" : ['10.70.8.1','10.70.8.1%2F9','./Capture link IP Sec/TCM/','TCM'],
        "TCM_2" : ['10.70.8.2','10.70.8.2%2F9','./Capture link IP Sec/TCM/','TCM'],
        "WBCA" : ['10.60.31.29','10.60.31.29%2F12','./Capture link IP Sec/WBCA-PI/','WBCA'],
        "WBCA_2" : ['10.60.31.30','10.60.31.30%2F12','./Capture link IP Sec/WBCA-PI/','WBCA']  
}

name_interface = [
    "BCALC1", "BCALC1_2", "BSD", "BSD_2", "CPC" , "CPC_2" , "FOR" , "FOR_2", "GSW" , "GSW_2", "HSB" , "HSB_2",
    "JDL" ,"JLD_2","LMP" ,"LMP_2","MJP" ,"MJP_2","SMG2","SMG2_2","TCM" ,"TCM_2","WBCA","WBCA_2"
]

month = {
    '1' :'Januari', '2' :'Februari', '3' :'Maret', '4' :'April', '5' :'Mei', '6' :'Juni', '7' :'Juli',
    '8' :'Agustus', '9' :'September', '10' :'Oktober', '11' :'November', '12' :'Desember'
}


# Kumpulan Fungsi ================================================================================
# Fungsi Clear CMD
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Fungsi untuk Membuat Folder
def crt_folder(direc):
    newpath = (direc)
    if not os.path.exists(newpath):
             os.makedirs(newpath)

# Fungsi untuk Screenshoot Harian
def loop (ip1:(str), ip2:(str), lokasi:(str), nama:(str)):
    web = 'http://10.38.3.25/report.jsp?templid=_if&output=chart&device=' + ip1 + '&if=' + ip2 + '&chartTitle=Traffic+Rate'
    driver.get(web+'&stime='+ str(int(epoch_time)) + '&etime=' + str(int(epoch_time2)) + '&sample_nunits=1&sample_unit=minute')
    driver.set_window_size(782, 768)
    wait_element = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'overlay')))
    time.sleep(1)
    element = driver.find_element('name','rep_form')
    crt_folder(lokasi+ f'{tahun}/' + str.title(month[month_s]))
    if (i % 2 == 0):
        element.screenshot(lokasi+ f'{tahun}/' + str.title(month[month_s]) + '/' + str(tgl_file)+f'-{tahun}_'+nama+'-WAN-IPSEC1_traffic.png')
    else:
        element.screenshot(lokasi+ f'{tahun}/' + str.title(month[month_s]) + '/' + str(tgl_file)+f'-{tahun}_'+nama+'-WAN-IPSEC2_traffic.png') 

# Fungsi untuk Screenshoot Custom
def loop2 (ip1:(str), ip2:(str), lokasi:(str), nama:(str)):
    if recog == 'Y':
        if io == 'IN':
            web = 'http://10.38.3.25/report.jsp?templid=0026&output=chart&device=' + ip1 + '&if=' + ip2 + '&chartTitle=Traffic+Rate&drilldown_filter=inif%3D'+ip2
        else:
            web = 'http://10.38.3.25/report.jsp?templid=0026&output=chart&device=' + ip1 + '&if=' + ip2 + '&chartTitle=Traffic+Rate&drilldown_filter=outif%3D'+ip2
    else:
        web = 'http://10.38.3.25/report.jsp?templid=_if&output=chart&device=' + ip1 + '&if=' + ip2 + '&chartTitle=Traffic+Rate'
    driver.get(web+'&stime='+ str(int(epoch_time)) + '&etime=' + str(int(epoch_time2)) + '&sample_nunits=1&sample_unit=minute')

    if recog == 'Y':
        driver.set_window_size(800, 900)
    else:
        driver.set_window_size(782, 768)
    wait_element = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'overlay')))
    time.sleep(1)
    element = driver.find_element('name','rep_form')
    crt_folder(lokasi+ f'{tahun}/' + 'Backup')

    if io == "IN" and ipsec == "1":
        element.screenshot(lokasi+ f'{tahun}/' + 'Backup' + '/' + str(tgl_file)+f'-{tahun}_'+nama+'-WAN-IPSEC1_traffic_IN.png')
    elif io == "IN" and ipsec == "2":
        element.screenshot(lokasi+ f'{tahun}/' + 'Backup' + '/' + str(tgl_file)+f'-{tahun}_'+nama+'-WAN-IPSEC2_traffic_IN.png')
    elif io == "OUT" and ipsec == "1":
        element.screenshot(lokasi+ f'{tahun}/' + 'Backup' + '/' + str(tgl_file)+f'-{tahun}_'+nama+'-WAN-IPSEC1_traffic_OUT.png')
    elif io == "OUT" and ipsec == "2":
        element.screenshot(lokasi+ f'{tahun}/' + 'Backup' + '/' + str(tgl_file)+f'-{tahun}_'+nama+'-WAN-IPSEC2_traffic_OUT.png')
    elif io == None and ipsec == "1":
        element.screenshot(lokasi+ f'{tahun}/' + 'Backup' + '/' + str(tgl_file)+f'-{tahun}_'+nama+'-WAN-IPSEC1_traffic.png')
    elif io == None and ipsec == "2":
        element.screenshot(lokasi+ f'{tahun}/' + 'Backup' + '/' + str(tgl_file)+f'-{tahun}_'+nama+'-WAN-IPSEC2_traffic.png')


pertanyaan = 'Y'
while(pertanyaan == 'Y'):
    while True:
        try:
            # Login
            print('==============================')
            username = input("MASUKAN USERNAME : ")
            password = input("MASUKAN PASSWORD : ")
            cls()

            # Input Pilihan Custom -----------------------------
            print('============================')
            print('1. Screenshoot Harian')
            print('2. Screenshoot Custom')
            print('============================')
            pilihan = input('Masukan Pilihan : ')
            if pilihan == "2" :
                io = None
                print('\n========== DEVICE NAME ===========')
                for x in range (len(name_interface)):
                    if x % 12 == 0 and x != 0:
                        print()

                    if x % 2== 0:
                        print(name_interface[x],end=', ')
                print('\n==================================')
                device =  str(input('Masukan Device(Ex.FOR/CPC) : '))
                ipsec = str(input('Pilih IPSEC (1-2) : '))
                recog = str.upper(input('Recognized Applications (Y/N) : '))
                if recog == 'Y':
                        io = str.upper(input('IN / OUT ? : '))

            # Input Data Waktu Netflow --------------------------
            print('\n==== Masukan Waktu Awal ====')
            waktu = str(input("Masukan Tanggal (2022/12/30) : ")) #ini akan Split [2022] [12] [30]
            waktu_s = waktu.split('/')

            jam = input("Masukan Jam (24.00) : ") #nanti akan mendapatkan nilai [07] [00]
            jam_s = jam.split('.')

            print('\n==== Masukan Jam Akhir ====')
            jam2 = input("Masukan Jam (24.00) : ")  #nanti akan mendapatkan nilai [19] [00]
            jam2_s = jam2.split('.')

            # -------------------------------------------------------------------------------------------------
            int_month_s = int(waktu_s[1]) #Ambil Data String Waktu_s [01] menjadi Nilai Integer [1]
            month_s = str(int_month_s) #Fungsinya Menghilangkan angka 0 di awal, lalu di Ubah ke Str
            int_day = int(waktu_s[2]) #dan Ini mengambil tanggal dan mengubahnya ke int
            tgl_file = str.upper(str(int_day) +'-'+ month[month_s]) #int_day berubah nilai dari Int ke Str
            # -------------------------------------------------------------------------------------------------

            tahun = (str(waktu_s[0])) #Variabel Tahun Untuk di pakai pada Fungsi Crt_Folder

            epoch_time = datetime.datetime(int(waktu_s[0]),int(waktu_s[1]), int(waktu_s[2]), int(jam_s[0]), int(jam_s[1]), 0).timestamp()*1000
            epoch_time2 = datetime.datetime(int(waktu_s[0]),int(waktu_s[1]), int(waktu_s[2]), int(jam2_s[0]), int(jam2_s[1]), 0).timestamp()*1000

        #Jika Terjadi Error 
        except ValueError:
            print('\n===================================')
            print("INPUT YANG ANDA MASUKAN SALAH !!!")
            print('===================================')
            time.sleep(1)
            cls()
            continue
        except IndexError:
            print('\n===================================')
            print("INPUT YANG ANDA MASUKAN SALAH !!!")
            print('===================================')
            time.sleep(1)
            cls()
            continue
        else:
            break
    #==============================================================================================================

    # Deklarasi webdriver & Tampilan Windows Maksimal ====================
    driver = webdriver.Chrome()
    driver.maximize_window()    


    # Login ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    driver.get('http://10.38.3.25/login/login.jsp')
    driver.find_element('name','j_username').send_keys(username)
    driver.find_element('name','j_password').send_keys(password + Keys.ENTER)
        
    # Kondisi dan Aksi Loop sesuai Input=========================================================================
    if pilihan == "2":
        if ipsec == "2":
            choice = interface[device + "_2"]
        else:
            choice = interface[device]
        # Looping (for IP - Location Folder - Name)
        loop2(choice[0], choice[1], choice[2], choice[3])
        time.sleep(2)
        cls()
        driver.minimize_window()
        pertanyaan = input(str.upper('Apakah Anda Ingin Lanjut(Y/T) : '))    
        
    elif pilihan == '1':
        # Looping (for IP - Location Folder - Name)
        for i in range(len(name_interface)):
            a = name_interface[i]
            choice = interface[a]
            loop(choice[0], choice[1], choice[2], choice[3])
        time.sleep(2)
        cls()
        driver.minimize_window()
        pertanyaan = input(str.upper('Apakah Anda Ingin Lanjut(Y/T) : '))    

# Keluar aplikasi 
driver.quit()  
