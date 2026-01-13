#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on enero 13, 2026, at 19:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'HLJT_local'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'language': ["English", "French", "Spanish", "German"],
    'response_mode': ["Both hands", "Right hand", "Left hand"],
    'practice_block': ["Yes", "No"],
    'n_angles': [ "8 (increments of 45º)", "4 (increments of 90º)", "6 (increments of 60º)", "12 (increments of 30º)"],
    'hand_views': ["Palmar and Dorsal", "Palmar", "Dorsal"],
    'n_reps': ["8", "12", "4"],
    'feedback': ["0.3", "0.5", "0.8", "1", "No feedback"],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1280, 720]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\morenoverdu\\OneDrive - UCL\\BAS-Lab\\Github_repos\\HLJT\\HLJT_local\\HLJT_local_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('adv_resp') is None:
        # initialise adv_resp
        adv_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='adv_resp',
        )
    if deviceManager.getDevice('inst_adv') is None:
        # initialise inst_adv
        inst_adv = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='inst_adv',
        )
    if deviceManager.getDevice('block_adv_resp') is None:
        # initialise block_adv_resp
        block_adv_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='block_adv_resp',
        )
    if deviceManager.getDevice('hljt_go_to_experiment_key') is None:
        # initialise hljt_go_to_experiment_key
        hljt_go_to_experiment_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='hljt_go_to_experiment_key',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('block_end_adv_resp') is None:
        # initialise block_end_adv_resp
        block_end_adv_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='block_end_adv_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "exp_settings" ---
    # Run 'Begin Experiment' code from response_mode
    use_i = "" # encodes which Excel file to use
    
    # response mode
    if expInfo['response_mode'] == "Both hands":
        use_i = "hljt_files/Instructions_both_hands.xlsx"
    elif expInfo['response_mode'] == "Right hand":
        use_i = "hljt_files/Instructions_right_hand.xlsx"
    elif expInfo['response_mode'] == "Left hand":
        use_i = "hljt_files/Instructions_left_hand.xlsx"
    # Run 'Begin Experiment' code from practice_block
    if expInfo['practice_block'] == "Yes":
        pract_block = 1
    else:
        pract_block = 0
    # Run 'Begin Experiment' code from number_of_stimuli
    # number of stimuli
    # n_reps sets the number of repetitions in total
    # per unique stimulus
    # we want 2 reps per block, and therefore 
    # the number of main blocks will vary accordingly
    main_blocks = 0
    reps_per_block = 2
    if expInfo['n_reps'] == "4":
        main_blocks = 2  # * 2 reps_per_block = 4
    elif expInfo['n_reps'] == "8":
        main_blocks = 4 # ...same
    elif expInfo['n_reps'] == "12":
        main_blocks = 6  # ...same
    
    # pract_block turns 1 or 0 if a practice block is
    # requested, therefore the total number of blocks is
    # the number of main blocks + pract_block
    total_blocks = main_blocks + pract_block
    # Run 'Begin Experiment' code from feedback_settings
    # define feedback time
    feedback_time = expInfo["feedback"]
    fb = True  # by default, show feedback
    task_fb = True # placeholder, it's updated after
    if feedback_time == "No feedback":
        feedback_time = 0.3  # the boxed will turn white
        task_fb = False
    else:
        feedback_time = float(feedback_time)
    
    # colors
    black = [-1, -1, -1]
    green = [-1, 0.0039, -1]
    red = [1, -1, -1]
    white = [1, 1, 1] 
    # Run 'Begin Experiment' code from number_of_angles
    conditions_file = "Stimuli_4angles.xlsx"
    
    if expInfo['n_angles'] == "4 (increments of 90º)":
        conditions_file = "hljt_files/Stimuli_4angles.xlsx"
    elif expInfo['n_angles'] == "6 (increments of 60º)":
        conditions_file = "hljt_files/Stimuli_6angles.xlsx"
    elif expInfo['n_angles'] == "8 (increments of 45º)":
        conditions_file = "hljt_files/Stimuli_8angles.xlsx"
    elif expInfo['n_angles'] == "12 (increments of 30º)":
        conditions_file = "hljt_files/Stimuli_12angles.xlsx"
    # Run 'Begin Experiment' code from hand_views
    import pandas as pd
    
    # load conditions file in data frame
    conditions_df = pd.read_excel(conditions_file)
    
    # filter based on view
    if expInfo['hand_views'] == "Palmar":
        filtered_df = conditions_df[conditions_df['hljt_view'] == 'palmar']
    elif expInfo['hand_views'] == "Dorsal":
        filtered_df = conditions_df[conditions_df['hljt_view'] == 'dorsal']
    else:
        filtered_df = conditions_df
    
    # generate conditions file for this run. It overwrites
    trial_conditions = "Stimuli_last_run.csv"
    filtered_df.to_csv(trial_conditions, index=False)
    # Run 'Begin Experiment' code from inter_trial_interval
    import numpy as np
    # define parameters
    n_trials = 600 # higher number than actual trials
    block_size = 64  # same
    low_iti_range = (0.6, 1)
    high_prob_range = (0.75, 0.85)
    high_prob_percentage = 0.5  # 50% values within high_prob_range
    
    # create list of ITIs
    iti_list = []
    
    for block in range(n_trials // block_size):
        # for each block:
        n_high_prob = int(block_size * high_prob_percentage)  # trials in high prob range
        n_low_prob = block_size - n_high_prob  # rest in general range
        # generate ITIs in the high prob range
        high_prob_itis = np.random.uniform(low=high_prob_range[0], high=high_prob_range[1], size=n_high_prob)
        # generate ITIs in the general range
        low_prob_itis = []
        while len(low_prob_itis) < n_low_prob:
            iti = np.random.uniform(low=low_iti_range[0], high=low_iti_range[1])
            if not (high_prob_range[0] <= iti <= high_prob_range[1]):
                low_prob_itis.append(iti)
        # combine them
        block_itis = np.concatenate((high_prob_itis, low_prob_itis))
        # shuffle within block
        np.random.shuffle(block_itis)
        # add block to list
        iti_list.extend(block_itis)
    
    
    
    # --- Initialize components for Routine "load_lg" ---
    # Run 'Begin Experiment' code from update_language_code
    # we define "lang_code" which is our variable to
    # be used for the language localisation dynamically
    # we set it to English as default language
    lang_code = "EN"
    thisExp.addData("language_code", lang_code)
    
    # --- Initialize components for Routine "update_msg" ---
    
    # --- Initialize components for Routine "welcome" ---
    welcome_text = visual.TextStim(win=win, name='welcome_text',
        text='',
        font='Arial',
        pos=(0, 0.1), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    adv_resp = keyboard.Keyboard(deviceName='adv_resp')
    hljt_image = visual.ImageStim(
        win=win,
        name='hljt_image', 
        image='HLJT_icon.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.3), draggable=False, size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "demographics" ---
    demographics_title = visual.TextStim(win=win, name='demographics_title',
        text='',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    age_text = visual.TextStim(win=win, name='age_text',
        text='',
        font='Arial',
        pos=(0, 0.32), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    age_textbox = visual.TextBox2(
         win, text=None, placeholder='...', font='Arial',
         ori=0.0, pos=(0, 0.25), draggable=False,      letterHeight=0.03,
         size=(0.12, 0.07), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='age_textbox',
         depth=-3, autoLog=True,
    )
    gender_text = visual.TextStim(win=win, name='gender_text',
        text='',
        font='Arial',
        pos=(0, 0.1), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    gender_slider = visual.Slider(win=win, name='gender_slider',
        startValue=None, size=(1.0, 0.05), pos=(0, 0), units=win.units,
        labels=('', '', '', '', '', ''), ticks=(1, 2, 3, 4, 5, 6), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor=[0.4824, 0.4353, -0.1608], lineColor=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-5, readOnly=False)
    label_female = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.5, -0.1), draggable=False,      letterHeight=0.03,
         size=(0.15, 0.05), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.8, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='label_female',
         depth=-6, autoLog=True,
    )
    label_male = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.3, -0.1), draggable=False,      letterHeight=0.03,
         size=(0.15, 0.05), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.8, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='label_male',
         depth=-7, autoLog=True,
    )
    label_transgender = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.1, -0.1), draggable=False,      letterHeight=0.0275,
         size=(0.18, 0.05), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.8, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='label_transgender',
         depth=-8, autoLog=True,
    )
    label_nonbinary = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.1, -0.1), draggable=False,      letterHeight=0.03,
         size=(0.15, 0.05), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.8, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='label_nonbinary',
         depth=-9, autoLog=True,
    )
    label_other = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.3, -0.1), draggable=False,      letterHeight=0.03,
         size=(0.15, 0.05), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.8, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='label_other',
         depth=-10, autoLog=True,
    )
    label_prefer_not_say = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.5, -0.1), draggable=False,      letterHeight=0.03,
         size=(0.15, 0.05), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.8, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='label_prefer_not_say',
         depth=-11, autoLog=True,
    )
    laterality_text = visual.TextStim(win=win, name='laterality_text',
        text='',
        font='Arial',
        pos=(0, -0.27), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-12.0);
    laterality_slider = visual.Slider(win=win, name='laterality_slider',
        startValue=None, size=(0.5, 0.05), pos=(0, -0.35), units=win.units,
        labels=('', '', ''), ticks=(1, 2, 3), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor=[0.4824, 0.4353, -0.1608], lineColor=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-13, readOnly=False)
    label_left = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.25, -0.45), draggable=False,      letterHeight=0.03,
         size=(0.15, 0.05), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.8, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='label_left',
         depth=-14, autoLog=True,
    )
    label_ambi = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.45), draggable=False,      letterHeight=0.03,
         size=(0.2, 0.05), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.8, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='label_ambi',
         depth=-15, autoLog=True,
    )
    label_right = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.25, -0.45), draggable=False,      letterHeight=0.03,
         size=(0.15, 0.05), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.8, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='label_right',
         depth=-16, autoLog=True,
    )
    next_button = visual.ButtonStim(win, 
        text='', font='Arial',
        pos=(0.7, -0.35),
        letterHeight=0.035,
        size=(0.2, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[0.6078, -0.2784, -0.2784], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='next_button',
        depth=-17
    )
    next_button.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "instructions" ---
    # Run 'Begin Experiment' code from inst_code
    inst_msg = ""
    text_x = 0
    inst_text = visual.TextStim(win=win, name='inst_text',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    advance_text = visual.TextStim(win=win, name='advance_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    inst_image = visual.ImageStim(
        win=win,
        name='inst_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), draggable=False, size=1.0,
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    inst_adv = keyboard.Keyboard(deviceName='inst_adv')
    
    # --- Initialize components for Routine "block_start" ---
    # Run 'Begin Experiment' code from block_start_code
    block_number = 0
    fb = True
    block_message = ""
    block_number_text = visual.TextStim(win=win, name='block_number_text',
        text='',
        font='Arial',
        pos=(0, 0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, 0.4980, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    block_start_main_text = visual.TextStim(win=win, name='block_start_main_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    block_start_adv_text = visual.TextStim(win=win, name='block_start_adv_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    block_adv_resp = keyboard.Keyboard(deviceName='block_adv_resp')
    
    # --- Initialize components for Routine "countdown" ---
    countdown_3 = visual.TextStim(win=win, name='countdown_3',
        text='3',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    countdown_4 = visual.TextStim(win=win, name='countdown_4',
        text='2',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    countdown_1 = visual.TextStim(win=win, name='countdown_1',
        text='1',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    hljt_go_to_experiment_key = keyboard.Keyboard(deviceName='hljt_go_to_experiment_key')
    
    # --- Initialize components for Routine "ITI" ---
    # Run 'Begin Experiment' code from ITI_code
    # Inter-trial interval (ITI)
    current_iti = 0.8 # placeholder
    iti_index = 0
    ITI_fix_cross = visual.ShapeStim(
        win=win, name='ITI_fix_cross', vertices='cross',
        size=(0.03, 0.03),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    ITI_box_left = visual.Rect(
        win=win, name='ITI_box_left',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    ITI_box_right = visual.Rect(
        win=win, name='ITI_box_right',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    
    # --- Initialize components for Routine "trial" ---
    stimulus = visual.ImageStim(
        win=win,
        name='stimulus', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.45, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    box_left = visual.Rect(
        win=win, name='box_left',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    box_right = visual.Rect(
        win=win, name='box_right',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-4.0, interpolate=True)
    
    # --- Initialize components for Routine "feedback" ---
    feedback_stimulus = visual.ImageStim(
        win=win,
        name='feedback_stimulus', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.45, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    feedback_box_left = visual.Rect(
        win=win, name='feedback_box_left',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    feedback_box_right = visual.Rect(
        win=win, name='feedback_box_right',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    
    # --- Initialize components for Routine "block_end" ---
    # Run 'Begin Experiment' code from block_end_code
    block_end_message = ""
    block_end_main_text = visual.TextStim(win=win, name='block_end_main_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    timer = visual.TextStim(win=win, name='timer',
        text='',
        font='Arial',
        pos=(-0.8, -0.45), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    block_end_adv_text = visual.TextStim(win=win, name='block_end_adv_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    block_end_adv_resp = keyboard.Keyboard(deviceName='block_end_adv_resp')
    
    # --- Initialize components for Routine "bye" ---
    bye_text = visual.TextStim(win=win, name='bye_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "exp_settings" ---
    # create an object to store info about Routine exp_settings
    exp_settings = data.Routine(
        name='exp_settings',
        components=[],
    )
    exp_settings.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for exp_settings
    exp_settings.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    exp_settings.tStart = globalClock.getTime(format='float')
    exp_settings.status = STARTED
    exp_settings.maxDuration = None
    # keep track of which components have finished
    exp_settingsComponents = exp_settings.components
    for thisComponent in exp_settings.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exp_settings" ---
    exp_settings.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=exp_settings,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            exp_settings.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp_settings.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exp_settings" ---
    for thisComponent in exp_settings.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for exp_settings
    exp_settings.tStop = globalClock.getTime(format='float')
    exp_settings.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "exp_settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    load_lg_loop = data.TrialHandler2(
        name='load_lg_loop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('Language_localiser.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(load_lg_loop)  # add the loop to the experiment
    thisLoad_lg_loop = load_lg_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoad_lg_loop.rgb)
    if thisLoad_lg_loop != None:
        for paramName in thisLoad_lg_loop:
            globals()[paramName] = thisLoad_lg_loop[paramName]
    
    for thisLoad_lg_loop in load_lg_loop:
        load_lg_loop.status = STARTED
        if hasattr(thisLoad_lg_loop, 'status'):
            thisLoad_lg_loop.status = STARTED
        currentLoop = load_lg_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisLoad_lg_loop.rgb)
        if thisLoad_lg_loop != None:
            for paramName in thisLoad_lg_loop:
                globals()[paramName] = thisLoad_lg_loop[paramName]
        
        # --- Prepare to start Routine "load_lg" ---
        # create an object to store info about Routine load_lg
        load_lg = data.Routine(
            name='load_lg',
            components=[],
        )
        load_lg.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from update_language_code
        # we put this code at the beginning of the routine.
        # at this point the language has already been selected
        # in the dialogue box by the participant
        
        # now we update the language code based on the
        # language localiser variable ISO_code
        if language == expInfo['language']:
            lang_code = ISO_code  
        
        thisExp.addData("language_code", lang_code)  # add it to output
        
        # this way now lang_code has the value of ISO_code
        # where language in our Excel sheet matches with the
        # language selected by the participant
        # store start times for load_lg
        load_lg.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        load_lg.tStart = globalClock.getTime(format='float')
        load_lg.status = STARTED
        thisExp.addData('load_lg.started', load_lg.tStart)
        load_lg.maxDuration = None
        # keep track of which components have finished
        load_lgComponents = load_lg.components
        for thisComponent in load_lg.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "load_lg" ---
        load_lg.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLoad_lg_loop, 'status') and thisLoad_lg_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=load_lg,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                load_lg.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in load_lg.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "load_lg" ---
        for thisComponent in load_lg.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for load_lg
        load_lg.tStop = globalClock.getTime(format='float')
        load_lg.tStopRefresh = tThisFlipGlobal
        thisExp.addData('load_lg.stopped', load_lg.tStop)
        # the Routine "load_lg" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisLoad_lg_loop as finished
        if hasattr(thisLoad_lg_loop, 'status'):
            thisLoad_lg_loop.status = FINISHED
        # if awaiting a pause, pause now
        if load_lg_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            load_lg_loop.status = STARTED
    # completed 1.0 repeats of 'load_lg_loop'
    load_lg_loop.status = FINISHED
    
    
    # set up handler to look after randomisation of conditions etc
    update_msg_loop = data.TrialHandler2(
        name='update_msg_loop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('Messages.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(update_msg_loop)  # add the loop to the experiment
    thisUpdate_msg_loop = update_msg_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisUpdate_msg_loop.rgb)
    if thisUpdate_msg_loop != None:
        for paramName in thisUpdate_msg_loop:
            globals()[paramName] = thisUpdate_msg_loop[paramName]
    
    for thisUpdate_msg_loop in update_msg_loop:
        update_msg_loop.status = STARTED
        if hasattr(thisUpdate_msg_loop, 'status'):
            thisUpdate_msg_loop.status = STARTED
        currentLoop = update_msg_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisUpdate_msg_loop.rgb)
        if thisUpdate_msg_loop != None:
            for paramName in thisUpdate_msg_loop:
                globals()[paramName] = thisUpdate_msg_loop[paramName]
        
        # --- Prepare to start Routine "update_msg" ---
        # create an object to store info about Routine update_msg
        update_msg = data.Routine(
            name='update_msg',
            components=[],
        )
        update_msg.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from update_messages_code
        ## THIS CODE DOES NOT AUTO-TRANSLATE!!!!
        
        # now that we have selected our new language (lang_code)
        # we can use a loop to iterate over the messages
        # every iteration, we're gonna update the value of our
        # global variables with the value corresponding to the
        # lang_code (ISO_code from the language localiser)
        # this way we don't need to manually specify the text
        
        # this iteration, select the message
        msg_name = message  # e.g. variable "welcome_msg"
        # for this iteration, assign the value based on code
        msg_value = eval(lang_code) # e.g. "Bienvenido" if lang_code = "ES"
        # update message based on code
        globals()[msg_name] = msg_value  # e.g. should update the value of welcome_msg by "Bienvenido"
        # finally we add the values to output just to check
        thisExp.addData("msg_name", msg_name)
        thisExp.addData("msg_value", msg_value)
        # store start times for update_msg
        update_msg.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        update_msg.tStart = globalClock.getTime(format='float')
        update_msg.status = STARTED
        update_msg.maxDuration = None
        # keep track of which components have finished
        update_msgComponents = update_msg.components
        for thisComponent in update_msg.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "update_msg" ---
        update_msg.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisUpdate_msg_loop, 'status') and thisUpdate_msg_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=update_msg,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                update_msg.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in update_msg.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "update_msg" ---
        for thisComponent in update_msg.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for update_msg
        update_msg.tStop = globalClock.getTime(format='float')
        update_msg.tStopRefresh = tThisFlipGlobal
        # the Routine "update_msg" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisUpdate_msg_loop as finished
        if hasattr(thisUpdate_msg_loop, 'status'):
            thisUpdate_msg_loop.status = FINISHED
        # if awaiting a pause, pause now
        if update_msg_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            update_msg_loop.status = STARTED
    # completed 1.0 repeats of 'update_msg_loop'
    update_msg_loop.status = FINISHED
    
    
    # --- Prepare to start Routine "welcome" ---
    # create an object to store info about Routine welcome
    welcome = data.Routine(
        name='welcome',
        components=[welcome_text, adv_resp, hljt_image],
    )
    welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    welcome_text.setText(welcome_msg)
    # create starting attributes for adv_resp
    adv_resp.keys = []
    adv_resp.rt = []
    _adv_resp_allKeys = []
    # store start times for welcome
    welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome.tStart = globalClock.getTime(format='float')
    welcome.status = STARTED
    welcome.maxDuration = None
    # keep track of which components have finished
    welcomeComponents = welcome.components
    for thisComponent in welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome" ---
    welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_text* updates
        
        # if welcome_text is starting this frame...
        if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_text.frameNStart = frameN  # exact frame index
            welcome_text.tStart = t  # local t and not account for scr refresh
            welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            welcome_text.status = STARTED
            welcome_text.setAutoDraw(True)
        
        # if welcome_text is active this frame...
        if welcome_text.status == STARTED:
            # update params
            pass
        
        # *adv_resp* updates
        waitOnFlip = False
        
        # if adv_resp is starting this frame...
        if adv_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            adv_resp.frameNStart = frameN  # exact frame index
            adv_resp.tStart = t  # local t and not account for scr refresh
            adv_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(adv_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'adv_resp.started')
            # update status
            adv_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(adv_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(adv_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if adv_resp.status == STARTED and not waitOnFlip:
            theseKeys = adv_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _adv_resp_allKeys.extend(theseKeys)
            if len(_adv_resp_allKeys):
                adv_resp.keys = _adv_resp_allKeys[-1].name  # just the last key pressed
                adv_resp.rt = _adv_resp_allKeys[-1].rt
                adv_resp.duration = _adv_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *hljt_image* updates
        
        # if hljt_image is starting this frame...
        if hljt_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hljt_image.frameNStart = frameN  # exact frame index
            hljt_image.tStart = t  # local t and not account for scr refresh
            hljt_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hljt_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'hljt_image.started')
            # update status
            hljt_image.status = STARTED
            hljt_image.setAutoDraw(True)
        
        # if hljt_image is active this frame...
        if hljt_image.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=welcome,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome
    welcome.tStop = globalClock.getTime(format='float')
    welcome.tStopRefresh = tThisFlipGlobal
    # check responses
    if adv_resp.keys in ['', [], None]:  # No response was made
        adv_resp.keys = None
    thisExp.addData('adv_resp.keys',adv_resp.keys)
    if adv_resp.keys != None:  # we had a response
        thisExp.addData('adv_resp.rt', adv_resp.rt)
        thisExp.addData('adv_resp.duration', adv_resp.duration)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "demographics" ---
    # create an object to store info about Routine demographics
    demographics = data.Routine(
        name='demographics',
        components=[demographics_title, age_text, age_textbox, gender_text, gender_slider, label_female, label_male, label_transgender, label_nonbinary, label_other, label_prefer_not_say, laterality_text, laterality_slider, label_left, label_ambi, label_right, next_button],
    )
    demographics.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from demo_code
    # make mouse visible
    win.mouseVisible = True
    demographics_title.setText(demographics_msg)
    age_text.setText(age_msg)
    age_textbox.reset()
    age_textbox.setText('')
    gender_text.setText(gender_msg)
    gender_slider.reset()
    label_female.reset()
    label_female.setText(f_msg)
    label_male.reset()
    label_male.setText(m_msg)
    label_transgender.reset()
    label_transgender.setText(tg_msg)
    label_nonbinary.reset()
    label_nonbinary.setText(nb_msg)
    label_other.reset()
    label_other.setText(o_msg)
    label_prefer_not_say.reset()
    label_prefer_not_say.setText(pns_msg)
    laterality_text.setText(laterality_msg)
    laterality_slider.reset()
    label_left.reset()
    label_left.setText(left_msg)
    label_ambi.reset()
    label_ambi.setText(ambi_msg)
    label_right.reset()
    label_right.setText(right_msg)
    next_button.setText(next_msg)
    # reset next_button to account for continued clicks & clear times on/off
    next_button.reset()
    # store start times for demographics
    demographics.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    demographics.tStart = globalClock.getTime(format='float')
    demographics.status = STARTED
    thisExp.addData('demographics.started', demographics.tStart)
    demographics.maxDuration = None
    # keep track of which components have finished
    demographicsComponents = demographics.components
    for thisComponent in demographics.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "demographics" ---
    demographics.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *demographics_title* updates
        
        # if demographics_title is starting this frame...
        if demographics_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            demographics_title.frameNStart = frameN  # exact frame index
            demographics_title.tStart = t  # local t and not account for scr refresh
            demographics_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demographics_title, 'tStartRefresh')  # time at next scr refresh
            # update status
            demographics_title.status = STARTED
            demographics_title.setAutoDraw(True)
        
        # if demographics_title is active this frame...
        if demographics_title.status == STARTED:
            # update params
            pass
        
        # *age_text* updates
        
        # if age_text is starting this frame...
        if age_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            age_text.frameNStart = frameN  # exact frame index
            age_text.tStart = t  # local t and not account for scr refresh
            age_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(age_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            age_text.status = STARTED
            age_text.setAutoDraw(True)
        
        # if age_text is active this frame...
        if age_text.status == STARTED:
            # update params
            pass
        
        # *age_textbox* updates
        
        # if age_textbox is starting this frame...
        if age_textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            age_textbox.frameNStart = frameN  # exact frame index
            age_textbox.tStart = t  # local t and not account for scr refresh
            age_textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(age_textbox, 'tStartRefresh')  # time at next scr refresh
            # update status
            age_textbox.status = STARTED
            age_textbox.setAutoDraw(True)
        
        # if age_textbox is active this frame...
        if age_textbox.status == STARTED:
            # update params
            pass
        
        # *gender_text* updates
        
        # if gender_text is starting this frame...
        if gender_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gender_text.frameNStart = frameN  # exact frame index
            gender_text.tStart = t  # local t and not account for scr refresh
            gender_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gender_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            gender_text.status = STARTED
            gender_text.setAutoDraw(True)
        
        # if gender_text is active this frame...
        if gender_text.status == STARTED:
            # update params
            pass
        
        # *gender_slider* updates
        
        # if gender_slider is starting this frame...
        if gender_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gender_slider.frameNStart = frameN  # exact frame index
            gender_slider.tStart = t  # local t and not account for scr refresh
            gender_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gender_slider, 'tStartRefresh')  # time at next scr refresh
            # update status
            gender_slider.status = STARTED
            gender_slider.setAutoDraw(True)
        
        # if gender_slider is active this frame...
        if gender_slider.status == STARTED:
            # update params
            pass
        
        # *label_female* updates
        
        # if label_female is starting this frame...
        if label_female.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_female.frameNStart = frameN  # exact frame index
            label_female.tStart = t  # local t and not account for scr refresh
            label_female.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_female, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label_female.started')
            # update status
            label_female.status = STARTED
            label_female.setAutoDraw(True)
        
        # if label_female is active this frame...
        if label_female.status == STARTED:
            # update params
            pass
        
        # *label_male* updates
        
        # if label_male is starting this frame...
        if label_male.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_male.frameNStart = frameN  # exact frame index
            label_male.tStart = t  # local t and not account for scr refresh
            label_male.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_male, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label_male.started')
            # update status
            label_male.status = STARTED
            label_male.setAutoDraw(True)
        
        # if label_male is active this frame...
        if label_male.status == STARTED:
            # update params
            pass
        
        # *label_transgender* updates
        
        # if label_transgender is starting this frame...
        if label_transgender.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_transgender.frameNStart = frameN  # exact frame index
            label_transgender.tStart = t  # local t and not account for scr refresh
            label_transgender.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_transgender, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label_transgender.started')
            # update status
            label_transgender.status = STARTED
            label_transgender.setAutoDraw(True)
        
        # if label_transgender is active this frame...
        if label_transgender.status == STARTED:
            # update params
            pass
        
        # *label_nonbinary* updates
        
        # if label_nonbinary is starting this frame...
        if label_nonbinary.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_nonbinary.frameNStart = frameN  # exact frame index
            label_nonbinary.tStart = t  # local t and not account for scr refresh
            label_nonbinary.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_nonbinary, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label_nonbinary.started')
            # update status
            label_nonbinary.status = STARTED
            label_nonbinary.setAutoDraw(True)
        
        # if label_nonbinary is active this frame...
        if label_nonbinary.status == STARTED:
            # update params
            pass
        
        # *label_other* updates
        
        # if label_other is starting this frame...
        if label_other.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_other.frameNStart = frameN  # exact frame index
            label_other.tStart = t  # local t and not account for scr refresh
            label_other.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_other, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label_other.started')
            # update status
            label_other.status = STARTED
            label_other.setAutoDraw(True)
        
        # if label_other is active this frame...
        if label_other.status == STARTED:
            # update params
            pass
        
        # *label_prefer_not_say* updates
        
        # if label_prefer_not_say is starting this frame...
        if label_prefer_not_say.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_prefer_not_say.frameNStart = frameN  # exact frame index
            label_prefer_not_say.tStart = t  # local t and not account for scr refresh
            label_prefer_not_say.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_prefer_not_say, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label_prefer_not_say.started')
            # update status
            label_prefer_not_say.status = STARTED
            label_prefer_not_say.setAutoDraw(True)
        
        # if label_prefer_not_say is active this frame...
        if label_prefer_not_say.status == STARTED:
            # update params
            pass
        
        # *laterality_text* updates
        
        # if laterality_text is starting this frame...
        if laterality_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            laterality_text.frameNStart = frameN  # exact frame index
            laterality_text.tStart = t  # local t and not account for scr refresh
            laterality_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(laterality_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            laterality_text.status = STARTED
            laterality_text.setAutoDraw(True)
        
        # if laterality_text is active this frame...
        if laterality_text.status == STARTED:
            # update params
            pass
        
        # *laterality_slider* updates
        
        # if laterality_slider is starting this frame...
        if laterality_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            laterality_slider.frameNStart = frameN  # exact frame index
            laterality_slider.tStart = t  # local t and not account for scr refresh
            laterality_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(laterality_slider, 'tStartRefresh')  # time at next scr refresh
            # update status
            laterality_slider.status = STARTED
            laterality_slider.setAutoDraw(True)
        
        # if laterality_slider is active this frame...
        if laterality_slider.status == STARTED:
            # update params
            pass
        
        # *label_left* updates
        
        # if label_left is starting this frame...
        if label_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_left.frameNStart = frameN  # exact frame index
            label_left.tStart = t  # local t and not account for scr refresh
            label_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_left, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label_left.started')
            # update status
            label_left.status = STARTED
            label_left.setAutoDraw(True)
        
        # if label_left is active this frame...
        if label_left.status == STARTED:
            # update params
            pass
        
        # *label_ambi* updates
        
        # if label_ambi is starting this frame...
        if label_ambi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_ambi.frameNStart = frameN  # exact frame index
            label_ambi.tStart = t  # local t and not account for scr refresh
            label_ambi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_ambi, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label_ambi.started')
            # update status
            label_ambi.status = STARTED
            label_ambi.setAutoDraw(True)
        
        # if label_ambi is active this frame...
        if label_ambi.status == STARTED:
            # update params
            pass
        
        # *label_right* updates
        
        # if label_right is starting this frame...
        if label_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_right.frameNStart = frameN  # exact frame index
            label_right.tStart = t  # local t and not account for scr refresh
            label_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_right, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label_right.started')
            # update status
            label_right.status = STARTED
            label_right.setAutoDraw(True)
        
        # if label_right is active this frame...
        if label_right.status == STARTED:
            # update params
            pass
        # *next_button* updates
        
        # if next_button is starting this frame...
        if next_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            next_button.frameNStart = frameN  # exact frame index
            next_button.tStart = t  # local t and not account for scr refresh
            next_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'next_button.started')
            # update status
            next_button.status = STARTED
            win.callOnFlip(next_button.buttonClock.reset)
            next_button.setAutoDraw(True)
        
        # if next_button is active this frame...
        if next_button.status == STARTED:
            # update params
            pass
            # check whether next_button has been pressed
            if next_button.isClicked:
                if not next_button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    next_button.timesOn.append(next_button.buttonClock.getTime())
                    next_button.timesOff.append(next_button.buttonClock.getTime())
                elif len(next_button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    next_button.timesOff[-1] = next_button.buttonClock.getTime()
                if not next_button.wasClicked:
                    # end routine when next_button is clicked
                    continueRoutine = False
                if not next_button.wasClicked:
                    # run callback code when next_button is clicked
                    pass
        # take note of whether next_button was clicked, so that next frame we know if clicks are new
        next_button.wasClicked = next_button.isClicked and next_button.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=demographics,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            demographics.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in demographics.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "demographics" ---
    for thisComponent in demographics.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for demographics
    demographics.tStop = globalClock.getTime(format='float')
    demographics.tStopRefresh = tThisFlipGlobal
    thisExp.addData('demographics.stopped', demographics.tStop)
    thisExp.addData('age_textbox.text',age_textbox.text)
    thisExp.addData('gender_slider.response', gender_slider.getRating())
    thisExp.addData('gender_slider.rt', gender_slider.getRT())
    thisExp.addData('laterality_slider.response', laterality_slider.getRating())
    thisExp.addData('laterality_slider.rt', laterality_slider.getRT())
    thisExp.addData('next_button.numClicks', next_button.numClicks)
    if next_button.numClicks:
       thisExp.addData('next_button.timesOn', next_button.timesOn[0])
       thisExp.addData('next_button.timesOff', next_button.timesOff[0])
    else:
       thisExp.addData('next_button.timesOn', "")
       thisExp.addData('next_button.timesOff', "")
    thisExp.nextEntry()
    # the Routine "demographics" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    instructions_loop = data.TrialHandler2(
        name='instructions_loop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(use_i), 
        seed=None, 
    )
    thisExp.addLoop(instructions_loop)  # add the loop to the experiment
    thisInstructions_loop = instructions_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
    if thisInstructions_loop != None:
        for paramName in thisInstructions_loop:
            globals()[paramName] = thisInstructions_loop[paramName]
    
    for thisInstructions_loop in instructions_loop:
        instructions_loop.status = STARTED
        if hasattr(thisInstructions_loop, 'status'):
            thisInstructions_loop.status = STARTED
        currentLoop = instructions_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
        if thisInstructions_loop != None:
            for paramName in thisInstructions_loop:
                globals()[paramName] = thisInstructions_loop[paramName]
        
        # --- Prepare to start Routine "instructions" ---
        # create an object to store info about Routine instructions
        instructions = data.Routine(
            name='instructions',
            components=[inst_text, advance_text, inst_image, inst_adv],
        )
        instructions.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from inst_code
        # hide mouse for the rest of the experiment
        win.mouseVisible = False
        # get column from excel sheet based on language code
        try:
            inst_msg = eval(f"inst_msg_{lang_code}")
        # default to english if this fails
        except ReferenceError:
            inst_msg = inst_msg_EN
        
        # if we are not goint to show feedback in the main
        # task, don't show screen explaining it
        if expInfo["feedback"] == "No feedback" and instructions_loop.thisN == 2:
            continueRoutine = False
        inst_text.setPos((-0.35, 0))
        inst_text.setText(inst_msg)
        advance_text.setText(adv_msg)
        inst_image.setSize((image_w, image_h))
        inst_image.setImage(inst_pics)
        # create starting attributes for inst_adv
        inst_adv.keys = []
        inst_adv.rt = []
        _inst_adv_allKeys = []
        # store start times for instructions
        instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        instructions.tStart = globalClock.getTime(format='float')
        instructions.status = STARTED
        instructions.maxDuration = None
        # keep track of which components have finished
        instructionsComponents = instructions.components
        for thisComponent in instructions.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "instructions" ---
        instructions.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisInstructions_loop, 'status') and thisInstructions_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inst_text* updates
            
            # if inst_text is starting this frame...
            if inst_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inst_text.frameNStart = frameN  # exact frame index
                inst_text.tStart = t  # local t and not account for scr refresh
                inst_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inst_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                inst_text.status = STARTED
                inst_text.setAutoDraw(True)
            
            # if inst_text is active this frame...
            if inst_text.status == STARTED:
                # update params
                pass
            
            # *advance_text* updates
            
            # if advance_text is starting this frame...
            if advance_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                advance_text.frameNStart = frameN  # exact frame index
                advance_text.tStart = t  # local t and not account for scr refresh
                advance_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(advance_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                advance_text.status = STARTED
                advance_text.setAutoDraw(True)
            
            # if advance_text is active this frame...
            if advance_text.status == STARTED:
                # update params
                pass
            
            # *inst_image* updates
            
            # if inst_image is starting this frame...
            if inst_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inst_image.frameNStart = frameN  # exact frame index
                inst_image.tStart = t  # local t and not account for scr refresh
                inst_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inst_image, 'tStartRefresh')  # time at next scr refresh
                # update status
                inst_image.status = STARTED
                inst_image.setAutoDraw(True)
            
            # if inst_image is active this frame...
            if inst_image.status == STARTED:
                # update params
                pass
            
            # *inst_adv* updates
            waitOnFlip = False
            
            # if inst_adv is starting this frame...
            if inst_adv.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inst_adv.frameNStart = frameN  # exact frame index
                inst_adv.tStart = t  # local t and not account for scr refresh
                inst_adv.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inst_adv, 'tStartRefresh')  # time at next scr refresh
                # update status
                inst_adv.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(inst_adv.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(inst_adv.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if inst_adv.status == STARTED and not waitOnFlip:
                theseKeys = inst_adv.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _inst_adv_allKeys.extend(theseKeys)
                if len(_inst_adv_allKeys):
                    inst_adv.keys = _inst_adv_allKeys[-1].name  # just the last key pressed
                    inst_adv.rt = _inst_adv_allKeys[-1].rt
                    inst_adv.duration = _inst_adv_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=instructions,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                instructions.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructions.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "instructions" ---
        for thisComponent in instructions.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for instructions
        instructions.tStop = globalClock.getTime(format='float')
        instructions.tStopRefresh = tThisFlipGlobal
        # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisInstructions_loop as finished
        if hasattr(thisInstructions_loop, 'status'):
            thisInstructions_loop.status = FINISHED
        # if awaiting a pause, pause now
        if instructions_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            instructions_loop.status = STARTED
    # completed 1.0 repeats of 'instructions_loop'
    instructions_loop.status = FINISHED
    
    
    # set up handler to look after randomisation of conditions etc
    blocks_loop = data.TrialHandler2(
        name='blocks_loop',
        nReps=total_blocks, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(blocks_loop)  # add the loop to the experiment
    thisBlocks_loop = blocks_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_loop.rgb)
    if thisBlocks_loop != None:
        for paramName in thisBlocks_loop:
            globals()[paramName] = thisBlocks_loop[paramName]
    
    for thisBlocks_loop in blocks_loop:
        blocks_loop.status = STARTED
        if hasattr(thisBlocks_loop, 'status'):
            thisBlocks_loop.status = STARTED
        currentLoop = blocks_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisBlocks_loop.rgb)
        if thisBlocks_loop != None:
            for paramName in thisBlocks_loop:
                globals()[paramName] = thisBlocks_loop[paramName]
        
        # --- Prepare to start Routine "block_start" ---
        # create an object to store info about Routine block_start
        block_start = data.Routine(
            name='block_start',
            components=[block_number_text, block_start_main_text, block_start_adv_text, block_adv_resp],
        )
        block_start.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from block_start_code
        win.mouseVisible = False
        # start block at 1 and increase every iteration
        block_number += 1
        thisExp.addData("block_number", block_number)
        # set up block messages according to task progress
        # and minimum time for pauses
        if block_number == 1 & pract_block == 1:
            # practice block
            block_message = practice_block_msg
        else:
            # task block
            block_message = task_block_msg
        
        
        
        
        block_number_text.setText(str(block_number) + ' ' + out_of_msg + ' ' + str(total_blocks) + ' ' + blocks_msg)
        block_start_main_text.setText(block_message)
        block_start_adv_text.setText(adv_msg)
        # create starting attributes for block_adv_resp
        block_adv_resp.keys = []
        block_adv_resp.rt = []
        _block_adv_resp_allKeys = []
        # store start times for block_start
        block_start.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        block_start.tStart = globalClock.getTime(format='float')
        block_start.status = STARTED
        thisExp.addData('block_start.started', block_start.tStart)
        block_start.maxDuration = None
        # keep track of which components have finished
        block_startComponents = block_start.components
        for thisComponent in block_start.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "block_start" ---
        block_start.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBlocks_loop, 'status') and thisBlocks_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *block_number_text* updates
            
            # if block_number_text is starting this frame...
            if block_number_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_number_text.frameNStart = frameN  # exact frame index
                block_number_text.tStart = t  # local t and not account for scr refresh
                block_number_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_number_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_number_text.started')
                # update status
                block_number_text.status = STARTED
                block_number_text.setAutoDraw(True)
            
            # if block_number_text is active this frame...
            if block_number_text.status == STARTED:
                # update params
                pass
            
            # *block_start_main_text* updates
            
            # if block_start_main_text is starting this frame...
            if block_start_main_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_start_main_text.frameNStart = frameN  # exact frame index
                block_start_main_text.tStart = t  # local t and not account for scr refresh
                block_start_main_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_start_main_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_start_main_text.started')
                # update status
                block_start_main_text.status = STARTED
                block_start_main_text.setAutoDraw(True)
            
            # if block_start_main_text is active this frame...
            if block_start_main_text.status == STARTED:
                # update params
                pass
            
            # *block_start_adv_text* updates
            
            # if block_start_adv_text is starting this frame...
            if block_start_adv_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                block_start_adv_text.frameNStart = frameN  # exact frame index
                block_start_adv_text.tStart = t  # local t and not account for scr refresh
                block_start_adv_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_start_adv_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                block_start_adv_text.status = STARTED
                block_start_adv_text.setAutoDraw(True)
            
            # if block_start_adv_text is active this frame...
            if block_start_adv_text.status == STARTED:
                # update params
                pass
            
            # *block_adv_resp* updates
            waitOnFlip = False
            
            # if block_adv_resp is starting this frame...
            if block_adv_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                block_adv_resp.frameNStart = frameN  # exact frame index
                block_adv_resp.tStart = t  # local t and not account for scr refresh
                block_adv_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_adv_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_adv_resp.started')
                # update status
                block_adv_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(block_adv_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(block_adv_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if block_adv_resp.status == STARTED and not waitOnFlip:
                theseKeys = block_adv_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _block_adv_resp_allKeys.extend(theseKeys)
                if len(_block_adv_resp_allKeys):
                    block_adv_resp.keys = _block_adv_resp_allKeys[-1].name  # just the last key pressed
                    block_adv_resp.rt = _block_adv_resp_allKeys[-1].rt
                    block_adv_resp.duration = _block_adv_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=block_start,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                block_start.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in block_start.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block_start" ---
        for thisComponent in block_start.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for block_start
        block_start.tStop = globalClock.getTime(format='float')
        block_start.tStopRefresh = tThisFlipGlobal
        thisExp.addData('block_start.stopped', block_start.tStop)
        # check responses
        if block_adv_resp.keys in ['', [], None]:  # No response was made
            block_adv_resp.keys = None
        blocks_loop.addData('block_adv_resp.keys',block_adv_resp.keys)
        if block_adv_resp.keys != None:  # we had a response
            blocks_loop.addData('block_adv_resp.rt', block_adv_resp.rt)
            blocks_loop.addData('block_adv_resp.duration', block_adv_resp.duration)
        # Run 'End Routine' code from block_settings_code
        # change conditions based on block
        # if there is a practice block
        if pract_block == 1:
            if block_number == 1:
                # present block as practice
                block_msg = practice_block_msg
                reps_per_block = 1
            elif block_number > 1: # task blocks
                block_msg = task_block_msg # regular text
                reps_per_block = 2
                # if we want feedback in these blocks
                if task_fb == False:
                    fb = False
        
        # if there is no practice block
        elif pract_block == 0:
            reps_per_block = 2
            block_msg = task_block_msg
            if task_fb == False:
                fb = False
        thisExp.addData("reps_per_block", reps_per_block)
        # the Routine "block_start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "countdown" ---
        # create an object to store info about Routine countdown
        countdown = data.Routine(
            name='countdown',
            components=[countdown_3, countdown_4, countdown_1, hljt_go_to_experiment_key],
        )
        countdown.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for hljt_go_to_experiment_key
        hljt_go_to_experiment_key.keys = []
        hljt_go_to_experiment_key.rt = []
        _hljt_go_to_experiment_key_allKeys = []
        # store start times for countdown
        countdown.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        countdown.tStart = globalClock.getTime(format='float')
        countdown.status = STARTED
        countdown.maxDuration = 3
        # keep track of which components have finished
        countdownComponents = countdown.components
        for thisComponent in countdown.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "countdown" ---
        countdown.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.0:
            # if trial has changed, end Routine now
            if hasattr(thisBlocks_loop, 'status') and thisBlocks_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > countdown.maxDuration-frameTolerance:
                countdown.maxDurationReached = True
                continueRoutine = False
            
            # *countdown_3* updates
            
            # if countdown_3 is starting this frame...
            if countdown_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                countdown_3.frameNStart = frameN  # exact frame index
                countdown_3.tStart = t  # local t and not account for scr refresh
                countdown_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(countdown_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                countdown_3.status = STARTED
                countdown_3.setAutoDraw(True)
            
            # if countdown_3 is active this frame...
            if countdown_3.status == STARTED:
                # update params
                pass
            
            # if countdown_3 is stopping this frame...
            if countdown_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > countdown_3.tStartRefresh + 0.9-frameTolerance:
                    # keep track of stop time/frame for later
                    countdown_3.tStop = t  # not accounting for scr refresh
                    countdown_3.tStopRefresh = tThisFlipGlobal  # on global time
                    countdown_3.frameNStop = frameN  # exact frame index
                    # update status
                    countdown_3.status = FINISHED
                    countdown_3.setAutoDraw(False)
            
            # *countdown_4* updates
            
            # if countdown_4 is starting this frame...
            if countdown_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                countdown_4.frameNStart = frameN  # exact frame index
                countdown_4.tStart = t  # local t and not account for scr refresh
                countdown_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(countdown_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                countdown_4.status = STARTED
                countdown_4.setAutoDraw(True)
            
            # if countdown_4 is active this frame...
            if countdown_4.status == STARTED:
                # update params
                pass
            
            # if countdown_4 is stopping this frame...
            if countdown_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > countdown_4.tStartRefresh + 0.9-frameTolerance:
                    # keep track of stop time/frame for later
                    countdown_4.tStop = t  # not accounting for scr refresh
                    countdown_4.tStopRefresh = tThisFlipGlobal  # on global time
                    countdown_4.frameNStop = frameN  # exact frame index
                    # update status
                    countdown_4.status = FINISHED
                    countdown_4.setAutoDraw(False)
            
            # *countdown_1* updates
            
            # if countdown_1 is starting this frame...
            if countdown_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                countdown_1.frameNStart = frameN  # exact frame index
                countdown_1.tStart = t  # local t and not account for scr refresh
                countdown_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(countdown_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                countdown_1.status = STARTED
                countdown_1.setAutoDraw(True)
            
            # if countdown_1 is active this frame...
            if countdown_1.status == STARTED:
                # update params
                pass
            
            # if countdown_1 is stopping this frame...
            if countdown_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > countdown_1.tStartRefresh + 0.9-frameTolerance:
                    # keep track of stop time/frame for later
                    countdown_1.tStop = t  # not accounting for scr refresh
                    countdown_1.tStopRefresh = tThisFlipGlobal  # on global time
                    countdown_1.frameNStop = frameN  # exact frame index
                    # update status
                    countdown_1.status = FINISHED
                    countdown_1.setAutoDraw(False)
            
            # *hljt_go_to_experiment_key* updates
            waitOnFlip = False
            
            # if hljt_go_to_experiment_key is starting this frame...
            if hljt_go_to_experiment_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hljt_go_to_experiment_key.frameNStart = frameN  # exact frame index
                hljt_go_to_experiment_key.tStart = t  # local t and not account for scr refresh
                hljt_go_to_experiment_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hljt_go_to_experiment_key, 'tStartRefresh')  # time at next scr refresh
                # update status
                hljt_go_to_experiment_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(hljt_go_to_experiment_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(hljt_go_to_experiment_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if hljt_go_to_experiment_key is stopping this frame...
            if hljt_go_to_experiment_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hljt_go_to_experiment_key.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    hljt_go_to_experiment_key.tStop = t  # not accounting for scr refresh
                    hljt_go_to_experiment_key.tStopRefresh = tThisFlipGlobal  # on global time
                    hljt_go_to_experiment_key.frameNStop = frameN  # exact frame index
                    # update status
                    hljt_go_to_experiment_key.status = FINISHED
                    hljt_go_to_experiment_key.status = FINISHED
            if hljt_go_to_experiment_key.status == STARTED and not waitOnFlip:
                theseKeys = hljt_go_to_experiment_key.getKeys(keyList=['space', 'return'], ignoreKeys=["escape"], waitRelease=False)
                _hljt_go_to_experiment_key_allKeys.extend(theseKeys)
                if len(_hljt_go_to_experiment_key_allKeys):
                    hljt_go_to_experiment_key.keys = _hljt_go_to_experiment_key_allKeys[-1].name  # just the last key pressed
                    hljt_go_to_experiment_key.rt = _hljt_go_to_experiment_key_allKeys[-1].rt
                    hljt_go_to_experiment_key.duration = _hljt_go_to_experiment_key_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=countdown,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                countdown.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in countdown.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "countdown" ---
        for thisComponent in countdown.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for countdown
        countdown.tStop = globalClock.getTime(format='float')
        countdown.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if countdown.maxDurationReached:
            routineTimer.addTime(-countdown.maxDuration)
        elif countdown.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        
        # set up handler to look after randomisation of conditions etc
        trials_loop = data.TrialHandler2(
            name='trials_loop',
            nReps=reps_per_block, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(
            trial_conditions, 
            selection='[0,1]'
        )
        , 
            seed=None, 
        )
        thisExp.addLoop(trials_loop)  # add the loop to the experiment
        thisTrials_loop = trials_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
        if thisTrials_loop != None:
            for paramName in thisTrials_loop:
                globals()[paramName] = thisTrials_loop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrials_loop in trials_loop:
            trials_loop.status = STARTED
            if hasattr(thisTrials_loop, 'status'):
                thisTrials_loop.status = STARTED
            currentLoop = trials_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
            if thisTrials_loop != None:
                for paramName in thisTrials_loop:
                    globals()[paramName] = thisTrials_loop[paramName]
            
            # --- Prepare to start Routine "ITI" ---
            # create an object to store info about Routine ITI
            ITI = data.Routine(
                name='ITI',
                components=[ITI_fix_cross, ITI_box_left, ITI_box_right],
            )
            ITI.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from ITI_code
            # obtain current iti through the index
            current_iti = iti_list[iti_index]
            # increase for next trial
            iti_index += 1
            # check if the list has finished
            if iti_index >= len(iti_list):
                iti_index = 0 
            # add to output
            thisExp.addData('ITI', current_iti)
            # store start times for ITI
            ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ITI.tStart = globalClock.getTime(format='float')
            ITI.status = STARTED
            thisExp.addData('ITI.started', ITI.tStart)
            ITI.maxDuration = current_iti
            # keep track of which components have finished
            ITIComponents = ITI.components
            for thisComponent in ITI.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ITI" ---
            ITI.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisTrials_loop, 'status') and thisTrials_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > ITI.maxDuration-frameTolerance:
                    ITI.maxDurationReached = True
                    continueRoutine = False
                
                # *ITI_fix_cross* updates
                
                # if ITI_fix_cross is starting this frame...
                if ITI_fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ITI_fix_cross.frameNStart = frameN  # exact frame index
                    ITI_fix_cross.tStart = t  # local t and not account for scr refresh
                    ITI_fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI_fix_cross, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ITI_fix_cross.status = STARTED
                    ITI_fix_cross.setAutoDraw(True)
                
                # if ITI_fix_cross is active this frame...
                if ITI_fix_cross.status == STARTED:
                    # update params
                    pass
                
                # *ITI_box_left* updates
                
                # if ITI_box_left is starting this frame...
                if ITI_box_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ITI_box_left.frameNStart = frameN  # exact frame index
                    ITI_box_left.tStart = t  # local t and not account for scr refresh
                    ITI_box_left.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI_box_left, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ITI_box_left.status = STARTED
                    ITI_box_left.setAutoDraw(True)
                
                # if ITI_box_left is active this frame...
                if ITI_box_left.status == STARTED:
                    # update params
                    pass
                
                # *ITI_box_right* updates
                
                # if ITI_box_right is starting this frame...
                if ITI_box_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ITI_box_right.frameNStart = frameN  # exact frame index
                    ITI_box_right.tStart = t  # local t and not account for scr refresh
                    ITI_box_right.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI_box_right, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ITI_box_right.status = STARTED
                    ITI_box_right.setAutoDraw(True)
                
                # if ITI_box_right is active this frame...
                if ITI_box_right.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=ITI,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    ITI.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ITI.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ITI" ---
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ITI
            ITI.tStop = globalClock.getTime(format='float')
            ITI.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ITI.stopped', ITI.tStop)
            # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "trial" ---
            # create an object to store info about Routine trial
            trial = data.Routine(
                name='trial',
                components=[stimulus, key_resp, box_left, box_right],
            )
            trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from trial_code
            # column from conditions file to get correct responses
            if expInfo['response_mode'] == "Both hands":
                correct_keys = hljt_correct_both
                resp_keys = ["s", "l"]
            elif expInfo['response_mode'] == "Right hand":
                correct_keys = hljt_correct_one
                resp_keys = ["g", "h"]
            elif expInfo['response_mode'] == "Left hand":
                correct_keys = hljt_correct_one
                resp_keys = ["g", "h"]
            stimulus.setOri(hljt_angle)
            stimulus.setImage(hljt_images)
            # create starting attributes for key_resp
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            # allowedKeys looks like a variable, so make sure it exists locally
            if 'resp_keys' in globals():
                resp_keys = globals()['resp_keys']
            # store start times for trial
            trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial.tStart = globalClock.getTime(format='float')
            trial.status = STARTED
            thisExp.addData('trial.started', trial.tStart)
            trial.maxDuration = None
            # keep track of which components have finished
            trialComponents = trial.components
            for thisComponent in trial.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial" ---
            trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisTrials_loop, 'status') and thisTrials_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *stimulus* updates
                
                # if stimulus is starting this frame...
                if stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stimulus.frameNStart = frameN  # exact frame index
                    stimulus.tStart = t  # local t and not account for scr refresh
                    stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulus.started')
                    # update status
                    stimulus.status = STARTED
                    stimulus.setAutoDraw(True)
                
                # if stimulus is active this frame...
                if stimulus.status == STARTED:
                    # update params
                    pass
                
                # *key_resp* updates
                waitOnFlip = False
                
                # if key_resp is starting this frame...
                if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp.frameNStart = frameN  # exact frame index
                    key_resp.tStart = t  # local t and not account for scr refresh
                    key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.started')
                    # update status
                    key_resp.status = STARTED
                    # allowed keys looks like a variable named `resp_keys`
                    if not type(resp_keys) in [list, tuple, np.ndarray]:
                        if not isinstance(resp_keys, str):
                            resp_keys = str(resp_keys)
                        elif not ',' in resp_keys:
                            resp_keys = (resp_keys,)
                        else:
                            resp_keys = eval(resp_keys)
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp.getKeys(keyList=list(resp_keys), ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_allKeys.extend(theseKeys)
                    if len(_key_resp_allKeys):
                        key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                        key_resp.rt = _key_resp_allKeys[0].rt
                        key_resp.duration = _key_resp_allKeys[0].duration
                        # was this correct?
                        if (key_resp.keys == str(correct_keys)) or (key_resp.keys == correct_keys):
                            key_resp.corr = 1
                        else:
                            key_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *box_left* updates
                
                # if box_left is starting this frame...
                if box_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    box_left.frameNStart = frameN  # exact frame index
                    box_left.tStart = t  # local t and not account for scr refresh
                    box_left.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(box_left, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    box_left.status = STARTED
                    box_left.setAutoDraw(True)
                
                # if box_left is active this frame...
                if box_left.status == STARTED:
                    # update params
                    pass
                
                # *box_right* updates
                
                # if box_right is starting this frame...
                if box_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    box_right.frameNStart = frameN  # exact frame index
                    box_right.tStart = t  # local t and not account for scr refresh
                    box_right.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(box_right, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    box_right.status = STARTED
                    box_right.setAutoDraw(True)
                
                # if box_right is active this frame...
                if box_right.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=trial,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial
            trial.tStop = globalClock.getTime(format='float')
            trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial.stopped', trial.tStop)
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
                # was no response the correct answer?!
                if str(correct_keys).lower() == 'none':
                   key_resp.corr = 1;  # correct non-response
                else:
                   key_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_loop (TrialHandler)
            trials_loop.addData('key_resp.keys',key_resp.keys)
            trials_loop.addData('key_resp.corr', key_resp.corr)
            if key_resp.keys != None:  # we had a response
                trials_loop.addData('key_resp.rt', key_resp.rt)
                trials_loop.addData('key_resp.duration', key_resp.duration)
            # the Routine "trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback" ---
            # create an object to store info about Routine feedback
            feedback = data.Routine(
                name='feedback',
                components=[feedback_stimulus, feedback_box_left, feedback_box_right],
            )
            feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from feedback_code
            if fb == True:
                # If response is correct:
                if key_resp.corr == 1:
                    if correct_keys == hljt_correct_both:
                        if key_resp.keys == "s":
                            fill_left = green
                            fill_right = black
                        elif key_resp.keys == "l":
                            fill_left = black
                            fill_right = green
                    elif correct_keys == hljt_correct_one:
                        if key_resp.keys == "g":
                            fill_left = green
                            fill_right = black
                        elif key_resp.keys == "h":
                            fill_left = black
                            fill_right = green
                #If response is incorrect:
                elif key_resp.corr == 0:
                    if correct_keys == hljt_correct_both:
                        if key_resp.keys == "s":
                            fill_left = red
                            fill_right = black
                        elif key_resp.keys == "l":
                            fill_left = black
                            fill_right = red
                    elif correct_keys == hljt_correct_one:
                        if key_resp.keys == "g":
                            fill_left = red
                            fill_right = black
                        elif key_resp.keys == "h":
                            fill_left = black
                            fill_right = red
            elif fb == False:
                if key_resp.keys in ["s", "g"]:
                    fill_left = white
                    fill_right = black
                elif key_resp.keys in ["h", "l"]:
                    fill_left = black
                    fill_right = white
            feedback_stimulus.setOri(hljt_angle)
            feedback_stimulus.setImage(hljt_images)
            feedback_box_left.setFillColor(fill_left)
            feedback_box_right.setFillColor(fill_right)
            # store start times for feedback
            feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback.tStart = globalClock.getTime(format='float')
            feedback.status = STARTED
            thisExp.addData('feedback.started', feedback.tStart)
            feedback.maxDuration = feedback_time
            # keep track of which components have finished
            feedbackComponents = feedback.components
            for thisComponent in feedback.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback" ---
            feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisTrials_loop, 'status') and thisTrials_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > feedback.maxDuration-frameTolerance:
                    feedback.maxDurationReached = True
                    continueRoutine = False
                
                # *feedback_stimulus* updates
                
                # if feedback_stimulus is starting this frame...
                if feedback_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_stimulus.frameNStart = frameN  # exact frame index
                    feedback_stimulus.tStart = t  # local t and not account for scr refresh
                    feedback_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_stimulus, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_stimulus.started')
                    # update status
                    feedback_stimulus.status = STARTED
                    feedback_stimulus.setAutoDraw(True)
                
                # if feedback_stimulus is active this frame...
                if feedback_stimulus.status == STARTED:
                    # update params
                    pass
                
                # *feedback_box_left* updates
                
                # if feedback_box_left is starting this frame...
                if feedback_box_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_box_left.frameNStart = frameN  # exact frame index
                    feedback_box_left.tStart = t  # local t and not account for scr refresh
                    feedback_box_left.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_box_left, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    feedback_box_left.status = STARTED
                    feedback_box_left.setAutoDraw(True)
                
                # if feedback_box_left is active this frame...
                if feedback_box_left.status == STARTED:
                    # update params
                    pass
                
                # *feedback_box_right* updates
                
                # if feedback_box_right is starting this frame...
                if feedback_box_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_box_right.frameNStart = frameN  # exact frame index
                    feedback_box_right.tStart = t  # local t and not account for scr refresh
                    feedback_box_right.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_box_right, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    feedback_box_right.status = STARTED
                    feedback_box_right.setAutoDraw(True)
                
                # if feedback_box_right is active this frame...
                if feedback_box_right.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=feedback,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    feedback.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback" ---
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback
            feedback.tStop = globalClock.getTime(format='float')
            feedback.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback.stopped', feedback.tStop)
            # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisTrials_loop as finished
            if hasattr(thisTrials_loop, 'status'):
                thisTrials_loop.status = FINISHED
            # if awaiting a pause, pause now
            if trials_loop.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                trials_loop.status = STARTED
            thisExp.nextEntry()
            
        # completed reps_per_block repeats of 'trials_loop'
        trials_loop.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "block_end" ---
        # create an object to store info about Routine block_end
        block_end = data.Routine(
            name='block_end',
            components=[block_end_main_text, timer, block_end_adv_text, block_end_adv_resp],
        )
        block_end.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from block_end_code
        if pract_block and block_number == 1:
            block_end_message = practice_end_msg
        else:
            block_end_message = block_end_msg
        # Run 'Begin Routine' code from timer_code
        # DOES NOT AUTOTRANSLATE!!!!
        # initialize timer
        screen_timer = core.Clock()
        block_end_main_text.setText(block_end_message)
        block_end_adv_text.setText(adv_msg)
        # create starting attributes for block_end_adv_resp
        block_end_adv_resp.keys = []
        block_end_adv_resp.rt = []
        _block_end_adv_resp_allKeys = []
        # store start times for block_end
        block_end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        block_end.tStart = globalClock.getTime(format='float')
        block_end.status = STARTED
        thisExp.addData('block_end.started', block_end.tStart)
        block_end.maxDuration = None
        # keep track of which components have finished
        block_endComponents = block_end.components
        for thisComponent in block_end.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "block_end" ---
        block_end.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBlocks_loop, 'status') and thisBlocks_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from timer_code
            # show timer
            elapsed = screen_timer.getTime()
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            timer_text = f"{minutes:02d}:{seconds:02d}"
            
            # *block_end_main_text* updates
            
            # if block_end_main_text is starting this frame...
            if block_end_main_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_end_main_text.frameNStart = frameN  # exact frame index
                block_end_main_text.tStart = t  # local t and not account for scr refresh
                block_end_main_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_end_main_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_end_main_text.started')
                # update status
                block_end_main_text.status = STARTED
                block_end_main_text.setAutoDraw(True)
            
            # if block_end_main_text is active this frame...
            if block_end_main_text.status == STARTED:
                # update params
                pass
            
            # *timer* updates
            
            # if timer is starting this frame...
            if timer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timer.frameNStart = frameN  # exact frame index
                timer.tStart = t  # local t and not account for scr refresh
                timer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'timer.started')
                # update status
                timer.status = STARTED
                timer.setAutoDraw(True)
            
            # if timer is active this frame...
            if timer.status == STARTED:
                # update params
                timer.setText(timer_text, log=False)
            
            # *block_end_adv_text* updates
            
            # if block_end_adv_text is starting this frame...
            if block_end_adv_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                block_end_adv_text.frameNStart = frameN  # exact frame index
                block_end_adv_text.tStart = t  # local t and not account for scr refresh
                block_end_adv_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_end_adv_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                block_end_adv_text.status = STARTED
                block_end_adv_text.setAutoDraw(True)
            
            # if block_end_adv_text is active this frame...
            if block_end_adv_text.status == STARTED:
                # update params
                pass
            
            # *block_end_adv_resp* updates
            waitOnFlip = False
            
            # if block_end_adv_resp is starting this frame...
            if block_end_adv_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                block_end_adv_resp.frameNStart = frameN  # exact frame index
                block_end_adv_resp.tStart = t  # local t and not account for scr refresh
                block_end_adv_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_end_adv_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_end_adv_resp.started')
                # update status
                block_end_adv_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(block_end_adv_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(block_end_adv_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if block_end_adv_resp.status == STARTED and not waitOnFlip:
                theseKeys = block_end_adv_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _block_end_adv_resp_allKeys.extend(theseKeys)
                if len(_block_end_adv_resp_allKeys):
                    block_end_adv_resp.keys = _block_end_adv_resp_allKeys[-1].name  # just the last key pressed
                    block_end_adv_resp.rt = _block_end_adv_resp_allKeys[-1].rt
                    block_end_adv_resp.duration = _block_end_adv_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=block_end,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                block_end.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in block_end.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block_end" ---
        for thisComponent in block_end.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for block_end
        block_end.tStop = globalClock.getTime(format='float')
        block_end.tStopRefresh = tThisFlipGlobal
        thisExp.addData('block_end.stopped', block_end.tStop)
        # check responses
        if block_end_adv_resp.keys in ['', [], None]:  # No response was made
            block_end_adv_resp.keys = None
        blocks_loop.addData('block_end_adv_resp.keys',block_end_adv_resp.keys)
        if block_end_adv_resp.keys != None:  # we had a response
            blocks_loop.addData('block_end_adv_resp.rt', block_end_adv_resp.rt)
            blocks_loop.addData('block_end_adv_resp.duration', block_end_adv_resp.duration)
        # the Routine "block_end" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisBlocks_loop as finished
        if hasattr(thisBlocks_loop, 'status'):
            thisBlocks_loop.status = FINISHED
        # if awaiting a pause, pause now
        if blocks_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            blocks_loop.status = STARTED
    # completed total_blocks repeats of 'blocks_loop'
    blocks_loop.status = FINISHED
    
    
    # --- Prepare to start Routine "bye" ---
    # create an object to store info about Routine bye
    bye = data.Routine(
        name='bye',
        components=[bye_text],
    )
    bye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    bye_text.setText(bye_msg)
    # store start times for bye
    bye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    bye.tStart = globalClock.getTime(format='float')
    bye.status = STARTED
    thisExp.addData('bye.started', bye.tStart)
    bye.maxDuration = 3
    # keep track of which components have finished
    byeComponents = bye.components
    for thisComponent in bye.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "bye" ---
    bye.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > bye.maxDuration-frameTolerance:
            bye.maxDurationReached = True
            continueRoutine = False
        
        # *bye_text* updates
        
        # if bye_text is starting this frame...
        if bye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bye_text.frameNStart = frameN  # exact frame index
            bye_text.tStart = t  # local t and not account for scr refresh
            bye_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bye_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bye_text.started')
            # update status
            bye_text.status = STARTED
            bye_text.setAutoDraw(True)
        
        # if bye_text is active this frame...
        if bye_text.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=bye,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            bye.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bye.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "bye" ---
    for thisComponent in bye.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for bye
    bye.tStop = globalClock.getTime(format='float')
    bye.tStopRefresh = tThisFlipGlobal
    thisExp.addData('bye.stopped', bye.tStop)
    thisExp.nextEntry()
    # the Routine "bye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
