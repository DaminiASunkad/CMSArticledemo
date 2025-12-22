import os
from urllib.parse import quote_plus

class Config(object):
    SECRET_KEY = "f91ede67a5dba270a487a8c29805b07e4e07c98ea7ff704523a327a0228b3685"

    # Azure Blob Storage
    BLOB_ACCOUNT = "images19"
    BLOB_STORAGE_KEY = "v542FfhCsBOqfoPIPYfmvy5sse+XASkorkyNmymq7ZCnFqWux5fjTVwCfuYzxdGdBThR1dvcyDrL+AStaVMEJQ=="
    BLOB_CONTAINER = "image"
    # Azure SQL Database
    SQL_SERVER = "cmsdemodb.database.windows.net"

    SQL_DATABASE = "cms"
    SQL_USER_NAME = "cmsadmin"
    # Only quote if password exists to avoid issues
    sql_pass = "CMS4dmin"
    SQL_PASSWORD = quote_plus(sql_pass)

    # Corrected URI for ODBC Driver 18 and Azure SQL
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}"
        f"@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&Encrypt=yes&TrustServerCertificate=no"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Azure Active Directory (MSAL)
    CLIENT_ID = "d9425ce4-ed95-4a74-8a20-bf071ea8458b"
    CLIENT_SECRET = "D_V8Q~Sw~LpRUtaU~s7CJhLMg.8D0KBHxmszFcMc"
    TENANT_ID = "f958e84a-92b8-439f-a62d-4f45996b6d07"

    AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID or 'common'}"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

    # Session configuration
    SESSION_TYPE = "filesystem"