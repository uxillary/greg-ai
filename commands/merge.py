import torch

decoder = torch.load("output/pretrained/Tacotron2Decoder.pt", map_location="cpu")
encoder = torch.load("output/pretrained/Tacotron2Encoder.pt", map_location="cpu")
postnet = torch.load("output/pretrained/Tacotron2Postnet.pt", map_location="cpu")
embedding = torch.load("output/pretrained/TextEmbedding.pt", map_location="cpu")

merged_model = {
    "decoder": decoder,
    "encoder": encoder,
    "postnet": postnet,
    "embedding": embedding
}

torch.save(merged_model, "output/pretrained/tacotron2_merged.pth")
