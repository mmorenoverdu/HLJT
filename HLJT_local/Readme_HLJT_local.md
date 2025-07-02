# HAND LATERALITY JUDGEMENT TASK (HLJT)

Marcos Moreno Verdú, 01/07/2025
PsychoPy version 2024.2.1
Local experiment
Languages supported: English, Spanish, French. Further languages can be added with no code (see Language Localisation below)

---------------------------------------
## GENERAL INSTRUCTIONS: ##

This README is not intended to explain how PsychoPy generally works, but the specific aspects of this experiment.

If you have never used PsychoPy, please have a look at the documentation on their webpage or tutorials, especially regarding conditions files, variables, routines and loops. This will save you time if you decide to modify any parameters from this experiment.

If you have never used PsychoPy, you should know that once you have decompressed the .zip file, you must not change the names of the files/folders, as the .psyexp file is going to look for specific names at specific locations. Additionally, you should avoid, wherever possible, changing any variable names, as again, the code depending on that variable name will need to be adjusted as well. Bear this in mind.

---------------------------------------
## SETUP INSTRUCTIONS ##

To run this task you need to have installed PsychoPy version 2024.2.1 or superior.

There are no dependencies for this task.

The data output MUST be processed to obtain meaningful information. An example of data processing (in R) can be found in the folder of this experiment. 

Step-by-step instructions:
1) Download all files from the repository
2) Unzip the file in  NEW folder WITHOUT any other PsychoPy experiments in it.
3) Open the file 'HLJT_local.psyexp' in PsychoPy.

---------------------------------------
## LANGUAGE LOCALISATION ##

We need 2 Excel sheets (with extension type .xlsx) to store:
- The available language localisations: "language_localiser.xlsx"
- The list of messages to use as variables to display text on screen: "messages.xlsx"

In the Experiment Settings button, in the Basic tab, the Experiment Info section must have a "language" field with the list of languages. This allows to select the language **before** every run of the Experiment through a dropdown menu in the pop-up dialogue box. These languages need to be specified as in the language column of the language localiser Excel sheet.

All the text components which should be dynamically updated for language should have their "Text" field in "Set to every repeat". This allows to change dynamically the value of the variable, which therefore changes the text to be shown.

*Adding a new language*

If you just want to add a new language without any further modifications (i.e., you do not want to provide other messages than the ones already used), you just need to modify 4 things:
1. In language_localiser.xlsx, add a new **ROW** with your new language and its code. Write this in English (e.g., "Chinese", "CH").
2. In messages.xlsx, add a new **COLUMN**, titled with the code you used in the previous step (e.g., "CH"). For each message, provide the corresponding translation into your desired language.
3. In PsychoPY, go to Experiment Settings and add a new language to the list of languages in the **language field**, with the name being the language you used in Step 1. It is critical that you add your language using '' (e.g., 'Chinese'). If you want your language to be the default choice every time you run the experiment, you just have to **place it at the beginning of the list**.
4. Add the corresponding columns with your language to the different instructions files and block messages (Excel sheets).

---------------------------------------
## TECHNICAL DETAILS: ##

The experiment has the following subfolders:

-hljt_images: It contains the four stimuli to be used in the task. This is left/right hand images in .png format. The images are divided into dorsal or palmar view, but the user can specify if both or only one are used.
	
-hljt_instr_images: It has the images to display in the instructions of the experiment, which include:
		
		-pic1: overall idea of the task.
		-pic2: how to respond to the task. It is different depending on the selected response mode (see below).
		-pic3: information about the feedback. It is suppressed depending on the user's preference (see below).

