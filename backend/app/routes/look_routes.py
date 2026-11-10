
from fastapi import APIRouter
from app.services.look_generator import generate_best_looks

router = APIRouter()

@router.post("/generate-look")
def generate_look():

    items = [
        {"name":"camisa azul","category":"top","color":"blue"},
        {"name":"calça preta","category":"bottom","color":"black"},
        {"name":"tenis branco","category":"shoes","color":"white"},
        {"name":"calça bege","category":"bottom","color":"beige"}
    ]

    looks = generate_best_looks(items, temperature=25, desired_style="casual")

    return {
        "looks": looks
    }
