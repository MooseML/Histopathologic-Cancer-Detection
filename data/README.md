# Data Directory

This folder should contain the dataset for **Histopathologic Cancer Detection**.

## 🔹 How to Get the Dataset
Due to file size constraints, the dataset is **not included in this repo**. You must download it manually.

### Option 1: Download from Kaggle
1. Go to [Kaggle Dataset Page](https://www.kaggle.com/competitions/histopathologic-cancer-detection/data).
2. Download `train.zip`, `test.zip`, and `train_labels.csv`.
3. Extract them into the `data/` folder.

Expected structure:
```bash
data/
├── train/                 # Training images
├── test/                  # Test images
├── train_labels.csv        # Labels for training images
```

### Option 2: Use the Kaggle API
Run:
```sh
python scripts/download_data.py
```

Now the dataset is ready to use!

---

# Models Directory

This folder contains **trained model weights** in `.h5` format.

## 📂 Available Models
| Model File               | Description                         |
|--------------------------|-------------------------------------|
| `efficientnet_model.h5`  | EfficientNetV2S trained model      |
| `vit_hybrid_model.h5`    | Vision Transformer Hybrid model    |

## 🔹 How to Use These Models
To load a saved model in TensorFlow:
```python
from tensorflow.keras.models import load_model

# Load EfficientNet
model = load_model("models/efficientnet_model.h5")

# Load ViT-Hybrid
vit_model = load_model("models/vit_hybrid_model.h5")
```

---

# Kaggle Submissions

This folder contains **final submission CSVs** for the Kaggle competition.

## Submission Files
| File Name                 | Description                           |
|---------------------------|---------------------------------------|
| `submission_effnet.csv`   | EfficientNetV2S predictions          |
| `submission_vit.csv`      | ViT-Hybrid predictions               |
| `submission_ensemble.csv` | Ensemble of EfficientNet & ViT-Hybrid |

## How to Submit on Kaggle
1. Go to [Kaggle Submission Page](https://www.kaggle.com/competitions/histopathologic-cancer-detection/submissions).
2. Upload the desired CSV file.
3. Click **Submit** and wait for the results.

```markdown
# Data Directory

This folder should contain the dataset for **Histopathologic Cancer Detection**.

## **🔹 How to Get the Dataset**
Due to file size constraints, the dataset is **not included in this repo**. You must download it manually.

### **Option 1: Download from Kaggle**
1. Go to [Kaggle Dataset Page](https://www.kaggle.com/competitions/histopathologic-cancer-detection/data).
2. Download `train.zip`, `test.zip`, and `train_labels.csv`.
3. Extract them into the `data/` folder.

Expected structure:
```
data/
├── train/                 # Training images
├── test/                  # Test images
├── train_labels.csv        # Labels for training images
```

### **Option 2: Use the Kaggle API**
Run:
```sh
python scripts/download_data.py
```

Now the dataset is ready to use!
```

---

## ** `models/README.md` (Model Storage)**
This **goes inside the `models/` folder**.

```markdown
# Models Directory

This folder contains **trained model weights** in `.h5` format.

## **📂 Available Models**
| Model File               | Description                         |
|--------------------------|-------------------------------------|
| `efficientnet_model.h5`  | EfficientNetV2S trained model      |
| `vit_hybrid_model.h5`    | Vision Transformer Hybrid model    |

## **🔹 How to Use These Models**
To load a saved model in TensorFlow:
```python
from tensorflow.keras.models import load_model

# Load EfficientNet
model = load_model("models/efficientnet_model.h5")

# Load ViT-Hybrid
vit_model = load_model("models/vit_hybrid_model.h5")
```
```

---

## ** `submissions/README.md` (Kaggle Submissions)**
This **goes inside the `submissions/` folder**.

```markdown
#  Kaggle Submissions

This folder contains **final submission CSVs** for the Kaggle competition.

## ** Submission Files**
| File Name                 | Description                           |
|---------------------------|---------------------------------------|
| `submission_effnet.csv`   | EfficientNetV2S predictions          |
| `submission_vit.csv`      | ViT-Hybrid predictions               |
| `submission_ensemble.csv` | Ensemble of EfficientNet & ViT-Hybrid |

## ** How to Submit on Kaggle**
1. Go to [Kaggle Submission Page](https://www.kaggle.com/competitions/histopathologic-cancer-detection/submissions).
2. Upload the desired CSV file.
3. Click **Submit** and wait for the results.
```

---
