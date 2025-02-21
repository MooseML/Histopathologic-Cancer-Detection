---

### ** `README.md` (Main Project Documentation)**
```markdown
#  Histopathologic Cancer Detection

This project uses **EfficientNetV2S** and **ViT-Hybrid** models to detect metastatic cancer in histopathologic images. It applies **CNNs for local feature extraction** and **Transformers for global feature learning**, achieving high classification performance.

## Project Structure
```
histopathologic-cancer-detection/
│── .devcontainer/             # VS Code DevContainer setup
│── data/                      # Dataset folder (not included in repo)
│── notebooks/                 # Jupyter Notebooks
│── scripts/                   # Utility scripts (e.g., dataset download)
│── models/                    # Saved model weights (.h5 files)
│── submissions/               # Kaggle CSV submissions
│── requirements.txt           # Python dependencies
│── README.md                  # Project documentation (this file)
```

##  **Getting Started**
### ** Clone the Repository**
```sh
git clone https://github.com/your_username/histopathologic-cancer-detection.git
cd histopathologic-cancer-detection
```

### ** Set Up the Environment**
Using **Docker**:
```sh
# Build and start the devcontainer in VS Code
# (If using VS Code, open the project and select "Reopen in Container")
```

Using **Virtual Environment (Optional)**
```sh
python -m venv env
source env/bin/activate  # For macOS/Linux
env\Scripts\activate     # For Windows

pip install -r requirements.txt
```

### ** Download the Dataset**
This dataset is too large for GitHub. Download it from **Kaggle**:

**🔹 Option 1: Manually Download**
1. Go to [Kaggle](https://www.kaggle.com/competitions/histopathologic-cancer-detection/data).
2. Download **train.zip** and **test.zip**.
3. Extract them into the `data/` directory.

**🔹 Option 2: Run the Kaggle API Script**
Ensure your **Kaggle API key (`kaggle.json`)** is set up, then run:
```sh
python scripts/download_data.py
```

### ** Train the Model**
Open **Jupyter Notebook**:
```sh
jupyter lab
```
Run **`notebooks/your_training_notebook.ipynb`** to train EfficientNetV2S or ViT-Hybrid.

---

##  **Model Details**
| Model              | Private Score | Public Score |
|-------------------|--------------|-------------|
| EfficientNetV2S  | 0.9359        | 0.9374      |
| ViT-Hybrid       | 0.9507        | 0.9487      |
| ViT-Hybrid + TTA | 0.9576        | 0.9647      |
| Ensemble Model   | 0.9650        | 0.9675      |

---

##  **License**
This project is licensed under the MIT License.

---

---

