# import os
# import zipfile
# import requests

# # Define the URL and the local path for the zip file
# url = 'https://storage.googleapis.com/learning-datasets/horse-or-human.zip'  # Replace with the actual URL
# local_zip = '/tmp/horse-or-human.zip'

# # Download the file if it doesn't exist
# if not os.path.exists(local_zip):
#     print("Downloading file...")
#     response = requests.get(url)
#     with open(local_zip, 'wb') as f:
#         f.write(response.content)
#     print("Download complete.")

# # Extract the zip file
# with zipfile.ZipFile(local_zip, 'r') as zip_ref:
#     zip_ref.extractall('/tmp/horse-or-human')

# # Directory with our training horse pictures
# train_horse_dir = os.path.join('/tmp/horse-or-human/horses')

# # Directory with our training human pictures
# train_human_dir = os.path.join('/tmp/horse-or-human/humans')

# # List first 10 horse images
# train_horse_names = os.listdir(train_horse_dir)
# print("Horse images:", train_horse_names[:10])

# # List first 10 human images
# train_human_names = os.listdir(train_human_dir)
# print("Human images:", train_human_names[:10])

# # Count total horse and human images
# print('Total training horse images:', len(os.listdir(train_horse_dir)))
# print('Total training human images:', len(os.listdir(train_human_dir)))




