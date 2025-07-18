import torch.nn as nn


class BucketedEmbedding(nn.Embedding):

    def __init__(self, bucket_size, num_embeddings, *args, **kwargs):
        self.bucket_size = bucket_size
        real_num_embeddings = (num_embeddings + bucket_size - 1) // bucket_size
        super(BucketedEmbedding, self).__init__(real_num_embeddings, *args, **kwargs)

    def forward(self, indices):
        x = super(BucketedEmbedding, self).forward(indices // self.bucket_size)
        return x.unsqueeze_(0) if x.ndim < 2 else x
