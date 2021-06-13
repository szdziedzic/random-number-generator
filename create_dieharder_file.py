from random_number_generator.generator import Generator

G = Generator()

with open('test_multi.txt', 'w') as file:
    file.write('#==================================================================\n')
    file.write('# generator multi1  seed = 1\n')
    file.write('#==================================================================\n')
    file.write('type: d\n')
    file.write('count: 1200000000\n')
    file.write('numbit: 32\n')
    for i in range(1200000000):
        number = G.generate_number()
        file.write(f'{number}\n')
