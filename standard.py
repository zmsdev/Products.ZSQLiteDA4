import os
from App.Common import package_home
from App.config import getConfiguration
data_dir= os.path.abspath(os.path.join(getConfiguration().instancehome, 'var', 'sqlite'))

class SQLiteError(Exception):
    pass

class QueryError(SQLiteError):
    pass
