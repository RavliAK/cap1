from prettytable import PrettyTable

karyawan=[
    ['001','bagas', 20, 'male', 10000],
    ['002','budi', 25, 'male', 10000],
    ['003','lucy', 20, 'female', 10000]
         ]


def display(x):
    while(True):
        
        print('menu display \n\nlist menu:\n1.tampilkan semua karyawan\n2.cari data karyawan(id)\n3.filter data\n4.back to previous menu')
        menu=input('masukan angka menu: ')
        if menu.isdigit()==True and len(menu)==1:
            menu=int(menu)
        if menu==1:
            table = PrettyTable()
            table.field_names = ["ID", "NAMA", "UMUR", "JENIS KELAMIN", 'GAJI']

            if len(x)!=0:
                for i in range(len(x)):
                    table.add_row([x[i][0],x[i][1],x[i][2],x[i][3],x[i][4]])
                print (table)
            else:
                print('\ndata empty\n')
        elif menu==2:
            if  len(x)==0:
                print('\ndata empty\n')
            else:
                search=input('masukkan ID karyawan(3 digits): ')
                while search.isdigit()==False or len(search)!=3:
                    print('\nFormat ID salah\n')
                    search=input('masukkan ID karyawan(3 digits): ')
                for i in range(len(x)):
                    if len(x)==0:
                        print('\ndata empty\n')
                    elif(x[i][0]==search):
                        print(f'\nID={x[i][0]}\nnama={x[i][1]}\numur={x[i][2]}\njenis kelamin={x[i][3]}\ngaji(per jam)={x[i][4]}')
                        break
                    elif i==len(x)-1:
                        print('karyawan tidak ditemukan')
        elif menu==3:
            if len(x)==0:
                print('\ndata empty\n')
            else:
                new=[]
                table = PrettyTable()
                table.field_names = ["ID", "NAMA", "UMUR", "JENIS KELAMIN", 'GAJI']
                filter=input('filter by:\n1.nama\n2.umur\n3.jenis kelamin\n4.gaji\npick one[input number]: ')
                while filter.isdigit()==False or len(filter)!=1:
                    filter=input('input salah\nfilter by:\n1.nama\n2.umur\n3.jenis kelamin\n4.gaji\npick one[input number]: ')
                filter=int(filter)
                if filter==1:
                    nama=input('masukkan nama yang dicari: ')
                    while(nama.replace(' ','').isalpha()==False):
                        nama=input('input salah\nmasukkan nama yang dicari: ')
                    for i in range(len(x)):
                        if(x[i][1].find(nama)!=-1):
                            new.append(x[i])
                    
                if filter==2:
                    paramater=input('pilih parameter filter\n1.filter umur >= nilai x\n2.filter umur <= nilai x\npick one[input number]: ')
                    while paramater.isdigit()==False or (int(paramater)<1 or int(paramater)>2):
                        paramater=input('input salah\npilih parameter filter\n1.filter umur >= nilai x\n2.filter umur <= nilai x\npick one[input number]: ')
                    paramater=int(paramater)
                    umur=input('masukkan nilai x: ')
                    while(umur.isdigit()==False):
                        umur=input('input salah\nmasukkan nilai x: ')
                    umur=int(umur)
                    if paramater==1:
                        for i in range(len(x)):
                            if(x[i][2]>=umur):
                                new.append(x[i])
                    elif paramater==2:
                        for i in range(len(x)):
                            if(x[i][2]<=umur):
                                new.append(x[i])
                    
                if filter==3:
                    kel=input('masukkan jenis Kelamin karyawan yang dicari(M/F): ')
                    kel=kel.upper()
                    while kel.isalpha()!=True or len(kel)!=1 or (kel!='M' and kel!='F'):
                        kel=input('input salah\nmasukkan jenis Kelamin karyawan yang dicari(M/F): ')
                        kel=kel.upper()
                    if(kel=='F'):
                        for i in range(len(x)):
                            if(x[i][3]=='female'):
                                new.append(x[i])
                    elif(kel=='M'):
                        for i in range(len(x)):
                            if(x[i][3]=='male'):
                                new.append(x[i])
                                
                if filter==4:
                    paramater=input('pilih parameter filter\n1.filter gaji >= nilai x\n2.filter gaji <= nilai x\npick one[input number]: ')
                    while paramater.isdigit()==False or (int(paramater)<1 or int(paramater)>2):
                        paramater=input('input salah\npilih parameter filter\n1.filter gaji >= nilai x\n2.filter gaji <= nilai x\npick one[input number]: ')
                    paramater=int(paramater)
                    gaji=input('masukkan nilai x: ')
                    while(gaji.isdigit()==False):
                        gaji=input('input salah\nmasukkan nilai x: ')
                    gaji=int(gaji)
                    if paramater==1:
                        for i in range(len(x)):
                            if(x[i][4]>=gaji):
                                new.append(x[i])
                    elif paramater==2:
                        for i in range(len(x)):
                            if(x[i][4]<=gaji):
                                new.append(x[i])

                    
                else:
                    print('\ninput invalid\n')
                
                if len(new)!=0:
                    for i in range(len(new)):
                        table.add_row([new[i][0],new[i][1],new[i][2],new[i][3],new[i][4]])
                    print (table)
                else:
                    print('\ndata empty\n')
            
        elif menu==4:
            mainmenu(x)
            break
        else:
            print('\ninput invalid\n')
            
    

