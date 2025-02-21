# Histopathologic Cancer Detection

This project uses **EfficientNetV2S** and **ViT-Hybrid** models to detect metastatic cancer in histopathologic images. It applies **CNNs for local feature extraction** and **Transformers for global feature learning**, achieving high classification performance.

## Project Structure
```bash
histopathologic-cancer-detection/
│── .devcontainer/             # VS Code DevContainer setup
│── data/                      # Dataset folder (not included in repo)
│── notebooks/                 # Jupyter Notebooks
│── scripts/                   # Utility scripts (e.g., dataset download, model fetch)
│── submissions/               # Kaggle CSV submissions
│── requirements.txt           # Python dependencies
│── README.md                  # Project documentation (this file)
```

## Getting Started

### Clone the Repository
```sh
git clone https://github.com/your_username/histopathologic-cancer-detection.git
cd histopathologic-cancer-detection
```

### Set Up the Environment

Using **Docker**:
```sh
# Build and start the devcontainer in VS Code
# (If using VS Code, open the project and select "Reopen in Container")
```

Using **Virtual Environment (Not Necessary)**:
```sh
python -m venv env
source env/bin/activate  # For macOS/Linux
env\Scripts\activate     # For Windows

pip install -r requirements.txt
```

### Download the Dataset
This dataset is too large for GitHub. Download it from **Kaggle**:

#### Option 1: Manually Download
1. Go to [Kaggle](https://www.kaggle.com/competitions/histopathologic-cancer-detection/data)
2. Click **Download All**.
3. Extract them into the `data/` directory.

#### Option 2: Run the Kaggle API Script
Ensure your **Kaggle API key (`kaggle.json`)** is set up, then run:
```sh
python scripts/download_data.py
```

### Download Pretrained Models
If you do not want to adjust the models and train from scratch you can download the pretrained models. Since the trained models were too large for GutHub, they are stored on the Hugging Face Hub.  

Run this script to automatically fetch them:
```sh
python scripts/download_models.py
```

### Train the Model 
Open **Jupyter Notebook**:
```sh
jupyter lab
```
Run **`notebooks/histopathic_cancer_detection.ipynb`** to train EfficientNetV2S or ViT-Hybrid.

---

## Model Details
| Model              | Private Score | Public Score |
|-------------------|--------------|-------------|
| EfficientNetV2S  | 0.9359        | 0.9374      |
| ViT-Hybrid       | 0.9507        | 0.9487      |
| ViT-Hybrid + TTA | 0.9576        | 0.9647      |
| Weight Ensemble  | 0.9647        | 0.9680      |

---
### Resources
1. Kaggle Competition [Kaggle](https://www.kaggle.com/competitions/histopathologic-cancer-detection/)
2. Hugging Face Models [Hugging Face](https://huggingface.co/MooseML/EfficientNet-Cancer-Detection)
---
## License
This project is licensed under the MIT License.
