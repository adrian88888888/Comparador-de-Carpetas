import stat
import os
import logging

# logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.basicConfig(level=logging.WARNING, format='%(message)s')
# logging.basicConfig(level=logging.CRITICAL, format='%(message)s')

# Settings
OLD_FOLDER          = r'C:\Users\adria\Desktop\Slave Folder....'
UP_TO_DATE_FOLDER   = r'C:\Users\adria\Desktop\Main Folder.....'
COMPARE_SUBFOLDERS  = True

def compare_old_folder_to_up_to_date_folder():
    logging.warning('Comparing old folder to up to date folder...')
    all_filepaths = get_filepaths_from(OLD_FOLDER)
    for each_filepath in all_filepaths:
        filename = get_filename_from(each_filepath)
        file_found = search_filename_in_up_to_date_folder(filename, UP_TO_DATE_FOLDER)
        if file_found:
            logging.info(filename + ' found in the up to date folder!')
            logging.info('-----------------------')
        if not file_found:
            logging.warning('The file ' + filename + ' is not in the up to date folder')
            logging.warning('-----------------------')
            # move_file(each_filepath, filename) # ===> si queres podes mover los archivos que se encuentren, o los no se encuentren, a algun lado

def get_filepaths_from(folder):
    logging.warning('-----------------------')
    logging.warning('Getting list of filepaths from(in old folder): ' + folder)
    filepaths = []
    for current_directory, folders, files in os.walk(folder):
        for each_file in files:
            filepath = os.path.join(current_directory, each_file)
            filepaths.append(filepath)
        if not COMPARE_SUBFOLDERS:
            break
    return filepaths

def get_filename_from(filepath):
    logging.info('Getting filename from filepath...')
    return os.path.basename(filepath)

def search_filename_in_up_to_date_folder(filename, UP_TO_DATE_FOLDER):
    logging.info('Searching ' + filename + ' in the up to date folder...')
    for current_directory, folders, files in os.walk(UP_TO_DATE_FOLDER):
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

def subtract_hidden_and_system_files(up_to_date_folders):
    logging.debug('Subtracting hidden and system folders')
    user_up_to_date_folders = []
    for each_folderpath in up_to_date_folders:
        if not is_hidden(each_folderpath):
            user_up_to_date_folders.append(each_folderpath)
    return user_up_to_date_folders

def is_hidden(path):
    name = os.path.basename(os.path.abspath(path))
    return name.startswith('.') or has_hidden_attribute(path)

def has_hidden_attribute(path):
    return bool(os.stat(path).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)


compare_old_folder_to_up_to_date_folder()
