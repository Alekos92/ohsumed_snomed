# ohsumed_snomed
Ohsumed dataset annotated with SNOMED


The ohsumed dictionary contains the following keys:

1. *texts*: The corresponding value is a dictionary that maps text ids to texts.
2. *training_labels*: The corresponding value is a dictionary that maps training text ids to one or more labels.
3. *testing_labels*: The corresponding value is a dictionary that maps testing text ids to one or more labels.
4. *annotations*: The corresponding value is a dictionary that maps text ids to snomed annotations in text (plus some semantic types, and more).
5. *label_codes*: The corresponding value is a list of label codes (C01, C02, ..., C23).
6. *label_names*: The corresponding value is a list of label names, ordered the same way as the codes.

