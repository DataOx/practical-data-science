
import adal, pyodbc, struct


authority_host_uri = 'https://login.microsoftonline.com'
tenant = 'dabd5d90-87c2-44c9-93cd-783e03236e40'
authority_uri = authority_host_uri + '/' + tenant
resource_uri = 'https://database.windows.net/'
client_id = 'db7dd86f-8f12-4c15-8e92-89b2c1f01885'
client_secret = 'oy.l=9wX89h4RwpEtgkTQhfmpT-fOr?='

context = adal.AuthenticationContext(authority_uri, api_version=None)
mgmt_token = context.acquire_token_with_client_credentials(resource_uri, client_id, client_secret)



SQL_COPT_SS_ACCESS_TOKEN = 1256 
# this script shows how  to connect ODBC via service principle 
server = 'gf-sqlsvr-supplyforecast-s-azwe.database.windows.net' 
database = 'gf-bd-supplyforcast-a-azwe'
connectStr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database


#get bytes from token obtained
tokenb = bytes(mgmt_token["accessToken"], "UTF-8")
exptoken = b''
for i in tokenb:
 exptoken += bytes({i})
 exptoken += bytes(1)
tokenstruct = struct.pack("=i", len(exptoken)) + exptoken

cnxn = pyodbc.connect(connectStr, attrs_before = { SQL_COPT_SS_ACCESS_TOKEN:tokenstruct})

cursor = cnxn.cursor()

'''
#Sample select query fom existing table
cursor.execute("SELECT TOP (10) [ZCOMPCODEID],[ZPRDHIERARCHYLVL7ID],[PERIODID],[ZAISTATFCQTY],[forcastDate] FROM [forecast].[forecastOutput]") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    print(row)
    row = cursor.fetchone()    
'''

cursor.execute("SELECT TOP (10) timestamp, noOfWorkingDays, C, Country FROM calendar.[calendarTest]") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    print(row)
    row = cursor.fetchone()


cursor.execute("""INSERT INTO calendar.[calendarTest] (timestamp, noOfWorkingDays, C, Country) VALUES ('2020-01-01',12,'abc','test')""") 
#cnxn.commit()
