# vdslm
A Very Dumb Small Language Model

# How To
Run ```python3 ./vdslm.py -f``` for first run.
Sample data is provided (thanks to Project Gutenberg), but can be changed (in ```data.txt```).

To train the model based on file ```filename``` (default is ```data.txt```) run ```python3 ./vdslm.py -t [filename]```.

To generate run ```python3 ./vdslm.py -g [len]``` and provide an input word to generate a response of length ```len``` (default is 50). 

```vdslm_model.bin``` is a pre-trained model based on ```data.txt```

# How it works
When training the model the data is read and sparated based on spaces. 

Then the successors of each word as well as their probabilities of appearing after the word are counted.

This is used when generating the response. If the input word is not found in the training data of the model, the closest word using Levenshtein distance is found and used.

The response is generated word-by-word using the last generated word as input.
