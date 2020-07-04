##########
# kalenderjawa.py
# ========
# Script Python untuk menkonversi Penanggalan Masehi - Penanggalan Jawa Walisongo
# serta fitur-fitur tambahan lainnya.
##########


# Impor library yang diprelukan
# Script ini mencoba untuk membuat dependensi seminimal mungkin.

from datetime import date, timedelta


class Tgl:
    """Tgl sebagai superclass"""


    def __init__(self, yy, mm, dd):
        """Attribute untuk Class Tgl
        Attr:
            yy (int) : tahun
            mm (int) : bulan
            dd (int) : hari
            n (int)  : arbritari, digunakan untuk penghitungan selisih (lihat fungsi pendhak)
            e (date) : Tanggal Epoch, hari pertama penanggalan islam Jawa
                       dalam penanggalan Masehi (Gregorian)
        """
        self.dd = dd
        self.mm = mm
        self.yy = yy
        #self.n = n
        self._e = date(1354, 2, 3)

        self.delta = None
        self._w210 = None
        self._erajawa = None
        self._eramasehi = None

        """
        Library: untuk penamaan dan penghitungan dalam siklus pawukon
        """
        self.w5 = ["Pahing", "Pon", "Wage", "Kliwon", "Legi"]
        self.w6 = ["Tungle", "Aryang", "Wurukung", "Paningron", "Uwas", "Mawulu"]
        self.w7 = ["Ahad", "Senen", "Selasa", "Rebo", "Kemis", "Jemuah", "Setu", "Ahad"]
        self.w30 = [
            "Sinta", "Landep", "Wukir", "Kurantil", "Tolu",
            "Gumbreng", "Warigalit", "Warigagung", "Julungwangi", "Sungsang",
            "Galungan", "Kuningan", "Langkir", "Mandhasiya", "Julungpujud",
            "Pahang", "Kuruwelut", "Marakeh", "Tambir", "Madangkungan",
            "Maktal", "Wuye", "Manail", "Prangbakat", "Bala",
            "Wugu", "Wayang", "Kulawu", "Dhukut", "Watugunung"]
        self.n7 = [5, 4, 3, 7, 8, 6, 9]
        self.n5 = [9, 7, 4, 8, 5]

        """
        Library: untuk penamaan panjang
        """
        self.mmmm = ["Desember", "Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
            "Agustus", "September", "Oktober", "Nopember", "Desember"]
        self.sasi = [
            None, "Sura", "Sapar", "Mulud", "Bakda Mulud", "Jumadil Awal", "Jumadil Akir",
            "Rejeb", "Ruwah", "Pasa", "Sawal", "Apit", "Besar"]
        self.taun = ["Alip", "Ehe", "Jimawal", "Je", "Dal", "Be", "Wawu", "Jimakir"]
        self.tumbuk = ["Kuntara", "Sengara", "Sancaya", "Adi"]
        self.kabisat = [0, 1, 0, 0, 1, 0, 0, 1]

        """
        Library: untuk penghitungan mangsa
        """
        self.ka = ["Kasanga", "Kasepuluh", "Desta", "Sada", "Kasa", "Karo",
            "Katelu", "Kapat", "Kalima", "Kanem", "Kapitu", "Kawolu"]
        self.umurka = [25, 24, 23, 41, 41, 23, 24, 25, 27, 43, 43, 27]


    def set_era(self):
        '''Digunakan untuk menyajikan nilai era dalam suatu list yang akan digunakan 
        dalam perhitungan lebih lanjut.
        Return:
        erajawa (list) terdiri atas:
            [0] Kurup, 120 tahun (8 windu, 42524 hari)
            [1] Windu, 8 tahun (2835 hari)
            [2] Taun, 1 tahun kalender (354/355 hari)
            [3] Sasi, 1 bulan (29/30 hari)
            [4] Hari
            Nilai didapatkan dari selisih tanggal terhadap hari epoch(self._e)
       ._eramasehi (list) terdiri atas:
            [0] Tahun
            [1] Bulan
            [2] Hari
            Nilai didapatkan dari posisi tanggal dalam penanggalan gregorian proleptik.
            (selengkapnya: )
            
        '''
        if self.delta is None:
            pass
        else:
            deltajawa = deltamasehi = self.delta

            erajawa = [0, 0, 0, 0, 0]
            erajawa[0], deltajawa = deltajawa // 42524, deltajawa % 42524
            erajawa[1], deltajawa = deltajawa // 2835, deltajawa % 2835
            erajawa[2], deltajawa = int((deltajawa + 0.625) // 354.375), int((deltajawa + 0.625) % 354.375)
            erajawa[3], erajawa[4] = int(deltajawa // 29.5), int(deltajawa % 29.5)        

            if erajawa[3] == 12:
                erajawa[3], erajawa[4] = 11, 29

            self._erajawa = erajawa

            eramasehi = self._e + timedelta(days=deltamasehi)
            eramasehi = [eramasehi.year, eramasehi.month, eramasehi.day]

            self._eramasehi = eramasehi


    def neptu(self, mode=35):
        '''Mengembalikan nilai neptu pada tanggal tertentu
        Args:
            mode = 5 untuk neptu pasaran, 7 untuk neptu hari, 35 untuk neptu selapanan
        Return: (int)
        '''
        if self._w210 is None:
            return "ERROR:Tanggal berada di luar jangkauan!"
        else:
            dct = {
                5:self.n5[self._w210 % 5],
                7:self.n7[self._w210 % 7],
                35:(self.n7[self._w210 % 7] + self.n5[self._w210 % 5])
            }

            try:
                return(dct[mode])
            except Exception as e:
                return e.args


    def pawukon(self, mode=35):
        '''Mengembalikan nama komponen pawukon dalam siklus 210 hari jawa.
        Args:
            Mode = 
                5 untuk nama pasaran
                6 untuk nama paringkelan
                7 untuk nama dina/hari
                35 untuk nama weton (hari dan pasaran)
                210 untuk nama wuku
        Return (str)
        '''
        if self._w210 is None:
            return "ERROR:Tanggal berada di luar jangkauan!"
        else:
            dct = {
                5:self.w5[self._w210 % 5],
                6:self.w6[self._w210 % 6],
                7:self.w7[self._w210 % 7],
                35:"{} {}".format(self.w7[self._w210 % 7], self.w5[self._w210 % 5]),
                210:self.w30[self._w210 // 7]
            }

            try:
                return(dct[mode])
            except Exception as e:
                return e.args


    def tgljawa(self, weton=True, tanggal=True, windu=True, wuku=False):
        '''Mengembalikan tanggal jawa untuk tanggal tertentu
        Args:
            weton = menampilkan nama weton
            tanggal = menampilkan tanggal
            windu = menampulkan nama windu
            wuku = menampilkan nama wuku
        Return (string)
        '''
        txt = ""
        y = 1267 + self._erajawa[0] * 120 + self._erajawa[1] * 8 + self._erajawa[2]
        
        if weton:
            txt += "{}, ".format(self.pawukon())

        if tanggal:
            txt += "{} {} {} {}".format(self._erajawa[4]+1, self.sasi[self._erajawa[3]+1], 
                    y, self.taun[self._erajawa[2]])

        if windu:
            txt += " Windu {}".format(self.tumbuk[(15*self._erajawa[0] + self._erajawa[1]) % 4])

        if wuku:
            txt += " Wuku {}".format(self.pawukon(210))

        return txt


    def tglmasehi(self, weton=True, wuku=False):
        '''Mengembalikan tanggal masehiuntuk tanggal tertentu
        Args:
            windu = menampulkan nama windu
            wuku = menampilkan nama wuku
        Return (string)
        '''
        txt = ""
        
        if weton:
            txt += "{}, ".format(self.pawukon())

        txt += "{} {} {}".format(self._eramasehi[2], self.mmmm[self._eramasehi[1]],
                self._eramasehi[0])

        if wuku:
            txt += " Wuku {}".format(self.pawukon(210))

        return txt


    def pendhak(self, dina=0, taun=0, form='masehi'):
        '''mencari jatuhnya hari setelah kejadian.
        sering digunakan untuk selamatan orang meninggal.
        Args:
            dina = berapa hari setelah kejadian
            taun = berapa tahun setelah kejadian
            format = mengembalikan dalam tahun jawa/masehi
        Return (string)
        '''
        n = self.delta
        era = self._erajawa[2]
        n += dina
        n += (354*taun) + sum([self.kabisat[(era+i) % 8] for i in range(taun)])
        _newdate = self._e + timedelta(n-1)
        _date = masehi(_newdate.year, _newdate.month, _newdate.day)
        if form == 'masehi':
            return _date.tglmasehi()
        elif form == 'jawa':
            return _date.tgljawa()



    def mangsa(self):
        '''Mengembalikan hari dan mangsa pada suatu tanggal masehi maupun jawa'''
        pass
        sasi = (self._eramasehi[1] + 9) % 12
        umur = 31*sasi - sum([(i%5)%2 for i in range(sasi)]) + self._eramasehi[2]
        sasi = -1
        while umur > 0:
            sasi += 1
            umur -= self.umurka[sasi]
        umur += self.umurka[sasi]
        return "{} {}".format(umur, self.ka[sasi])


class masehi(Tgl):
    """Class untuk tanggal masehi.
    Args:
    yy (int) tahun
    mm (int) bulan (1-12)
    dd (int) tanggal
    """

    def __init__(self, yy, mm, dd):
        Tgl.__init__(self, yy, mm, dd)
        self.d = date(self.yy, self.mm, self.dd)
        self.set_element()
        self.set_era()

    
    def set_element(self):
        delta, fix = (self.d - self._e).days, 196
        if delta >= 0: self.delta = delta
        if delta >= 0: self._w210 = (delta + fix) % 210


class jawa(Tgl):
    """Class untuk tanggal Jawa.
    Args:
    yy (int) tahun
    mm (int) bulan (1-12)
    dd (int) tanggal
    """

    def __init__(self, yy, mm, dd):
        Tgl.__init__(self, yy, mm, dd)
        self.d = "{}-{:0>2d}-{:0>2d} AJ".format(yy, mm, dd)
        self.set_element()
        self.set_era()


    def set_element(self):
        y, m, d = self.yy - 1267, self.mm - 1, self.dd - 1
        delta, fix, dlist = 0, 196, [0,0,0]
        dlist[0], y = y // 120, y % 120
        dlist[1], dlist[2] = y // 8, y % 8

        delta += dlist[0] * 42524
        delta += dlist[1] * 2835
        delta += (dlist[2] * 354) + ((dlist[2]+1) // 3)
        delta += (m*29) + ((m+1) // 2)
        delta += d
        delta += self.n

        if delta >= 0: self.delta = delta
        if delta >= 0: self._w210 = (delta + fix) % 210
