##### EXAMPLE OF OUTPUT PROCESSING FROM HAND LATERALITY JUDGEMENT TASK (HLJT) ####

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

# if the script is in the experiment folder, a 'data' folder can be called directly
data_raw <- read_csv("data/Example_HLJT_local.csv")

# inspect the data
str(data_raw)

# Parameters -------------------------------------------------------------

# parameters of the task
parameters <- data_raw |>
  select(participant,
         session,
         language_code,
         response_mode,
         practice_block,
         n_angles,
         hand_views,
         n_reps,
         feedback,
         date,
         psychopyVersion,
         frameRate) |>
  slice(1)

# time to complete the task (from first to last screen, including breaks)
completion_time <- data_raw |>
  select(completion_time) |>
  filter(!is.na(completion_time)) |>
  mutate(completion_time = round(completion_time / 60, digits = 2)) |> # put in minutes
  pull()

# Process data from task -----------------------------------------------------

# Select columns, filter relevant rows and put data in an optimal format
data <- data_raw |>
  # select relevant columns and rename them in a single step
  select(participant,
         block = test_block.thisN, # iteration for the block loop (starts at 0)
         angle = hljt_angle, # rotation angle for the trial
         view = hljt_view,  # hand view
         laterality = hljt_side, # hand laterality
         direction = hljt_direction, # direction for biomechanical constraints analysis
         stimulus = hljt_images, # file that was presented
         #correct_key = ifelse(unique(data_raw$response_mode == "Both hands"), hljt_correct_both, hljt_correct_one),
         # 3 KEY COLUMNS FROM THE TEST BLOCKS (MAIN BLOCKS, NOT PRACTICE BLOCKS)
         key = test_hljt_response.keys,  # key that was pressed by the participant
         accuracy = test_hljt_response.corr, # was this correct? 0 = incorrect, 1 = correct
         rt = test_hljt_response.rt) |> # what was the reaction time for the key press (in seconds)?
  # remove all rows in which no key was pressed, as this means this was not a trial in the main blocks
  filter(!is.na(key)) |>
  mutate(rt = rt *1000, # transform to milliseconds
         block = block + 1 # start at 1
         )

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

# similarly we can export the main data frame in case you want to analyse it in other software
write_csv(df, paste0(participant, "_data_processed.csv"))
write.xlsx(df, paste0(participant, "_data_processed.xlsx"))


