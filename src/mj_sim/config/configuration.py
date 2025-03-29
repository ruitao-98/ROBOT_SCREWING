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

class ModelFitConfig:
    """
    Class for storing flags for the model fitting scripts.
    """

    # ## Dataset loading ## #
    ds_name = "sim_dataset"
    ds_metadata = {
        "groove1": True, 
        "groove2": False,  
        "screw1": False,                      
        "screw2": False,   
    }

    # ds_metadata = {
    #     "gazebo": "default",
    # }

    # ## Visualization ## #
    # Training mode
    visualize_training_result = False
    visualize_data = False

    # Visualization mode
    grid_sampling_viz = True
    x_viz = [7, 8, 9]
    u_viz = []
    y_viz = [7, 8, 9]

    # ## Data post-processing ## # 用于数据后处理，数据清洗，按照一定规则删除异常数据
    histogram_bins = 40              # Cluster data using histogram binning
    histogram_threshold = 0.001      # Remove bins where the total ratio of data is lower than this threshold
    velocity_cap = 16                # Also remove datasets point if abs(velocity) > x_cap

    # ############# Experimental ############# #

    # ## Use fit model to generate synthetic data ## #
    use_dense_model = False
    dense_model_version = ""
    dense_model_name = ""
    dense_training_points = 200

    # ## Clustering for multidimensional models ## #
    clusters = 5  # 决定了使用几个GP模型
    load_clusters = False
