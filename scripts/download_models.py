from huggingface_hub import hf_hub_download
from tensorflow.keras.models import load_model

def download_models():
    """Downloads EfficientNetV2S & ViT-Hybrid models from Hugging Face Hub"""
    
    # download EfficientNetV2S model
    eff_model_path = hf_hub_download(repo_id="MooseML/EfficientNet-Cancer-Detection", filename="efficientnet_cancer_model.h5")
    eff_model = load_model(eff_model_path)
    print("EfficientNetV2S model downloaded and loaded!")

    # Download ViT-Hybrid model
    vit_model_path = hf_hub_download(repo_id="MooseML/EfficientNet-Cancer-Detection", filename="ViT_hybrid_cancer_model.h5")
    vit_model = load_model(vit_model_path)
    print("ViT-Hybrid model downloaded and loaded!")

    return eff_model, vit_model

if __name__ == "__main__":
    download_models()
