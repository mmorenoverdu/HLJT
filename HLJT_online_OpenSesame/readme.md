# HAND LATERALITY JUDGEMENT TASK (HLJT) — Online version

**Author:** Marcos Moreno Verdu, 06/07/2026
**Software used:** OpenSesame 4.1.9 (or later)
**Experiment Type:** Online
**Languages supported:** English (EN) = default, Spanish (ES), French (FR), German (DE). Further languages can be added, which requires simple changes to the `.csv` files (see [Language Localization](#language-localization)).

---------------------------------------
## GENERAL INSTRUCTIONS

This experiment is built using [OpenSesame](https://osdoc.cogsci.nl/) 4.1.9. To run it online, it uses the [OSWeb](https://osdoc.cogsci.nl/4.1/manual/osweb/osweb/) backend, hosted on a [JATOS](https://www.jatos.org/) server. It is a JavaScript port of `HLJT_local_OpenSesame`, and the two behave the same way from a participant's point of view, with a small number of deliberate, documented differences (see [Technical Details](#technical-details)).

Every screen is written as editable code — as `inline_javascript` items instead of `inline_script` (Python) items, since Python does not run in a browser. Blocks and trials are still built from native `loop`/`sequence` items, so the overall flow stays visible and editable in OpenSesame's Overview tab, exactly like the local version.

If you are unfamiliar with OpenSesame, please refer to the [documentation](https://osdoc.cogsci.nl/) on their website first. This README specifically details the structure and customization of this **HLJT online** implementation, not OpenSesame/OSWeb/JATOS in general.

---------------------------------------
## SETUP INSTRUCTIONS

To edit or run this task, you need to have **OpenSesame** (4.1.9 or later) installed.
To run the task online, you will need a [JATOS server](https://www.jatos.org/). At the time of writing, [MindProbe](https://mindprobe.eu/) serves as a JATOS server free of charge.

**Step-by-step instructions:**
1. **Download** all files from the repository (`HLJT_online_OpenSesame` folder).
2. **Open** `HLJT_online.osexp` in OpenSesame 4.1.9+ (desktop). This file bundles its own file pool (every image and `.csv` the experiment needs) inside a `.tar.gz` archive — OpenSesame opens it the same way as any other `.osexp`.
3. Open the **`settings`** item and edit the experimenter-facing options directly in the JavaScript code (see [Experiment Settings](#experiment-settings-parameters-to-choose)).
4. Use **OpenSesame's OSWeb preview** to click through the whole experiment at least once (Menu → Run → "Run in browser"). This is the fastest way to confirm everything works before deploying, and to try out any changes you make.
5. **Export for JATOS**: in OpenSesame, open the OSWeb extension ("Tools" in the top bar → "OSWeb and JATOS control panel") and click "Export to JATOS archive". This saves a `.jzip` file.
6. Log in to your JATOS server, click "Import Study", and select the exported `.jzip`. Generate a study link ("Study Links" → choose a link type → copy the URL) and distribute it to your participants — they run the task directly in their browser.
7. **Download data**: in JATOS, go to your study → *Results* → select the entries you want → *Export Results → JATOS Results Archive*. Convert the downloaded `jatos_results_<timestamp>.jzip` to `.csv`/`.xlsx` using OpenSesame's **"Convert OSWeb results to csv/xlsx"** extension (desktop OpenSesame, under Tools/Extensions).

---------------------------------------
## LANGUAGE LOCALIZATION

This experiment uses external `.csv` files to manage text and translations, the same idea as the local version, except the lookup tables are `.csv` instead of `.xlsx` (OSWeb has no bundled xlsx reader — only the `csv-parse` library is available).

**How it works:** `Language_localiser.csv` maps a **language** name to an **ISO_code**. `Messages.csv` contains one column per ISO_code (e.g. `EN`, `ES`) and is read once, in the `setup` item's Run phase (right after `language_form`), to build the `msg` lookup object used by every other item (e.g. `msg["welcome_msg"]`). Every message is also copied onto the experiment's own variable store (`vars[key] = value`), so any message key can be inserted directly into a form's title or options as `{key}`.

The language is chosen via a native **`language_form`** (`form_multiple_choice`), shown right after `settings` — a ready-made OpenSesame form, not a custom-drawn screen.

### Adding a new language

#### 1. Open the relevant `.csv` files
- `Language_localiser.csv`
- `Messages.csv`

#### 2. Extend `Language_localiser.csv` by adding a new row

The file must contain the columns:
```
language,ISO_code
English,EN
Spanish,ES
French,FR
German,DE
```

Add your new language (e.g. Dutch) as a new row:
```
language,ISO_code
English,EN
Spanish,ES
French,FR
German,DE
Dutch,NL
```

#### 3. Extend `Messages.csv` by adding a new column

The file must contain a `message` column and one column per language (named by *ISO_code*). Add a new column titled with your new code (e.g. `NL`) and provide a translation for **every** message row.

⚠️ Do this consistently for **all** message keys — a missing translation shows up as blank text, not as an error.

#### 4. Re-import the edited csv files into the file pool

Because this `.osexp` bundles its own copies of the csv files inside its pool (rather than reading them from disk, as the local version does), editing the file on disk does **not** update the copy OpenSesame actually uses. You must:
- In OpenSesame's File Pool panel (bottom-right by default), right-click `Language_localiser.csv` / `Messages.csv` → remove, then drag-and-drop your edited files back in with the **exact same filename**.

#### 5. Add the new option to `language_form`

1. Open the **`language_form`** item (`form_multiple_choice`) in OpenSesame.
2. Add a new entry to its options list, e.g. `Dutch`. This value must exactly match the entry you added to `Language_localiser.csv`.
3. Save the experiment, then re-test in the OSWeb preview before exporting.

---
> **⚠️ Important:** When editing `Messages.csv` in Excel, save it specifically as **"CSV UTF-8 (Comma delimited)"** — the plain "CSV" option saves accented characters in your system's default encoding instead of UTF-8, which silently corrupts non-English text (e.g. "años", "âge"). Also make sure every row keeps all 5 columns (`message,EN,ES,FR,DE`) — a row with missing columns makes the csv parser reject the **entire file** at runtime with a `CsvError: Invalid Record Length`.
>
> **⚠️ Important:** Do not rename items, variables, or pool files. The pool is a flat namespace (no subfolders), and every script/JS reference in this experiment expects the exact filenames listed in [Technical Details](#technical-details).

---------------------------------------
## TECHNICAL DETAILS

The bundled `.osexp` file pool includes:
- 4 hand-stimulus images (`left_dorsal.png`, `left_palmar.png`, `right_dorsal.png`, `right_palmar.png`)
- 5 instruction images (`instr_pic1.jpg`, `instr_pic2_both.jpg`, `instr_pic2_left.jpg`, `instr_pic2_right.jpg`, `instr_pic3.jpg`)
- `HLJT_icon.jpg` — task icon shown on the welcome screen
- `Language_localiser.csv`, `Messages.csv` — language configuration
- `Instructions_both_hands.csv`, `Instructions_left_hand.csv`, `Instructions_right_hand.csv` — one per response mode
- `Stimuli_4angles.csv`, `Stimuli_6angles.csv`, `Stimuli_8angles.csv`, `Stimuli_12angles.csv` — trial tables for each angle-count setting

**How the experiment is built (OSWeb specifics), and how it differs from the local version:**

- `settings` — experimenter-editable options, plain JavaScript (Prepare phase only). All backends (`sampler`, `mouse`, `keyboard`, `color`, `clock`, `canvas`) are set to `osweb`, not `psycho` (the desktop-only backend).
- `language_form` — on-screen language picker, a native `form_multiple_choice` item (see [Language Localization](#language-localization)).
- `setup` — loads the csv files via the `csv-parse` library, derives every setting, and defines helper functions (image scaling, ITI sampling, trial-list building, paragraph text drawing) shared by later items.
- `welcome_seq`, `instructions_loop`/`instructions_seq`, `demographics_seq` (`age_form`, `gender_form`, `hand_form`), `blocks_loop`/`block_sequence` (`block_start_seq`, `countdown_seq`, `trials_loop`/`trial_sequence` with `ITI_seq`/`trial_seq`/`feedback_seq`, `block_end_seq`), `bye_seq` — one sub-sequence per screen/step.

**Design notes and deviations from the local version:**

1. **`countdown`** (3, 2, 1) is three separate, statically-drawn screens shown for exactly 1 second each, instead of one continuously-redrawn screen, since JavaScript in OSWeb cannot block execution the way Python's `clock.sleep()` can.
2. **`block_end`** (the rest-break screen) shows a static "take a break" message instead of a live mm:ss timer, for the same reason.
3. **Multi-paragraph text** (welcome, instructions, block intros, goodbye screen) is drawn with a shared `draw_paragraphs()`/`wrap_line()` helper that manually word-wraps each paragraph and draws it line by line, rather than relying on the Canvas's own `max_width`/`html` text-wrapping properties — these did not reliably wrap or interpret line breaks in OSWeb during testing, showing literal `<br />` text and clipped content instead.
4. **`age_form`** is a custom `form_base` with a `text_input` widget, letting participants type their age directly, instead of a long `form_multiple_choice` picklist.
5. **`gender_form`/`hand_form`** options are localized via `{key}` substitution inside their `__options__` block (each option references a `Messages.csv` row, e.g. `{f_msg}`, `{left_msg}`), so participants see the options in their chosen language. Since the value stored by `form_multiple_choice` is the localized text itself, add a small recoding step (an `inline_javascript` run right after `demographics_seq`, comparing the response against the same localized message variable) if you want the logged data to use one fixed, language-independent code (e.g. `"female"`/`"male"`, `"left"`/`"right"`) instead of the raw localized text — see [Output](#output).
6. **No `items["x"].dm = ...` assignment is used anywhere** (this is a Python-only API and throws a runtime error in JavaScript). Instead, `instructions_loop`, `blocks_loop`, and `trials_loop` each wrap a plain JavaScript array (built by `setup` or `block_start`) together with a running index variable (`instructions_idx`, `block_idx`, `trial_idx`). Each loop uses a fixed `cycles=1` plus a generously large `repeat` (a safe upper bound), with a `break_if` condition (e.g. `"trial_idx >= trial_count"`) that stops it at the right point.
7. **Values that are recomputed every trial** (`iti_ms`, `feedback_ms`) are computed in the **Prepare** phase of the item that produces them, not its Run phase. Within a sequence, all children's Prepare phases run (in order) before any of their Run phases — so the very next item (`iti_wait`/`feedback_wait`) needs the value already available at its own Prepare phase, before the drawing item's Run phase would otherwise have set it.

One important rule if you edit or add items: OpenSesame runs the **Prepare** phase of every item inside a `sequence`, in order, before running the **Run** phase of any of them. This is why `language` is only available from `setup`'s Run phase onward — it is set by `language_form`'s Run phase, which happens after every item's Prepare phase has already executed.

---------------------------------------
## EXPERIMENT SETTINGS (parameters to choose)

The experimenter edits settings directly in the **`settings`** item (JavaScript), before exporting. There is no startup dialog — language is the one exception, chosen on-screen by the participant (see [Language Localization](#language-localization)).

### Available Parameters

| Variable | Options | Description |
| :--- | :--- | :--- |
| `response_mode` | • **Both hands** (Default)<br>• Right hand<br>• Left hand | Determines the required input method. |
| `practice_block` | • **Yes** (Default)<br>• No | Whether a practice block (all stimuli, 1 repetition, with feedback) precedes the test blocks. |
| `n_angles` | • **8**, increments of 45° (Default)<br>• 4, increments of 90°<br>• 6, increments of 60°<br>• 12, increments of 30° | Selects the corresponding `Stimuli_*angles.csv` file. |
| `hand_views` | • **Palmar and Dorsal** (Default)<br>• Palmar<br>• Dorsal | Which hand view(s) are shown. |
| `n_reps` | • **8** (Default)<br>• 4<br>• 12 | Total repetitions per unique stimulus across the test blocks (2 repetitions per block, so the number of test blocks is 2/4/6 for `n_reps` 4/8/12). |
| `feedback` | • **No feedback** (Default)<br>• 0.3<br>• 0.5<br>• 0.8<br>• 1 | Duration of feedback (in seconds) per trial in the test blocks. |
| `practice_n_trials` | • **5** (Default)<br>• "all"<br>• any number | How many stimuli to show in the practice block; `"all"` shows every filtered stimulus once. |
| `test_n_trials` | • **2** (Default)<br>• "all"<br>• any number | How many stimuli to show per test block; `"all"` shows every filtered stimulus twice. A small number is handy for quickly testing the whole pipeline. |

> **Important:** If you export and upload the `.osexp` without editing `settings`, these **Default** values (bolded above) will be used.

### Changing the Defaults

1. Open the **`settings`** item in the Overview tab.
2. Edit the values assigned to each variable directly in the JavaScript code.
3. Save the experiment, test in the OSWeb preview, then re-export to JATOS.

### Letting Participants Select Settings

In the current implementation, only the **language** is chosen by the participant (via `language_form`, always shown at the start). All other settings are fixed by the experimenter in the `settings` item before export. If you want participants to choose additional settings themselves (e.g. response mode), add a new `form_multiple_choice` item following the same pattern as `language_form`, and insert it into the `experiment` sequence before `setup` runs (since `setup` reads these variables to derive everything else).

### Disable Demographic Questions

The experiment includes Age, Gender, and Handedness questions by default, collected via `demographics_seq` (`age_form`, `gender_form`, `hand_form`). These support normative data collection.

If you do not want to collect demographics, remove the line `run demographics_seq True` from the **`experiment`** sequence.

### Saving and Exporting

To try out the experiment after changing settings or adding a new language, use OpenSesame's OSWeb preview (Run → "Run in browser"). This mode is **not** suitable for data collection, only for debugging. When testing repeatedly, clear your browser's cache to make sure your latest changes are actually displayed.

Once you are done configuring:
1. **Save** the experiment in OpenSesame.
2. **Export** as `.jzip`: "Tools" → "OSWeb and JATOS control panel" → "Export to JATOS archive".
3. **Upload** the resulting `.jzip` to your JATOS server.

---------------------------------------
## PARTICIPANT WORKFLOW

Once a participant opens the study link, it guides them through the task without further supervision.

1. **Language selection:** the participant picks their language (English / Español / Français / Deutsch).
2. **Welcome screen:** a brief description of the goal of the task.
3. **Demographics:** the participant answers Age (typed in directly), Gender, and Handedness (if not disabled), via three form screens.
4. **Instructions:** a couple of screens explaining the task and the response-key assignment for the selected response mode.
5. **Practice Block** (if enabled):
   - Block intro message.
   - 3-2-1 countdown.
   - Practice trials with all (or `practice_n_trials`) stimuli, always with feedback.
6. **Test Blocks** (2/4/6, depending on `n_reps`):
   - Block intro message.
   - 3-2-1 countdown.
   - Block of trials.
   - Break screen (self-paced; press space to continue).
7. **Completion:** goodbye screen, shown for 3 seconds.

#### HLJT trial procedure

The sequence of a single trial (`trial_sequence`) is as follows:

1. Inter-trial interval (`ITI_seq`): fixation cross + response boxes, shown for a duration drawn from the same probability distribution as the local version (mostly ~0.75–0.85 s, occasionally 0.6–1 s).
2. Stimulus presentation (`trial_seq`): stays on screen until a keypress is recorded (untimed).
3. Feedback (`feedback_seq`, conditional): if enabled, colored response boxes are shown for the selected duration, and the trial's data row is logged.

   → *Automatic advance to the next trial.*

---------------------------------------
## OUTPUT

Data is collected by JATOS as participants complete the study, and downloaded as a `jatos_results_<timestamp>.jzip` archive from the JATOS web interface (*Results → Export Results → JATOS Results Archive*). Convert it to `.csv`/`.xlsx` using OpenSesame's **"Convert OSWeb results to csv/xlsx"** extension — see step 7 in [Setup Instructions](#setup-instructions).

Once converted, the resulting table has the same one-row-per-trial structure as the local version's `subject-N.csv`, since both use OpenSesame's logger to write one row per trial.

> **Note:** Raw data should always be inspected and cleaned of outliers or errors prior to statistical analysis.

### Variable Documentation

#### 1. Trial data (one row per trial, logged by `logger` inside `trial_sequence`)

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `participant`, `session` | character/numeric | As set in the `settings` item. |
| `this_block_number` | integer | Block index (the practice block, if enabled, is block 1). |
| `this_is_practice` | 0/1 | Whether this row belongs to the practice block. |
| `trial_idx` | integer | Trial index within the block (0-based). |
| `last_key` | character | Key pressed by the participant. |
| `last_rt` | numeric | Response time, in **seconds**. |
| `last_correct` | 0/1 | Accuracy. |
| `hljt_side` | factor | Side of the stimulus hand ("left"/"right"). |
| `hljt_view` | factor | View of the stimulus ("dorsal"/"palmar"). |
| `hljt_angle` | numeric | Rotation angle of the stimulus (degrees). |
| `hljt_direction` | factor | Rotation direction category (up/medial/lateral/down); used to quantify the biomechanical-constraints effect. |
| `current_iti` | numeric | Duration (seconds) of the inter-trial interval preceding this trial. |

#### 2. Demographic responses (repeated on every trial row — set once during `demographics_seq`, then persisting in the variable store for the rest of the run)

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `age_response` | character | Participant age in years, typed in directly via `age_form`. |
| `gender_response` | character | The option selected in `gender_form`, in the participant's chosen language unless a recoding step has been added (see [Technical Details](#technical-details), point 5). |
| `hand_response` | character | The option selected in `hand_form` ("Left"/"Ambidextrous"/"Right", or their translations), with the same caveat as above. |

#### 3. Settings columns (repeated on every row)

| Variable Name | Description |
| :--- | :--- |
| `language`, `lang_code` | Language chosen on-screen, and its ISO code. |
| `response_mode`, `practice_block`, `n_angles`, `hand_views`, `n_reps`, `feedback` | Copies of the corresponding `settings` item values, for convenience during analysis. |

---------------------------------------

OpenSesame/OSWeb/JATOS version updates may require adjustments to the experiment file.
As developers, we are not responsible for adapting the task to every use case.
Before collecting data, always test the experiment in OpenSesame's OSWeb preview, and check the data output end-to-end (including a full JATOS export/download/conversion cycle) with a couple of pilot runs.

Contributions are welcome.

---------------------------------------
## REFERENCE

Please cite [Moreno-Verdú et al. 2025](https://linkinghub.elsevier.com/retrieve/pii/S0306452225001800) when using this resource.
