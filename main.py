from CreateSBD import *
from GetData import *
import requests
import json
import os , os.path

class main(object):
	"""docstring for main"""
	def __init__(self):
		super(main, self).__init__()
	
	def main(self):
		folder = "C:/Users/TanLoc/OneDrive - ut.edu.vn/Máy tính/THPTQG/Data"
		try:
			os.mkdir(folder)
			# os.system("mkdir C:/Users/TanLoc/OneDrive - ut.edu.vn/Máy tính/THPTQG/Data") #Tao thu muc Data trong drive
			print("Đã tạo thư mực lưu trữ trong đường dẫn  " + folder)
		except:
			print("Thư mực đã tồn tại !!!")
		filename = str(input("Nhap ten file can luu (vi du: diemthi2022.csv): ")) #tạo tên file lưu
		dir = os.path.join(folder, filename+'.csv')
		# dir = 'C:-Users-TanLoc-"OneDrive - ut.edu.vn"-Máy tính-THPTQG-Data'+filename

		number = 0
		i =0
		idTinh =1
		
		file = open(dir,mode="w+")
		file.write("sbd,toan,van,ngoaiNgu,vatLy,hoaHoc,sinhHoc,diemTBTuNhien,lichSu,diaLy,gdcd,diemTBXaHoi,\n")
		while True:
			SBD = CreateSBD(idTinh,number).create() #tao so bao danh 
			try:
				 #sử dụng ngoại lệ để khi số báo danh không có người thi thì sẽ không bị dừng process
				process = GetData(2022,SBD).rawData()
				if process["sbd"] == None:
					i += 1
					print(f"{SBD} không tồn tại {i} ")
				else:
					i = 0
					s = ""
					# process.pop("ListGroup") #xóa key ListGroup đi
					# process.pop("Result") #xóa key Result đi
				
					for key,mark in process.items():
						if mark  == None:
							mark = -1  #các điểm trống, tức môn không thi sẽ cho = -1
						s += str(mark) + "," #tạo format csv
					file.write(s+"\n")
					print(f"Đã Crawl {SBD} thành công!!")
			except:
				i += 1
				print(f"{SBD} không tồn tại!!! {i} ")
			number += 1
			if i==100: #khi chạy 100 thí sinh kế tiếp mà kh có dữ liệu thì chuyển qua mã tỉnh khác
				i =0
				idTinh += 1
				number =1
			if idTinh == 65: #vi ma tinh chay tu 1 den 64, nen qua 65 sẽ kết thúc
				break
		file.close()		

if __name__ == '__main__':
	main().main()