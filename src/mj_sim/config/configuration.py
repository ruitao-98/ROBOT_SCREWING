import os


class DirectoryConfig:
    """
    Class for storing directories within the package
    """

    _dir_path = os.path.dirname(os.path.realpath(__file__))
    SAVE_DIR = _dir_path + '/../results/model_fitting'
    RESULTS_DIR = _dir_path + '/../results'
    CONFIG_DIR = _dir_path + ''
    DATA_DIR = _dir_path + '/../data'


class SimpleSimConfig:
    """
    Class for storing the Simplified Simulator configurations.
    """
    simulation_disturbances = {
        "groove1": True, 
        "groove2": False,  
        "screw1": False,                      
        "screw2": False,                               
    }

class RecordingOptions:
    recording_options = {
        "dataset_name": "sim_dataset",
        "training_split": True,
    }