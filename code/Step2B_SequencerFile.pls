            SET    0.1,2,0         ; Get rate and scaling OK
            DIGOUT [......00]
            HALT   

AI:     'X  MOV    V3,V1           ; Number of stimulation blocks
            WAVEGO X               ; Play waveform X
            DELAY  V4              ; We wait this amount of steps before we start with stimulation
AS:         DIGOUT [......10]
            DAC    1,1             ; Stimulation block here, repeat until DNBZ V3,RA2
            DELAY  V6              ; 4.7 ms but also 3 steps (DIGOUT, DAC and DELAY itself) which take 0.2 ms
            DIGOUT [......00]
            DAC    1,0
            DELAY  V7              ; 4.6 ms but also 4 steps (DIGOUT, DAC, DELAY and DBNZ) which take 0.3 ms
            DBNZ   V3,AS           ; if 0 first block is done, continue with waiting for next block
            DELAY  V5
            MOV    V3,V1           ; Reset number of stimulation blocks to input of user!
            DBNZ   V2,AS           ; Repeat number of stim cycles
            DAC    0,V8
AE:         HALT   

; Set motor to initial (I) length. For this we will slowly ramp (see blow).
IA:     'I  DAC    0,V1
            RAMP   0,V2,1.0/S(5)  ; Ramp up with 0.2 V/s
IRD:        WAITC  0,IRD
            HALT   