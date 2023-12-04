# llm-dataset-gen
Provides a `LLMDatasetGen` class for generating and adding data to datasets using LLMs (OpenAI API)

## Installation
Install the following packages:
`pip install openai==1.3.5 pandas==2.1.3 python-dotenv==1.0.0`

## Usage
1. Create a .env file in the root directory of the project and add your OpenAI API key to it:
```
OPENAI_API_KEY=<your-openai-api-key>
```
2. Create an instance of the LLMDatasetGen class and call the load_dataset method with the path to your dataset file:
```python
data_filepath = "./data/LC_Dataset.csv"
dataset = LLMDatasetMgr(dataset_path=data_filepath)
```
3. Call the add_data method with context and number of samples to add to the dataset:
```python
dataset_context="For Context, this dataset represents requirements engineering excerpts and their corresponding Language Construct (LC) and Language Quality (LQ) codings"
dataset.add_data(context=dataset_context, num_samples=20)
```
