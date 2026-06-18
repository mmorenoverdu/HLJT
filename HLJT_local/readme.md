# HAND LATERALITY JUDGEMENT TASK (HLJT)

**Author:** Marcos Moreno Verdu, 13/01/2026  
**Software used:** PsychoPy 2025.1.1 (or superior)  
**Experiment Type:** Local  
**Languages supported:** English (EN) = default, Spanish (ES), French (FR) and German (DE). **[FLAG]** Further languages can be added with no code changes (see [Language Localisation](#language-localisation)).

---------------------------------------

## GENERAL INSTRUCTIONS

This experiment is built using [PsychoPy](https://www.psychopy.org/) (Builder) and is intended for **local execution**. Please make sure you are running PsychoPy version 2025.1.1 or superior, as other versions might behave unexpectedly.

This README is not intended to explain how PsychoPy generally works, but rather the specific aspects of this **HLJT** implementation. If you have never used PsychoPy before, please refer to the [documentation](https://www.psychopy.org/documentation.html) on their website, or available tutorials — especially regarding conditions files, variables, routines, and loops. This will save you time if you decide to modify any parameters of this experiment.

---------------------------------------

## SETUP INSTRUCTIONS

To run this task, you need to have **PsychoPy** (version 2025.1.1 or superior) installed. There are no other dependencies for this task.

The data output **must** be processed to obtain meaningful information. **[FLAG]** *The original readme refers only to "an example of data processing (in R)" without naming the script or its R version (MBRT names its script `data-prep.R`, R 4.5.2) — please provide these details.*

**Step-by-step instructions:**
1. **Download** all files from the repository.
2. **Unzip** the files into a **new** folder, making sure it contains no other PsychoPy experiments.
3. **Open** the file `HLJT_local.psyexp` in PsychoPy (Builder).
4. Click the **Run** button to start the experiment.
5. Participants **complete** the experiment locally, guided automatically without supervision.
6. Data is automatically **saved** into the `data/` folder.
7. **Process the data** using the R script provided in the experiment folder. **[FLAG]** *(see note above — script name/version not specified)*

---------------------------------------

## LANGUAGE LOCALISATION

This experiment uses external spreadsheet files to manage on-screen text and translations.

Two Excel sheets (`.xlsx`) are needed:
- The available language localisations: `language_localiser.xlsx`
- The list of messages used as variables to display text on screen: `messages.xlsx`

**[FLAG]** *The exact folder location of these two files isn't stated in the original readme (e.g., top level vs. inside `hljt_files/`, the way MBRT specifies `MBRT_files/Messages.xlsx`) — please confirm so [Technical Details](#technical-details) lists the correct path.*

The language is selected via a dropdown in the PsychoPy startup dialog (Experiment Settings → Basic tab → Experiment Info → `language` field; see [Experiment settings](#experiment-settings-parameters-to-choose)). The language name chosen must exactly match an entry in the `language` column of `language_localiser.xlsx`.

All text components that should update dynamically by language must have their "Text" field set to **"Set to every repeat."** This allows the displayed text to update dynamically from the corresponding language variable.

### Adding a new language

If you just want to add a new language without providing any further/new messages, you need to modify 4 things:

#### 1. Open the relevant files
- `language_localiser.xlsx`
- `messages.xlsx`

#### 2. Extend `language_localiser.xlsx` by adding a new row

The file must contain the columns:
- `language`
- `code` **[FLAG]** *(column name assumed — MBRT calls the equivalent column `ISO_code`; please confirm the actual header used in HLJT's file)*

Example (current state). **[FLAG]** *Codes for English/Spanish/French/German below are assumed standard ISO-style codes — not explicitly stated in the original readme:*

| language | code |
| :--- | :--- |
| English | EN |
| Spanish | ES |
| French | FR |
| German | DE |

Add your new language (e.g., Chinese) in a new row, written in English:

| language | code |
| :--- | :--- |
| English | EN |
| Spanish | ES |
| French | FR |
| German | DE |
| Chinese | CH |

#### 3. Extend `messages.xlsx` by adding a new column

The file must contain a `message` column (variable names used inside PsychoPy) **[FLAG]** *(column name assumed)* and one column per language, named by its code.

Example (current state — placeholder message keys). **[FLAG]** *No concrete message variable names were given in the original readme; replace the placeholders below with your actual keys:*

| message | EN | ES | FR | DE |
| :--- | :--- | :--- | :--- | :--- |
| [welcome_msg] | … | … | … | … |
| [instructions_msg] | … | … | … | … |

Add a new column titled with your new code (e.g., `CH`) and provide a translation for every message key:

| message | EN | ES | FR | DE | CH |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [welcome_msg] | … | … | … | … | … |
| [instructions_msg] | … | … | … | … | … |

⚠️ Do this consistently for **all** message keys used by the experiment!

#### 4. Update the experiment
1. Open `HLJT_local.psyexp` in PsychoPy.
2. Go to **Experiment Settings** (cogwheel icon) → Basic → Experiment Info.
3. Add your new language to the `language` field's list of options. It is critical that you write it using `''` (e.g., `'Chinese'`), exactly matching the entry you wrote in `language_localiser.xlsx`. If you want it to be the default choice, place it at the **beginning** of the list.
4. Add the corresponding new-language column to the relevant instructions files and block-message Excel sheets as well. **[FLAG]** *The original readme mentions updating "the different instructions files and block messages" beyond `messages.xlsx` — please confirm exactly which files these are (e.g., the per-response-mode instructions files in `hljt_files/`?).*
5. Save the experiment.

> ⚠️ **Important:** Once you have decompressed the `.zip` file, do not change the names of the files or folders, as the `.psyexp` file looks for specific names at specific locations. Avoid changing variable names wherever possible, since any code depending on those names would need to be adjusted accordingly.

---------------------------------------

## TECHNICAL DETAILS

The decompressed repository includes:
- `HLJT_local.psyexp` — main PsychoPy experiment file
- `language_localiser.xlsx` — language configuration file **[FLAG]** *(exact location unconfirmed — see note in Language Localisation)*
- a data-processing script in R **[FLAG]** *(filename/version not specified in the original readme)*

**Folder `hljt_images`:**
- The four stimuli used in the task — left/right hand images in `.png` format, divided into dorsal or palmar view. The experimenter can specify whether both or only one view is used.

**Folder `hljt_instr_images`:**
- Images displayed in the instructions: `pic1` (overall idea of the task), `pic2` (how to respond, depending on response mode), `pic3` (information about feedback, suppressed depending on user preference).

**Folder `hljt_files`:** Contains key files used to run the experiment.
- Instructions files (`.xlsx`): one per available response mode, encoding the instructions and images for that mode.
- `Stimuli_*angles.xlsx`: the main conditions files (must not be modified unless strictly necessary) — 4 files, one per rotation increment (90° = 4 angles, 60° = 6 angles, 45° = 8 angles, 30° = 12 angles), containing:
  - `hljt_images`: which image to use.
  - `hljt_side`: which side (left/right) the image corresponds to.
  - `hljt_view`: dorsal or palmar.
  - `hljt_angle`: rotation angle, always applied clockwise.
  - `hljt_direction`: up (0°), medial/lateral (depends on side), or down (180°) — used to quantify the "biomechanical constraints" effect (medial vs. lateral response times). For right-hand images: lateral = 1–179°, medial = 181–359°. For left-hand images: lateral = 181–359°, medial = 1–179°.
  - `hljt_correct_both`: correct key if `response_mode` = "Both hands" (S = left hand, L = right hand).
  - `hljt_correct_one`: correct key if `response_mode` = "Right hand" or "Left hand" (G = left hand, H = right hand).
- **[FLAG]** *Per the Language Localisation section, `language_localiser.xlsx` and `messages.xlsx` may also live in this folder — please confirm.*

**Folder `data`:** **[FLAG]** *(not listed as a folder in the original Technical Details section — added here for structural parity with MBRT, based on the Output section)*
- Storage location for output data.

---------------------------------------

## EXPERIMENT SETTINGS (parameters to choose)

The experimenter selects these settings in the PsychoPy startup dialog **before each run**. Default options can be modified by going to Experiment Settings and changing the order of the options for the corresponding field (see [Setting default values](#setting-default-values) below).

### Available Parameters

| Variable | Options | Description |
| :--- | :--- | :--- |
| `participant` | Free text/number (optional) | ID of the participant. |
| `session` | Free text/number (optional) | ID of the session. |
| `language` | • **English** (Default)<br>• Spanish<br>• French **[FLAG]** | Sets the language of the experiment; selected via dropdown before each run. |
| `response_mode` | • **Both hands** (Default)<br>• Right hand<br>• Left hand | "Both hands" uses S/L response keys; one-hand modes use G/H. |
| `practice_block` | • **Yes** (Default)<br>• No | Whether a practice block (all stimuli, 1 repetition, with feedback) precedes the test blocks. |
| `n_angles` | • **8**, increments of 45° (Default)<br>• 4, increments of 90°<br>• 6, increments of 60°<br>• 12, increments of 30° **[FLAG]** | Selects the corresponding `Stimuli_*angles.xlsx` file. |
| `hands_views` | • **Dorsal and Palmar** (Default)<br>• Palmar<br>• Dorsal | Which hand view(s) are shown; auto-generates `Stimuli_last_run.csv` (overwritten each run, contains no participant data). |
| `n_reps` | • **12** (Default)<br>• 8<br>• 4 | Repetitions per unique stimulus across the 4 test blocks. Only these values are supported — changing this requires corresponding code adjustments, or the experiment will crash. |

**[FLAG]** *(1)* `language` *— German is listed as a supported language elsewhere in this README but is missing from this options list in the original readme; please confirm whether it should be added here. (2)* `n_angles` *— the original readme lists the 12-angle option as "increments of 90 degrees," which conflicts with the Technical Details section (90° = 4 angles; 30° = 12 angles). Corrected to 30° above based on that cross-reference — please verify.*

### Setting default values

**[FLAG]** *Unlike MBRT, the original HLJT readme does not document a code-based method for setting defaults (i.e., specific code component/routine names, like MBRT's `n_reps_settings`). Only the dialog-based method below is described in the source — please provide code-based instructions if an equivalent exists.*

1. Open `HLJT_local.psyexp` in PsychoPy.
2. Go to **Experiment Settings** (cogwheel icon) → Basic → Experiment Info.
3. For the field you want to change, reorder its list of options so your desired default value is listed first.
4. Save the experiment.

### Disable demographic questions

The experiment includes Age, Gender, and Hand dominance questions by default, collected via a `demographics` routine.

If you do not want to collect demographics, you can disable or remove this routine from the experiment flow. **[FLAG]** *The original readme doesn't give the exact PsychoPy steps for this — the steps below assume the same generic mechanism MBRT uses; please confirm.*

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
2. **Demographics:** Participants indicate Age, Gender, and Hand dominance (if not disabled). **[FLAG]** *Merged here from a separate section in the original readme — please confirm this is the correct position in the sequence (e.g., relative to the instructions screens below).*
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
**[FLAG]** *The original readme doesn't describe the timing/sequence within a single trial (e.g., fixation duration, stimulus duration, response window, feedback duration, ITI) the way MBRT does for its trial procedure. Please provide these details if you'd like an equivalent breakdown added here.*

---------------------------------------

## OUTPUT

The output file generated by PsychoPy will be a `.csv` file saved in the `data/` subfolder, always named using the participant field and the date. **[FLAG]** *The original readme only mentions `.csv` output; MBRT also lists `.log` and `.psydat` as standard PsychoPy outputs. Please confirm whether HLJT also generates these.*

This `.csv` will contain every variable shown in the startup dialog box (`participant`, `session`, `language`, `response_mode`, `practice_block`, `n_angles`, `hands_views`, `n_reps`), plus the trial-level variables documented below.

An example script for data processing in R is provided in the experiment folder. **[FLAG]** *The script's filename, R version, and the structure of its output (e.g., long/wide dataframes, or an `.rdata` file as in MBRT's `data-prep.R`) are not specified in the original readme — please provide these details.*

> **Note:** This script likely relies on the standard PsychoPy output structure, expecting a participant ID column (`participant`) and the response columns `key_resp.rt` and `key_resp.corr`, plus the conditions-file columns `hljt_side`, `hljt_view`, `hljt_angle`, and `hljt_direction`. **[FLAG]** *(assumed by analogy with MBRT — please confirm against the actual script)*. As with MBRT, raw data should always be inspected and cleaned of outliers or errors prior to statistical analysis.

### Variable Documentation

#### 1. Testblock Trials Data
**[FLAG]** *Dataframe name not specified in the original readme (MBRT's equivalent is `data_long_tbl`).*

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
**[FLAG]** *Dataframe name not specified (MBRT's equivalent is `data_wide`).*

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `age` | integer | Participant age in years. |
| `gender` | **[FLAG]** | Gender (options: Female, Male, Non-binary, Trans-gender, Other, Prefer not to say). |
| `handedness` | **[FLAG]** | Hand dominance (options: Left, Ambidextrous, Right). |

**[FLAG]** *The original readme does not specify the output column names for `age`/`gender`/`handedness`, nor whether `gender`/`handedness` are saved as text labels or as coded integers (MBRT codes these, e.g., gender 1–6). Names above are assumed by analogy with MBRT — please confirm actual column names and coding scheme.*

---------------------------------------

PsychoPy version updates may require adjustments. Developers are not responsible for adapting the task to every use case.
Before collecting data, always test the experiment and check the data output.
Contributions are welcome.

**[FLAG]** *This disclaimer paragraph wasn't present in the original HLJT readme — added for structural parity with MBRT. Edit or remove as desired.*

---------------------------------------

## REFERENCE

**[FLAG]** *The original HLJT readme has no citation/reference section. If there is a publication associated with this implementation that should be cited when this resource is used, please add it here.*
