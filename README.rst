Random names generator, which uses seed of input words to pseudo-randomly combine new ones from syllables of given words.

This is usable for names of new projects, which you may just describe in plain words (each word on new line) and it will generate combined pseudo-similar names.

`example.txt` ::

    random
    names
    generator

`$ ./random_names_generator.py example.txt -n 3` ::

    arandmer
    memeomand
    domea

Help
----

::
    usage: random_names_generator.py [-h] [-n NUMBER] SEED_FILE

    Mix random names from word seeds.

    positional arguments:
      SEED_FILE             File with list of seed words. Use - for stdin.

    optional arguments:
      -h, --help            show this help message and exit
      -n NUMBER, --number NUMBER
                            Number of generated words. Default 20.
