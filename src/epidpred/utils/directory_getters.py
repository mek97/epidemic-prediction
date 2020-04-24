import os

EPIDEMIC_PRED_DIR = os.getenv('EPIDEMIC_PRED_DIR', "~/Workspace/personal/epidemic-prediction")


class DirectoryGetter:

    @staticmethod
    def get_base_directory(path=""):
        return str(os.path.join(EPIDEMIC_PRED_DIR, path))

    @staticmethod
    def get_data_path(path):
        base_dir = DirectoryGetter.get_base_directory()
        return str(os.path.join(base_dir, "data", path))
