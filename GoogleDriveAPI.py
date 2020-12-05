from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']



class GoogleDriveAPI:
    @staticmethod
    def getService():
      creds = None
      # The file token.pickle stores the user's access and refresh tokens, and is
      # created automatically when the authorization flow completes for the first
      # time.
      if os.path.exists('token.pickle'):
          with open('token.pickle', 'rb') as token:
              creds = pickle.load(token)
      # If there are no (valid) credentials available, let the user log in.
      if not creds or not creds.valid:
          if creds and creds.expired and creds.refresh_token:
              creds.refresh(Request())
          else:
              flow = InstalledAppFlow.from_client_secrets_file(
                  'credentials.json', SCOPES)
              creds = flow.run_local_server(port=0)
          # Save the credentials for the next run
          with open('token.pickle', 'wb') as token:
              pickle.dump(creds, token)
      return build('drive', 'v3', credentials=creds)

       

    def getAllFiles(self):
        service = GoogleDriveAPI.getService()
        # Call the Drive v3 API
        page_token = None
        returnArray = []
        while True:
            response = service.files().list( 
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
            for file in response.get('files', []):
                print ('Found file: %s (%s)' % (file.get('name'), file.get('id')))
                resultAsDict = self.convertToDict(file.get('name'))
                returnArray.append(resultAsDict)
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return returnArray


    def getAllFilesContaingName(self,name):
        # Call the Drive v3 API
        service = GoogleDriveAPI.getService()
        page_token = None
        returnArray = []
        while True:
            response = service.files().list(q="name contains " + "'" + name + "'",
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
            for file in response.get('files', []):
                print ('Found file: %s (%s)' % (file.get('name'), file.get('id')))
                resultAsDict = self.convertToDict(file.get('name'))
                returnArray.append(resultAsDict)
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return returnArray


    def convertToDict(self, result):
          
          file = {}

          if result:
              value = result
              file['file_name'] = value
          return file



googleDriveAPI = GoogleDriveAPI()
