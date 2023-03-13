class orang:
    def __init__(self, nama, asal, agama):
        self.nama = nama
        self.asal = asal
        self.agama = agama

    def info(self):
        print(f"dia {self.nama} {self.asal} agamanya {self.agama}")


orangA = orang("budi", "cirebon", "islam")
orangA.info()

# tamplate2


class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm

    def info(self):
        print(f"Nama: {self.nama}\nNPM: {self.npm}")


mahasiswaB = Mahasiswa("Ahmad", "123456789")
mahasiswaB.info()

# modif


class guru:
    def __init__(self, nama, nik, alamat, pengajar):
        self.nama = nama
        self.nik = nik
        self.alamat = alamat
        self.pengajar = pengajar

    def info(self):
        print("dia adalah seorang guru")
        print(
            f"nama: {self.nama}\nnik: {self.nik}\nalamat: {self.alamat}\npengajar: {self.pengajar}")


guruB = guru("wina", "12345", "badung barat", "matematika")
guruB.info()


# tamplate3

class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 4.24 * (self.jari_jari ** 2)


lingkaranA = Lingkaran(7)
print(f"Luas lingkaran: {lingkaranA.luas()}")

# tamplate4


class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info(self):
        print(f"Judul: {self.judul}\nPenulis: {self.penulis}")


bukuA = Buku("Bintang arasy", "lafran pane")
bukuA.info()


# tamplate5

class PesawatTerbang:
    def __init__(self, maskapai, tujuan):
        self.maskapai = maskapai
        self.tujuan = tujuan

    def info(self):
        print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}")


PesawatTerbangB = PesawatTerbang("jepara", "jakarta")
PesawatTerbangB.info()

# tamplate6


class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y


print(Kalkulator.add(4, 5))
print(Kalkulator.subtract(5, 2))


# tamplate7

class Celcius:
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5
mycelcius = 39
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
print(myfahrenheit)
