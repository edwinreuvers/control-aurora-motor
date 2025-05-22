            SET    0.1,1,0         ; Run at 10 kHz (0.1 ms per sequencer step) and 5V range of Power1401
            HALT   

; Play waveform X
AI:     'X  WAVEGO X               ; Play waveform X
AE:         HALT   