"""alzheimers: Thie file contains the custom implementaion of 4 class Alzheimers dataset.
See citation below for additional details and links
"""

#from __future__ import absolute_import
#from __future__ import division
#from __future__ import print_function


import io
import os
import tarfile

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds
#import tensorflow_datasets as tfds

# TODO(alzheimers): BibTeX citation
_CITATION = """
https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images
"""

# TODO(alzheimers):
_DESCRIPTION = """
This is a multi class alzheimers detection dataset.
It has 4 classes ranging from no demetia to severe dementia.
All images are pre-processed and properly aligned
"""

_LABELS = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]

class Alzheimers(tfds.core.GeneratorBasedBuilder):
  """TODO(alzheimers): Short description of my dataset."""

  # TODO(alzheimers): Set up version.
  VERSION = tfds.core.Version('0.1.0')
  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  Dataset can be downloaded from https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images.
  After downloading, unzip train and test directories under folder called alzheimers
  """
  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Image(shape=[208, 176, 3]),
            'label': tfds.features.ClassLabel(names=_LABELS),
            'filename': tfds.features.Text(),

        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=('image', 'label'),
        # Homepage of the dataset for documentation
        homepage="http://custom.net",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # TODO(alzheimers): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    train_path = os.path.join(dl_manager.manual_dir, 'alzheimers', 'train')
    test_path = os.path.join(dl_manager.manual_dir, 'alzheimers', 'test')
    if not tf.io.gfile.exists(train_path) or not tf.io.gfile.exists(test_path):
      raise AssertionError(
          'Alzheimers dataset requires manual download of the data. Please download '
          'the train and val set and place them into: {}, {}'.format(
              train_path, test_path))
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'path': train_path},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={'path': test_path},
        ),
    ]

  def _generate_examples(self, path):
    """Yields examples."""
    for label in tf.io.gfile.listdir(path):
      for filename in tf.io.gfile.glob(os.path.join(path, label, '*.jpg')):
        example = {
          'image': filename,
          'label': label,
          'filename': os.path.basename(filename)
        }
        yield filename, example
