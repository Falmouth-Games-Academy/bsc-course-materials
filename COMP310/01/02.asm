  LDX #$08      ; set X=8
decrement:
  DEX           ; subtract 1 from X
  STX $0200     ; store X in top left pixel
  CPX #$03      ; compare X to 3
  BNE decrement ; if not equal, jump
  STX $0201     ; store X in next pixel
  BRK           ; halt execution
