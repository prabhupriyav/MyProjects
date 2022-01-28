def string_out(l):
    for i in l.copy():
        if str(i).isdigit():
            pass
        else:
            l.remove(i)
    print(l)
string_out(['s',2,3,'t'])
