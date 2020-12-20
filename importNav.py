listFile = ["index.html", "print.html", "00-intro/index.html", "00-intro/inf.html", "00-intro/kimia.html", 
			"02-cybersec/deepweeb.html", "02-cybersec/footprinting.html", "02-cybersec/index.html", 
			"02-cybersec/tcpip.html", "03-ctf/index.html", "03-ctf/binex.html", "03-ctf/binex-pwnshell.html", "03-ctf/assembly.html",  
			"04-tips/index.html", "05-jarkom/networking.html", "05-jarkom/basicdatasec.html", "05-jarkom/cmlNwireshark.html", 
			"05-jarkom/dsnpi.html", "05-jarkom/email.html", "05-jarkom/hacking.html", "05-jarkom/index.html", "05-jarkom/ipv6.html", 
			"05-jarkom/keamananJar.html", "05-jarkom/nlipv4.html", "05-jarkom/nmb.html", "05-jarkom/pemjar.html", 
			"05-jarkom/pendahuluan.html", "05-jarkom/pkjdll.html", "05-jarkom/pwwi.html", "05-jarkom/rnat.html", 
			"05-jarkom/simJar.html", "05-jarkom/sm.html", "05-jarkom/tl.html", "05-jarkom/voip.html", "05-jarkom/webcms.html", 
			"06-tools/nmap.html", "06-tools/index.html"]	# ini diisi file oprec
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

ind = open("index.html", "r")
bersihkan = ind.read()
bersihkan = bersihkan.replace("../", "")
ind.close()

ind = open("index.html", "w")
ind.write(bersihkan)
ind.close()








