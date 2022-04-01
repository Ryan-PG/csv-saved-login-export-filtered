import csv
from io import TextIOWrapper

def open_csv_file():
  """
  Opens a CSV file and return a reader on that file.
  """
  
  csv_file = ''
  csv_file_reader = ''

  # Get CSV file path
  csv_file_path = input('  > Enter CSV file path(empty for current directory): ')

  # Get CSV file name
  csv_file_name = input('  > Enter CSV file name: ')
  if csv_file_name.__contains__('.csv') == False:
    csv_file_name += '.csv'

  # Opening CSV file
  try:
    if csv_file_path == '':
      csv_file = open(csv_file_name)
    else:
      csv_file = open(csv_file_path + '\\' + csv_file_name)

  except:
    print('\n CSV file not found... \n')
    exit(0)

  return csv_file


def csv_reader(csv_file:csv.__file__):
  return csv.reader(csv_file) # CSV Reader 


def open_export_file():
  """
  Opens a 'txt' file for exporting data and returns it.
  """
  
  # Opening Export file
  exportedLogins_file_name = input('\n  > Enter export file name(exported_logins.txt): ')

  if exportedLogins_file_name == '': exportedLogins_file_name = 'exported_logins.txt'
  if exportedLogins_file_name.__contains__('.txt') == False: 
    exportedLogins_file_name += '.txt'

  return open(exportedLogins_file_name, mode='w')


def index_identifier(csv_reader:csv.reader):
  """
  Identifies 'url', 'username' and 'password' column indexes
  """
  
  # Indentify column indexes
  index_identifier = next(csv_reader)
  url_index, username_index, password_index = \
    index_identifier.index('url'), index_identifier.index('username'), index_identifier.index('password')
  
  return [url_index, username_index, password_index]


def export_data(csv_file, export_file:TextIOWrapper, filter_key:str = None):
  """
  Reads CSV file via CSV_Reader and export data to a text file
  """

  csv_file.seek(0) # returns to first of csv_file
  csv_reader = csv.reader(csv_file)
  url_index, username_index, password_index = index_identifier(csv_reader)
  csv_file.seek(0) # returns to first of csv_file

  # Read File and proccess
  while True:
    # line = csv_reader.__next__() # read a line -> List
    try:
      line = next(csv_reader) # read a line -> List
    except StopIteration:
      print('Proccess finished.')
      break
      
    url = line[url_index] # remove (") from first and end of string
    username, password = line[username_index], line[password_index]
    
    # print(url, username, password)
    if filter_key == None:
      export_file.write(f'{url}\n{username}\n{password}\n\n')
    else:
      if url.__contains__(filter_key):
        export_file.write(f'{url}\n{username}\n{password}\n\n')


def export_filtered_data(csv_file):
  filter = input('  > Do you want generate filtered output? (Y/N) ')
  if filter != '' and filter.lower().__contains__('y'):
    # Filtered file name
    filterKey = input('\n  Enter filter key: ')
    
    filteredExportFile = open(filterKey+'.txt', 'w')
    export_data(csv_file, filteredExportFile, filter_key=filterKey)
  
    filteredExportFile.close()