"""
Script to upload files to AWS S3 using classes
    2 classes and 4 methods.
1. Upload Script (Class)
    1.1 Read from Local Folder (Method)
    1.2 Get files from specific bucket in S3 (Method)
    1.3 Compare & upload the files to S3 (Method)
    1.4 Get status for uplodEd Files
    1.5 Create a temp HTML File

"""

import boto3
import os
from botocore.exceptions import ClientError
from datetime import date
import sys

class awsUpload ():
    """ This class is used to upload files to s3 """
    def __init__ (self,localFolderPath,bucketName, bucketFolderName, htmlFileName):
        self.localFolderPath = localFolderPath
        self.bucketName = bucketName
        self.bucketFolderName = bucketFolderName
        self.htmlFileName = htmlFileName
        self.localFile = []
        self.s3_Bucket_filesList = []
        self.uploadedFiles = []
        self.listUploadFiles = []
    
    def readLocalFolder(self):
        """ Creating a list of files from the folder """
        try:
            self.localFile = os.listdir(path=self.localFolderPath)
            print ("Read from LocalFolder")
        except Exception as e:
            print ("Can'T read the Directory", e)
            quit()

    def s3List(self):
        """ listing The contents of the specified bucket from S3 """
        
        #Requesting s3 resource from Boto and fetching a bucket
        s3 = boto3.resource ('s3')
        bucket = s3.Bucket (self.bucketName)

        """
        Filtering out the required folder from bucket and storing it in 2D List
        The results are fetched in 2 variables: "Values & Keys".
        "files.key" is used to filter just the keys of the contents fetched.
        """
        try:
            s3_Bucket_valuesList = [files.key.split("/") for files in bucket.objects.filter (Prefix=self.bucketFolderName)]
        except Exception as s:
            print ("Cannot fetch the specified Bucket", s)
            quit()
        for f in s3_Bucket_valuesList:
            self.s3_Bucket_filesList.append(f[1])
        print ("Fetched list form s3")
        
    def s3Upload(self):
        """ This method uploads the files which are not Already on s3 by comparing it with files from Local Folder.
        Counter Variable keeps track of files uploaded and is also useful to print result, i.e. Directory is Synced.
        This Also prints the files and Number fo files needs to be uploaded.
        """
        #listUploadFiles = []
        s3 = boto3.client('s3')

        for files in self.localFile:
            if files not in self.s3_Bucket_filesList:
                #print ("Currently uploading: "+files)
                self.uploadedFiles.append(files)
                #We require the full Path of the file to be given to be uploaded.
                localFilesPath = self.localFolderPath + "\\" + files

                try:
                    s3.upload_file (localFilesPath,self.bucketName,self.bucketFolderName+files)
                except Exception as u:
                    print ("Cannot upload the Files", u)
                    quit()

        return self.uploadedFiles #Returning uploaded files to be used in Creation of HTML Files.
    
    def uploadFileStatuses (self):
        """ This method calculates the files and number of Files to be Uploaded.
        
        """
        self.listUploadFiles = set(self.localFile) - set(self.s3_Bucket_filesList) #Creates a new List with difference in files in local folder and files in s3.
        if len(self.listUploadFiles) == 0:
            print ("Nothing New to upload.")
        else: 
            print ("============================= FILES TO BE UPLOADED =========================")
            print (len(self.listUploadFiles))
            print ("\n")
            print (self.listUploadFiles)
            print ("============================= UPLOADED TO S3================================")
            print (len(self.uploadedFiles))
            print ("\n")
            print (self.uploadedFiles)
            if len(self.uploadedFiles) != len(self.listUploadFiles):
                print("================= PLEASE RE-TRY THE FOLLOWING FILES ===============")
                print ("Number of files not uploaded: ", len(self.listUploadFiles)-len(self.uploadedFiles))
                print ("Files that were not uploaded",set(self.listUploadFiles)-set(self.uploadedFiles))

    def jSondata (self):
        """ 1. Store data in jSON
            2. Store jSON data in SQl
            3. Fetch Data from SQl & Generate the hTMl Report.
            4. Data Types: 
                a. Date
                b. Machine
                c. No. of Files & FIles
                d. Success or Failure.
        """

    def createStatusHTML (self, uploadedFiles):
        """ Creating a temporary file, which will later be merged 
            List of Files which were Uploaded successfully.
        """
        dates = date.today()
        #print (uploadedFiles)
        with open(self.htmlFileName+str(dates)+".htm", "w") as f_Handle: #Createing and Opening the file in Write mode
                f_Handle.write("<table border=\"2\">")
                f_Handle.write("<tr> <td rowspan=\"")
                f_Handle.write(str(len(self.uploadedFiles)+1))
                f_Handle.write("\">")
                f_Handle.write(self.htmlFileName)
                f_Handle.write("</td> <td>")
                f_Handle.write(str(dates))
                f_Handle.write("</td>")
                for u in uploadedFiles:
                    #f_Handle.write("<tr>")
                    f_Handle.write("<td>")
                    f_Handle.write(u)
                    f_Handle.write("</td>")
                    #f_Handle.write("</tr>")
                f_Handle.write("</tr>")

#uploadStart = awsUpload("Z:\\DC-01 CopyJob AWS","uspl-server-backups","DC-01 CopyJob AWS/")
uploadStart = awsUpload(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

uploadStart.readLocalFolder()
uploadStart.s3List()
uploadedFiles = uploadStart.s3Upload()
uploadStart.uploadFileStatuses()
uploadStart.createStatusHTML(uploadedFiles)



