# Writing to a file
import logging
logging.basicConfig(level=logging.DEBUG)

def write_content_to_file(file_name, content):
    with open(file_name, 'w') as file:
        logging.info(f"{content} is being added to {file_name}")
        file.write(content)


list_of_awesome_ppl = ["Elon", "Mark", "Jeff"]

for person in list_of_awesome_ppl:
    print(person)
    write_content_to_file("Great_People.txt", f"\n{person}")



