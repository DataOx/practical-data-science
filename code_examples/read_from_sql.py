import sweetviz as sv
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv()

def connect2SQL():
    """sample code to test SQL connection
    """    
    server = ****
    database = *** 
    userName =  os.getenv("db_ue_onPrem")
    uepwd = os.getenv("db_pwd_onPrem")
    connectStr ='DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+userName+';PWD='+ uepwd
    cnxn = pyodbc.connect(connectStr)
    cursor = cnxn.cursor()
    #Sample select query fom existing table
    cursor.execute("SELECT  TOP(10) * FROM [adf].[BPMASTER]") 
    row = cursor.fetchone() 
    while row: 
        print(row[0])
        print(row)
        row = cursor.fetchone() 
        
        
def get_query(select='TOP 501',
              where=None,
              database='dba',
              schema='adf',
              table='abc'):
    """generate query string. 

    Args:
        select (str, optional): select statement. Defaults to 'TOP 501'.
        where ([type], optional): where statement. Defaults to None.
        database (str, optional): db name. Defaults to 'GF-SqlDB-dkdevsma-T'.
        schema (str, optional): schema. Defaults to 'adf'.
        table (str, optional): table name. Defaults to 'ORDERSHEAD_ZCOPE_M88_Q0034_CLEAN'.
    Returns:
        [string]: query string
    """    
    query = f'SELECT {select}'
    query += f' FROM [{database}].{schema}.{table}'
    if where is not None:
        query += f' WHERE {where}'
    return query
    
def fetchData(selectStr,whereStr,database,schema,tablename, conn, dataReport = False,reportName = 'masterData'):
    """fetch data and provide data report.

    Args:
        selectStr (string): select string
        whereStr (string): where clause
        database (string): db name
        schema (string): schema of the table
        tablename (string): tablename
        conn (object): pyodbc connection
        dataReport (bool, optional): return report or not. Defaults to False.
        reportName (str, optional): name of the report. Defaults to 'masterData'.

    Returns:
        [dataframe]: queried data 
    """
    query = get_query(selectStr,whereStr,database,schema,tablename)    
    dfO = pd.read_sql(query, conn)
    if dataReport:
        #analyzing the dataset
        masterData_report = sv.analyze(dfO)
        #display the report
        masterData_report.show_html(reportName + '.html')
    return dfO


def save2SQL(calOut_py,toSql = True):
    '''
    This function save data to SQL.
    :param calOut_py: (dataframe) dataframe contains country names, number of working days.
    :return:
        
    Example:         
    '''
        
    import pyodbc
    from sqlalchemy import create_engine
    import urllib
    
    server = ***
    database = ****
    # connect via ActiveDirectoryInteractive
    #userName = 'lji@***.com' 
    #connectStr = 'DRIVER={ODBC Driver 17 for SQL Server};server='+server+';database='+database+';UID='+userName+';Authentication=ActiveDirectoryInteractive'
    # connect via activedirectorypassword
    username = os.environ.get("db_user") 
    password = os.environ.get("db_key") 
    connectStr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password

    cnxn = pyodbc.connect(connectStr)
    # for first time log in, a pop-up window show up asks for password 
    #cursor = cnxn.cursor()
    # insert whole dataframe into sql
    if toSql:
        print(toSql)
        '''
        quoted = urllib.parse.quote_plus(connectStr)
        engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
        print('engine created')
        # run fetchCalendar.py to get the dataframe first.
        calOut_py.to_sql('calendarTest', schema='calendar', con = engine, if_exists='append', chunksize=200, index=False)
        '''
        cursor = cnxn.cursor()
        cursor.execute("""INSERT INTO calendar.[calendarTest] (timestamp, noOfWorkingDays, C, Country) VALUES ('2020-01-01',12,'abc','test')""") 
        cnxn.commit()
        
    cnxn.close()    
    return True


