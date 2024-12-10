stack = ["menjalankan office word", "membuka google chrome", "menjalankan visual studio code"]
history = []

def aksi(item):
    stack.append(item)
    history.clear()
    print ("tambahkan aksi:", item)
    print("aksi setelah ditambahkan:", stack)

def undo():
    if  stack:
        item = stack.pop()
        history.append(item)
        print ("Undo:", item)
        print("aksi setelah di-Undo Stack:", stack)
    else:
        print ("Tidak ada tindakan yang bisa dilakukan!")


def redo():
    if stack:
        item = stack.pop()
        history.append(item)
        print ("Redo:", item)
        print("aksi setelah di-redo Stack:", stack)
    else:
        print ("Tidak ada tindakan yang bisa dilakukan!")

def hasil_stack():
    print ("Undo Stack:", stack)
    print ("Redo Stack:", history)  

while True:
    print ()
    print ("Uji coba Program Undo dan Redo")
    print ("1. Tambahkan aksi")
    print ("2. Undo")
    print ("3. Redo")
    print ("4. lihat stack undo dan redo")
    print ("5. Keluar")
    
    pilihan = input("Pilih Tindakan (1-5): ")
    if pilihan == '1':
        item = input ("Masukan item uji coba :")
        aksi (item)
    elif pilihan == '2' :
        undo ()
    elif pilihan == '3' :
        redo ()
    elif pilihan == '4' :
        hasil_stack()
    elif pilihan == '5' :
        print ("Keluar dari program")
        break
    else :
        print ("Pilihan tidak ada dalam daftar!")
