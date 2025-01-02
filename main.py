import create_tested_data
import preprocess_tested_data
import prepare_model
import test_model

if __name__ == "__main__":
    data_creation.create_data()
    data_preprocessing.preprocess_data()
    prepare_model.prepare_model()
    test_model.test_model()
