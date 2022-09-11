from __future__ import print_function

import os.path
import random
import smtplib
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def send_message(subject, message, recipient):
    email = email_auth['email']
    password = email_auth['password']

    #set up email server
    server = smtplib.SMTP("smtp.outlook.com", 587)
    server.starttls()
    server.login(email,password)

    # Setup email msg
    msg = MIMEText(message)
    msg['Subject'] = 'Recipes of the Week'
    msg['From'] = email
    msg['To'] = recipient

    # Send email
    server.sendmail(email, recipient, msg.as_string())

def create_drive_service():
  """Shows basic usage of the Drive v3 API.
  Prints the names and ids of the first 10 files the user has access to.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists('token.json'):
      creds = Credentials.from_authorized_user_file('token.json', SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file(
              'credentials.json', SCOPES)
          creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open('token.json', 'w') as token:
          token.write(creds.to_json())

  try:
      service = build('drive', 'v3', credentials=creds)
      return service

  except HttpError as error:
      # TODO(developer) - Handle errors from drive API.
      print(f'An error occurred: {error}')

def getThisWeeksRecipes():
  service = create_drive_service()
  results = service.files().list( q = "'1POCho24Gmbia0wGwnb9y-qQik0vVq-sg' in parents", fields="files(name)").execute()
  items = results.get('files', [])

  recipes_of_the_week = random.sample(items, 4)
  return recipes_of_the_week

def main():
  items = getThisWeeksRecipes()

  if not items:
      print('No files found.')
      return
  print('Files:')
  # print(items)
  for item in items:
      print(item)


if __name__ == '__main__':
  main()
