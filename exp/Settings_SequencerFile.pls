            SET    0.1,2,0         ; Get rate and scaling OK
            DIGOUT [......00]
            HALT   

AI:     'X  WAVEGO X               ; Play waveform X
AE:         HALT   

; Set motor to initial (I) length. For this we will slowly ramp (see below).
IA:     'I  DAC    0,V1
            RAMP   0,V2,2.0/S(5)  ; Ramp up with 0.2 V/s
IRD:        WAITC  0,IRD
            HALT   

; Set motor to initial (I) length. For this we will slowly ramp (see below).
JA:     'J  DAC    0,V1
            RAMP   0,-4.0,2.0/S(5)  ; Ramp up with 0.2 V/s
JRD:        WAITC  0,JRD
            HALT   