def add(x):
    while(True):
        print('menu add \n\nlist menu:\n1.masukkan data karyawan\n2.back to previous menu')
        menu=input('masukan angka menu: ')
        if(menu.isdigit()==True) and len(menu)==1:
                menu=int(menu)
        
        if menu==1:
                id=input('masukkan ID karyawan terbaru(3digit): ')
                while id.isdigit()==False or len(id)!=3:
                    print('Format ID salah')
                    id=input('masukkan ID karyawan terbaru(3digit): ')
                if len(x)==0:
                        new=[]
                        new.append(id)
                        nama=input('masukkan nama karyawan terbaru: ')
                        while(nama.replace(' ','').isalpha()==False):
                            nama=input('input salah\nmasukkan nama karyawan terbaru: ')
                        new.append(nama)
                        umur=input('masukkan umur karyawan terbaru(>18): ')
                        while(umur.isdigit()==False) or int(umur)<=18:
                            umur=input('input salah\nmasukkan umur karyawan terbaru(>18): ')
                        umur=int(umur) 
                        new.append(umur)

                        kel=input('masukkan jenis Kelamin karyawan terbaru(M/F): ')
                        kel=kel.upper()
                        while kel.isalpha()!=True or len(kel)!=1 or (kel!='M' and kel!='F'):
                            kel=input('input salah\nmasukkan jenis Kelamin karyawan terbaru(M/F): ')
                            kel=kel.upper()
                        if(kel=='F'):
                            new.append('female')
                        elif(kel=='M'):
                            new.append('male')
                
                        gaji=input('masukkan gaji karyawan terbaru(=>10k): ')
                        while(gaji.isdigit()==False) or int(gaji)<10000:
                            gaji=input('input salah\nmasukkan gaji karyawan terbaru(=>10k): ')
                        gaji=int(gaji) 
                        new.append(gaji)
                        print(f'ID={new[0]}\nnama={new[1]}\numur={new[2]}\njenis kelamin={new[3]}\ngaji={new[4]}')
                        confirm=input('simpan data berikut?(Y/N) ')
                        while confirm.isalpha()!=True or len(confirm)!=1:
                            confirm=input('input salah\nsimpan data berikut?(Y/N) ')
                        confirm=confirm.upper()
                        if confirm=='Y':
                            print('\ndata telah dimasukan\n')
                            x.append(new)
                        else:
                            print('\noperasi di batalkan\n')
                else:
                    for i in range(len(x)):
                        if(x[i][0]==id):
                            print('ID sudah terpakai')
                            break
                        elif i==len(x)-1 or len(x)==0:
                            new=[]
                            new.append(id)
                            nama=input('masukkan nama karyawan terbaru: ')
                            while(nama.replace(' ','').isalpha()==False):
                                nama=input('input salah\nmasukkan nama karyawan terbaru: ')
                            new.append(nama)
                            umur=input('masukkan umur karyawan terbaru(>18): ')
                            while(umur.isdigit()==False) or int(umur)<=18:
                                umur=input('input salah\nmasukkan umur karyawan terbaru(>18): ')
                            umur=int(umur) 
                            new.append(umur)

                            kel=input('masukkan jenis Kelamin karyawan terbaru(M/F): ')
                            kel=kel.upper()
                            while kel.isalpha()!=True or len(kel)!=1 or (kel!='M' and kel!='F'):
                                kel=input('input salah\nmasukkan jenis Kelamin karyawan terbaru(M/F): ')
                                kel=kel.upper()
                            if(kel=='F'):
                                new.append('female')
                            elif(kel=='M'):
                                new.append('male')
                           
                            gaji=input('masukkan gaji karyawan terbaru(=>10k): ')
                            while(gaji.isdigit()==False) or int(gaji)<10000:
                                gaji=input('input salah\nmasukkan gaji karyawan terbaru(=>10k): ')
                            gaji=int(gaji) 
                            new.append(gaji)
                            print(f'ID={new[0]}\nnama={new[1]}\numur={new[2]}\njenis kelamin={new[3]}\ngaji={new[4]}')
                            confirm=input('simpan data berikut?(Y/N) ')
                            while confirm.isalpha()!=True or len(confirm)!=1:
                                confirm=input('input salah\nsimpan data berikut?(Y/N) ')
                            confirm=confirm.upper()
                            if confirm=='Y':
                                print('data telah dimasukan')
                                x.append(new)
                                break
                            else:
                                print('operasi di batalkan')
                                break
        elif menu==2:
            mainmenu(x)
            break
        else:
            print('\ninput invalid\n')

    

