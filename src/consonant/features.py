#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import librosa

#############################################################################
#
#  Short Term Features - Analyisis Window
#
#  1. MFCC (15)
#  2. Spectral Centroid (1)
#  3. Spectral Rolloff (1)
#  4. Spectral Flux (1)
#  5. Zero Cross Rate (1)
#  6. OSC (18)
#  7. Low Energy (1)
#  8. OMSC(10)
#  9. MSFM (10)
# 10. MSCM (10)
#
#  Compressive Sensind Feature Dimension: 68
#
#############################################################################

def compressive_sensing(file):
    features=[]
    audio, sample_rate = librosa.load(file)
    # MFCC
    features['mfcc'] = numpy.mean(librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=15).T,axis=0)
    # STFT
    stft = numpy.abs(librosa.stft(audio))
    # Spectral Centroid
    features['centroid'] = numpy.mean(librosa.feature.spectral_centroid(y=audio, sr=sample_rate))
    return features
