# Hand Laterality Judgement Task (HLJT)
# Marcos Moreno Verdú, 17/09/2024

---------------------------------------
GENERAL INSTRUCTIONS:

This README is not intended to explain how PsychoPy generally works, but the specific aspects of this experiment.

If you have never used PsychoPy, please have a look at the documentation on their webpage or tutorials, especially regarding conditions files, variables, routines and loops. This will save you time if you decide to modify any parameters from this experiment.

If you have never used PsychoPy, you should know that once you have decompressed the .zip file, you must not change the names of the files/folders, as the .psyexp file is going to look for specific names at specific locations. Additionally, you should avoid, wherever possible, changing any variable names, as again, the code depending on that variable name will need to be adjusted as well. Bear this in mind.

---------------------------------------
SPECIFIC INSTRUCTIONS FOR THIS EXPERIMENT:

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
	
	-Further languages could be implemented, but the code and files must be modified.

-response_mode: mandatory.
	
	-Options: Both hands (default)/Right hand/Left hand.
	
	-This is to specify if the user will respond with both hands or their left/right hand. The instructions differ between these modes (if set to both hands, the keys S and L will be used, whereas if set to only one hand (regardless of which), keys G and H will be used.

-practice_block: mandatory.
	
	-Options: Yes (default)/No.
	
	-This is to specify if the test blocks will be preceeded by a practice block where all the stimuli which will be used are going to be displayed in a random order. The practice block is useful to get familiar with the task.

-n_angles: mandatory.
	
	-Options: 8 with increments of 45º(default)/4 with increments of 90º/6 with increments of 60º /12 with increments of 90º.
	
	-The set of angles to rotate the stimuli in the task. The experiment will look for the specific Excel file.

-hands_views: mandatory.
	
	-Options: Dorsal and Palmar (default)/Palmar/Dorsal.
	
	-Whether to display the rotated images in a palmar or dorsal view, or both. The code will filter out the corresponding stimuli, and will use a conditions file named "Stimuli_last_run.csv" which will be created automatically on every run, and therefore will overwrite any previous files with the same name. This is a way to make sure which set of stimuli were used in the last run of the experiment. It does not contain any output from the participant. 


-n_reps: mandatory.
	
	-Options: 12 (default)/8/4.
	
	-Total number of repetitions per unique stimulus in the test blocks (excluding the practice block). As of now there is a fixed number of test blocks (4 blocks). The only options available are the one listed there. If you change the number you will need to adjust the corresponding code, or the experiment will crash.

---------------------------------------
WORKFLOW:

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

-test_hljt_response.corr: Encodes the accuracy for each trials of the test blocks. Correct (=1) or incorrect (=0).

Aside from those, we will need to retain the variables some variable from our conditions file for analysis:

	-hljt_side
	-hljt_view
	-hljt_angle
	-hljt_direction

All the variables shown in the dialog box will be saved.
