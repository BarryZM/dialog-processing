class Config(object):
    def __init__(self, task):
        # Data processing
        self.download_url = "http://www.mpi-sws.org/~cristian/data/cornell_movie_dialogs_corpus.zip"

        # Management
        self.raw_data_dir = "../data/cornellmovie/raw_data"

        # Task-specific management
        self.task = task
        self.task_data_dir = f"../data/cornellmovie/{task}"
        self.dataset_path = f"{self.task_data_dir}/dataset.txt"
        self.word_count_path = f"{self.task_data_dir}/word_count.txt"

        # Pretrained embeddings (for initialization and evaluation)
        self.word_embedding_path = f"{self.task_data_dir}/glove_twitter_200.json"
        self.eval_word_embedding_path = f"{self.task_data_dir}/google_news_300.json"
