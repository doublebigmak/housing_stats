'''
package for commonly used functions

'''

def read_database(path = None,begin=None, end=None, variables=None):
    """
    Reads Calgary Property Assessment Database
    Reads SQLite Database passes into DF
    """
    from sqlalchemy import create_engine
    import pandas as pd
    from datetime import datetime

    
    if(path==None):
        print('input path variable')
        return None
    
    else:
        
        
        currentYear = datetime.now().year
        engine = create_engine('sqlite:///'+path)
        dataframe = pd.DataFrame()
        print('Reading database from',path)
        if(begin==None):
            begin = 2005
        if(end ==None):
            end = currentYear
            
        query = 'SELECT '
        if variables == None:
            query = query + '* FROM CAL_ASSESS WHERE ROLL_YEAR >='+str(begin) +" AND"+ ' ROLL_YEAR<=' + str(end)
            data = pd.read_sql_query(query,engine)
            print('read complete')
            return data
        else:
            try:
                var_string = ",".join(variables)
                query = query + var_string+" FROM 'CAL_ASSESS' WHERE ROLL_YEAR >="+str(begin) +" AND"+ " ROLL_YEAR<=" + str(end)
                data = pd.read_sql_query(query,engine)

                print('read complete')
                return data
            except Exception as e:
                print(e)
                