  CPX #$01      ; compare X to 1
  BMI else      ; if X < 1, jump
  DEY           ; Y = Y - 1
  JMP end       ; skip over else block
else:
  INY           ; Y = Y + 1
end:
