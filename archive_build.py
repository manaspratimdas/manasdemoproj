#!/usr/bin/env python
import boto
import sys, os
from boto.s3.key import Key

LOCAL_PATH = 'entytle'
AWS_ACCESS_KEY_ID = 'AKIAJEKNN3KEYYLORFNQ'
AWS_SECRET_ACCESS_KEY = 'dblKYujZdXlw1lbgkfGuvDxe2CIeDV5Hp0nlOJ6z'

bucket_name = 'entytle-development'
sourc_folder='rothko/builds/rothko-env/'
dest_folder='archive/'
build_name='SampleBT-manasdemodepolyver.zip'
# connect to the bucket
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
                AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket(bucket_name)

keys = bucket.list(sourc_folder)
for k in keys:
 
 if k.name != sourc_folder:
  print("old name-->"+k.name)
  newkeyname = dest_folder + k.name.partition(sourc_folder)[2]
  print("new name-->"+newkeyname)
  if k.name == 'rothko/builds/rothko-env/SampleBT-manasdemodepolyver.zip':
   print("delete  :"+k.name)
   k.delete()
  else:
   print("copy & delete  :"+k.name)
   k.copy(bucket,newkeyname)
   k.delete()
   
