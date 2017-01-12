
# PEP 498: Formatted literal strings


one_billion = 1_000_000_000
aaa_billion = 1_000_000_000

print(f'one billion = {one_billion:,}')
print('aaa billion = {:,}'.format(aaa_billion))

one_color = 0x_FF_FF_FF_FF
aaa_color = 0x_FF_FF_FF_FF

print(f'color = {one_color:#x}')
print('color = {:#x}'.format(aaa_color))