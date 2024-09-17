import pkg_resources
# List of packages to check
packages_to_check = ['spacy', 'scispacy', 'transformers', 'torch']

# Get a dictionary of installed packages and their versions
installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

# Check each package in the list
for package_name in packages_to_check:
    if package_name in installed_packages:
        print(f"'{package_name}' is installed, version: {installed_packages[package_name]}")
    else:
        print(f"'{package_name}' is not installed.")
import spacy

# List of models to check
models_to_check = ['en_core_sci_sm', 'en_ner_bc5cdr_md']

for model in models_to_check:
    try:
        nlp = spacy.load(model)
        print(f"Model '{model}' is installed and can be loaded.")
    except OSError:
        print(f"Model '{model}' is not installed.")
'''
CHECKING CODE OUTPUT:
  import pkg_resources
'spacy' is installed, version: 3.7.6
'scispacy' is installed, version: 0.5.4
'transformers' is installed, version: 4.45.0.dev0
'torch' is installed, version: 2.4.1
C:\Users\Ky\anaconda3\envs\hit137env\lib\site-packages\spacy\language.py:2195: FutureWarning: Possible set union at position 6328
  deserializers["tokenizer"] = lambda p: self.tokenizer.from_disk(  # type: ignore[union-attr]
Model 'en_core_sci_sm' is installed and can be loaded.
Model 'en_ner_bc5cdr_md' is installed and can be loaded.
PS C:\Users\Ky\OneDrive\Desktop\hit137_assignment2_group12> 
'''
