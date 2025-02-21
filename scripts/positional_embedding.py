# positional_embedding.py
from tensorflow.keras.layers import Layer 
class PositionalEmbedding(Layer):
    def __init__(self, num_patches, embedding_dim):
        super(PositionalEmbedding, self).__init__()
        self.pos_embedding = self.add_weight("pos_embedding", shape=(1, num_patches, embedding_dim), initializer="random_normal")

    def call(self, inputs):
        return inputs + self.pos_embedding