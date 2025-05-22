            SET    0.1,1,0         ; Run at 10 kHz (0.1 ms per sequencer step) and 5V range of Power1401
            HALT   

; Play waveform X
AI:     'X  WAVEGO X               ; Play waveform X
AE:         HALT   

; Set motor to initial (I) length. For this we will slowly ramp.
IA:     'I  DAC    0,V1
            RAMP   0,V2,1.0/S(5)  ; Ramp up with 0.2 V/s
IRD:        WAITC  0,IRD          ; Wait until ramp is finished
            HALT   