from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from app.core.security import create_access_token, verify_password, get_password_hash
from app.schemas.schemas import Token, UserResponse

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

# Demo User Profile
DEMO_USER = {
    "id": "usr_cni_admin_01",
    "email": "analyst@sentinel.cni.gov",
    "full_name": "Senior SOC Lead",
    "role": "SOC Analyst",
    "is_active": True,
    "created_at": "2026-01-01T00:00:00"
}

@router.post("/login", response_model=Token)
async def login(req: LoginRequest):
    if req.email == "analyst@sentinel.cni.gov" and req.password == "sentinel2026":
        token = create_access_token(subject=DEMO_USER["id"])
        return Token(access_token=token, token_type="bearer", user=UserResponse(**DEMO_USER))
    
    # Allow any login for demo convenience
    token = create_access_token(subject="usr_demo")
    return Token(
        access_token=token, 
        token_type="bearer", 
        user=UserResponse(
            id="usr_demo",
            email=req.email,
            full_name="SOC Security Engineer",
            role="Admin",
            is_active=True,
            created_at="2026-01-01T00:00:00"
        )
    )

@router.get("/me", response_model=UserResponse)
async def get_me():
    return UserResponse(**DEMO_USER)
