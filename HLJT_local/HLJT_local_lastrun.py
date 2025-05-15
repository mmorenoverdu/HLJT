#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.1),
    on May 13, 2025, at 11:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2024.2.1')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.1'
expName = 'HLJT_local'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '',
    'language': ["English", "Spanish", "French"],
    'response_mode': ["Both hands", "Right hand", "Left hand"],
    'practice_block': ["Yes", "No"],
    'n_angles': [ "8 (increments of 45º)", "4 (increments of 90º)", "6 (increments of 60º)", "12 (increments of 30º)"],
    'hand_views': ["Palmar and Dorsal", "Palmar", "Dorsal"],
    'n_reps': ["12", "8", "4"],
    'feedback': ["0.3", "0.5", "0.8", "1", "No feedback"],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
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
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\morenoverdu\\OneDrive - UCL\\BAS-Lab\\Project 4 - HLJT\\PyschoPy Experiments\\HLJT_local\\HLJT_local_lastrun.py',
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
            logging.getLevel('exp')
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
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = True
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
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
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('welcome_adv_key') is None:
        # initialise welcome_adv_key
        welcome_adv_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='welcome_adv_key',
        )
    if deviceManager.getDevice('hljt_instr_adv_key') is None:
        # initialise hljt_instr_adv_key
        hljt_instr_adv_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='hljt_instr_adv_key',
        )
    if deviceManager.getDevice('pract_welc_adv') is None:
        # initialise pract_welc_adv
        pract_welc_adv = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='pract_welc_adv',
        )
    if deviceManager.getDevice('hljt_go_to_experiment_key') is None:
        # initialise hljt_go_to_experiment_key
        hljt_go_to_experiment_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='hljt_go_to_experiment_key',
        )
    if deviceManager.getDevice('pract_hljt_response') is None:
        # initialise pract_hljt_response
        pract_hljt_response = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='pract_hljt_response',
        )
    if deviceManager.getDevice('hljt_test_adv_key') is None:
        # initialise hljt_test_adv_key
        hljt_test_adv_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='hljt_test_adv_key',
        )
    if deviceManager.getDevice('test_hljt_response') is None:
        # initialise test_hljt_response
        test_hljt_response = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='test_hljt_response',
        )
    if deviceManager.getDevice('hljt_block_adv_key') is None:
        # initialise hljt_block_adv_key
        hljt_block_adv_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='hljt_block_adv_key',
        )
    if deviceManager.getDevice('Exit') is None:
        # initialise Exit
        Exit = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Exit',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
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
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
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
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
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
    
    # --- Initialize components for Routine "language_settings" ---
    # Run 'Begin Experiment' code from language_settings_code
    # rest of the experiment
    if expInfo["language"] == "English":
        advance = "Press SPACE to continue"
        pract_welc_msg = "You are going to start the practice block\n\n" + advance
    elif expInfo["language"] == "Spanish":
        advance = "Presiona ESPACIO para continuar"
        pract_welc_msg = "Vas a empezar el bloque de práctica\n\n" + advance
    elif expInfo["language"] == "French":
        advance = "Appuyez sur ESPACE pour continuer"
        pract_welc_msg = "Vous allez commencer le bloc de pratique\n\n" + advance
    
    # --- Initialize components for Routine "experiment_settings" ---
    # Run 'Begin Experiment' code from response_mode
    use_i = "" # encodes which Excel file to use
    
    # response mode
    if expInfo['response_mode'] == "Both hands":
        use_i = "hljt_files/Instructions_both_hands.xlsx"
    elif expInfo['response_mode'] == "Right hand":
        use_i = "hljt_files/Instructions_right_hand.xlsx"
    elif expInfo['response_mode'] == "Left hand":
        use_i = "hljt_files/Instructions_left_hand.xlsx"
    # Run 'Begin Experiment' code from number_of_stimuli
    # number of stimuli
    # n_reps sets the number of repetitions per block
    # there are four blocks
    # therefore if n_reps = 1, total = 4, etc.
    n_reps = 1
    
    if expInfo['n_reps'] == "4":
        n_reps = n_reps*1
    elif expInfo['n_reps'] == "8":
        n_reps = n_reps*2
    elif expInfo['n_reps'] == "12":
        n_reps = n_reps*3
    # Run 'Begin Experiment' code from feedback
    # define feedback time
    feedback_time = expInfo["feedback"]
    
    if feedback_time == "No feedback":
        feedback_time = 0
    else:
        feedback_time = float(feedback_time)
    
    # Run 'Begin Experiment' code from practice_block
    if expInfo['practice_block'] == "Yes":
        pract_block = 1
    else:
        pract_block = 0
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
    
    # Definir los parámetros
    n_trials = 600
    block_size = 50
    low_iti_range = (0.6, 1)
    high_prob_range = (0.75, 0.85)
    high_prob_percentage = 0.5  # 50% de los valores entre 750 y 850 ms
    
    # Crear la lista de ITIs
    iti_list = []
    
    for block in range(n_trials // block_size):
        # Para cada bloque de 50 trials:
        n_high_prob = int(block_size * high_prob_percentage)  # Número de ITIs en el rango de alta probabilidad
        n_low_prob = block_size - n_high_prob  # El resto será en el rango general
        
        # Generar ITIs en el rango 750-850
        high_prob_itis = np.random.uniform(low=high_prob_range[0], high=high_prob_range[1], size=n_high_prob)
        
        # Generar ITIs en el rango general (600-1000), excluyendo el rango de 750-850
        low_prob_itis = []
        while len(low_prob_itis) < n_low_prob:
            iti = np.random.uniform(low=low_iti_range[0], high=low_iti_range[1])
            if not (high_prob_range[0] <= iti <= high_prob_range[1]):
                low_prob_itis.append(iti)
        
        # Combinar los ITIs de alta y baja probabilidad
        block_itis = np.concatenate((high_prob_itis, low_prob_itis))
        
        # Mezclar aleatoriamente los ITIs dentro del bloque para evitar orden predecible
        np.random.shuffle(block_itis)
        
        # Agregar el bloque a la lista completa
        iti_list.extend(block_itis)
    
    
    
    # --- Initialize components for Routine "Welcome" ---
    welcome_text1 = visual.TextStim(win=win, name='welcome_text1',
        text=None,
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    welcome_text2 = visual.TextStim(win=win, name='welcome_text2',
        text=None,
        font='Open Sans',
        pos=(0, -0.45), draggable=False, height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    welcome_adv_key = keyboard.Keyboard(deviceName='welcome_adv_key')
    
    # --- Initialize components for Routine "instructions" ---
    # Run 'Begin Experiment' code from hljt_instr_code
    text_position = [-0.35, 0]
    hljt_instr_text = visual.TextStim(win=win, name='hljt_instr_text',
        text=None,
        font='Open Sans',
        pos=[0,0], draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    hljt_instr_image = visual.ImageStim(
        win=win,
        name='hljt_instr_image', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    hljt_instr_adv_text = visual.TextStim(win=win, name='hljt_instr_adv_text',
        text=None,
        font='Open Sans',
        pos=(0, -0.45), draggable=False, height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    hljt_instr_adv_key = keyboard.Keyboard(deviceName='hljt_instr_adv_key')
    
    # --- Initialize components for Routine "pract_welcome" ---
    pract_welc_text = visual.TextStim(win=win, name='pract_welc_text',
        text=pract_welc_msg,
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    pract_welc_adv = keyboard.Keyboard(deviceName='pract_welc_adv')
    
    # --- Initialize components for Routine "countdown" ---
    countdown_3 = visual.TextStim(win=win, name='countdown_3',
        text='3',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    countdown_2 = visual.TextStim(win=win, name='countdown_2',
        text='2',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    countdown_1 = visual.TextStim(win=win, name='countdown_1',
        text='1',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    hljt_go_to_experiment_key = keyboard.Keyboard(deviceName='hljt_go_to_experiment_key')
    
    # --- Initialize components for Routine "ITI" ---
    # Run 'Begin Experiment' code from code_iti
    current_iti = 0.8
    iti_index = 0
    pract_fix_cross_2 = visual.ShapeStim(
        win=win, name='pract_fix_cross_2', vertices='cross',
        size=(0.03, 0.03),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    box_left = visual.Rect(
        win=win, name='box_left',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    box_right = visual.Rect(
        win=win, name='box_right',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    
    # --- Initialize components for Routine "pract_trial" ---
    # Run 'Begin Experiment' code from code
    correct_keys = "" # encodes which column to use from Excel file
    resp_keys = "" # variable to select the keys to be used
    pract_square = visual.Rect(
        win=win, name='pract_square',
        width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    pract_hljt_image = visual.ImageStim(
        win=win,
        name='pract_hljt_image', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.45, 0.45),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    pract_hljt_response = keyboard.Keyboard(deviceName='pract_hljt_response')
    square_left = visual.Rect(
        win=win, name='square_left',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-4.0, interpolate=True)
    square_right = visual.Rect(
        win=win, name='square_right',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-5.0, interpolate=True)
    
    # --- Initialize components for Routine "pract_feedback" ---
    # Run 'Begin Experiment' code from pract_feedback_code
    black = [-1, -1, -1]
    green = [-1, 0.0039, -1]
    red = [1, -1, -1]
    
    fill_left = black
    fill_right = black
    
    feedback_time_pract = feedback_time
    pract_square_2 = visual.Rect(
        win=win, name='pract_square_2',
        width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 1.0000, 1.0000], fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    pract_hljt_image_2 = visual.ImageStim(
        win=win,
        name='pract_hljt_image_2', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.45, 0.45),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    square_left_2 = visual.Rect(
        win=win, name='square_left_2',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    square_right_2 = visual.Rect(
        win=win, name='square_right_2',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    
    # --- Initialize components for Routine "block_welcome" ---
    hljt_test_text = visual.TextStim(win=win, name='hljt_test_text',
        text=None,
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    hljt_test_adv_text = visual.TextStim(win=win, name='hljt_test_adv_text',
        text=None,
        font='Open Sans',
        pos=(0, -0.45), draggable=False, height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    hljt_test_adv_key = keyboard.Keyboard(deviceName='hljt_test_adv_key')
    
    # --- Initialize components for Routine "countdown" ---
    countdown_3 = visual.TextStim(win=win, name='countdown_3',
        text='3',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    countdown_2 = visual.TextStim(win=win, name='countdown_2',
        text='2',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    countdown_1 = visual.TextStim(win=win, name='countdown_1',
        text='1',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    hljt_go_to_experiment_key = keyboard.Keyboard(deviceName='hljt_go_to_experiment_key')
    
    # --- Initialize components for Routine "ITI" ---
    # Run 'Begin Experiment' code from code_iti
    current_iti = 0.8
    iti_index = 0
    pract_fix_cross_2 = visual.ShapeStim(
        win=win, name='pract_fix_cross_2', vertices='cross',
        size=(0.03, 0.03),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    box_left = visual.Rect(
        win=win, name='box_left',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    box_right = visual.Rect(
        win=win, name='box_right',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    
    # --- Initialize components for Routine "test_trial" ---
    test_square = visual.Rect(
        win=win, name='test_square',
        width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    test_hljt_image = visual.ImageStim(
        win=win,
        name='test_hljt_image', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.45, 0.45),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    test_hljt_response = keyboard.Keyboard(deviceName='test_hljt_response')
    square_left_3 = visual.Rect(
        win=win, name='square_left_3',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-4.0, interpolate=True)
    square_right_3 = visual.Rect(
        win=win, name='square_right_3',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-5.0, interpolate=True)
    
    # --- Initialize components for Routine "test_feedback" ---
    test_square_2 = visual.Rect(
        win=win, name='test_square_2',
        width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    test_hljt_image_2 = visual.ImageStim(
        win=win,
        name='test_hljt_image_2', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.45, 0.45),
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    square_left_4 = visual.Rect(
        win=win, name='square_left_4',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    square_right_4 = visual.Rect(
        win=win, name='square_right_4',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    
    # --- Initialize components for Routine "block_pause" ---
    hljt_block_pause_text = visual.TextStim(win=win, name='hljt_block_pause_text',
        text=None,
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    hljt_block_adv_text = visual.TextStim(win=win, name='hljt_block_adv_text',
        text=None,
        font='Open Sans',
        pos=(0, -0.45), draggable=False, height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    hljt_block_adv_key = keyboard.Keyboard(deviceName='hljt_block_adv_key')
    
    # --- Initialize components for Routine "Goodbye" ---
    bye_text = visual.TextStim(win=win, name='bye_text',
        text=None,
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Exit = keyboard.Keyboard(deviceName='Exit')
    
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
    
    # --- Prepare to start Routine "language_settings" ---
    # create an object to store info about Routine language_settings
    language_settings = data.Routine(
        name='language_settings',
        components=[],
    )
    language_settings.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for language_settings
    language_settings.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    language_settings.tStart = globalClock.getTime(format='float')
    language_settings.status = STARTED
    language_settings.maxDuration = None
    # keep track of which components have finished
    language_settingsComponents = language_settings.components
    for thisComponent in language_settings.components:
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
    
    # --- Run Routine "language_settings" ---
    language_settings.forceEnded = routineForceEnded = not continueRoutine
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
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            language_settings.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in language_settings.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "language_settings" ---
    for thisComponent in language_settings.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for language_settings
    language_settings.tStop = globalClock.getTime(format='float')
    language_settings.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "language_settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "experiment_settings" ---
    # create an object to store info about Routine experiment_settings
    experiment_settings = data.Routine(
        name='experiment_settings',
        components=[],
    )
    experiment_settings.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for experiment_settings
    experiment_settings.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    experiment_settings.tStart = globalClock.getTime(format='float')
    experiment_settings.status = STARTED
    experiment_settings.maxDuration = None
    # keep track of which components have finished
    experiment_settingsComponents = experiment_settings.components
    for thisComponent in experiment_settings.components:
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
    
    # --- Run Routine "experiment_settings" ---
    experiment_settings.forceEnded = routineForceEnded = not continueRoutine
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
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            experiment_settings.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experiment_settings.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "experiment_settings" ---
    for thisComponent in experiment_settings.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for experiment_settings
    experiment_settings.tStop = globalClock.getTime(format='float')
    experiment_settings.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "experiment_settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Welcome" ---
    # create an object to store info about Routine Welcome
    Welcome = data.Routine(
        name='Welcome',
        components=[welcome_text1, welcome_text2, welcome_adv_key],
    )
    Welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from welcome_code
    if expInfo["language"] == "English":
        welcome_text1.text = "Welcome to the Hand Laterality Judgement Task!\n\nThe purpose is to quantify your ability to make laterality judgements (right/left) on hand images."
        welcome_text2.text = advance
    elif expInfo["language"] == "Spanish":
        welcome_text1.text = "¡Bienvenid@ a la Tarea de Discriminación de Lateralidad!\n\nEl objetivo es cuantificar tu capacidad para decidir la lateralidad (derecha/izquierda) de imágenes de manos."
        welcome_text2.text = advance
    elif expInfo["language"] == "French":
        welcome_text1.text = "Bienvenue à la Tâche de Jugement de Latéralité de la Main !\n\nLe but est de quantifier votre capacité à décider de la latéralité (droite/gauche) d'images de mains."
        welcome_text2.text = advance
    
    # get Start time and add to data output
    start_time = core.getTime()
    thisExp.addData('start_time', start_time)
    # create starting attributes for welcome_adv_key
    welcome_adv_key.keys = []
    welcome_adv_key.rt = []
    _welcome_adv_key_allKeys = []
    # store start times for Welcome
    Welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Welcome.tStart = globalClock.getTime(format='float')
    Welcome.status = STARTED
    thisExp.addData('Welcome.started', Welcome.tStart)
    Welcome.maxDuration = None
    # keep track of which components have finished
    WelcomeComponents = Welcome.components
    for thisComponent in Welcome.components:
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
    
    # --- Run Routine "Welcome" ---
    Welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_text1* updates
        
        # if welcome_text1 is starting this frame...
        if welcome_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_text1.frameNStart = frameN  # exact frame index
            welcome_text1.tStart = t  # local t and not account for scr refresh
            welcome_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_text1, 'tStartRefresh')  # time at next scr refresh
            # update status
            welcome_text1.status = STARTED
            welcome_text1.setAutoDraw(True)
        
        # if welcome_text1 is active this frame...
        if welcome_text1.status == STARTED:
            # update params
            pass
        
        # *welcome_text2* updates
        
        # if welcome_text2 is starting this frame...
        if welcome_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_text2.frameNStart = frameN  # exact frame index
            welcome_text2.tStart = t  # local t and not account for scr refresh
            welcome_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_text2, 'tStartRefresh')  # time at next scr refresh
            # update status
            welcome_text2.status = STARTED
            welcome_text2.setAutoDraw(True)
        
        # if welcome_text2 is active this frame...
        if welcome_text2.status == STARTED:
            # update params
            pass
        
        # *welcome_adv_key* updates
        waitOnFlip = False
        
        # if welcome_adv_key is starting this frame...
        if welcome_adv_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            welcome_adv_key.frameNStart = frameN  # exact frame index
            welcome_adv_key.tStart = t  # local t and not account for scr refresh
            welcome_adv_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_adv_key, 'tStartRefresh')  # time at next scr refresh
            # update status
            welcome_adv_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(welcome_adv_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(welcome_adv_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if welcome_adv_key.status == STARTED and not waitOnFlip:
            theseKeys = welcome_adv_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _welcome_adv_key_allKeys.extend(theseKeys)
            if len(_welcome_adv_key_allKeys):
                welcome_adv_key.keys = _welcome_adv_key_allKeys[-1].name  # just the last key pressed
                welcome_adv_key.rt = _welcome_adv_key_allKeys[-1].rt
                welcome_adv_key.duration = _welcome_adv_key_allKeys[-1].duration
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
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome" ---
    for thisComponent in Welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Welcome
    Welcome.tStop = globalClock.getTime(format='float')
    Welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Welcome.stopped', Welcome.tStop)
    thisExp.nextEntry()
    # the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
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
            components=[hljt_instr_text, hljt_instr_image, hljt_instr_adv_text, hljt_instr_adv_key],
        )
        instructions.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from hljt_instr_code
        if expInfo["language"] == "English":
            hljt_instr_text.text = instr_msg_en
            hljt_instr_image.image = instr_pics
            hljt_instr_adv_text.text = advance
        elif expInfo["language"] == "Spanish":
            hljt_instr_text.text = instr_msg_es
            hljt_instr_image.image = instr_pics
            hljt_instr_adv_text.text = advance
        elif expInfo["language"] == "French":
            hljt_instr_text.text = instr_msg_fr
            hljt_instr_image.image = instr_pics
            hljt_instr_adv_text.text = advance
        
        # set position of text for last screen
        if expInfo["feedback"] == "No feedback" and instructions_loop.thisN == 2:
            continueRoutine = False
        hljt_instr_text.setPos(text_position)
        hljt_instr_image.setSize([images_sizeW, images_sizeH])
        # create starting attributes for hljt_instr_adv_key
        hljt_instr_adv_key.keys = []
        hljt_instr_adv_key.rt = []
        _hljt_instr_adv_key_allKeys = []
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
        # if trial has changed, end Routine now
        if isinstance(instructions_loop, data.TrialHandler2) and thisInstructions_loop.thisN != instructions_loop.thisTrial.thisN:
            continueRoutine = False
        instructions.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *hljt_instr_text* updates
            
            # if hljt_instr_text is starting this frame...
            if hljt_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hljt_instr_text.frameNStart = frameN  # exact frame index
                hljt_instr_text.tStart = t  # local t and not account for scr refresh
                hljt_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hljt_instr_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                hljt_instr_text.status = STARTED
                hljt_instr_text.setAutoDraw(True)
            
            # if hljt_instr_text is active this frame...
            if hljt_instr_text.status == STARTED:
                # update params
                pass
            
            # *hljt_instr_image* updates
            
            # if hljt_instr_image is starting this frame...
            if hljt_instr_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hljt_instr_image.frameNStart = frameN  # exact frame index
                hljt_instr_image.tStart = t  # local t and not account for scr refresh
                hljt_instr_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hljt_instr_image, 'tStartRefresh')  # time at next scr refresh
                # update status
                hljt_instr_image.status = STARTED
                hljt_instr_image.setAutoDraw(True)
            
            # if hljt_instr_image is active this frame...
            if hljt_instr_image.status == STARTED:
                # update params
                pass
            
            # *hljt_instr_adv_text* updates
            
            # if hljt_instr_adv_text is starting this frame...
            if hljt_instr_adv_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hljt_instr_adv_text.frameNStart = frameN  # exact frame index
                hljt_instr_adv_text.tStart = t  # local t and not account for scr refresh
                hljt_instr_adv_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hljt_instr_adv_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                hljt_instr_adv_text.status = STARTED
                hljt_instr_adv_text.setAutoDraw(True)
            
            # if hljt_instr_adv_text is active this frame...
            if hljt_instr_adv_text.status == STARTED:
                # update params
                pass
            
            # *hljt_instr_adv_key* updates
            waitOnFlip = False
            
            # if hljt_instr_adv_key is starting this frame...
            if hljt_instr_adv_key.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                hljt_instr_adv_key.frameNStart = frameN  # exact frame index
                hljt_instr_adv_key.tStart = t  # local t and not account for scr refresh
                hljt_instr_adv_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hljt_instr_adv_key, 'tStartRefresh')  # time at next scr refresh
                # update status
                hljt_instr_adv_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(hljt_instr_adv_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(hljt_instr_adv_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if hljt_instr_adv_key.status == STARTED and not waitOnFlip:
                theseKeys = hljt_instr_adv_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _hljt_instr_adv_key_allKeys.extend(theseKeys)
                if len(_hljt_instr_adv_key_allKeys):
                    hljt_instr_adv_key.keys = _hljt_instr_adv_key_allKeys[-1].name  # just the last key pressed
                    hljt_instr_adv_key.rt = _hljt_instr_adv_key_allKeys[-1].rt
                    hljt_instr_adv_key.duration = _hljt_instr_adv_key_allKeys[-1].duration
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
                    timers=[routineTimer], 
                    playbackComponents=[]
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
    # completed 1.0 repeats of 'instructions_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    pract_block = data.TrialHandler2(
        name='pract_block',
        nReps=pract_block, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(pract_block)  # add the loop to the experiment
    thisPract_block = pract_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPract_block.rgb)
    if thisPract_block != None:
        for paramName in thisPract_block:
            globals()[paramName] = thisPract_block[paramName]
    
    for thisPract_block in pract_block:
        currentLoop = pract_block
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisPract_block.rgb)
        if thisPract_block != None:
            for paramName in thisPract_block:
                globals()[paramName] = thisPract_block[paramName]
        
        # --- Prepare to start Routine "pract_welcome" ---
        # create an object to store info about Routine pract_welcome
        pract_welcome = data.Routine(
            name='pract_welcome',
            components=[pract_welc_text, pract_welc_adv],
        )
        pract_welcome.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for pract_welc_adv
        pract_welc_adv.keys = []
        pract_welc_adv.rt = []
        _pract_welc_adv_allKeys = []
        # store start times for pract_welcome
        pract_welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        pract_welcome.tStart = globalClock.getTime(format='float')
        pract_welcome.status = STARTED
        pract_welcome.maxDuration = None
        # keep track of which components have finished
        pract_welcomeComponents = pract_welcome.components
        for thisComponent in pract_welcome.components:
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
        
        # --- Run Routine "pract_welcome" ---
        # if trial has changed, end Routine now
        if isinstance(pract_block, data.TrialHandler2) and thisPract_block.thisN != pract_block.thisTrial.thisN:
            continueRoutine = False
        pract_welcome.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pract_welc_text* updates
            
            # if pract_welc_text is starting this frame...
            if pract_welc_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pract_welc_text.frameNStart = frameN  # exact frame index
                pract_welc_text.tStart = t  # local t and not account for scr refresh
                pract_welc_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pract_welc_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                pract_welc_text.status = STARTED
                pract_welc_text.setAutoDraw(True)
            
            # if pract_welc_text is active this frame...
            if pract_welc_text.status == STARTED:
                # update params
                pass
            
            # *pract_welc_adv* updates
            waitOnFlip = False
            
            # if pract_welc_adv is starting this frame...
            if pract_welc_adv.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                pract_welc_adv.frameNStart = frameN  # exact frame index
                pract_welc_adv.tStart = t  # local t and not account for scr refresh
                pract_welc_adv.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pract_welc_adv, 'tStartRefresh')  # time at next scr refresh
                # update status
                pract_welc_adv.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(pract_welc_adv.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(pract_welc_adv.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if pract_welc_adv.status == STARTED and not waitOnFlip:
                theseKeys = pract_welc_adv.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _pract_welc_adv_allKeys.extend(theseKeys)
                if len(_pract_welc_adv_allKeys):
                    pract_welc_adv.keys = _pract_welc_adv_allKeys[-1].name  # just the last key pressed
                    pract_welc_adv.rt = _pract_welc_adv_allKeys[-1].rt
                    pract_welc_adv.duration = _pract_welc_adv_allKeys[-1].duration
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
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                pract_welcome.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pract_welcome.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pract_welcome" ---
        for thisComponent in pract_welcome.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for pract_welcome
        pract_welcome.tStop = globalClock.getTime(format='float')
        pract_welcome.tStopRefresh = tThisFlipGlobal
        # the Routine "pract_welcome" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "countdown" ---
        # create an object to store info about Routine countdown
        countdown = data.Routine(
            name='countdown',
            components=[countdown_3, countdown_2, countdown_1, hljt_go_to_experiment_key],
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
        # if trial has changed, end Routine now
        if isinstance(pract_block, data.TrialHandler2) and thisPract_block.thisN != pract_block.thisTrial.thisN:
            continueRoutine = False
        countdown.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.0:
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
            
            # *countdown_2* updates
            
            # if countdown_2 is starting this frame...
            if countdown_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                countdown_2.frameNStart = frameN  # exact frame index
                countdown_2.tStart = t  # local t and not account for scr refresh
                countdown_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(countdown_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                countdown_2.status = STARTED
                countdown_2.setAutoDraw(True)
            
            # if countdown_2 is active this frame...
            if countdown_2.status == STARTED:
                # update params
                pass
            
            # if countdown_2 is stopping this frame...
            if countdown_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > countdown_2.tStartRefresh + 0.9-frameTolerance:
                    # keep track of stop time/frame for later
                    countdown_2.tStop = t  # not accounting for scr refresh
                    countdown_2.tStopRefresh = tThisFlipGlobal  # on global time
                    countdown_2.frameNStop = frameN  # exact frame index
                    # update status
                    countdown_2.status = FINISHED
                    countdown_2.setAutoDraw(False)
            
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
                    timers=[routineTimer], 
                    playbackComponents=[]
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
        pract_loop = data.TrialHandler2(
            name='pract_loop',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(trial_conditions), 
            seed=None, 
        )
        thisExp.addLoop(pract_loop)  # add the loop to the experiment
        thisPract_loop = pract_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPract_loop.rgb)
        if thisPract_loop != None:
            for paramName in thisPract_loop:
                globals()[paramName] = thisPract_loop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisPract_loop in pract_loop:
            currentLoop = pract_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisPract_loop.rgb)
            if thisPract_loop != None:
                for paramName in thisPract_loop:
                    globals()[paramName] = thisPract_loop[paramName]
            
            # --- Prepare to start Routine "ITI" ---
            # create an object to store info about Routine ITI
            ITI = data.Routine(
                name='ITI',
                components=[pract_fix_cross_2, box_left, box_right],
            )
            ITI.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_iti
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
            # if trial has changed, end Routine now
            if isinstance(pract_loop, data.TrialHandler2) and thisPract_loop.thisN != pract_loop.thisTrial.thisN:
                continueRoutine = False
            ITI.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
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
                
                # *pract_fix_cross_2* updates
                
                # if pract_fix_cross_2 is starting this frame...
                if pract_fix_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pract_fix_cross_2.frameNStart = frameN  # exact frame index
                    pract_fix_cross_2.tStart = t  # local t and not account for scr refresh
                    pract_fix_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pract_fix_cross_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    pract_fix_cross_2.status = STARTED
                    pract_fix_cross_2.setAutoDraw(True)
                
                # if pract_fix_cross_2 is active this frame...
                if pract_fix_cross_2.status == STARTED:
                    # update params
                    pass
                
                # if pract_fix_cross_2 is stopping this frame...
                if pract_fix_cross_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > pract_fix_cross_2.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        pract_fix_cross_2.tStop = t  # not accounting for scr refresh
                        pract_fix_cross_2.tStopRefresh = tThisFlipGlobal  # on global time
                        pract_fix_cross_2.frameNStop = frameN  # exact frame index
                        # update status
                        pract_fix_cross_2.status = FINISHED
                        pract_fix_cross_2.setAutoDraw(False)
                
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
                        timers=[routineTimer], 
                        playbackComponents=[]
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
            # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "pract_trial" ---
            # create an object to store info about Routine pract_trial
            pract_trial = data.Routine(
                name='pract_trial',
                components=[pract_square, pract_hljt_image, pract_hljt_response, square_left, square_right],
            )
            pract_trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code
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
            pract_hljt_image.setOri(hljt_angle)
            pract_hljt_image.setImage(hljt_images)
            # create starting attributes for pract_hljt_response
            pract_hljt_response.keys = []
            pract_hljt_response.rt = []
            _pract_hljt_response_allKeys = []
            # allowedKeys looks like a variable, so make sure it exists locally
            if 'resp_keys' in globals():
                resp_keys = globals()['resp_keys']
            # store start times for pract_trial
            pract_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            pract_trial.tStart = globalClock.getTime(format='float')
            pract_trial.status = STARTED
            pract_trial.maxDuration = None
            # keep track of which components have finished
            pract_trialComponents = pract_trial.components
            for thisComponent in pract_trial.components:
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
            
            # --- Run Routine "pract_trial" ---
            # if trial has changed, end Routine now
            if isinstance(pract_loop, data.TrialHandler2) and thisPract_loop.thisN != pract_loop.thisTrial.thisN:
                continueRoutine = False
            pract_trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *pract_square* updates
                
                # if pract_square is starting this frame...
                if pract_square.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    pract_square.frameNStart = frameN  # exact frame index
                    pract_square.tStart = t  # local t and not account for scr refresh
                    pract_square.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pract_square, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    pract_square.status = STARTED
                    pract_square.setAutoDraw(True)
                
                # if pract_square is active this frame...
                if pract_square.status == STARTED:
                    # update params
                    pass
                
                # *pract_hljt_image* updates
                
                # if pract_hljt_image is starting this frame...
                if pract_hljt_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    pract_hljt_image.frameNStart = frameN  # exact frame index
                    pract_hljt_image.tStart = t  # local t and not account for scr refresh
                    pract_hljt_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pract_hljt_image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pract_hljt_image.started')
                    # update status
                    pract_hljt_image.status = STARTED
                    pract_hljt_image.setAutoDraw(True)
                
                # if pract_hljt_image is active this frame...
                if pract_hljt_image.status == STARTED:
                    # update params
                    pass
                
                # *pract_hljt_response* updates
                waitOnFlip = False
                
                # if pract_hljt_response is starting this frame...
                if pract_hljt_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    pract_hljt_response.frameNStart = frameN  # exact frame index
                    pract_hljt_response.tStart = t  # local t and not account for scr refresh
                    pract_hljt_response.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pract_hljt_response, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pract_hljt_response.started')
                    # update status
                    pract_hljt_response.status = STARTED
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
                    win.callOnFlip(pract_hljt_response.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(pract_hljt_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if pract_hljt_response.status == STARTED and not waitOnFlip:
                    theseKeys = pract_hljt_response.getKeys(keyList=list(resp_keys), ignoreKeys=["escape"], waitRelease=False)
                    _pract_hljt_response_allKeys.extend(theseKeys)
                    if len(_pract_hljt_response_allKeys):
                        pract_hljt_response.keys = _pract_hljt_response_allKeys[0].name  # just the first key pressed
                        pract_hljt_response.rt = _pract_hljt_response_allKeys[0].rt
                        pract_hljt_response.duration = _pract_hljt_response_allKeys[0].duration
                        # was this correct?
                        if (pract_hljt_response.keys == str(correct_keys)) or (pract_hljt_response.keys == correct_keys):
                            pract_hljt_response.corr = 1
                        else:
                            pract_hljt_response.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *square_left* updates
                
                # if square_left is starting this frame...
                if square_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    square_left.frameNStart = frameN  # exact frame index
                    square_left.tStart = t  # local t and not account for scr refresh
                    square_left.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(square_left, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    square_left.status = STARTED
                    square_left.setAutoDraw(True)
                
                # if square_left is active this frame...
                if square_left.status == STARTED:
                    # update params
                    pass
                
                # *square_right* updates
                
                # if square_right is starting this frame...
                if square_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    square_right.frameNStart = frameN  # exact frame index
                    square_right.tStart = t  # local t and not account for scr refresh
                    square_right.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(square_right, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    square_right.status = STARTED
                    square_right.setAutoDraw(True)
                
                # if square_right is active this frame...
                if square_right.status == STARTED:
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
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    pract_trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pract_trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pract_trial" ---
            for thisComponent in pract_trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for pract_trial
            pract_trial.tStop = globalClock.getTime(format='float')
            pract_trial.tStopRefresh = tThisFlipGlobal
            # check responses
            if pract_hljt_response.keys in ['', [], None]:  # No response was made
                pract_hljt_response.keys = None
                # was no response the correct answer?!
                if str(correct_keys).lower() == 'none':
                   pract_hljt_response.corr = 1;  # correct non-response
                else:
                   pract_hljt_response.corr = 0;  # failed to respond (incorrectly)
            # store data for pract_loop (TrialHandler)
            pract_loop.addData('pract_hljt_response.keys',pract_hljt_response.keys)
            pract_loop.addData('pract_hljt_response.corr', pract_hljt_response.corr)
            if pract_hljt_response.keys != None:  # we had a response
                pract_loop.addData('pract_hljt_response.rt', pract_hljt_response.rt)
                pract_loop.addData('pract_hljt_response.duration', pract_hljt_response.duration)
            # the Routine "pract_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "pract_feedback" ---
            # create an object to store info about Routine pract_feedback
            pract_feedback = data.Routine(
                name='pract_feedback',
                components=[pract_square_2, pract_hljt_image_2, square_left_2, square_right_2],
            )
            pract_feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from pract_feedback_code
            # set feedback even feedback_time == 0
            if feedback_time == 0:
                feedback_time_pract = 0.3
            else:
                feedback_time_pract = feedback_time
            
            # If response is correct:
            if pract_hljt_response.corr == 1:
                if correct_keys == hljt_correct_both:
                    if pract_hljt_response.keys == "s":
                        fill_left = green
                        fill_right = black
                    elif pract_hljt_response.keys == "l":
                        fill_left = black
                        fill_right = green
                elif correct_keys == hljt_correct_one:
                    if pract_hljt_response.keys == "g":
                        fill_left = green
                        fill_right = black
                    elif pract_hljt_response.keys == "h":
                        fill_left = black
                        fill_right = green
            
            #If response is incorrect:
            if pract_hljt_response.corr == 0:
                if correct_keys == hljt_correct_both:
                    if pract_hljt_response.keys == "s":
                        fill_left = red
                        fill_right = black
                    elif pract_hljt_response.keys == "l":
                        fill_left = black
                        fill_right = red
                elif correct_keys == hljt_correct_one:
                    if pract_hljt_response.keys == "g":
                        fill_left = red
                        fill_right = black
                    elif pract_hljt_response.keys == "h":
                        fill_left = black
                        fill_right = red
            pract_hljt_image_2.setOri(hljt_angle)
            pract_hljt_image_2.setImage(hljt_images)
            square_left_2.setFillColor(fill_left)
            square_left_2.setLineColor(fill_left)
            square_right_2.setFillColor(fill_right)
            square_right_2.setLineColor(fill_right)
            # store start times for pract_feedback
            pract_feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            pract_feedback.tStart = globalClock.getTime(format='float')
            pract_feedback.status = STARTED
            pract_feedback.maxDuration = feedback_time_pract
            # keep track of which components have finished
            pract_feedbackComponents = pract_feedback.components
            for thisComponent in pract_feedback.components:
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
            
            # --- Run Routine "pract_feedback" ---
            # if trial has changed, end Routine now
            if isinstance(pract_loop, data.TrialHandler2) and thisPract_loop.thisN != pract_loop.thisTrial.thisN:
                continueRoutine = False
            pract_feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > pract_feedback.maxDuration-frameTolerance:
                    pract_feedback.maxDurationReached = True
                    continueRoutine = False
                
                # *pract_square_2* updates
                
                # if pract_square_2 is starting this frame...
                if pract_square_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    pract_square_2.frameNStart = frameN  # exact frame index
                    pract_square_2.tStart = t  # local t and not account for scr refresh
                    pract_square_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pract_square_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    pract_square_2.status = STARTED
                    pract_square_2.setAutoDraw(True)
                
                # if pract_square_2 is active this frame...
                if pract_square_2.status == STARTED:
                    # update params
                    pass
                
                # *pract_hljt_image_2* updates
                
                # if pract_hljt_image_2 is starting this frame...
                if pract_hljt_image_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    pract_hljt_image_2.frameNStart = frameN  # exact frame index
                    pract_hljt_image_2.tStart = t  # local t and not account for scr refresh
                    pract_hljt_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pract_hljt_image_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    pract_hljt_image_2.status = STARTED
                    pract_hljt_image_2.setAutoDraw(True)
                
                # if pract_hljt_image_2 is active this frame...
                if pract_hljt_image_2.status == STARTED:
                    # update params
                    pass
                
                # *square_left_2* updates
                
                # if square_left_2 is starting this frame...
                if square_left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    square_left_2.frameNStart = frameN  # exact frame index
                    square_left_2.tStart = t  # local t and not account for scr refresh
                    square_left_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(square_left_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    square_left_2.status = STARTED
                    square_left_2.setAutoDraw(True)
                
                # if square_left_2 is active this frame...
                if square_left_2.status == STARTED:
                    # update params
                    pass
                
                # *square_right_2* updates
                
                # if square_right_2 is starting this frame...
                if square_right_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    square_right_2.frameNStart = frameN  # exact frame index
                    square_right_2.tStart = t  # local t and not account for scr refresh
                    square_right_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(square_right_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    square_right_2.status = STARTED
                    square_right_2.setAutoDraw(True)
                
                # if square_right_2 is active this frame...
                if square_right_2.status == STARTED:
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
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    pract_feedback.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pract_feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pract_feedback" ---
            for thisComponent in pract_feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for pract_feedback
            pract_feedback.tStop = globalClock.getTime(format='float')
            pract_feedback.tStopRefresh = tThisFlipGlobal
            # the Routine "pract_feedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'pract_loop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed pract_block repeats of 'pract_block'
    
    
    # set up handler to look after randomisation of conditions etc
    test_block = data.TrialHandler2(
        name='test_block',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('hljt_files/Block_messages.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(test_block)  # add the loop to the experiment
    thisTest_block = test_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTest_block.rgb)
    if thisTest_block != None:
        for paramName in thisTest_block:
            globals()[paramName] = thisTest_block[paramName]
    
    for thisTest_block in test_block:
        currentLoop = test_block
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisTest_block.rgb)
        if thisTest_block != None:
            for paramName in thisTest_block:
                globals()[paramName] = thisTest_block[paramName]
        
        # --- Prepare to start Routine "block_welcome" ---
        # create an object to store info about Routine block_welcome
        block_welcome = data.Routine(
            name='block_welcome',
            components=[hljt_test_text, hljt_test_adv_text, hljt_test_adv_key],
        )
        block_welcome.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from test_code_2
        if expInfo["language"] == "English":
            hljt_test_text.text = test_msg_en
            hljt_test_adv_text.text = advance
        elif expInfo["language"] == "Spanish":
            hljt_test_text.text = test_msg_es
            hljt_test_adv_text.text = advance
        elif expInfo["language"] == "French":
            hljt_test_text.text = test_msg_fr
            hljt_test_adv_text.text = advance
        
        
        # create starting attributes for hljt_test_adv_key
        hljt_test_adv_key.keys = []
        hljt_test_adv_key.rt = []
        _hljt_test_adv_key_allKeys = []
        # store start times for block_welcome
        block_welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        block_welcome.tStart = globalClock.getTime(format='float')
        block_welcome.status = STARTED
        thisExp.addData('block_welcome.started', block_welcome.tStart)
        block_welcome.maxDuration = None
        # keep track of which components have finished
        block_welcomeComponents = block_welcome.components
        for thisComponent in block_welcome.components:
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
        
        # --- Run Routine "block_welcome" ---
        # if trial has changed, end Routine now
        if isinstance(test_block, data.TrialHandler2) and thisTest_block.thisN != test_block.thisTrial.thisN:
            continueRoutine = False
        block_welcome.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *hljt_test_text* updates
            
            # if hljt_test_text is starting this frame...
            if hljt_test_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hljt_test_text.frameNStart = frameN  # exact frame index
                hljt_test_text.tStart = t  # local t and not account for scr refresh
                hljt_test_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hljt_test_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                hljt_test_text.status = STARTED
                hljt_test_text.setAutoDraw(True)
            
            # if hljt_test_text is active this frame...
            if hljt_test_text.status == STARTED:
                # update params
                pass
            
            # *hljt_test_adv_text* updates
            
            # if hljt_test_adv_text is starting this frame...
            if hljt_test_adv_text.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                hljt_test_adv_text.frameNStart = frameN  # exact frame index
                hljt_test_adv_text.tStart = t  # local t and not account for scr refresh
                hljt_test_adv_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hljt_test_adv_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                hljt_test_adv_text.status = STARTED
                hljt_test_adv_text.setAutoDraw(True)
            
            # if hljt_test_adv_text is active this frame...
            if hljt_test_adv_text.status == STARTED:
                # update params
                pass
            
            # *hljt_test_adv_key* updates
            waitOnFlip = False
            
            # if hljt_test_adv_key is starting this frame...
            if hljt_test_adv_key.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                hljt_test_adv_key.frameNStart = frameN  # exact frame index
                hljt_test_adv_key.tStart = t  # local t and not account for scr refresh
                hljt_test_adv_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hljt_test_adv_key, 'tStartRefresh')  # time at next scr refresh
                # update status
                hljt_test_adv_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(hljt_test_adv_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(hljt_test_adv_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if hljt_test_adv_key.status == STARTED and not waitOnFlip:
                theseKeys = hljt_test_adv_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _hljt_test_adv_key_allKeys.extend(theseKeys)
                if len(_hljt_test_adv_key_allKeys):
                    hljt_test_adv_key.keys = _hljt_test_adv_key_allKeys[-1].name  # just the last key pressed
                    hljt_test_adv_key.rt = _hljt_test_adv_key_allKeys[-1].rt
                    hljt_test_adv_key.duration = _hljt_test_adv_key_allKeys[-1].duration
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
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                block_welcome.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in block_welcome.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block_welcome" ---
        for thisComponent in block_welcome.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for block_welcome
        block_welcome.tStop = globalClock.getTime(format='float')
        block_welcome.tStopRefresh = tThisFlipGlobal
        thisExp.addData('block_welcome.stopped', block_welcome.tStop)
        # the Routine "block_welcome" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "countdown" ---
        # create an object to store info about Routine countdown
        countdown = data.Routine(
            name='countdown',
            components=[countdown_3, countdown_2, countdown_1, hljt_go_to_experiment_key],
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
        # if trial has changed, end Routine now
        if isinstance(test_block, data.TrialHandler2) and thisTest_block.thisN != test_block.thisTrial.thisN:
            continueRoutine = False
        countdown.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.0:
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
            
            # *countdown_2* updates
            
            # if countdown_2 is starting this frame...
            if countdown_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                countdown_2.frameNStart = frameN  # exact frame index
                countdown_2.tStart = t  # local t and not account for scr refresh
                countdown_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(countdown_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                countdown_2.status = STARTED
                countdown_2.setAutoDraw(True)
            
            # if countdown_2 is active this frame...
            if countdown_2.status == STARTED:
                # update params
                pass
            
            # if countdown_2 is stopping this frame...
            if countdown_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > countdown_2.tStartRefresh + 0.9-frameTolerance:
                    # keep track of stop time/frame for later
                    countdown_2.tStop = t  # not accounting for scr refresh
                    countdown_2.tStopRefresh = tThisFlipGlobal  # on global time
                    countdown_2.frameNStop = frameN  # exact frame index
                    # update status
                    countdown_2.status = FINISHED
                    countdown_2.setAutoDraw(False)
            
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
                    timers=[routineTimer], 
                    playbackComponents=[]
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
        test_trial_loop = data.TrialHandler2(
            name='test_trial_loop',
            nReps=n_reps, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(trial_conditions), 
            seed=None, 
        )
        thisExp.addLoop(test_trial_loop)  # add the loop to the experiment
        thisTest_trial_loop = test_trial_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTest_trial_loop.rgb)
        if thisTest_trial_loop != None:
            for paramName in thisTest_trial_loop:
                globals()[paramName] = thisTest_trial_loop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTest_trial_loop in test_trial_loop:
            currentLoop = test_trial_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTest_trial_loop.rgb)
            if thisTest_trial_loop != None:
                for paramName in thisTest_trial_loop:
                    globals()[paramName] = thisTest_trial_loop[paramName]
            
            # --- Prepare to start Routine "ITI" ---
            # create an object to store info about Routine ITI
            ITI = data.Routine(
                name='ITI',
                components=[pract_fix_cross_2, box_left, box_right],
            )
            ITI.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_iti
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
            # if trial has changed, end Routine now
            if isinstance(test_trial_loop, data.TrialHandler2) and thisTest_trial_loop.thisN != test_trial_loop.thisTrial.thisN:
                continueRoutine = False
            ITI.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
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
                
                # *pract_fix_cross_2* updates
                
                # if pract_fix_cross_2 is starting this frame...
                if pract_fix_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    pract_fix_cross_2.frameNStart = frameN  # exact frame index
                    pract_fix_cross_2.tStart = t  # local t and not account for scr refresh
                    pract_fix_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pract_fix_cross_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    pract_fix_cross_2.status = STARTED
                    pract_fix_cross_2.setAutoDraw(True)
                
                # if pract_fix_cross_2 is active this frame...
                if pract_fix_cross_2.status == STARTED:
                    # update params
                    pass
                
                # if pract_fix_cross_2 is stopping this frame...
                if pract_fix_cross_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > pract_fix_cross_2.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        pract_fix_cross_2.tStop = t  # not accounting for scr refresh
                        pract_fix_cross_2.tStopRefresh = tThisFlipGlobal  # on global time
                        pract_fix_cross_2.frameNStop = frameN  # exact frame index
                        # update status
                        pract_fix_cross_2.status = FINISHED
                        pract_fix_cross_2.setAutoDraw(False)
                
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
                        timers=[routineTimer], 
                        playbackComponents=[]
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
            # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "test_trial" ---
            # create an object to store info about Routine test_trial
            test_trial = data.Routine(
                name='test_trial',
                components=[test_square, test_hljt_image, test_hljt_response, square_left_3, square_right_3],
            )
            test_trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_2
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
            test_hljt_image.setOri(hljt_angle)
            test_hljt_image.setImage(hljt_images)
            # create starting attributes for test_hljt_response
            test_hljt_response.keys = []
            test_hljt_response.rt = []
            _test_hljt_response_allKeys = []
            # allowedKeys looks like a variable, so make sure it exists locally
            if 'resp_keys' in globals():
                resp_keys = globals()['resp_keys']
            # store start times for test_trial
            test_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            test_trial.tStart = globalClock.getTime(format='float')
            test_trial.status = STARTED
            thisExp.addData('test_trial.started', test_trial.tStart)
            test_trial.maxDuration = None
            # keep track of which components have finished
            test_trialComponents = test_trial.components
            for thisComponent in test_trial.components:
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
            
            # --- Run Routine "test_trial" ---
            # if trial has changed, end Routine now
            if isinstance(test_trial_loop, data.TrialHandler2) and thisTest_trial_loop.thisN != test_trial_loop.thisTrial.thisN:
                continueRoutine = False
            test_trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *test_square* updates
                
                # if test_square is starting this frame...
                if test_square.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    test_square.frameNStart = frameN  # exact frame index
                    test_square.tStart = t  # local t and not account for scr refresh
                    test_square.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(test_square, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'test_square.started')
                    # update status
                    test_square.status = STARTED
                    test_square.setAutoDraw(True)
                
                # if test_square is active this frame...
                if test_square.status == STARTED:
                    # update params
                    pass
                
                # *test_hljt_image* updates
                
                # if test_hljt_image is starting this frame...
                if test_hljt_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    test_hljt_image.frameNStart = frameN  # exact frame index
                    test_hljt_image.tStart = t  # local t and not account for scr refresh
                    test_hljt_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(test_hljt_image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'test_hljt_image.started')
                    # update status
                    test_hljt_image.status = STARTED
                    test_hljt_image.setAutoDraw(True)
                
                # if test_hljt_image is active this frame...
                if test_hljt_image.status == STARTED:
                    # update params
                    pass
                
                # *test_hljt_response* updates
                waitOnFlip = False
                
                # if test_hljt_response is starting this frame...
                if test_hljt_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    test_hljt_response.frameNStart = frameN  # exact frame index
                    test_hljt_response.tStart = t  # local t and not account for scr refresh
                    test_hljt_response.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(test_hljt_response, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'test_hljt_response.started')
                    # update status
                    test_hljt_response.status = STARTED
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
                    win.callOnFlip(test_hljt_response.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(test_hljt_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if test_hljt_response.status == STARTED and not waitOnFlip:
                    theseKeys = test_hljt_response.getKeys(keyList=list(resp_keys), ignoreKeys=["escape"], waitRelease=False)
                    _test_hljt_response_allKeys.extend(theseKeys)
                    if len(_test_hljt_response_allKeys):
                        test_hljt_response.keys = _test_hljt_response_allKeys[0].name  # just the first key pressed
                        test_hljt_response.rt = _test_hljt_response_allKeys[0].rt
                        test_hljt_response.duration = _test_hljt_response_allKeys[0].duration
                        # was this correct?
                        if (test_hljt_response.keys == str(correct_keys)) or (test_hljt_response.keys == correct_keys):
                            test_hljt_response.corr = 1
                        else:
                            test_hljt_response.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *square_left_3* updates
                
                # if square_left_3 is starting this frame...
                if square_left_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    square_left_3.frameNStart = frameN  # exact frame index
                    square_left_3.tStart = t  # local t and not account for scr refresh
                    square_left_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(square_left_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'square_left_3.started')
                    # update status
                    square_left_3.status = STARTED
                    square_left_3.setAutoDraw(True)
                
                # if square_left_3 is active this frame...
                if square_left_3.status == STARTED:
                    # update params
                    pass
                
                # *square_right_3* updates
                
                # if square_right_3 is starting this frame...
                if square_right_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    square_right_3.frameNStart = frameN  # exact frame index
                    square_right_3.tStart = t  # local t and not account for scr refresh
                    square_right_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(square_right_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'square_right_3.started')
                    # update status
                    square_right_3.status = STARTED
                    square_right_3.setAutoDraw(True)
                
                # if square_right_3 is active this frame...
                if square_right_3.status == STARTED:
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
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    test_trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in test_trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "test_trial" ---
            for thisComponent in test_trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for test_trial
            test_trial.tStop = globalClock.getTime(format='float')
            test_trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('test_trial.stopped', test_trial.tStop)
            # check responses
            if test_hljt_response.keys in ['', [], None]:  # No response was made
                test_hljt_response.keys = None
                # was no response the correct answer?!
                if str(correct_keys).lower() == 'none':
                   test_hljt_response.corr = 1;  # correct non-response
                else:
                   test_hljt_response.corr = 0;  # failed to respond (incorrectly)
            # store data for test_trial_loop (TrialHandler)
            test_trial_loop.addData('test_hljt_response.keys',test_hljt_response.keys)
            test_trial_loop.addData('test_hljt_response.corr', test_hljt_response.corr)
            if test_hljt_response.keys != None:  # we had a response
                test_trial_loop.addData('test_hljt_response.rt', test_hljt_response.rt)
                test_trial_loop.addData('test_hljt_response.duration', test_hljt_response.duration)
            # the Routine "test_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "test_feedback" ---
            # create an object to store info about Routine test_feedback
            test_feedback = data.Routine(
                name='test_feedback',
                components=[test_square_2, test_hljt_image_2, square_left_4, square_right_4],
            )
            test_feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from test_feedback_code
            # If response is correct:
            if test_hljt_response.corr == 1:
                if correct_keys == hljt_correct_both:
                    if test_hljt_response.keys == "s":
                        fill_left = green
                        fill_right = black
                    elif test_hljt_response.keys == "l":
                        fill_left = black
                        fill_right = green
                elif correct_keys == hljt_correct_one:
                    if test_hljt_response.keys == "g":
                        fill_left = green
                        fill_right = black
                    elif test_hljt_response.keys == "h":
                        fill_left = black
                        fill_right = green
            
            #If response is incorrect:
            if test_hljt_response.corr == 0:
                if correct_keys == hljt_correct_both:
                    if test_hljt_response.keys == "s":
                        fill_left = red
                        fill_right = black
                    elif test_hljt_response.keys == "l":
                        fill_left = black
                        fill_right = red
                elif correct_keys == hljt_correct_one:
                    if test_hljt_response.keys == "g":
                        fill_left = red
                        fill_right = black
                    elif test_hljt_response.keys == "h":
                        fill_left = black
                        fill_right = red
            test_hljt_image_2.setOri(hljt_angle)
            test_hljt_image_2.setImage(hljt_images)
            square_left_4.setFillColor(fill_left)
            square_left_4.setLineColor(fill_left)
            square_right_4.setFillColor(fill_right)
            square_right_4.setLineColor(fill_right)
            # store start times for test_feedback
            test_feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            test_feedback.tStart = globalClock.getTime(format='float')
            test_feedback.status = STARTED
            thisExp.addData('test_feedback.started', test_feedback.tStart)
            test_feedback.maxDuration = feedback_time
            # keep track of which components have finished
            test_feedbackComponents = test_feedback.components
            for thisComponent in test_feedback.components:
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
            
            # --- Run Routine "test_feedback" ---
            # if trial has changed, end Routine now
            if isinstance(test_trial_loop, data.TrialHandler2) and thisTest_trial_loop.thisN != test_trial_loop.thisTrial.thisN:
                continueRoutine = False
            test_feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > test_feedback.maxDuration-frameTolerance:
                    test_feedback.maxDurationReached = True
                    continueRoutine = False
                
                # *test_square_2* updates
                
                # if test_square_2 is starting this frame...
                if test_square_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    test_square_2.frameNStart = frameN  # exact frame index
                    test_square_2.tStart = t  # local t and not account for scr refresh
                    test_square_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(test_square_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    test_square_2.status = STARTED
                    test_square_2.setAutoDraw(True)
                
                # if test_square_2 is active this frame...
                if test_square_2.status == STARTED:
                    # update params
                    pass
                
                # *test_hljt_image_2* updates
                
                # if test_hljt_image_2 is starting this frame...
                if test_hljt_image_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    test_hljt_image_2.frameNStart = frameN  # exact frame index
                    test_hljt_image_2.tStart = t  # local t and not account for scr refresh
                    test_hljt_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(test_hljt_image_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    test_hljt_image_2.status = STARTED
                    test_hljt_image_2.setAutoDraw(True)
                
                # if test_hljt_image_2 is active this frame...
                if test_hljt_image_2.status == STARTED:
                    # update params
                    pass
                
                # *square_left_4* updates
                
                # if square_left_4 is starting this frame...
                if square_left_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    square_left_4.frameNStart = frameN  # exact frame index
                    square_left_4.tStart = t  # local t and not account for scr refresh
                    square_left_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(square_left_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    square_left_4.status = STARTED
                    square_left_4.setAutoDraw(True)
                
                # if square_left_4 is active this frame...
                if square_left_4.status == STARTED:
                    # update params
                    pass
                
                # *square_right_4* updates
                
                # if square_right_4 is starting this frame...
                if square_right_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    square_right_4.frameNStart = frameN  # exact frame index
                    square_right_4.tStart = t  # local t and not account for scr refresh
                    square_right_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(square_right_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    square_right_4.status = STARTED
                    square_right_4.setAutoDraw(True)
                
                # if square_right_4 is active this frame...
                if square_right_4.status == STARTED:
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
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    test_feedback.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in test_feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "test_feedback" ---
            for thisComponent in test_feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for test_feedback
            test_feedback.tStop = globalClock.getTime(format='float')
            test_feedback.tStopRefresh = tThisFlipGlobal
            thisExp.addData('test_feedback.stopped', test_feedback.tStop)
            # the Routine "test_feedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed n_reps repeats of 'test_trial_loop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "block_pause" ---
        # create an object to store info about Routine block_pause
        block_pause = data.Routine(
            name='block_pause',
            components=[hljt_block_pause_text, hljt_block_adv_text, hljt_block_adv_key],
        )
        block_pause.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from hljt_block_pause_code
        if expInfo["language"] == "English":
            hljt_block_pause_text.text = block_pause_msg_en
            hljt_block_adv_text.text = advance
        elif expInfo["language"] == "Spanish":
            hljt_block_pause_text.text = block_pause_msg_es
            hljt_block_adv_text.text = advance
        elif expInfo["language"] == "French":
            hljt_block_pause_text.text = block_pause_msg_fr
            hljt_block_adv_text.text = advance
        # create starting attributes for hljt_block_adv_key
        hljt_block_adv_key.keys = []
        hljt_block_adv_key.rt = []
        _hljt_block_adv_key_allKeys = []
        # store start times for block_pause
        block_pause.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        block_pause.tStart = globalClock.getTime(format='float')
        block_pause.status = STARTED
        thisExp.addData('block_pause.started', block_pause.tStart)
        block_pause.maxDuration = None
        # keep track of which components have finished
        block_pauseComponents = block_pause.components
        for thisComponent in block_pause.components:
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
        
        # --- Run Routine "block_pause" ---
        # if trial has changed, end Routine now
        if isinstance(test_block, data.TrialHandler2) and thisTest_block.thisN != test_block.thisTrial.thisN:
            continueRoutine = False
        block_pause.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *hljt_block_pause_text* updates
            
            # if hljt_block_pause_text is starting this frame...
            if hljt_block_pause_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hljt_block_pause_text.frameNStart = frameN  # exact frame index
                hljt_block_pause_text.tStart = t  # local t and not account for scr refresh
                hljt_block_pause_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hljt_block_pause_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                hljt_block_pause_text.status = STARTED
                hljt_block_pause_text.setAutoDraw(True)
            
            # if hljt_block_pause_text is active this frame...
            if hljt_block_pause_text.status == STARTED:
                # update params
                pass
            
            # *hljt_block_adv_text* updates
            
            # if hljt_block_adv_text is starting this frame...
            if hljt_block_adv_text.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                hljt_block_adv_text.frameNStart = frameN  # exact frame index
                hljt_block_adv_text.tStart = t  # local t and not account for scr refresh
                hljt_block_adv_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hljt_block_adv_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                hljt_block_adv_text.status = STARTED
                hljt_block_adv_text.setAutoDraw(True)
            
            # if hljt_block_adv_text is active this frame...
            if hljt_block_adv_text.status == STARTED:
                # update params
                pass
            
            # *hljt_block_adv_key* updates
            waitOnFlip = False
            
            # if hljt_block_adv_key is starting this frame...
            if hljt_block_adv_key.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                hljt_block_adv_key.frameNStart = frameN  # exact frame index
                hljt_block_adv_key.tStart = t  # local t and not account for scr refresh
                hljt_block_adv_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hljt_block_adv_key, 'tStartRefresh')  # time at next scr refresh
                # update status
                hljt_block_adv_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(hljt_block_adv_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(hljt_block_adv_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if hljt_block_adv_key.status == STARTED and not waitOnFlip:
                theseKeys = hljt_block_adv_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _hljt_block_adv_key_allKeys.extend(theseKeys)
                if len(_hljt_block_adv_key_allKeys):
                    hljt_block_adv_key.keys = _hljt_block_adv_key_allKeys[-1].name  # just the last key pressed
                    hljt_block_adv_key.rt = _hljt_block_adv_key_allKeys[-1].rt
                    hljt_block_adv_key.duration = _hljt_block_adv_key_allKeys[-1].duration
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
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                block_pause.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in block_pause.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block_pause" ---
        for thisComponent in block_pause.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for block_pause
        block_pause.tStop = globalClock.getTime(format='float')
        block_pause.tStopRefresh = tThisFlipGlobal
        thisExp.addData('block_pause.stopped', block_pause.tStop)
        # the Routine "block_pause" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'test_block'
    
    
    # --- Prepare to start Routine "Goodbye" ---
    # create an object to store info about Routine Goodbye
    Goodbye = data.Routine(
        name='Goodbye',
        components=[bye_text, Exit],
    )
    Goodbye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_exit
    if expInfo["language"] == "English":
        bye_text.text = "This is the end of the experiment\n\nThanks for participating!\n\nWait 3 seconds to exit"
    elif expInfo["language"] == "Spanish":
        bye_text.text = "Este es el final del experimento\n\n¡Gracias por participar!\n\nEspera 3 segundos para salir"
    elif expInfo["language"] == "French":
        bye_text.text = "Ceci est la fin de l'expérience\n\nMerci d'avoir participé !\n\nAttendez 3 secondes pour quitter"
    
    # get Finish time and add to data output
    end_time = core.getTime()
    thisExp.addData('end_time', end_time)
    
    # calculate experiment time and add to data output
    completion_time = end_time - start_time
    thisExp.addData('completion_time', completion_time)
    # create starting attributes for Exit
    Exit.keys = []
    Exit.rt = []
    _Exit_allKeys = []
    # store start times for Goodbye
    Goodbye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Goodbye.tStart = globalClock.getTime(format='float')
    Goodbye.status = STARTED
    thisExp.addData('Goodbye.started', Goodbye.tStart)
    Goodbye.maxDuration = 3
    # keep track of which components have finished
    GoodbyeComponents = Goodbye.components
    for thisComponent in Goodbye.components:
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
    
    # --- Run Routine "Goodbye" ---
    Goodbye.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > Goodbye.maxDuration-frameTolerance:
            Goodbye.maxDurationReached = True
            continueRoutine = False
        
        # *bye_text* updates
        
        # if bye_text is starting this frame...
        if bye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bye_text.frameNStart = frameN  # exact frame index
            bye_text.tStart = t  # local t and not account for scr refresh
            bye_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bye_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            bye_text.status = STARTED
            bye_text.setAutoDraw(True)
        
        # if bye_text is active this frame...
        if bye_text.status == STARTED:
            # update params
            pass
        
        # *Exit* updates
        waitOnFlip = False
        
        # if Exit is starting this frame...
        if Exit.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            Exit.frameNStart = frameN  # exact frame index
            Exit.tStart = t  # local t and not account for scr refresh
            Exit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Exit, 'tStartRefresh')  # time at next scr refresh
            # update status
            Exit.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Exit.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Exit.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Exit.status == STARTED and not waitOnFlip:
            theseKeys = Exit.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Exit_allKeys.extend(theseKeys)
            if len(_Exit_allKeys):
                Exit.keys = _Exit_allKeys[-1].name  # just the last key pressed
                Exit.rt = _Exit_allKeys[-1].rt
                Exit.duration = _Exit_allKeys[-1].duration
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
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Goodbye.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Goodbye.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Goodbye" ---
    for thisComponent in Goodbye.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Goodbye
    Goodbye.tStop = globalClock.getTime(format='float')
    Goodbye.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Goodbye.stopped', Goodbye.tStop)
    thisExp.nextEntry()
    # the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
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
