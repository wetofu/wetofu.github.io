import os

# melist SEMUA file ekstensi .html kecuali listBase
listFile = []
listBase = ["baseNav.html"]
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
             tmp = os.path.join(root, file)
             tmp = tmp.replace('./', '')
             if tmp not in listBase:
	             listFile.append(tmp)

# jika ada file < 10byte (kosong/baru), maka akan diisi base/base.html
FileBase = open("../base/index.html", "r")
isi_fileBase = FileBase.read()
FileBase.close()
for file in listFile:
	if os.stat(file).st_size < 10:
		isi = open(file, "w")
		isi.write(isi_fileBase)
		isi.close()

# mengisi &/ mengganti NAV ke listFile
baseFile = "baseNav.html"
firstTextLooking = "<!-- ---------------------------------------- NAV ---------------------------------------- -->"
endTextLooking = "<!-- ---------------------------------------# NAV #--------------------------------------- -->"
for file in listFile:
	# mengambil isi mulai batas bawah nav, sampai akhir isi file
	file1 = open(file, "rw+")
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
	repairing = repairing.replace('<a href="'+file+'">', '<a href="'+file+'" style="color: rgb(255, 115, 138);">')
	file1.write(repairing)
	file1.close()


