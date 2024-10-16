# **Construction PPE Detection 🚧**

This project utilizes a **YOLOv8** object detection model to identify essential Personal Protective Equipment (PPE) on construction workers, such as helmets, vests, gloves, and boots. It ensures safety compliance by detecting whether workers are wearing the required gear.

---

## **Table of Contents**
1. [Project Overview](#project-overview)  
2. [Dataset](#dataset)  
3. [Model Training](#model-training)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Results](#results)  
7. [FastAPI and Streamlit Application](#fastapi-and-streamlit-application)  
8. [Folder Structure](#folder-structure)  


---

## **Project Overview**
Ensuring workers wear appropriate PPE on construction sites is crucial for safety. This project leverages YOLOv8 for real-time detection of PPE in images and videos. The model is trained to identify:
- **Helmets**
- **Vests**
- **Gloves**
- **Boots**
- **Humans**

The goal is to assist in safety monitoring and compliance enforcement on construction sites.

---

## **Dataset**
- The dataset contains images of construction workers wearing or not wearing required PPE.  
- **Classes:**  
  - `0: boots`
  - `1: gloves`
  - `2: helmet`
  - `3: human`
  - `4: vest`

**Note:** The dataset used is too large to include in this repository. You can download the dataset from [Roboflow](https://roboflow.com/) or use your own dataset by configuring the `data.yaml` file.

---

## **Model Training**
We used **YOLOv8** for training and evaluation:
- **Epochs:** 20  
- **Image Size:** 640x640  
- **Optimizer:** SGD/Adam  
- **Loss:** Cross-entropy + IoU Loss  

Trained model weights are saved under `train/weights/`.

---

## **Installation**

1. Clone this repository:
   ```bash
   git clone https://github.com/IbrahimAl-Labbad/Construction-PPE-Detection.git
   cd Construction-PPE-Detection

2. Install dependencies:
   ```bash
   pip install ultralytics opencv-python-headless matplotlib
   
3. Verify the installation by running:
     ```bash
     yolo help
     
## **Usage**
1. Train the Model
   Make sure to modify data.yaml to point to your dataset, then run:
   ```bash
   yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=20 imgsz=640


2. Evaluate the Model
   To validate the model on the validation dataset:
   ```bash
    yolo task=detect mode=val model=runs/detect/train/weights/best.pt data=data.yaml imgsz=640
   
3. Test the Model
   Run the model on the test dataset:
     ```bash
   yolo task=detect mode=test model=runs/detect/train/weights/best.pt data=data.yaml imgsz=640

## **Results**
The model detects the following PPE equipment:

-  **Helmets:** ✅
-  **Vests:** ✅
-  **Gloves:** ✅
-  **Boots:** ✅
-  **Humans:** ✅

##  **FastAPI and Streamlit Application**
- This project includes a FastAPI backend that serves a RESTful API for PPE detection. It utilizes the YOLOv8 model to process image uploads and return detection results.

- A Streamlit frontend provides an interactive interface for users to upload images and view detected PPE in real time. The combination of FastAPI and Streamlit allows for efficient processing and user-friendly interactions.


## **Folder Structure**
```
Construction-PPE-Detection/
│
├── train/
│   ├── weights/
│   └── ...  
│
├── fastapi_app/
│   └── main.py
│
├── streamlit_app/
│   └── app.py
│
├── data.yaml
├── requirements.txt
└── README.md
```
## **Thanks for Reading!** 🙏

I appreciate your interest in the Construction PPE Detection project. If you have any questions or feedback, feel free to reach out!