def change(x):
    while(True):
        print('menu change \n\nlist menu:\n1.ubah data karyawan\n2.back to previous menu')
        menu=input('masukan angka menu: ')
        if(menu.isdigit()==True) and len(menu)==1:
            menu=int(menu)
        
        if menu==1:
            if  len(x)==0:
                print('\ndata empty\n')
            else:
                search=input('masukkan ID karyawan(3 digits): ')
                while search.isdigit()==False or len(search)!=3:
                    print('Format ID salah')
                    search=input('masukkan ID karyawan(3 digits): ')
                for i in range(len(x)):
                    if(x[i][0]==search):
                        print(f'\nID={x[i][0]}\nnama={x[i][1]}\numur={x[i][2]}\njenis kelamin={x[i][3]}\ngaji={x[i][4]}')
                        confirm=input('ganti data berikut?(Y/N) ')
                        while confirm.isalpha()!=True or len(confirm)!=1:
                            confirm=input('input salah\nganti data berikut?(Y/N) ')
                        confirm=confirm.upper()
                        if confirm=='Y':
                            pick= input('masukkan data yang akan diganti(id/nama/umur/jenis kelamin/gaji): ')
                            pick=pick.lower()
                            while (pick.isalpha()!=True) or (pick!='id' and pick!='nama' and pick!='umur' and pick!='jenis kelamin' and pick!='gaji'):
                                pick=input('input salah\nmasukkan data yang akan diganti(id/nama/umur/jenis kelamin/gaji): ')
                                pick=pick.lower()
                            if pick=='id':
                                id=input('masukkan ID karyawan terbaru(3digit): ')
                                while id.isdigit()==False or len(id)!=3:
                                    print('Format ID salah')
                                    id=input('masukkan ID karyawan terbaru(3digit): ')
                                print(f'ubah {x[i][0]} jadi {id}')
                                confirm2=input('simpan data berikut?(Y/N) ')
                                while confirm2.isalpha()!=True or len(confirm)!=1:
                                    confirm2=input('input salah\nsimpan data berikut?(Y/N) ')
                                confirm2=confirm2.upper()
                                if confirm2=='Y':
                                    x[i][0]=id
                                    print('\ndata telah diganti\n')
                                    break
                                else:
                                    print('\noperasi di batalkann\n')
                                    break 
                            elif pick=='nama':
                                nama=input('masukkan nama karyawan terbaru: ')
                                while(nama.replace(' ','').isalpha()==False):
                                    nama=input('input salah\nmasukkan nama karyawan terbaru: ')
                                print(f'ubah {x[i][1]} jadi {nama}')
                                confirm2=input('simpan data berikut?(Y/N) ')
                                while confirm2.isalpha()!=True or len(confirm)!=1:
                                    confirm2=input('input salah\nsimpan data berikut?(Y/N) ')
                                confirm2=confirm2.upper()
                                if confirm2=='Y':
                                    x[i][1]=nama
                                    print('\ndata telah diganti\n')
                                    break
                                else:
                                    print('\noperasi di batalkann\n')
                                    break 
                            elif pick=='umur':
                                umur=input('masukkan umur karyawan terbaru(>18): ')
                                while(umur.isdigit()==False) or int(umur)<=18:
                                    umur=input('input salah\nmasukkan umur karyawan terbaru(>18): ')
                                umur=int(umur)
                                print(f'ubah {x[i][2]} jadi {umur}')
                                confirm2=input('simpan data berikut?(Y/N) ')
                                while confirm2.isalpha()!=True or len(confirm)!=1:
                                    confirm2=input('input salah\nsimpan data berikut?(Y/N) ')
                                confirm2=confirm2.upper()
                                if confirm2=='Y':
                                    x[i][2]=umur
                                    print('\ndata telah diganti\n')
                                    break
                                else:
                                    print('\noperasi di batalkann\n')
                                    break 
                               
                            elif pick=='jenis kelamin':
                                kel=input('masukkan jenis Kelamin karyawan terbaru(M/F): ')
                                kel=kel.upper()
                                while kel.isalpha()!=True or len(kel)!=1 or (kel!='M' and kel!='F'):
                                    kel=input('input salah\nmasukkan jenis Kelamin karyawan terbaru(M/F): ')
                                    kel=kel.upper()
                                if(kel=='F'):
                                    print(f'ubah {x[i][3]} jadi female')
                                    confirm2=input('simpan data berikut?(Y/N) ')
                                    while confirm2.isalpha()!=True or len(confirm)!=1:
                                        confirm2=input('input salah\nsimpan data berikut?(Y/N) ')
                                    confirm2=confirm2.upper()
                                    if confirm2=='Y':
                                        x[i][3]='female'
                                        print('\ndata telah diganti\n')
                                        break
                                    else:
                                        print('\noperasi di batalkann\n')
                                        break 
                                elif(kel=='M'):
                                    print(f'ubah {x[i][3]} jadi male')
                                    confirm2=input('simpan data berikut?(Y/N) ')
                                    while confirm2.isalpha()!=True or len(confirm)!=1:
                                        confirm2=input('input salah\nsimpan data berikut?(Y/N) ')
                                    confirm2=confirm2.upper()
                                    if confirm2=='Y':
                                        x[i][3]='male'
                                        print('\ndata telah diganti\n')
                                        break
                                    else:
                                        print('\noperasi di batalkann\n')
                                        break 
                            elif pick=='gaji':
                                gaji=input('masukkan gaji karyawan terbaru(=>10k): ')
                                while(gaji.isdigit()==False) or int(gaji)<10000:
                                    gaji=input('input salah\nmasukkan gaji karyawan terbaru(=>10k): ')
                                gaji=int(gaji)
                                print(f'ubah {x[i][4]} jadi {gaji}')
                                confirm2=input('simpan data berikut?(Y/N) ')
                                while confirm2.isalpha()!=True or len(confirm)!=1:
                                    confirm2=input('input salah\nsimpan data berikut?(Y/N) ')
                                confirm2=confirm2.upper()
                                if confirm2=='Y':
                                    x[i][4]=gaji
                                    print('\ndata telah diganti\n')
                                    break
                                else:
                                    print('\noperasi di batalkann\n')
                                    break 
                        else:
                            print('\noperasi di batalkan\n')
                            break
                    elif i==len(x)-1:
                        print('\nkaryawan tidak ditemukan\n')
        elif menu==2:
            mainmenu(x)
            break

        else:
            print('\ninput invalid\n')

