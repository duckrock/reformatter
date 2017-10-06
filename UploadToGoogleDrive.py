import requests
#url = 'https://www.googleapis.com/upload/drive/v3?uploadType=media HTTP/1.1'
#data = 'Content-Type: application/rtf ' \
#       'Content-Length: 10000 ' \
#       'Authorization: Bearer ' \
#       'ReformattedSong.txt'
#response = requests.post(url, data=data)

folder_id = '0BxEVptkmnm5hMkRicTd6VjY1ajA'
file_metadata = {
    'name': 'ReformattedSong.txt',
    'parents': [folder_id]
}
media = MediaFileUpload('files/ReformattedSong.txt',
                        mimetype='application/rtf',
                        resumable=True)
file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
print ('File ID: %s' % file.get('id'))