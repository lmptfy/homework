# Import necessary dependencies
from sqlalchemy.orm import Session
from models import Experience

# Create a data.csv model object
def upload_data(db:Session, dataset): 

    # Iterate over dataset
    for data in dataset:

        # Ensure 'Machine_N_cycles' column has no negative number (as it should be impossible)
        if data[0] < 0:
            print('Machine_N_cycles cannot be smaller than 0. Verify your data.')

        # If data is valid, then add it to the record
        else:
            record = Experience(**{
                'Machine_N_cycles': data[0],
                'Machine_Load': data[1],
                'Machine_Displacement': data[2]})

            db.add(record) # Add object in db session
    db.commit()            # Commit whole to the db
    db.refresh(record)     # Refresh attributes
    
    return dataset


# Get a specific experience
def getAnExperience(db:Session, id:int):
    anExperience = db.query(Experience).filter(Experience.id==id).one()
    return anExperience


# Delete a specific experience
def deleteAnExperience(db:Session, id:int):
    # Get the reference from prev func
    anExperience = getAnExperience(db=db, id=id)
    db.delete(anExperience)
    db.commit() 