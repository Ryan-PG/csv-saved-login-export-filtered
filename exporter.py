
import export_data_from_logins_csv as csv_handler


csvFile = csv_handler.open_csv_file()
csvReader = csv_handler.csv_reader(csvFile)
exportFile = csv_handler.open_export_file()

# Generate Not-filtered Output
csv_handler.export_data(csvFile, exportFile)

# Generate Filtered Output
csv_handler.export_filtered_data(csvFile)


csvFile.close()
exportFile.close()