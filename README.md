# COMP550_project
The full goodreads_reviews_young_adult.json used for this can be found here:
https://mengtingwan.github.io/data/goodreads.html
## Initial labelling, stats and loading of data
Initial data labelling and preprocessing can be found /data folder
Needs to include goodreads_reviews_young_adult.json
## HPC Scripts
Most processing and training required large amount of ram and processing power, so they where run on a HPC-cluster (High Performance Computing)
HPC scripts covers all high data volume processing and training of embeddings using word2vec.
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

The pretrained models from our analisys can be found in the /models folder.
They are they are all there except the entire datamodel, which requires the download of an addtional file "full_young.wordvectors.vectors.npy" which can be downloaded here:
https://drive.google.com/file/d/1sTgbDlwCm7_DjXyJ2nmaqDpg65p457f8/view?usp=drive_link
