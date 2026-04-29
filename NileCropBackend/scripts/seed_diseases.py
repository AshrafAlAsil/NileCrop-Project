from database import SessionLocal
from models import DiseaseInfo

db = SessionLocal()

diseases = [
    {
        "name": "Powdery Mildew",
        "description": "White powdery spots on leaves and stems.",
        "treatment": "Use sulfur-based fungicide and improve air circulation."
    },
    {
        "name": "Leaf Rust",
        "description": "Orange-brown rust spots on leaves.",
        "treatment": "Apply rust-resistant fungicide."
    },
    {
        "name": "Early Blight",
        "description": "Dark concentric spots on older leaves.",
        "treatment": "Use copper fungicide and remove infected leaves."
    },
    {
        "name": "Late Blight",
        "description": "Large dark blotches on leaves and fruit.",
        "treatment": "Apply systemic fungicide immediately."
    },
    {
        "name": "Bacterial Spot",
        "description": "Small water-soaked spots on leaves.",
        "treatment": "Use copper sprays and avoid overhead watering."
    },
    {
        "name": "Downy Mildew",
        "description": "Yellow patches on leaves with fuzzy underside.",
        "treatment": "Improve drainage and apply fungicide."
    },
    {
        "name": "Leaf Mold",
        "description": "Yellow spots turning brown with mold underneath.",
        "treatment": "Increase ventilation and apply fungicide."
    },
    {
        "name": "Anthracnose",
        "description": "Dark sunken lesions on fruit and leaves.",
        "treatment": "Remove infected parts and spray fungicide."
    },
    {
        "name": "Septoria Leaf Spot",
        "description": "Small circular spots with gray centers.",
        "treatment": "Remove affected leaves and apply fungicide."
    },
    {
        "name": "Target Spot",
        "description": "Brown spots with concentric rings.",
        "treatment": "Use appropriate fungicide spray."
    },
    {
        "name": "Healthy",
        "description": "No disease detected. Plant is healthy.",
        "treatment": "No treatment needed."
    },
    {
        "name": "Yellow Leaf Curl Virus",
        "description": "Leaves curl and turn yellow.",
        "treatment": "Control whiteflies and remove infected plants."
    },
    {
        "name": "Mosaic Virus",
        "description": "Mosaic pattern of light and dark green on leaves.",
        "treatment": "Remove infected plants and disinfect tools."
    },
    {
        "name": "Fusarium Wilt",
        "description": "Wilting and yellowing of leaves.",
        "treatment": "Use resistant varieties and soil treatment."
    },
    {
        "name": "Verticillium Wilt",
        "description": "Yellowing between veins and wilting.",
        "treatment": "Crop rotation and soil sterilization."
    },
    {
        "name": "Root Rot",
        "description": "Roots become brown and mushy.",
        "treatment": "Improve drainage and avoid overwatering."
    },
    {
        "name": "Leaf Miner",
        "description": "Winding trails inside leaves.",
        "treatment": "Use insecticide and remove affected leaves."
    }
]

for d in diseases:
    db.add(DiseaseInfo(**d))

db.commit()
db.close()

print("Diseases seeded successfully")