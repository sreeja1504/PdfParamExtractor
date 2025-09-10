from fastapi import FastAPI, APIRouter, HTTPException, Query
from bson import ObjectId
from dbconfig import part_info_collection
from models import PartData

app = FastAPI()
router = APIRouter()
  
@router.post("/add-part")
def create_part_data(part_data : PartData):
    try:
        # 1. Check for existing data based on company_name and generic_part_number
        existing_part = part_info_collection.find_one({
            "company_name": part_data.company_name,
            "generic_part_number": part_data.generic_part_number
        })

        # 2. If a match is found, return the existing ID
        if existing_part:
            return {
                "status_code": 200, 
                "message": f"Part data already exists with id: {str(existing_part['_id'])}."
            }
        
        # 3. If no match is found, save the new data
        else:
            part_data_dict = part_data.dict()
            resp = part_info_collection.insert_one(part_data_dict)
            return {"status_code":200,  "message": f"Part data saved successfully with id: {str(resp.inserted_id)}!"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error occured : {e.detail}")

@router.get("/all-parts")
def get_all_parts():
    try:
        all_parts = part_info_collection.find().to_list()
        
        # Convert ObjectID to string for serialization
        for part in all_parts:
            if '_id' in part:
                part['_id'] = str(part['_id'])
        
        return all_parts

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error occured : {e.detail}")

@router.put("/update_part")
async def update_part_data(
    updated_part_data : PartData, 
    part_id : str | None = Query(None), 
    company_name : str | None = Query(None), 
    generic_part_number : str | None = Query(None)):
    try:
        # Build the filter dynamically
        update_filter = {}
        if part_id:
            update_filter["_id"] = ObjectId(part_id)
        elif company_name and generic_part_number:
            update_filter["company_name"] = company_name
            update_filter["generic_part_number"] = generic_part_number
        else:
            raise HTTPException(
                status_code=400,
                detail="Either 'part_id' or a combination of 'company_name' and 'generic_part_number' must be provided."
            )
        
        update_fields = updated_part_data.dict(exclude_unset=True)
        
        if not update_fields:
            raise HTTPException(
                status_code=400,
                detail="No update data provided in the request body."
            )

        # Perform the update operation
        resp = part_info_collection.update_one(update_filter, {"$set": update_fields})

        if resp.matched_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Part data does not exist for the provided identifiers."
            )

        return {"status_code": 200, "message": "Part data updated successfully"}
 
    except Exception as e:
        status_code = e.status_code if isinstance(e, HTTPException) else 500
        return HTTPException(status_code=status_code, detail=f"Error occured : {e.detail}")

app.include_router(router)
