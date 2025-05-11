"""
Tests for the data processor module.
"""
import pytest
import pandas as pd
import numpy as np
from src.data.processor import DataProcessor

@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({
        'numeric_col': [1, 2, np.nan, 4, 5],
        'categorical_col': ['A', 'B', 'A', 'C', 'B'],
        'text_col': ['text1', 'text2', 'text3', 'text4', 'text5']
    })

@pytest.fixture
def processor():
    """Create a DataProcessor instance for testing."""
    return DataProcessor()

def test_load_data_csv(tmp_path, processor):
    """Test loading data from a CSV file."""
    # Create a temporary CSV file
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    file_path = tmp_path / "test.csv"
    df.to_csv(file_path, index=False)
    
    # Test loading
    loaded_data = processor.load_data(str(file_path))
    assert isinstance(loaded_data, pd.DataFrame)
    assert loaded_data.shape == (3, 2)

def test_preprocess_basic(processor, sample_data):
    """Test basic preprocessing functionality."""
    processed_data = processor.preprocess(sample_data)
    assert isinstance(processed_data, pd.DataFrame)
    assert processed_data.shape == sample_data.shape

def test_save_processed_data(tmp_path, processor, sample_data):
    """Test saving processed data."""
    # Test saving as CSV
    csv_path = tmp_path / "processed.csv"
    processor.save_processed_data(sample_data, str(csv_path))
    assert csv_path.exists()
    
    # Test saving as parquet
    parquet_path = tmp_path / "processed.parquet"
    processor.save_processed_data(sample_data, str(parquet_path))
    assert parquet_path.exists()

def test_error_handling(processor):
    """Test error handling for invalid file paths."""
    with pytest.raises(Exception):
        processor.load_data("nonexistent_file.csv")
    
    with pytest.raises(ValueError):
        processor.load_data("file.unsupported") 