-hljt_files: It contains KEY files that are used to run the experiment.
		
		-Block_messages.xlsx: Encodes the messages to show before/after each test block. The number of rows will determine the number of test blocks.
		
		-Instructions files (.xlsx): Each file encodes the instructions and images for each response mode available (see below).
		
		-Stimuli_*angles.xlsx: The main conditions file. Must not be modified unless strictly necessary. There are 4 files with sets of stimuli depending on the increments at which the rotation must be applied (90º = 4 angles; 60º = 6 angles; 45º = 8 angles; 30º = 12 angles).
			-hljt_images: column to tell PsychoPy which image to use.
			-hljt_side: which side the images corresponds to.
			-hljt_view: the view of the stimulus. Can be dorsal or palmar.
			-hljt_angle: the angle to rotate the stimulus to, always in the clockwise direction.
			-hljt_direction: the direction of rotation considering left/right and palmar/dorsal.
				
				-Options are:
					-up (0º).
					-medial/lateral (will depend on side).
					-down (180º).
				
				-The direction allows the later quantify the 'biomechanical constraints' effect (medial vs lateral response times). A note on this:
					-for right images, lateral is 1-179º; medial is 181º-359º.
					-for left images, lateral is 181º-359º; medial is 1-179º.

			-hljt_correct_both: the corresponding correct key to press if response mode is set to "Both hands" (S for left hands, L for right hands).
			-hljt_correct_one: the corresponding correct key to press if response mode is set to Right or Left hand (G for left hands, H for right hands).
			
---------------------------------------
EXPERIMENT SETTINGS (parameters to choose):

The experiment is set so that before going into the task itself, the user will be able to choose some options. Default options can be easily modified by going to Experiment settings and changing the order of each corresponding field.

-participant: optional. ID of the participant. Can be a number or a name.

-session: optional. ID of the session. Can be a number or a name.

-language: mandatory.
	
	-Options: English (default)/Spanish/French.
	
	-Further languages could be implemented (see Language Localisation above).


-response_mode: mandatory.
	
	-This is to specify if the user will respond with both hands or their left/right hand. The instructions differ between these modes (if set to both hands, the keys S and L will be used, whereas if set to only one hand (regardless of which), keys G and H will be used.	
	
	-Options: Both hands (default)/Right hand/Left hand.
	

-practice_block: mandatory.
	
	-This is to specify if the test blocks will be preceeded by a practice block where all the stimuli which will be used are going to be displayed in a random order. The practice block is useful to get familiar with the task.

	-Options: Yes (default)/No.
	

-n_angles: mandatory.
	
	-The set of angles to rotate the stimuli in the task. The experiment will look for the specific Excel file.
	
	-Options: 8 with increments of 45º(default)/4 with increments of 90º/6 with increments of 60º /12 with increments of 90º.
	

-hands_views: mandatory.
	
	-Whether to display the rotated images in a palmar or dorsal view, or both. The code will filter out the corresponding stimuli, and will use a conditions file named "Stimuli_last_run.csv" which will be created automatically on every run, and therefore will overwrite any previous files with the same name. This is a way to make sure which set of stimuli were used in the last run of the experiment. It does not contain any output from the participant. 
	
	-Options: Dorsal and Palmar (default)/Palmar/Dorsal.
	
	
-n_reps: mandatory.
	
	-Total number of repetitions per unique stimulus in the test blocks (excluding the practice block). As of now there is a fixed number of test blocks (4 blocks). The only options available are the one listed there. If you change the number you will need to adjust the corresponding code, or the experiment will crash.

	-Options: 12 (default)/8/4.
	
	
---------------------------------------
PARTICIPANT WORKFLOW:

Once the experiment starts, it will guide the participant through it without the need for any other explicit supervision. There will be:
-A welcome screen with a brief description of the goal of the task.
	
-A couple of screens with instructions.

-A practice block (as decided by the user) with:
	
	-A welcome screen.
	
	-A countdown of 3 seconds.
	
	-Practice trials with all stimuli (1 repetition per unique stimulus). Always with feedback.

-A test block (4 in total, duration will depend on the set of stimuli to be chosen):
	
	-Welcome screen.
	
	-Countdown.
	
	-Block of trials.
	
	-Break screen.

-A goodbye screen.

---------------------------------------
OUTPUT:

The output file that PsychoPy will generate will be a .csv file in a subfolder "data". This .csv will contain all the variables encoded in the experiment. It will always be named with the participant field and the date.

The output variables we will be interested in, specifically for the HLJT, are:
	
-test_hljt_response.rt: Encodes the response time for each trial of the test blocks. It does it in SECONDS.

-test_hljt_response.corr: Encodes the accuracy for each trial of the test blocks. Correct (=1) or incorrect (=0).

Aside from those, we will need to retain the variables from our conditions file for analysis:
	-hljt_side
	-hljt_view
	-hljt_angle
-hljt_direction

All the variables shown in the dialog box will be saved.

