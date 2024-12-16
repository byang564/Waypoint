from fastapi import APIRouter
from src.models.dtos.coords import Coords
from src.services.ShortestPathOSM import ShortestPath
from src.services.geocode import locate

router = APIRouter(prefix="/path")

@router.post("/")
async def receive_path(data: Coords):
    start = data.start
    end = data.end
    data_structure = data.data_structure

    start_coords = locate(start)
    end_coords = locate(end)
    
    return ShortestPath(start_coords, end_coords, data_structure)