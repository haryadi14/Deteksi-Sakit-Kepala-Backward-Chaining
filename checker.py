# Inisialisasi variabel yang digunakan dalam sistem pakar
gejala = {
    'mual': False,
    'pusing': False,
    'migrain': False,
    'tekanan_darah_tinggi': False,
    'mata_berair': False
}

# Aturan-aturan yang digunakan dalam sistem pakar
aturan = {
    'A': ['mual', 'pusing'],
    'B': ['migrain', 'mata_berair'],
    'C': ['tekanan_darah_tinggi'],
    'D': ['A', 'C'],
    'E': ['B', 'C']
}

# Fungsi untuk menghasilkan hasil diagnosis
def diagnosis():
    if gejala['migrain'] and gejala['mata_berair'] and gejala['tekanan_darah_tinggi']:
        return 'Anda menderita migrain dengan tekanan darah tinggi'
    elif gejala['mual'] and gejala['pusing'] and gejala['tekanan_darah_tinggi']:
        return 'Anda menderita sakit kepala karena tekanan darah tinggi'
    else:
        return 'Maaf, kami tidak bisa menentukan penyebab sakit kepala Anda'

# Fungsi untuk melakukan backward chaining
def backward_chaining(goal):
    if gejala[goal]:
        return True
    else:
        for k in aturan.keys():
            if goal in aturan[k]:
                print(f"Apakah Anda memiliki gejala {k}? (y/n)")
                jawaban = input()
                if jawaban == 'y':
                    for g in aturan[k]:
                        if not backward_chaining(g):
                            return False
                    gejala[goal] = True
                    return True
        return False

# Main program
print("Selamat datang di sistem pakar diagnosis sakit kepala.")
print("Silakan jawab pertanyaan berikut untuk membantu kami mendiagnosis Anda.")

for g in gejala.keys():
    print(f"Apakah Anda memiliki gejala {g}? (y/n)")
    jawaban = input()
    if jawaban == 'y':
        gejala[g] = True

if backward_chaining('migrain'):
    print(diagnosis())
elif backward_chaining('A'):
    print(diagnosis())
elif backward_chaining('B'):
    print(diagnosis())
elif backward_chaining('C'):
    print(diagnosis())
else:
    print(diagnosis())
