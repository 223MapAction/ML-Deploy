import torch
from torchvision.models import vgg16_bn, VGG16_BN_Weights


def m_a_model(num_classes: int):
    """
    Initializes and modifies a VGG16 model with batch normalization to classify a specified number of classes.
    """
    # Load VGG16 model with batch normalization weights
    vgg16_bn_weights = VGG16_BN_Weights.DEFAULT
    model = vgg16_bn(weights=vgg16_bn_weights)

    # Freeze all parameters in the model
    for params in model.parameters():
        params.requires_grad = False

    # Modify the classifier to adapt to the number of classes
    num_features = model.classifier[-1].in_features
    features = list(model.classifier.children())[:-1]  # Remove the last layer
    features.extend([torch.nn.Linear(num_features, num_classes)])
    model.classifier = torch.nn.Sequential(*features)

    return model
