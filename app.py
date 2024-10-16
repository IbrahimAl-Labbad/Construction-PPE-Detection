from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import uvicorn
import cv2
import numpy as np
from ultralytics import YOLO
from io import BytesIO

# Initialize FastAPI app
app = FastAPI()

# Load the YOLOv8n model with custom weights
model = YOLO('C:/Users/AcTivE/Desktop/Project/Construction PPE Detection/train/weights/best.pt')

def draw_boxes(image, results):
    """Draw bounding boxes on the image."""
    for box in results[0].boxes:
        x_min, y_min, x_max, y_max = map(int, box.xyxy[0].tolist())
        class_name = results[0].names.get(int(box.cls[0]), "Unknown")
        confidence = box.conf[0]

        # Draw rectangle and label on the image
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        label = f"{class_name}: {confidence:.2f}"
        cv2.putText(image, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image

@app.post("/detect")
async def detect_objects(file: UploadFile = File(...)):
    try:
        # Ensure uploaded file is an image
        if not file.filename.lower().endswith((".jpg", ".jpeg", ".png")):
            print(f"Invalid file format: {file.filename}")  # Debugging line
            raise HTTPException(status_code=400, detail="Invalid file format. Please upload a JPG or PNG image.")

        # Read and decode the uploaded image
        image_bytes = await file.read()
        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

        if image is None:
            print("Image decoding failed.")  # Debugging line
            raise HTTPException(status_code=400, detail="Invalid image format")

        # Run inference on the image
        results = model(image)

        # Draw bounding boxes on the image
        image_with_boxes = draw_boxes(image, results)

        # Encode the processed image as JPEG
        _, img_encoded = cv2.imencode('.jpg', image_with_boxes)
        return StreamingResponse(BytesIO(img_encoded.tobytes()), media_type="image/jpeg")

    except Exception as e:
        # Return error response in case of exception
        print(f"Error occurred: {str(e)}")  # Debugging line
        raise HTTPException(status_code=500, detail=str(e))

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
