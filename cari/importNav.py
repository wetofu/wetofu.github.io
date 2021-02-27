import os

# melist SEMUA file ekstensi .html kecuali BlackList

listFile = []
BlackList = ["../404.html", "../print.html"]
			# "../base/baseNav.html", 
			# "../cari/index.html", "../cari/baseNav.html", 
			# "../00-intro/baseNav.html", "../02-cybersec/baseNav.html", "../03-ctf/baseNav.html",
			# "../04-tips/baseNav.html", "../05-jarkom/baseNav.html", "../06-tools/baseNav.html",
			# "../07-robotics/baseNav.html"]
for root, dirs, files in os.walk("../"):
	for file in files:
		if file.endswith(".html"):
			tmp = os.path.join(root, file)
			tmp2 = tmp
			tmp3 = tmp2
			tmp3 = tmp3.replace('../', '').replace('.html', '').replace("00-intro/", "").replace("02-cybersec/", "").replace("03-ctf/", "").replace("04-tips/", "").replace("05-jarkom/", "").replace("06-tools/", "").replace("07-robotics/", "").replace("08-ujian/", "")
			if tmp not in BlackList and 'baseNav.html' not in tmp and 'index.html' not in tmp:
				tmp = tmp.replace(tmp, '<li class="chapter-item expanded'+' "><a href='+'"'+tmp2+'"'+'><span><strong aria-hidden="'+'true">'+tmp3+"</strong></span></a></li>")
				listFile.append(tmp)

listFile.sort()

total_isi = len(listFile)

firstTextLooking = "<!-- ----------------------------------------------- DIGANTI MENU ----------------------------------------------- -->"
endTextLooking = "<!-- ----------------------------------------------# DIGANTI MENU #---------------------------------------------- -->"

# mengambil isi mulai batas bawah nav, sampai akhir isi file
file1 = open("index.html", "rw+")
tmp = 0
for x in file1:
	tmp += len(x)
	if endTextLooking in x:
		global cari_seek
		cari_seek = tmp
file1.seek(cari_seek)
tampungAkhir = file1.read()

# mencari batas atas nav, lalu menghapus isi file mulai dari batas atas nav sampai akhir isi file 
cari_seek = 0
file1.seek(cari_seek)
cari_truncate = 0
for x in file1:
	cari_truncate += len(x)
	if firstTextLooking in x:		
		file1.truncate(cari_truncate)

file1.close()

# tamping = "Total topik :"
# finishing
file1 = open("index.html", "a")
file1.write("<h2>Total topik : "+str(total_isi)+"</h2>")
file1.write("\n")
file1.write("<div style='columns: 3;'>")
file1.write("\n")
file1.write("<ol class='chapter' id='myUL2'>")
file1.write("\n")
for x in listFile:
	file1.write(x)
	file1.write('\n')
file1.write(endTextLooking)
file1.write('\n')
file1.write(tampungAkhir)
file1.close()

