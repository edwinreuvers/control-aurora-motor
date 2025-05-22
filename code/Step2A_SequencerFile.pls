            SET    0.1,2,0         ; Get rate and scaling OK
            DIGOUT [......00]
            HALT   

AI:     'X  DELAY  V4              ; Wait this amount of steps before we start stimulating
AS:         DIGOUT [......10]      ; Stimulation block: repeat until DNBZ V1,AS
            DAC    1,1             
            DELAY  V6              
            DIGOUT [......00]
            DAC    1,0
            DELAY  V7              
            DBNZ   V1,AS           ; if 0 block is done
AE:         HALT   