from dotenv import load_dotenv
from utils import *
from llm_dataset_mgr import LLMDatasetMgr

if __name__ == "__main__":
    load_dotenv()

    # To create an empty dataset, use the create_dataset.py script

    definitions = {
        "symbol": "A Symbol (represented as SY) is a Noun or set of nouns acting as a substantial representation of the concept meant. The symbol stands for and represents the concept.",
        "concept": "A Concept (represented as CO) is a Noun or set of nouns introducing new intrinsic or mutual properties.",
        "incompleteness": "Incomplete (represented as INC) means that after having described a concept, no symbol is introduced or determined to refer to this concept.",
        "meaningless": "Meaningless (represented as MLN) means that after having used a symbol, no definition of the symbol is given and the subsequent utterances make clear that the corresponding concept is missing or unclear.",
        "redundancy": "Redundancy (represented as RDC) means that after having used a symbol for the reference of a concept, a different symbol is used for the reference of the same concept.",
        "ambiguity": "Ambiguity (represented as AMB) means that after having used a symbol for the reference of a concept, a different concept can be detected, which is represented by the same symbol.",
    }

    # The LLMDatasetMgr Class automatically creates a dataset_description, which describes the column names for the given dataset so that the LLM can generate data in a format that matches the dataset
    # However, you should also provide an additional context whenever calling add_data, which further describes the data that should be added to the dataset
    dataset_context = f"For Context, the dataset represents requirements engineering excerpts and their corresponding Language Construct (LC) and Language Quality (LQ) codings, as described by a research paper titled 'Language quality in requirements development: tracing communication in the process of information systems development'. Language Construct (LC) represents the linguistic construction of a symbol-concept relationship that can be observed during the language development process. LC Codings may contain concepts (CO) and symbols (SY). {definitions['concept']} {definitions['symbol']} Each symbol and concept should also be numbered because a symbol may correspond to a concept (for example, SY1, SY2, CO1, and so on). Note that the numbering of symbols and concepts should be independent for each data entry. The dataset contains 4 types of language quality issues: incompleteness, meaningless, redundancy, and ambiguity. For the generated data, ensure the Language Quality is 'ambiguity'. {definitions['ambiguity']} For the comment, provide what the symbols and concepts correspond to in the excerpt (in the format 'SY1: Word') and a brief description of the language quality issue."
    
    data_filepath = "./data/LC_Dataset.csv"
    dataset = LLMDatasetMgr(dataset_path=data_filepath)
    dataset.print_attributes()
    print(f"\nDataset Context: {dataset_context}")

    dataset.add_data(context=dataset_context, num_samples=10)
