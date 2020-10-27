# ohsumed_snomed
Ohsumed dataset annotated with SNOMED


The ohsumed dictionary contains the following keys:

1. *texts*: The corresponding value is a dictionary that maps text ids to texts.
2. *training_labels*: The corresponding value is a dictionary that maps training text ids to one or more labels.
3. *testing_labels*: The corresponding value is a dictionary that maps testing text ids to one or more labels.
4. *annotations*: The corresponding value is a dictionary that maps text ids to snomed annotations in text (plus some semantic types, and more).
5. *label_codes*: The corresponding value is a list of label codes (C01, C02, ..., C23).
6. *label_names*: The corresponding value is a list of label names, ordered the same way as the codes.

Update: added snomed neighborhood file, where for each sctid in the ohsumed dataset, the values are a dictionary that maps distances to edges on the graph. Example is {1: {('58998006', '106672000')}, 2: {('106672000', '106668004'), ('106672000', '243667001')}, 3: {('106668004', '106649002'), ('243667001', '311526004'), ('106668004', '243667001'), ('243667001', '363743006')}, 4: {('106649002', '421727006'), ('363743006', '370115009'), ('106649002', '31426007'), ('311526004', '31426007'), ('311526004', '363743006')}, 5: {('370115009', '138875005'), ('421727006', '441649000'), ('31426007', '37017009'), ('421727006', '387961004')}, 6: {('37017009', '272608008'), ('37017009', '363743006'), ('387961004', '4748007'), ('387961004', '410607006'), ('441649000', '387961004'), ('37017009', '37763007')}}
