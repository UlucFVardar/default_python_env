# PROJECT AWS TAGS


Owner    : DataTeam
Name     : 
IsTest   : True | False
Stack    : 
State    : All / Prod / Dev / Test
!Stack   : S3


# Put DB connection to ENV Values

"user": os.environ["DbUser"],
"password": os.environ["DbPassword"],
"database": os.environ["DbDatabase"],
"host": os.environ["DbHost"],