import os, pathlib, shutil, json
# import datetime
import logging as log

log.basicConfig(
    filename="foldercleaner.log",
    level=log.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Sorter:
    def __init__(self, entry, result_label):
        self.entry = entry
        self.result_label = result_label
        log.info(f"Sorter initialized with entry and result_label on path {self.entry.get()}")

    def sort(self):
        global check
        global list_extension
        global source_file
        list_extension = []
        with open(os.path.join(os.getcwd(), "maps.json"), 'r') as f:
            # For mapping extensions to the folder
            common_extensions = json.load(f)

        try:
            # Source  directory to sort
            source_directory = self.entry.get()
            # List of all the available files in folder
            list_of_files = os.listdir(source_directory)
            # Iterating through elements of the source folder
            for i in list_of_files:
                # To check whether the specified filetype is in the dictionary or not
                check = 0
                # Making a path to the file
                source_file = os.path.join(source_directory, i)
                # Getting the file extension
                extension = pathlib.Path(source_file).suffix
                list_extension.append(extension)
                # To avoid key error if extension is not a key in dictionary
                if extension in common_extensions:
                    check = 1
                # Making destination accessible in the for loop
                if extension and (check == 1):
                    # Place to move file
                    destination = os.path.join(source_directory, common_extensions[extension])
                    # Make the folder if it does not exist
                    if not os.path.exists(destination):
                        log.info(f"Creating directory {destination} for extension {extension}")
                        os.makedirs(destination)
                        shutil.move(source_file, destination)
                        # log.info(f"Moved {source_file} to {destination}")
                # Move the file if it is mapped
                    else:
                        try:
                            if i not in os.listdir(destination):
                                shutil.move(source_file, destination)
                                # log.info(f"Moved {source_file} to {destination}")
                            else:
                                os.remove(source_file)
                                log.warning(f"Repeated file found: {source_file}")
                        except:
                            current = self.result_label.get()
                            self.result_label.set("repeated file found")
                            print(source_file, "----")

                else:
                    continue
                # print(f"Moved {i} to {destination}")
                log.info(f"Moved {source_file} to {destination}")

            if check == 0:
                current = self.result_label.get()
                self.result_label.set("The present entities are a folder or not have been mapped")
                log.warning(f"Unmapped files found in {source_directory}: {list_of_files}")
            else:
                current = self.result_label.get()
            self.result_label.set("Successful All files which can be mapped are moved")
            log.info(f"All files which can be mapped are moved from {source_directory}")
        except:
            current = self.result_label.get()
            self.result_label.set("Invalid Input")
            log.error(f"Invalid input for source directory: {self.entry.get()}")
        # print(source_file, "----")
