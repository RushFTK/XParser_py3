# -*- coding: utf-8 -*-
import imp

def environment_tester():
    state = 0
    reason = 'Unknown reason'
    try:
        imp.find_module('win32api')
        state = 1
        reason = 'Windows python environment is ready'
    except ImportError:
        state = 0
        reason = 'Non-Windows system or windows support module not ready' + ImportError.message()
    return state,reason
