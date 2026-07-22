from fastapi import APIRouter
from app.schemas.schemas import CopilotMessage, CopilotResponse
from app.agents.copilot_agent import ask_soc_copilot

router = APIRouter()

@router.post("/chat", response_model=CopilotResponse)
async def chat_with_soc_copilot(req: CopilotMessage):
    result = ask_soc_copilot(query=req.message, incident_context=req.incident_id)
    return CopilotResponse(**result)
