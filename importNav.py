import os

# melist SEMUA file ekstensi .html
listFile = []
listBase = ["base/baseNav.html", "base/tesbase.html", "base/base.html"]
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
             tmp = os.path.join(root, file)
             tmp = tmp.replace('./', '')
             if tmp not in listBase:
	             listFile.append(tmp)

# jika ada file < 10byte (kosong/baru), maka akan diisi file base/base.html
FileBase = open("base/base.html", "r")
isi_fileBase = FileBase.read()
FileBase.close()
for file in listFile:
	if os.stat(file).st_size < 10:
		isi = open(file, "w")
		isi.write(isi_fileBase)
		isi.close()

# mengisi NAV ke file yg belum ada NAV-nya			
baseFile = "base/baseNav.html"
firstTextLooking = "<!-- ---------------------------------------- NAV ---------------------------------------- -->"
endTextLooking = "<!-- ---------------------------------------# NAV #--------------------------------------- -->"
for file in listFile:
	# membuka akhir teks file yg akan diganti, lalu truncate sblm nav
	file1 = open(file, "rw+")
	tmp = 0
	for x in file1:
		tmp += len(x)
		if endTextLooking in x:	# ini diganti
			global cari_seek
			cari_seek = tmp
	file1.seek(cari_seek)
	tampungAkhir = file1.read()

	cari_seek = 0
	file1.seek(cari_seek)
	cari_truncate = 0
	for x in file1:
		cari_truncate += len(x)
		if firstTextLooking in x:		# ini diganti
			file1.truncate(cari_truncate)

	file1.close()

	# mengambil base Nav
	base = open(baseFile, "r")
	bs = base.read()

	# finishing
	file1 = open(file, "a")
	file1.write(bs)
	file1.write('\n')
	file1.write(tampungAkhir)
	file1.close()

	# menambah highlight warna rgb(255, 115, 138)
	file1 = open(file, "r")
	repairing = file1.read()
	file1.close()

	file1 = open(file, "w")
	repairing = repairing.replace('<a href="../'+file+'">', '<a href="../'+file+'" style="color: rgb(255, 115, 138);">')
	file1.write(repairing)
	file1.close()

pembersihan = ["index.html", "print.html"]
for x in pembersihan:
	ind = open(x, "r")
	bersihkan = ind.read()
	bersihkan = bersihkan.replace("../", "")
	ind.close()

	ind = open(x, "w")
	ind.write(bersihkan)
	ind.close()

