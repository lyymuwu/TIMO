import os

from .utils import Datum, DatasetBase
from .oxford_pets import OxfordPets


template = ['a photo of a {}.']


class Caltech101(DatasetBase):

    dataset_dir = 'caltech-101'

    def __init__(self, root, num_shots):
        self.dataset_dir = os.path.join(root, self.dataset_dir)
        self.image_dir = os.path.join(self.dataset_dir, '101_ObjectCategories')
        self.split_path = os.path.join(self.dataset_dir, 'split_zhou_Caltech101.json')

        self.template = template
        self.cupl_path = './Prompt_CuPL/caltech101.json'
        self.waffle_path = './Prompt_Waffle/caltech101.json'
        self.DCLIP_path = './Prompt_DCLIP/caltech101.json'

        train, val, test = OxfordPets.read_split(self.split_path, self.image_dir)
        train = self.generate_fewshot_dataset(train, num_shots=num_shots)

        super().__init__(train_x=train, val=val, test=test)