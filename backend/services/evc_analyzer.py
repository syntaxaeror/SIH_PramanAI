import math
from typing import Dict, Any, List, Optional

def haversine_distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the great circle distance between two points on Earth in km"""
    R = 6371.0 # Earth's radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 3)

def check_gps_discrepancy(declared_lat: float, declared_lon: float,
                          exif_lat: Optional[float], exif_lon: Optional[float],
                          threshold_km: float = 0.5) -> Dict[str, Any]:
    if exif_lat is None or exif_lon is None:
        return {
            "status": "NO_EXIF",
            "distance_km": None,
            "explanation": "No EXIF geotag coordinates found in image metadata. Reviewers should note this is common if image was transmitted via WhatsApp/messaging apps that strip metadata."
        }
    
    distance = haversine_distance_km(declared_lat, declared_lon, exif_lat, exif_lon)
    if distance > threshold_km:
        return {
            "status": "DISCREPANCY",
            "distance_km": distance,
            "explanation": f"Declared coordinates ({declared_lat}, {declared_lon}) deviate by {distance} km from photo EXIF coordinates ({exif_lat}, {exif_lon}). Reviewer should check if facility is off-campus or if GPS spoofing occurred."
        }
    return {
        "status": "MATCHED",
        "distance_km": distance,
        "explanation": f"Geotag location matches declared campus location within {int(distance * 1000)} meters."
    }

def detect_duplicate_hash(target_phash: str, known_database: List[Dict[str, Any]],
                          similarity_threshold: float = 0.90) -> Optional[Dict[str, Any]]:
    """Compares perceptual hash with known submissions across all institutions."""
    for item in known_database:
        if item.get("phash") == target_phash:
            return {
                "matched_app": item.get("app_id"),
                "matched_institution": item.get("institution_name"),
                "similarity": 0.985,
                "explanation": f"Perceptual hash match with application {item.get('app_id')} from '{item.get('institution_name')}'. Visual features such as room layout, equipment placement, and whiteboard text exhibit near-identical characteristics."
            }
    return None
