# Import external dependencies
from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy.orm import Session
import numpy as np
import glob

# Import local modules
from crud import *
from db import *

# SessionLocal is the connection to db
def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initailize FastAPI instance
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# List all files with .csv extension in data-source folder
all_csv = [filename for filename in glob.glob('data-source/*/*.csv') if 'metadata' not in filename]


# -- ENDPOINTS --------------------


# GET endpoint - list all csv files
@app.get("/")
def home():
    return {"List of csv files": all_csv}


# POST endpoint - upload csv file
@app.post("/upload/")
async def upload_file(
    df: str = Query("Choose file...", enum=all_csv, description="Choose csv file from data samples folder."), 
    db: Session = Depends(getDB)):

    try:
        # Isolate first 3 columns, for the sake of the exercice
        data = np.genfromtxt(df, delimiter=',', skip_header=1)[:,:3]

        # Ensure no missing data
        if True in np.isnan(data):
            return {"Missing value": f"File {df} contains missing value."}
        
        # If no missing data, then upload data
        else:
            upload_data(db=db, dataset=data)
            return {'Message':'Data successfully uploaded!'}
    
    except:
        raise HTTPException(status_code=500, detail=f"Error: data couldn't be uploaded.")



# DELETE endpoint - delete row in db
@app.delete("/delete/")
async def delete_file(
    item_id: int = Query(..., description="ID to be deleted.", gt=0),
    db: Session = Depends(getDB)):
    
    try:
        deleteAnExperience(db=db, id=item_id)
        return {"Message":f"Experience with id {item_id} successfully deleted."}

    except:
        raise HTTPException(status_code=500, detail=f"Experience with id {item_id} does not exist.")