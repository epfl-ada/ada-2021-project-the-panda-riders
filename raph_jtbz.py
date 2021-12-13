# conda install pyarrow fastparquet pandas gdown

# Imports you may need
from dataloader import *
from finance import *
import pandas as pd
import pageviewapi 
from tqdm import tqdm

from finance import stock, compare
from quotebankexploration import *
from wikipedia import *

if __name__ == "__main__":
    # Get some data frames
    wiki_data = concat_wiki_files()
    filtered_quotes = get_filtered_quotes()
    speakers_id = pd.DataFrame(get_speakers_ids(filtered_quotes))
    speakers_labels = get_speakers_labels()

    '''
    REMARK: Année de 2017 à 2020 => 2015 et 2016 déjà fait
    '''
    year = 2015

    # DO NOT TOUCH
    tqdm.pandas()
    path = os.path.join('data/wiki_speaker_attributes/speakers_pageviews_'+str(year))
    speakers_labels[str(year)] = speakers_labels.label.progress_apply(lambda label: get_page_views_per_year(label, year))
    speakers_labels.to_pickle(path)