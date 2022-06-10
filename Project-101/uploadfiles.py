import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    
                local_path = os.path.join(root, filename)

                    
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    #uploading the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BJTruaQAo72IwO8dZAVZsNJAt8RCQZR-C2lbnEzpbeNz8NpcrH63Py011kvS1yDLUwjCALmROyKSV1JJYHNK0WaKXQ8pEnYq5ShUsRKN_zOCNNivFQAwu5cH6eLbyPp9jsHR7-w3q6Pr'
    transferData = TransferData(access_token)

    file_from = str(input(" the folder path to transfer : -"))
    file_to = input("the full path to upload to dropbox:- ")  

    
    transferData.upload_file(file_from,file_to)
    print("the file/s has been moved")

main()