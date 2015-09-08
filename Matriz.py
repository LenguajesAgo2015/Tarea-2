

ERR = 200;
E = 24;


#       min  may   @    A    E   I   D    C    T   u    b    e    t    o    d    z    q    a    r    .    $    (    )    ,    ;   " "   &    |    -    <    =    ~    >
MT = [[  1,   2,   3,   2,   2,  2,  2,   2,   2,  1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 107, 999, 108, 109, 110, 111, 112,  18,  18,  21,  22,  19,  20,   E], # 0 inicio
      [  1,   E,   E,   E,   E,  E,  E,   E,   E,  1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 101, 101, 101, 101, 101, 101, 101,   E,   E,   E,   E,   E,   E,   E], # 1 variable
      [  E,   2,   E,   2,   2,  2,  2,   2,   2,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, 102, 102, 102, 102, 102, 102, 102,   E,   E,   E,   E,   E,   E,   E], # 2 constantes
      [  E,   E,   E,   4,   5,  6,  7,   8,   9,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 3 @
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   10,  E,   E,   E,   E, 104, 104, 104, 104, 104, 104, 104,   E,   E,   E,   E,   E,   E,   E], # 4 @A
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, 104, 104, 104, 104, 104, 104, 104,   E,   E,   E,   E,   E,   E,   E], # 5 @E
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,  11,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 6 @I
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,  12,   E,  13,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 7 @D
      [  E,   E,   E,   E,   E,  E,  E,   E,   E, 14,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 8 @C
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,  15,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 9 @T
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,  16,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 10 @Ad
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,  16,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 11 @Iz
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,  16,   E,   E,   E,   E,   E,  16, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 12 @De
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,  17,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 13 @Do
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,  17,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 14 @Cu
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,  17,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E], # 15 @Te
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, 105, 105, 105, 105, 105, 105, 105,   E,   E,   E,   E,   E,   E,   E], # 16 binario
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, 106, 106, 106, 106, 106, 106, 106,   E,   E,   E,   E,   E,   E,   E], # 17 unario
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, 113, 113, 113, 113, 113, 113, 113,   E,   E,   E,   E,   E,   E,   E], # 18 op binario
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, 114, 114, 114, 114, 114, 114, 114,   E,   E,   E,   E,   E,   E,   E], # 19 =
      [115, 115, 115, 115, 115,115,115, 115, 115,115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115, 115,   E], # 20 ~
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,  18], # 21 -
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,  23,   E,   E,   E,   E], # 22 <
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,  18], # 23 <-
      [  E,   E,   E,   E,   E,  E,  E,   E,   E,  E,   E,   E,   E,   E,   E,   E,   E,   E,   E, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   E,   E,   E,   E,   E,   E,   E]] # 24 error
