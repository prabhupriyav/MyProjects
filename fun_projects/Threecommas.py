
def add_comma(wealth):
    with_commas = '{:,}'.format(wealth)
    print(f'Wealth with commas  {with_commas}')
wealth = int(input('Enter your wealth : '))
add_comma(wealth)
