def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print('Error: The file does not exist.')
    except IOError:
        print('Error: An IOError occurred.')
    finally:
        print('Finished reading file.')

file_content = read_file('sample.txt')
print(file_content)
