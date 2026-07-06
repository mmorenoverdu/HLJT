##### EXAMPLE OF OUTPUT PROCESSING FROM HAND LATERALITY JUDGEMENT TASK (HLJT) ####
##### OpenSesame version #####

## The data processing consists in the following steps:
## 1. Select the necessary columns
## 2. Filter the necessary rows (those from the test blocks)
## 3. OPTIONAL: Apply thresholds to reject trials (this depends on the participant being tested)
## 4. Generate summary
## 5. Export

# Load packages -----------------------------------------------------------

# you need to have the following packages installed:
library(tidyverse) # to read and wrangle data
library(this.path) # to set path automatically
library(openxlsx) # to export to Excel sheet

# Load data ---------------------------------------------------------------

# this sets the working directory to the location of the script
setwd(here())

# Unlike the PsychoPy version, OpenSesame writes its automatic log directly
# in the experiment folder (not inside "data/"), and names it "subject-N.csv"
# (N = 1, 2, 3... increasing by one on every run). Point this at the file
# for the participant you want to process.
data_raw <- read_csv("subject-1.csv")

# inspect the data
str(data_raw)

# NOTE: OpenSesame's automatic log ("auto_log yes") writes EVERY Python
# variable that exists in the experiment at the time each row is logged -
# hundreds of columns, most of them internal OpenSesame bookkeeping
# (colors, screen settings, item counters, instruction text, etc.). The
# steps below simply select the handful of columns that are actually
# useful for analysis; everything else can be ignored.

# Parameters -------------------------------------------------------------

# parameters of the task
parameters <- data_raw |>
  select(participant,
         session,
         language,
         language_code,
         response_mode,
         practice_block,
         n_angles,
         hand_views,
         n_reps,
         feedback) |>
  slice(1)

# NOTE: OpenSesame's native log has no direct equivalent to PsychoPy's
# "date" / "psychopyVersion" / "frameRate" / "completion_time" columns.
# It does log per-item "time_*" / "count_*" bookkeeping variables (e.g.
# time_experiment), but these are internal timing diagnostics, not a
# reliable measure of total completion time, so they are not used here.
# If you need completion time, consider timestamping it yourself (e.g.
# from the file's creation time), or ask about adding this back into the
# experiment.

# Process data from task -----------------------------------------------------

# Select columns, filter relevant rows and put data in an optimal format
data <- data_raw |>
  # OpenSesame logs "is_practice" as the text "True"/"False"; make it a
  # proper logical so we can filter on it below
  mutate(is_practice = tolower(as.character(is_practice)) == "true") |>
  # select relevant columns and rename them in a single step
  select(participant,
         block = block_number, # block index (practice block, if any, counts as block 1)
         is_practice,          # TRUE for the practice block, FALSE for test blocks
         trial = trial_number, # trial index within the block
         angle = hljt_angle,   # rotation angle for the trial
         view = hljt_view,     # hand view
         laterality = hljt_side, # hand laterality
         direction = hljt_direction, # direction for biomechanical constraints analysis
         stimulus = hljt_images, # file that was presented
         correct_key = correct_key_value, # correct key for this trial (already resolved
                                           # for the chosen response_mode by the experiment)
         key = last_key,       # key that was pressed by the participant
         accuracy = last_correct, # was this correct? 0 = incorrect, 1 = correct
         rt = last_rt,         # reaction time for the key press (in seconds)
         iti = current_iti) |> # inter-trial interval preceding this trial (in seconds)
  # keep only the test-block trials (drop the practice block)
  filter(!is_practice) |>
  select(-is_practice) |>
  mutate(rt = rt * 1000, # transform to milliseconds
         # renumber test blocks starting at 1 (block 1 was the practice
         # block, if practice_block == "Yes", so it needs to be subtracted)
         block = block - ifelse(unique(data_raw$practice_block) == "Yes", 1, 0))

# OPTIONAL
# In healthy individuals, response times are typically within 300ms and 3,000ms
# Hence we can reject the trials outside of these thresholds
early <- 300
late <- 3000
# if no thresholds want to be applied, simply set early to 0 and late to a very big number (e.g. 10^6)

# create labels for trials and filter those within the defined thresholds
data <- data |>
  mutate(trial_label = case_when(rt < early ~ "early",
                                 rt > late ~ "late",
                                 TRUE ~ "typical"))

# how many trials for each label?
data |>
  group_by(trial_label) |>
  summarise(n = n())

# create a new object to keep the original data frame intact, only with trials within the thresholds
df <- data |>
  filter(trial_label == "typical")

# how many trials did we reject?
length(data) - length(df)

# Obtain summary ----------------------------------------------------------

# What is the overall accuracy?
overall_accuracy <- df |>
  summarise(mean = mean(accuracy)*100) |> # calculate the mean and put in %
  mutate(mean = round(mean, digits = 2)) |> # round
  pull() # extract the value

# What is the overall response time? We only consider the CORRECT trials for this
overall_rt <- df |>
  filter(accuracy == 1) |> # we filter the data frame to consider only correct trials
  summarise(mean = mean(rt)) |> # calculate mean
  mutate(mean = round(mean, digits = 2)) |> # round
  pull() # extract the value

# What is the overall biomechanical constraints effect in response time?
overall_biom_const <- df |>
  filter(accuracy == 1) |> # again we only take correct trials
  summarise(medial = mean(rt[direction == "medial"]), # average for medial
            lateral = mean(rt[direction == "lateral"]) # average for lateral
            ) |>
  mutate(biom_const = lateral - medial, # difference between the two
         biom_const = round(biom_const, digits = 2) # round
         ) |>
  # positive values indicate shorter reaction times for medial stimuli
  pull() # extract the value


# Export ------------------------------------------------------------------

# extract participant
participant <- df |>
  select(participant) |>
  slice(1) |>
  pull()

# create a summary table with the main summaries
summary <- data.frame(participant = participant,
                      accuracy = overall_accuracy,
                      rt = overall_rt,
                      biomechanical_constraints = overall_biom_const)

# export this to an .csv or Excel sheet
write_csv(summary, paste0(participant, "_summary.csv"))
write.xlsx(summary, paste0(participant, "_summary.xlsx"))

# similarly we can export the main data frame in case you want to analyse it in another software
write_csv(df, paste0(participant, "_data_processed.csv"))
write.xlsx(df, paste0(participant, "_data_processed.xlsx"))
