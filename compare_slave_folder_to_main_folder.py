import stat
import os
import logging

# logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.basicConfig(level=logging.WARNING, format='%(message)s')
# logging.basicConfig(level=logging.CRITICAL, format='%(message)s')

slave_folder = r'C:\Users\adria\Desktop\Slave Folder....'
main_folder  = r'C:\Users\adria\Desktop\Main Folder.....'

def compare_slave_folder_to_main_folder():
    logging.warning('Comparing slave folder to main folder...')
    all_filepaths = get_filepaths_from(slave_folder)
    for each_filepath in all_filepaths:
        filename = get_filename_from(each_filepath)
        file_found = search_filename_in_main_folder(filename, main_folder)
        if file_found:
            logging.info(filename + ' found in the main folder!')
            logging.info('-----------------------')
        if not file_found:
            logging.warning('The file ' + filename + ' is not in the main folder')
            logging.warning('-----------------------')
            # move_file(each_filepath, filename) # ===> si queres podes mover los archivos que se encuentren, o los no se encuentren, a algun lado

def get_filepaths_from(folder):
    logging.warning('-----------------------')
    logging.warning('Getting list of filepaths from(in slave folder): ' + folder)
    filepaths = []
    for current_directory, folders, files in os.walk(folder):
        for each_file in files:
            filepath = os.path.join(current_directory, each_file)
            filepaths.append(filepath)
        break # ===> sacar esto para mirar dentro de las subcarpetas o dejarlo para mirar solo en el primer nivel
    return filepaths

def get_filename_from(filepath):
    logging.info('Getting filename from filepath...')
    return os.path.basename(filepath)

def search_filename_in_main_folder(filename, main_folder):
    logging.info('Searching ' + filename + ' in the main folder...')
    for current_directory, folders, files in os.walk(main_folder):
        if filename in files:
            return os.path.join(current_directory, filename)

def move_file(each_filepath, filename):
    logging.warning('Moving ' + each_filepath + ' to ' + 'C:/Users/adria/Desktop/Test')
    move_from = each_filepath
    move_to = 'C:/Users/adria/Desktop/Test/' + filename
    os.rename(move_from, move_to)

# ----------------------------------------------------------

# funciones que no se usan en el script pero que podrian ser
# utiles si quiero tener en cuenta los archivos ocultos:

def subtract_hidden_and_system_files(main_folders):
    logging.debug('Subtracting hidden and system folders')
    user_main_folders = []
    for each_folderpath in main_folders:
        if not is_hidden(each_folderpath):
            user_main_folders.append(each_folderpath)
    return user_main_folders

def is_hidden(path):
    name = os.path.basename(os.path.abspath(path))
    return name.startswith('.') or has_hidden_attribute(path)

def has_hidden_attribute(path):
    return bool(os.stat(path).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)


compare_slave_folder_to_main_folder()
