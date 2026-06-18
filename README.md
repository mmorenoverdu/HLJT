# Hand Laterality Judgement Task (HLJT)
Available in **English, Spanish, French & German** (see below to implement the task in other languages)

The HLJT is a behavioural paradigm aiming to assess the ability to manipulate movement imagery. If you are interested in assessing Movement Imagery ability, visit the [Movement Imagery Ability Task Platform](https://movementimageryability.github.io/) for an overview of open-source behavioural tasks.

Originally described in [Cooper and Shepard 1975](https://psycnet.apa.org/doiLanding?doi=10.1037%2F0096-1523.1.1.48) and later investigated in [Parsons 1987](https://www.sciencedirect.com/science/article/abs/pii/0010028587900119), it has been extensively used in cognitive and clinical neuroscience. This repository contains the materials for an **open-source (and user-friendly)** version of the HLJT for local and online use. These versions have been tested as in **Moreno-Verdú et. al 2025** ([Publication](https://www.ibroneuroscience.org/article/S0306-4522(25)00180-0/fulltext) | [Preprint](https://www.biorxiv.org/content/10.1101/2024.10.17.618819v1.full) | [OSF](https://osf.io/8h7ec/)). The most updated versions can be found in this repository.

Subsequent updates in native software ([PsychoPy](https://www.psychopy.org/)) may need adjustments. As developers, we are not responsible for implementing these in every use case.

An example of the setup is shown below.
![HLJT Animation](HLJT_example.gif)

## Repository information
This repository has two main folders, which contain **PsychoPy** experiments (`.psyexp`), together with associated files to run them **locally** (lab/desktop experiments) or **online** (in a browser). 
Please consult the accompanying manuscript [Moreno-Verdú et al., 2025](https://www.ibroneuroscience.org/article/S0306-4522(25)00180-0/fulltext) on the [Movement Imagery Ability Task Platform](https://movementimageryability.github.io/) for a guide on necessary steps to run a task in each of the deployment modes, which can help with the decision.
- [HLJT PsychoPy local](/HLJT_local)
- [HLJT PsychoPy online](/HLJT_online)

The versions provided in this repository allow flexibility in terms of key experiment parameters of the HLJT:
- angles of rotation
- hand views
- types of response
- trial-to-trial feedback
- number of repetitions

The optimal protocol is at the user's discretion, but sensible defaults have been implemented.

## Language expansion
If you want to contribute to this repository by providing a language translation, or want to run the task in your own language, expansions can be done relatively easily thanks to the implementation of language localisations (please read each README to understand how to implement these). You can also see these demos showing how to implement a language localisation in [PsychoPy](https://github.com/mmorenoverdu/language_localisation_demo) and [OpenSesame](https://github.com/carlacz/OpenSesame_Language-Localisation-Demo) with virtually no code.