def fire(x):
    while(True):
        print('menu fire \n\nlist menu:\n1.hapus data karyawan\n2.back to previous menu')
        menu=input('masukan angka menu: ')
        if(menu.isdigit()==True) and len(menu)==1:
            menu=int(menu)
        
        if menu==1:
            if  len(x)==0:
                print('\ndata empty\n')
            else: 
                search=input('masukkan ID karyawan(3 digits): ')
                while search.isdigit()==False or len(search)!=3:
                    print('Format ID salah')
                    search=input('masukkan ID karyawan(3 digits): ')
                for i in range(len(x)):
                    if(x[i][0]==search):
                        print(f'ID={x[i][0]}\nnama={x[i][1]}\numur={x[i][2]}\njenis kelamin={x[i][3]}\ngaji={x[i][4]}')
                        confirm=input('hapus data berikut?(Y/N) ')
                        while confirm.isalpha()!=True or len(confirm)!=1:
                            confirm=input('input salah\nmhapus data berikut?(Y/N) ')
                        confirm=confirm.upper()
                        if confirm=='Y':
                            x.pop(i)
                            print('\ndata telah dihapus\n')
                            break
                        else:
                            print('\noperasi di batalkan\n')
                            break
                    elif i==len(x)-1:
                        print('\nkaryawan tidak ditemukan\n')
        elif menu==2:
            mainmenu(x)
            break

        else:
            print('\ninput invalid\n')

def mainmenu(x):
    while(True):
        print('Database karyawan \n\nlist menu:\n1.menampilkan daftar karyawan\n2.memasukkan data karyawan\n3.mengubah data karyawan\n4.menghapus data karyawan\n5.exit')
        menu=input('masukan angka menu: ')
        if(menu.isdigit()==True) and len(menu)==1:
            menu=int(menu)
        if menu==1:
            display(x)
            break
        elif menu==2:
            add(x)
            break
        elif menu==3:
            change(x)
            break
        elif menu==4:
            fire(x)
            break
        elif menu==5:
            break
        else:
            print('\ninput invalid\n')
mainmenu(karyawan)