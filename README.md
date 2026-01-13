# Hand Laterality Judgement Task (HLJT)
**Available in English, Spanish, French & German** (see below to implement the task in other languages)

The HLJT is a behavioural paradigm aiming to assess the ability to manipulate movement imagery. If you are interested in assessing Movement Imagery ability, visit this [Task Platform Project](https://movementimageryability.github.io/) for an overview of open-source behavioural tasks.

Originally described in [Cooper and Shepard 1975](https://psycnet.apa.org/doiLanding?doi=10.1037%2F0096-1523.1.1.48) and later investigated in [Parsons 1987](https://www.sciencedirect.com/science/article/abs/pii/0010028587900119), it has been extensively used in cognitive and clinical neuroscience. This repository contains the materials for an **open-source (and user-friendly)** version of the HLJT for local and online use. These versions have been tested as in **Moreno-Verdú et. al 2025** ([Publication](https://www.ibroneuroscience.org/article/S0306-4522(25)00180-0/fulltext) | [Preprint](https://www.biorxiv.org/content/10.1101/2024.10.17.618819v1.full) | [OSF](https://osf.io/8h7ec/)). The most updated versions can be found in this repository.

Subsequent updates in native software ([PsychoPy](https://www.psychopy.org/)) may need adjustments. As developers, we are not responsible for implementing these in every use case.

An example of the setup is shown below.
![HLJT Animation](HLJT_example.gif)

## Repository information
The repository has two main folders, which contain **PsychoPy experiments (.psyexp)** and associated files to be able to run them **locally or online**. Please consult the Readme files for each version before using them (local and online versions are **NOT** equivalent in terms of configuration). The Readme files contain extensive documentation on the most relevant task settings and detailed information to allow the user further customization.

The versions provided in this repository allow flexibility in terms of key experiment parameters of the HLJT (e.g. angles of rotation, hand views, types of response, trial-to-trial feedback, number of trials, etc). The optimal protocol is at the user's discretion, but sensible defaults have been implemented.

## Language expansion
If you want to contribute to this repository by providing a language translation, or want to run the task in your own language, expansions can be done relatively easily thanks to the implementation of **language localisations** (please read each Readme to understand how to implement these). You can also see [this demo](https://github.com/mmorenoverdu/language_localisation_local) showing how to implement a language localisation in PsychoPy with virtually no code (for local use only).


