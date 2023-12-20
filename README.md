# COMP550_project
## Initial labelling, stats and loading of data
Initial data labelling and preprocessing can be found /data folder
## HPC Scripts
Most processing and training required large amount of ram and processing power, so they where run on a HPC-cluster (High Performance Computing)
HPC scripts covers all high data volume processing and training of embeddings using word2vec.
The full goodreads_reviews_young_adult.json should be provided.
### clean_to_pickle.py
Cleans and preprocesses the entire dataset and compiles it to single file.
### Cluster_review.py
Trains the classifier model on the split labelled dataset provided.
### evalute classifier.py
Used for additional stats of the classifier, with a given confidence.
### gender_split_data.py
Uses the trained classifier model to create a male and female dataset, from the entire dataset with high confidence samples.
### merge_dataset.ipynb
Merges the human labelled and classified datasets to one using sets.
### word2vec.py
Skipgram model.
Train the embeddings on a given dataset.
### submit.sh
HPC script specifying python script and ressources for the HPC.

## Analisys and semaxis.
SemAxis contain the SemAxis framework functions.
Plots and analisys loads the embeddings models that where trained on the hpc, and uses the SemAxis framework to make some analisys functions and create plots using the axis word found in the folder /axes.