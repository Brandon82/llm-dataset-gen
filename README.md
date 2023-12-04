# llm-dataset-gen
Provides a `LLMDatasetMgr` class for generating and adding data to datasets using LLMs (OpenAI API)
- Supported file types for dataset files: `.csv`

## Installation
Install the following packages:
`pip install openai==1.3.5 pandas==2.1.3 python-dotenv==1.0.0`

## Usage
1. Create a .env file in the root directory of the project and add your OpenAI API key to it:
```
OPENAI_API_KEY=<your-openai-api-key>
```
2. Create an empty dataset file using the `create_and_save_empty_dataset` function in utils.py
```python
from utils import create_and_save_empty_dataset
dataset_columns = ["ID", "Excerpt", "Comment"]
create_and_save_empty_dataset(columns=dataset_columns, filename="./data/Dataset.csv")
```
- This function supports the following file types: `.csv`
- You can skip this step if you already have a dataset file
2. Create an instance of the `LLMDatasetMgr` class and pass in a `dataset_path`:
```python
data_filepath = "./data/Dataset.csv"
dataset = LLMDatasetMgr(dataset_path=data_filepath)
```
3. Call the `add_data` method by providing the `context` and `num_samples` parameters:
```python
dataset_context="For Context, this dataset represents requirements engineering excerpts and their corresponding Language Construct (LC) and Language Quality (LQ) codings"
dataset.add_data(context=dataset_context, num_samples=20)
```
- The `add_data` method will automatically overwrite/save the dataset file after appending the new data
- The `context` parameter is the prompt that will be used to generate the data
- The `num_samples` parameter is the number of data samples to generate and add to the dataset