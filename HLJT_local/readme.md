# HAND LATERALITY JUDGEMENT TASK (HLJT)

**Author:** Marcos Moreno Verdu, 18/06/2026  
**Software used:** PsychoPy 2025.1.1 (or superior)  
**Experiment Type:** Local  
**Languages supported:** English (EN) = default, Spanish (ES), French (FR) and German (DE). Further languages can be added with no code changes (see [Language Localisation](#language-localisation)).

---------------------------------------

## GENERAL INSTRUCTIONS

This experiment is built using [PsychoPy](https://www.psychopy.org/) (Builder) and is intended for **local execution**. Please make sure you are running PsychoPy version 2025.1.1 or superior, as other versions might behave unexpectedly.

This README is not intended to explain how PsychoPy generally works, but rather the specific aspects of this **HLJT** implementation. If you have never used PsychoPy before, please refer to the [documentation](https://www.psychopy.org/documentation.html) on their website, or available tutorials — especially regarding conditions files, variables, routines, and loops. This will save you time if you decide to modify any parameters of this experiment.

This README specifically details the structure and customization of this **HLJT** implementation.

---------------------------------------

## SETUP INSTRUCTIONS

To edit or run this task, you need to have **PsychoPy** installed. There are no other dependencies for this task.

PsychoPy exports results directly as `.csv` plus `.log` / `.psydat` (depending on run mode). A script for data preparation in [R](https://www.r-project.org/) (4.5.2) is provided. The data output **must** be processed to obtain meaningful information.

**Step-by-step instructions:**
1. **Download** all files from the repository.
2. **Unzip** the files into a **new** folder, making sure it contains no other PsychoPy experiments.
3. **Open** the file `.psyexp` in PsychoPy (Builder).
4. Click the **Run** button to start the experiment.
5. Participants **complete** the experiment locally, guided automatically without supervision.
6. Data is automatically **saved** into the `data/` folder.
7. **Process the data** using the `Example data processing.R` script provided.

---------------------------------------

## LANGUAGE LOCALISATION

This experiment uses external spreadsheet files to manage on-screen text and translations. This makes adding new languages relatively easy, but strict formatting rules apply.

The language can be selected via the PsychoPy startup dialog (Experiment Info; see #Experiment settings). The experiment then uses the corresponding *ISO_code* (e.g., `EN`, `DE`) to retrieve the corresponding text from columns in the external message sheet.
- `language_localiser.xlsx` maps a **language** to an **ISO_code**.
- The message sheet (e.g., `messages.xlsx`) contains one column per ISO_code (e.g., `EN`, `DE`) and is iterated to populate the global text variables used across routines.

All text components that should update dynamically by language must have their "Text" field set to **"Set to every repeat."** This allows the displayed text to update dynamically from the corresponding language variable.

### Adding a new language

#### 1. Open the relevant files
- `language_localiser.xlsx`
- `messages.xlsx`

#### 2. Extend `language_localiser.xlsx` by adding a new row

The file must contain the columns:
- `language`
- `ISO_code`

Example:

| language | code |
| :--- | :--- |
| English | EN |
| Spanish | ES |
| French | FR |
| German | DE |

Add your new language (e.g., Chinese) in a new row:

| language | code |
| :--- | :--- |
| English | EN |
| Spanish | ES |
| French | FR |
| German | DE |
| Chinese | CH |

#### 3. Extend `messages.xlsx` by adding a new column

The file must contain:
- a `message` column (variable names used inside PsychoPy), and
- one column per language (named by *ISO_code*).

Example:

| message | EN | ES | 
| :--- | :--- | :--- |
| welcome_msg | Welcome! | Bienvenido! | 
| adv_msg | Press SPACE to continue | Presiona ESPACIO para continuar | 

Add a new column titled with your new code (e.g., `IT`) and provide a translation for every message key:

| message | EN | ES | IT |
| :--- | :--- | :--- | :--- |
| welcome_msg | Welcome! | Bienvenido! | Benvenuti al compito! |
| adv_msg | Press SPACE to continue | Presiona ESPACIO para continuar | Premi SPAZIO per continuare |

⚠️ Do this consistently for **all** message keys used by the experiment!

#### 4. Update the experiment
1. Open `.psyexp` in PsychoPy.
2. Go to **Experiment Settings** (cogwheel icon) → Basic → Experiment Info.
3. Update the `language` entry by adding your new language name (e.g., `Italian`). It must exactly match the entry in `language_localiser.xlsx`.
4. Save the experiment.

> ⚠️ **Important:** Do not change folder or file names. Do not rename variables. Do not move files after decompressing the repository. The experiment depends on exact paths and identifiers. Moving or renaming files may cause crashes.

---------------------------------------

## TECHNICAL DETAILS

The decompressed repository includes:
- `.psyexp` — main PsychoPy experiment file
- `language_localiser.xlsx` — language configuration file
- `messages.xlsx` - including messages across routines
- a data-processing script in R

**Folder `hljt_images`:**
- The four stimuli used in the task — left/right hand images in `.png` format, divided into dorsal or palmar view. The experimenter can specify whether both or only one view is used.

**Folder `hljt_instr_images`:**
- Images displayed in the instructions: `pic1` (overall idea of the task), `pic2` (how to respond, depending on response mode), `pic3` (information about feedback, suppressed depending on user preference).

**Folder `hljt_files`:** Contains key files used to run the experiment.
- Instructions files (`.xlsx`): one per available response mode, encoding the instructions and images for that mode.
- `Stimuli_*angles.xlsx`: excel files including the trials of the practice and test block for different experiment settings

**Folder `data`:**
- Storage location for output data.

---------------------------------------

## EXPERIMENT SETTINGS (parameters to choose)

The experimenter selects settings in the PsychoPy startup dialog **at the beggining of each run**.

### Available Parameters

| Variable | Options | Description |
| :--- | :--- | :--- |
| `response_mode` | • **Both hands** (Default)<br>• Right hand<br>• Left hand | Determines the required input method |
| `practice_block` | • **Yes** (Default)<br>• No | Whether a practice block (all stimuli, 1 repetition, with feedback) precedes the test blocks. |
| `n_angles` | • **8**, increments of 45° (Default)<br>• 4, increments of 90°<br>• 6, increments of 60°<br>• 12, increments of 30° | Selects the corresponding `Stimuli_*angles.xlsx` file. |
| `hands_views` | • **Dorsal and Palmar** (Default)<br>• Palmar<br>• Dorsal | Which hand view(s) are shown; auto-generates `Stimuli_last_run.csv` (overwritten each run, contains no participant data). |
| `n_reps` | • **12** (Default)<br>• 8<br>• 4 | Repetitions per unique stimulus across the 4 test blocks. Only these values are supported — changing this requires corresponding code adjustments, or the experiment will crash. |
| `feedback` | • 0.3 (Default)<br>• 0.5<br>• 0.8<br>• 1<br>• **No feedback in testblock(s)** | Duration of feedback (in seconds) per trial in the test blocks. |

### Disable demographic questions

The experiment includes Age, Gender, and Hand dominance questions by default, collected via a `demographics` routine. These support normative data collection.

If you do not want to collect demographics, you can remove this routine from the experiment flow, or alternatively:

1. Click the `demographics` routine.
2. Open **Routine settings**.
3. In the **Testing** tab → click **Disable Routine**.

#### Saving
1. Save the experiment.
2. Run locally via PsychoPy.

---------------------------------------

## PARTICIPANT WORKFLOW

Once the experiment starts (after the experimenter has selected the settings above), it guides the participant through it without the need for further supervision.

1. **Welcome screen:** A brief description of the goal of the task.
2. **Demographics:** Participants indicate Age, Gender, and Hand dominance (if not disabled).
3. **Instructions:** A couple of screens explaining the task and the response-key assignment for the selected response mode.
4. **Practice Block** (as decided by the experimenter):
   - Welcome screen.
   - Countdown of 3 seconds.
   - Practice trials with all stimuli (1 repetition per unique stimulus), always with feedback.
5. **Test Blocks** (4 in total; duration depends on the chosen stimulus set):
   - Welcome screen.
   - Countdown.
   - Block of trials.
   - Break screen.
6. **Completion:** Goodbye screen.

#### HLJT trial procedure

The sequence of a single trial is as follows:

1. Fixation cross: Presented for 800ms.
2. Stimulus presentation: Stays on screen until a keypress is recorded.
3. Feedback (conditional): If enabled, feedback is shown for the selected duration.
   
   → *Automatic advance to the next trial.*

---------------------------------------

## OUTPUT

All data is sved locally inside the `data/`folder.

Each run generates:

- `.csv`data file
- `.log`
- `.psydat`

The provided R script is designed to reall .csv files in the `data/` folder, extract relevant observations from the HLJT test blocks and save the processed data.

To run the script, open it and **source** it.

> **Note:** This script relies on the standard PsychoPy output structure. It expects a participant ID column (`participant` or `subject_nr`) and standard  response columns such as `response.keys`, `response.corr`, and `response.rt`. If modifications were made beyond the configurable experiment settings, the code may need adaptation. Raw data should always be inspected and cleaned of outliers or errors prior to statistical analysis.

### Variable Documentation

#### 1. Testblock Trials Data

*One row per trial*

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `participant` | character/numeric | Participant ID, as entered in the startup dialog. |
| `session` | character/numeric | Session ID, as entered in the startup dialog (if used). |
| `key_resp.rt` | numeric | Response time, in **seconds**, for each test-block trial. |
| `key_resp.corr` | integer | Accuracy (1 = correct, 0 = incorrect). |
| `hljt_side` | factor | Side of the stimulus hand ("left"/"right"). |
| `hljt_view` | factor | View of the stimulus ("dorsal"/"palmar"). |
| `hljt_angle` | numeric | Rotation angle of the stimulus (degrees). |
| `hljt_direction` | factor | Rotation direction category (up/medial/lateral/down); used to quantify the biomechanical-constraints effect. |

#### 2. Demographic Data

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `age` | integer | Participant age in years. |
| `gender` | character | Gender (options: Female, Male, Non-binary, Trans-gender, Other, Prefer not to say). |
| `handedness` | character | Hand dominance (options: Left, Ambidextrous, Right). |

---------------------------------------

PsychoPy version updates may require adjustments. Developers are not responsible for adapting the task to every use case.
Before collecting data, always test the experiment and check the data output.
Contributions are welcome.

---------------------------------------

## REFERENCE

Please cite [Moreno-Verdú et al. 2025](https://linkinghub.elsevier.com/retrieve/pii/S0306452225001800) when using this resource.
