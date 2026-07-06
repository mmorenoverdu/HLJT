# HAND LATERALITY JUDGEMENT TASK (HLJT) — OpenSesame version

**Author:** Marcos Moreno Verdu, 06/07/2026

**Software used:** OpenSesame 4.1.9 (or superior)

**Experiment Type:** Local

**Languages supported:** English (EN) = default, Spanish (ES), French (FR) and German (DE). Further languages can be added with almost no code changes (see [Language Localisation](#language-localisation)).

---------------------------------------

## GENERAL INSTRUCTIONS

This experiment is built using [OpenSesame](https://osdoc.cogsci.nl/) and is intended for **local execution**. Please make sure you are running OpenSesame version 4.1.9 or superior, as other versions might behave unexpectedly.

Unlike the PsychoPy version, this experiment does not use OpenSesame's native GUI stimulus items (`sketchpad`, `keyboard_response`, `form`, etc.) at all — every screen is written as plain Python inside `inline_script` items, using OpenSesame's Python API (`Canvas`, `Keyboard`, `Mouse`, `clock`, `var`). Blocks and trials are still built from native `loop`/`sequence` items, so the overall flow is visible and editable in OpenSesame's interface, exactly like a normal experiment.

This README is not intended to explain how OpenSesame generally works, but rather the specific aspects of this **HLJT** implementation. If you have never used OpenSesame before, please refer to the [documentation](https://osdoc.cogsci.nl/) on their website — especially regarding loops, sequences, and the Python API used inside `inline_script` items. This will save you time if you decide to modify any parameters of this experiment.

This README specifically details the structure and customization of this OpenSesame **HLJT** implementation.

---------------------------------------

## SETUP INSTRUCTIONS

To edit or run this task, you need **OpenSesame** (4.1.9+) installed, with the `openpyxl` and `datamatrix` Python packages available in its Python environment. Both are core OpenSesame dependencies, so they should already be present in any normal install.

OpenSesame exports results as a single `.csv` file per participant (see [Output](#output)) — there are no separate `.log`/`.psydat` files, and no external data-processing script is needed: the file is already a flat, one-row-per-trial table.

**Step-by-step instructions:**
1. **Download** all files from the repository.
2. **Unzip** the files into a **new** folder, making sure it contains no other OpenSesame experiments. Do not rename or move any file or folder — see the warning at the end of [Language Localisation](#language-localisation).
3. **Open** the file `HLJT_local.osexp` in OpenSesame.
4. Open the **`settings`** item and edit the experimenter-facing options directly in the Python code (see [Experiment Settings](#experiment-settings-parameters-to-choose)).
5. Click the **Run** button to start the experiment.
6. The first screen lets the participant/experimenter **choose the language** by clicking a button; everything after that runs automatically without further supervision.
7. Data is automatically **saved** into the `data/` folder.

---------------------------------------

## LANGUAGE LOCALISATION

This experiment uses external spreadsheet files to manage on-screen text and translations, exactly like the PsychoPy version. This makes adding new languages relatively easy, but strict formatting rules apply.

Unlike the PsychoPy version (which selects the language from the startup dialog), the language here is chosen by **clicking a button** on the `language_select` screen, shown right after `settings`. The experiment then uses the corresponding *ISO_code* (e.g., `EN`, `DE`) to retrieve the corresponding text from columns in the external message sheet, exactly as before.

- `Language_localiser.xlsx` maps a **language** name to an **ISO_code**.
- `Messages.xlsx` contains one column per ISO_code (e.g., `EN`, `DE`) and is read once, in the `setup` item's Run phase (right after `language_select`), to build the `msg` dictionary used by every other item (e.g. `msg['welcome_msg']`).

Because every screen is an `inline_script` item that reads `msg[...]` directly when it runs, text always reflects the chosen language automatically — there is no PsychoPy-style "Set to every repeat" setting to configure.

### Adding a new language

#### 1. Open the relevant files
- `Language_localiser.xlsx`
- `Messages.xlsx`

#### 2. Extend `Language_localiser.xlsx` by adding a new row

The file must contain the columns:
- `language`
- `ISO_code`

Example:

| language | ISO_code |
| :--- | :--- |
| English | EN |
| Spanish | ES |
| French | FR |
| German | DE |

Add your new language (e.g., Dutch) in a new row:

| language | ISO_code |
| :--- | :--- |
| English | EN |
| Spanish | ES |
| French | FR |
| German | DE |
| Dutch | NL |

#### 3. Extend `Messages.xlsx` by adding a new column

The file must contain:
- a `message` column (variable names used inside the `msg` dictionary), and
- one column per language (named by *ISO_code*).

Add a new column titled with your new code (e.g., `NL`) and provide a translation for every message key.

⚠️ Do this consistently for **all** message keys used by the experiment!

#### 4. Add a button to `language_select`

1. Open the **`language_select`** item in OpenSesame.
2. Add a new tuple to the `btn_defs` list, e.g. `("Dutch", "Nederlands")`. The first value must exactly match the entry you added to `Language_localiser.xlsx`; the second is just the button's on-screen label.
3. Save the experiment.

> ⚠️ **Important:** Do not change folder or file names. Do not rename variables. Do not move files after decompressing the repository. The experiment depends on exact paths and identifiers. Moving or renaming files may cause crashes.

---------------------------------------

## TECHNICAL DETAILS

The decompressed repository includes:
- `HLJT_local.osexp` — main OpenSesame experiment file (built entirely from `inline_script`, `loop` and `sequence` items — no sketchpad/form/keyboard_response GUI items)
- `Language_localiser.xlsx` — language configuration file
- `Messages.xlsx` — messages used across items
- `HLJT_icon.jpg` — task icon shown on the welcome screen

**Folder `hljt_images`:**
- The four stimuli used in the task — left/right hand images in `.png` format, divided into dorsal or palmar view. The experimenter can specify whether both or only one view is used.

**Folder `hljt_instr_images`:**
- Images displayed in the instructions: `pic1` (overall idea of the task), `pic2` (how to respond, depending on response mode), `pic3` (information about feedback, suppressed depending on user preference).

**Folder `hljt_files`:** Contains key files used to run the experiment.
- Instructions files (`.xlsx`): one per available response mode, encoding the instructions and images for that mode.
- `Stimuli_*angles.xlsx`: excel files including the trials of the practice and test blocks for different experiment settings.

**Folder `data`:**
- Storage location for output data (one `.csv` per participant).

**How the experiment is built (OpenSesame specifics):**
- `settings` — experimenter-editable options (Python variables, edited directly in the item).
- `language_select` — on-screen language picker (see [Language Localisation](#language-localisation)).
- `setup` — loads the xlsx files, derives every setting, opens the data file, and defines helper functions shared by later items.
- `welcome`, `demographics`, `instructions_loop`/`instructions`, `blocks_loop`/`block_sequence` (`block_start`, `countdown`, `trials_loop`/`trial_sequence` with `ITI`/`trial`/`feedback`, `block_end`), `bye` — one item per screen/step, wired together with native `loop`/`sequence` items so the flow is visible in OpenSesame's interface.

One important rule if you edit or add items: OpenSesame runs the **Prepare** phase of every item inside a `sequence`, in order, before running the **Run** phase of any of them. So a later item's Prepare phase can only rely on values set in an *earlier* item's Prepare phase — never its Run phase (Run-to-Run dependencies between siblings, on the other hand, are always safe, since those execute strictly in order too). This is why, for example, `language` is only available from `setup`'s Run phase onward — it is set by `language_select`'s Run phase, which happens after every item's Prepare has already executed.

OpenSesame also creates its own default log file (e.g. `subject-1.csv`) in the experiment folder on every run; this is normal OpenSesame behaviour and can be ignored/deleted — the actual data is written to `data/<participant>_HLJT_local_OpenSesame_<timestamp>.csv`.

---------------------------------------

## EXPERIMENT SETTINGS (parameters to choose)

The experimenter edits settings directly in the **`settings`** item, before pressing Run. (OpenSesame has no equivalent to PsychoPy's startup dialog — language is the one exception, chosen on-screen; see [Language Localisation](#language-localisation).)

### Available Parameters

| Variable | Options | Description |
| :--- | :--- | :--- |
| `response_mode` | • **Both hands** (Default)<br>• Right hand<br>• Left hand | Determines the required input method |
| `practice_block` | • **Yes** (Default)<br>• No | Whether a practice block (all stimuli, 1 repetition, with feedback) precedes the test blocks. |
| `n_angles` | • **8**, increments of 45° (Default)<br>• 4, increments of 90°<br>• 6, increments of 60°<br>• 12, increments of 30° | Selects the corresponding `Stimuli_*angles.xlsx` file. |
| `hand_views` | • **Palmar and Dorsal** (Default)<br>• Palmar<br>• Dorsal | Which hand view(s) are shown; auto-generates `Stimuli_last_run.csv` (overwritten each run, contains no participant data). |
| `n_reps` | • **8** (Default)<br>• 4<br>• 12 | Total repetitions per unique stimulus across the test blocks (2 repetitions per block, so the number of test blocks is 2/4/6 for `n_reps` 4/8/12). Only these values are supported — changing this requires corresponding code adjustments, or the experiment will crash. |
| `feedback` | • **0.3** (Default)<br>• 0.5<br>• 0.8<br>• 1<br>• No feedback | Duration of feedback (in seconds) per trial in the test blocks. |
| `practice_n_trials` | • **"all"** (Default)<br>• any number | How many stimuli to show in the practice block; `"all"` shows every filtered stimulus once. |
| `test_n_trials` | • **"all"** (Default)<br>• any number | How many stimuli to show per test block; `"all"` shows every filtered stimulus `reps_per_block` (2) times. A small number is handy for quickly testing the whole pipeline. |

### Disable demographic questions

The experiment includes Age, Gender, and Hand dominance questions by default, collected via the `demographics` item. These support normative data collection.

If you do not want to collect demographics, remove the line `run demographics always` from the **`experiment`** sequence (OpenSesame has no per-item "Disable" toggle like PsychoPy's Routine settings).

#### Saving
1. Save the experiment.
2. Run locally via OpenSesame.

---------------------------------------

## PARTICIPANT WORKFLOW

Once the experiment starts, it guides the participant through it without the need for further supervision (after the experimenter has selected the settings above and the participant has picked a language).

1. **Language selection:** the participant/experimenter clicks a button (English / Español / Français / Deutsch).
2. **Welcome screen:** A brief description of the goal of the task.
3. **Demographics:** Participants indicate Age, Gender, and Hand dominance (if not disabled).
4. **Instructions:** A couple of screens explaining the task and the response-key assignment for the selected response mode.
5. **Practice Block** (as decided by the experimenter):
   - Block intro message.
   - Countdown of 3 seconds.
   - Practice trials with all (or `practice_n_trials`) stimuli, always with feedback.
6. **Test Blocks** (2/4/6, depending on `n_reps`):
   - Block intro message.
   - Countdown.
   - Block of trials.
   - Break screen (with a live timer).
7. **Completion:** Goodbye screen.

#### HLJT trial procedure

The sequence of a single trial is as follows:

1. Inter-trial interval (`ITI`): fixation cross + response boxes, shown for a duration drawn from the same probability distribution as the PsychoPy version (mostly ~0.75–0.85 s, occasionally 0.6–1 s).
2. Stimulus presentation (`trial`): stays on screen until a keypress is recorded (untimed).
3. Feedback (`feedback`, conditional): if enabled, colored response boxes are shown for the selected duration, and the trial's data row is logged.

   → *Automatic advance to the next trial.*

---------------------------------------

## OUTPUT

All data is saved locally inside the `data/` folder.

Each run generates a single `.csv` file: `data/<participant>_HLJT_local_OpenSesame_<timestamp>.csv`, with one demographics row followed by one row per trial. No separate `.log`/`.psydat` files are produced, and no external processing script is needed — the file is already a flat table ready for analysis.

> **Note:** OpenSesame also creates its own default log file (e.g. `subject-1.csv`) on every run; this is normal OpenSesame behaviour, contains no useful data for this task, and can be ignored/deleted.

### Variable Documentation

#### 1. Trial Data

*One row per trial*

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `participant` | character/numeric | Participant ID, as set in the `settings` item. |
| `session` | character/numeric | Session ID, as set in the `settings` item. |
| `block_number` | integer | Block index (the practice block, if enabled, is block 1). |
| `block_type` | factor | `"practice"` or `"test"`. |
| `trial_number` | integer | Trial index within the block. |
| `response_time` | numeric | Response time, in **seconds**, for each trial. |
| `correct` | integer | Accuracy (1 = correct, 0 = incorrect). |
| `response` | character | Key pressed by the participant. |
| `hljt_side` | factor | Side of the stimulus hand ("left"/"right"). |
| `hljt_view` | factor | View of the stimulus ("dorsal"/"palmar"). |
| `hljt_angle` | numeric | Rotation angle of the stimulus (degrees). |
| `hljt_direction` | factor | Rotation direction category (up/medial/lateral/down); used to quantify the biomechanical-constraints effect. |
| `iti` | numeric | Duration (seconds) of the inter-trial interval preceding this trial. |

#### 2. Demographic Data

*Logged once, on its own row*

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `age` | integer | Participant age in years. |
| `gender` | character | Gender (options: Female, Male, Non-binary, Trans-gender, Other, Prefer not saying). |
| `handedness` | character | Hand dominance (options: Left, Ambidextrous, Right). |

#### 3. Settings columns (repeated on every row)

| Variable Name | Description |
| :--- | :--- |
| `language`, `language_code` | Language chosen on-screen, and its ISO code. |
| `response_mode`, `practice_block`, `n_angles`, `hand_views`, `n_reps`, `feedback_setting` | Copies of the corresponding `settings` item values, for convenience during analysis. |

---------------------------------------

OpenSesame version updates may require adjustments. Developers are not responsible for adapting the task to every use case.
Before collecting data, always test the experiment and check the data output.
Contributions are welcome.

---------------------------------------

## REFERENCE

Please cite [Moreno-Verdú et al. 2025](https://linkinghub.elsevier.com/retrieve/pii/S0306452225001800) when using this resource.
