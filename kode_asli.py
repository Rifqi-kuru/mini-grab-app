# Fungsi hitung tarif dan cetak
def htg(a, b, c):
    # c adalah tipe kendaraan
    if c == 1:
        res = a * 2000
    else:
        res = a * 5000
    
    print("User: " + b)
    print("Total: " + str(res))
    return res

# Main
htg(10, "Budi", 1)
htg(5, "Andi", 2)
