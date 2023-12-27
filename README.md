# vdslm
A Very Dumb Small Language Model

# How To
Run ```python3 ./vdslm.py -f``` for first run.
Sample data is provided (thanks to Project Gutenberg), but can be changed (in ```data.txt```).

To train the model based on file ```filename``` (default is ```data.txt```) run ```python3 ./vdslm.py -t [filename]```
To generate run ```python3 ./vdslm.py -g [len]``` and provide an input word to generate a response of length ```len``` (default is 50). 

```vdslm_model.bin``` is a pre-trained model based on ```data.txt```
