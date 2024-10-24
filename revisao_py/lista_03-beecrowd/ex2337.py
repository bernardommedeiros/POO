tot_arr = int(input())

amostral = 2 ** tot_arr

eventos = amostral - ((tot_arr - 1) + (tot_arr // 2))

for i in range(amostral, 0, -1):
    if (amostral % i == 0 and eventos % i == 0):
        mdc = i
        break

print(f'{eventos//mdc}/{amostral//mdc}')

# ERRADO