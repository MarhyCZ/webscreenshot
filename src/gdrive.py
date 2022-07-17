from __future__ import print_function
import io
import os
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive.file']
ROOT_FOLDER_ID = '14wjOlArTsnehIbLcBNKuLh0jMYjOVKGB'


def load_credentials():
    config_path = os.path.abspath(os.path.dirname(__file__)) + '/config'
    token_path = f'{config_path}/token.json'
    secret_path = f'{config_path}/client_secret.json'
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(
            token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                secret_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    return creds


def upload_basic(filename: str, file: bytes):
    """Insert new file.
    Returns : Id's of the file uploaded
    """
    creds = load_credentials()

    try:
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {'name': filename, 'parents': [ROOT_FOLDER_ID]}
        media = MediaIoBaseUpload(io.BytesIO(file),
                                  mimetype='image/png')
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()
        print(F'File ID: {file.get("id")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.get('id')
