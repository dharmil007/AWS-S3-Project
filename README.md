# AWS-S3-Project

AWS_Main_Script.py

The script accepts 4 arguments: LocalFolderName, s3Bucket Name, s3 Folder name & FileName.

Script to upload files to AWS S3.
This program does the following things: 

1. Reads from the local directory (readLocalFolder)
2. Reads from the S3 Bucket (s3List)
3. Uploads to S3 by comparing local & s3 files. (s3Upload)
4. Gives upload status (success, failure, partial, nothing new) (uploadFileStatuses)
5. Serializes the data in jSon Format (jSondata)
6. Connects to SQL & inserts data in the SQL Tabel (mySqlConnection)

Pending : 

    Create a HTML file to display data from SQL.