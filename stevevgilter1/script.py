
from urllib import request
data="""data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABwgAAASwCAIAAABggIlUAAAACXBIWXMAAAsT
AAALEwEAmpwYAAAKT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnV
FPpFj333vRCS4iAlEtvUhUIIFJCi4AUkSYqIQkQSoghodkVUcERRUUEG8igiAOOjoCM
FVEsDIoK2AfkIaKOg6OIisr74Xuja9a89+bN/
rXXPues852zzwfACAyWSDNRNYAMqUIeEeCDx8TG4eQuQIEKJHAAEAizZCFz/
SMBAPh+PDwrIsAHvgABeNMLCADATZvAMByH/w/
qQplcAYCEAcB0kThLCIAUAEB6jkKmAEBGAYCdmCZTAKAEAGDLY2LjAFAtAGAnf+b
TAICd+Jl7AQBblCEVAaCRACATZYhEAGg7AKzPVopFAFgwABRmS8Q5ANgtADBJV2
ZIALC3AMDOEAuyAAgMADBRiIUpAAR7AGDIIyN4AISZABRG8lc88SuuEOcqAAB4m
bI8uSQ5RYFbCC1xB1dXLh4ozkkXKxQ2YQJhmkAuwnmZGTKBNA/
g88wAAKCRFRHgg/P9eM4Ors7ONo62Dl8t6r8G/
yJiYuP+5c+rcEAAAOF0ftH+LC+zGoA7BoBt/qIl7gRoXgugdfeLZrIPQLUAoOnaV/
Nw+H48PEWhkLnZ2eXk5NhKxEJbYcpXff5nwl/AV/1s+X48/
Pf14L7iJIEyXYFHBPjgwsz0TKUcz5IJhGLc5o9H/LcL//
wd0yLESWK5WCoU41EScY5EmozzMqUiiUKSKcUl0v9k4t8s+wM+3zUAsGo+AXuR
LahdYwP2SycQWHTA4vcAAPK7b8HUKAgDgGiD4c93/+8//
UegJQCAZkmScQAAXkQkLlTKsz/HCAAARKCBKrBBG/TBGCzABhzBBdzBC/
xgNoRCJMTCQhBCCmSAHHJgKayCQiiGzbAdKmAv1EAdNMBRaIaTcA4uwlW4Dj1w
D/
phCJ7BKLyBCQRByAgTYSHaiAFiilgjjggXmYX4IcFIBBKLJCDJiBRRIkuRNUgxUopUIF
VIHfI9cgI5h1xGupE7yAAygvyGvEcxlIGyUT3UDLVDuag3GoRGogvQZHQxmo8WoJv
QcrQaPYw2oefQq2gP2o8+Q8cwwOgYBzPEbDAuxsNCsTgsCZNjy7EirAyrxhqwVqw
Du4n1Y8+xdwQSgUXACTYEd0IgYR5BSFhMWE7YSKggHCQ0EdoJNwkDhFHCJyKT
qEu0JroR+cQYYjIxh1hILCPWEo8TLxB7iEPENyQSiUMyJ7mQAkmxpFTSEtJG0m5SI
+ksqZs0SBojk8naZGuyBzmULCAryIXkneTD5DPkG+Qh8lsKnWJAcaT4U+IoUspqSh
nlEOU05QZlmDJBVaOaUt2ooVQRNY9aQq2htlKvUYeoEzR1mjnNgxZJS6WtopXTG
mgXaPdpr+h0uhHdlR5Ol9BX0svpR+iX6AP0dwwNhhWDx4hnKBmbGAcYZxl3GK+Y
TKYZ04sZx1QwNzHrmOeZD5lvVVgqtip8FZHKCpVKlSaVGyovVKmqpqreqgtV81XL
VI+pXlN9rkZVM1PjqQnUlqtVqp1Q61MbU2epO6iHqmeob1Q/pH5Z/
YkGWcNMw09DpFGgsV/jvMYgC2MZs3gsIWsNq4Z1gTXEJrHN2Xx2KruY/
R27iz2qqaE5QzNKM1ezUvOUZj8H45hx+Jx0TgnnKKeX836K3hTvKeIpG6Y0TLkxZV
xrqpaXllirSKtRq0frvTau7aedpr1Fu1n7gQ5Bx0onXCdHZ4/
OBZ3nU9lT3acKpxZNPTr1ri6qa6UbobtEd79up+6Ynr5egJ5Mb6feeb3n+hx9L/1U/
W36p/
VHDFgGswwkBtsMzhg8xTVxbzwdL8fb8VFDXcNAQ6VhlWGX4YSRudE8o9VGjUYPj
GnGXOMk423GbcajJgYmISZLTepN7ppSTbmmKaY7TDtMx83MzaLN1pk1mz0x1zLn
m+eb15vft2BaeFostqi2uGVJsuRaplnutrxuhVo5WaVYVVpds0atna0l1rutu6cRp7lOk0
6rntZnw7Dxtsm2qbcZsOXYBtuutm22fWFnYhdnt8Wuw+6TvZN9un2N/
T0HDYfZDqsdWh1+c7RyFDpWOt6azpzuP33F9JbpL2dYzxDP2DPjthPLKcRpnVOb0
0dnF2e5c4PziIuJS4LLLpc+Lpsbxt3IveRKdPVxXeF60vWdm7Obwu2o26/
uNu5p7ofcn8w0nymeWTNz0MPIQ+BR5dE/
C5+VMGvfrH5PQ0+BZ7XnIy9jL5FXrdewt6V3qvdh7xc+9j5yn+M+4zw33jLeWV/
MN8C3yLfLT8Nvnl+F30N/I/9k/3r/
0QCngCUBZwOJgUGBWwL7+Hp8Ib+OPzrbZfay2e1BjKC5QRVBj4KtguXBrSFoyOy
QrSH355jOkc5pDoVQfujW0Adh5mGLw34MJ4WHhVeGP45wiFga0TGXNXfR3ENz3
0T6RJZE3ptnMU85ry1KNSo+qi5qPNo3ujS6P8YuZlnM1VidWElsSxw5LiquNm5svt/
87fOH4p3iC+N7F5gvyF1weaHOwvSFpxapLhIsOpZATIhOOJTwQRAqqBaMJfITdyW
OCnnCHcJnIi/
RNtGI2ENcKh5O8kgqTXqS7JG8NXkkxTOlLOW5hCepkLxMDUzdmzqeFpp2IG0yPT
q9MYOSkZBxQqohTZO2Z+pn5mZ2y6xlhbL+xW6Lty8elQfJa7OQrAVZLQq2QqboV
Foo1yoHsmdlV2a/zYnKOZarnivN7cyzytuQN5zvn//
tEsIS4ZK2pYZLVy0dWOa9rGo5sjxxedsK4xUFK4ZWBqw8uIq2Km3VT6vtV5eufr0m
ek1rgV7ByoLBtQFr6wtVCuWFfevc1+1dT1gvWd+1YfqGnRs+FYmKrhTbF5cVf9go3Hj
lG4dvyr+Z3JS0qavEuWTPZtJm6ebeLZ5bDpaql+aXDm4N2dq0Dd9WtO319kXbL5
fNKNu7g7ZDuaO/
PLi8ZafJzs07P1SkVPRU+lQ27tLdtWHX+G7R7ht7vPY07NXbW7z3/
T7JvttVAVVN1WbVZftJ+7P3P66Jqun4lvttXa1ObXHtxwPSA/
0HIw6217nU1R3SPVRSj9Yr60cOxx++/p3vdy0NNg1VjZzG4iNwRHnk6fcJ3/
ceDTradox7rOEH0x92HWcdL2pCmvKaRptTmvtbYlu6T8w+0dbq3nr8R9sfD5w0PFl
5SvNUyWna6YLTk2fyz4ydlZ19fi753GDborZ752PO32oPb++6EHTh0kX/
i+c7vDvOXPK4dPKy2+UTV7hXmq86X23qdOo8/
pPTT8e7nLuarrlca7nuer21e2b36RueN87d9L158Rb/1tWeOT3dvfN6b/fF9/
XfFt1+cif9zsu72Xcn7q28T7xf9EDtQdlD3YfVP1v+3Njv3H9qwHeg89HcR/cGhYPP/
pH1jw9DBY+Zj8uGDYbrnjg+OTniP3L96fynQ89kzyaeF/6i/
suuFxYvfvjV69fO0ZjRoZfyl5O/bXyl/
erA6xmv28bCxh6+yXgzMV70VvvtwXfcdx3vo98PT+R8IH8o/2j5sfVT0Kf7kxmTk/
8EA5jz/GMzLdsAAAAgY0hSTQAAeiUAAICDAAD5/
wAAgOkAAHUwAADqYAAAOpgAABdvkl/
FRgAAI15JREFUeNrs2kERAzEQA8FN6njZzEzN0PI4FpluCHpO6bPWmpm99wAAAA
AA/Lt778x8DQEAAAAA1DzvV/
ScYwsAAAAAIMJjFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADI
EUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIE
UYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEU
YBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUY
BAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYB
AAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBA
AAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAA
AAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAA
AgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAA
gBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAg
BxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBx
hFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhF
AAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFA
AAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAA
AAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAA
AADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAA
ADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAA
DIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADI
EUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIE
UYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEU
YBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUY
BAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYB
AAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBA
AAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAA
AAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAA
AgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAA
gBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAg
BxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBx
hFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhF
AAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFA
AAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAA
AAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAA
AADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAA
ADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAA
DIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADI
EUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIE
UYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEU
YBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUY
BAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYB
AAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBA
AAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAA
AAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAA
AgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAA
gBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAg
BxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBx
hFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhF
AAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFA
AAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAA
AAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAA
AADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAA
ADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAA
DIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADI
EUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIE
UYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEU
YBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUY
BAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYB
AAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBA
AAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAA
AAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAA
AgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAA
gBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAg
BxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBx
hFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhF
AAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFA
AAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAA
AAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAA
AADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAA
ADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAA
DIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADI
EUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIE
UYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEU
YBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUY
BAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYB
AAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBA
AAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAA
AAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAA
AgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAA
gBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAg
BxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBx
hFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhF
AAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFA
AAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAA
AAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAA
AADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAA
ADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAA
DIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADI
EUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIE
UYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEU
YBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUY
BAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYB
AAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBA
AAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAA
AAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAA
AgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAA
gBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAg
BxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBx
hFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhF
AAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFA
AAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAA
AAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAA
AADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAA
ADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAA
DIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADI
EUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIE
UYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEU
YBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUY
BAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYB
AAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBA
AAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAA
AAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAA
AgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAA
gBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAg
BxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBx
hFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhF
AAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFA
AAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAA
AAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAA
AADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAA
ADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAA
DIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADI
EUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIE
UYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEU
YBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUY
BAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYB
AAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBA
AAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAA
AAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAA
AgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAA
gBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAg
BxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBx
hFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhF
AAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFA
AAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAA
AAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAA
AADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAA
ADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAA
DIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADI
EUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIE
UYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEU
YBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUY
BAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYB
AAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBA
AAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAA
AAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAA
AgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAA
gBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAg
BxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBx
hFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhF
AAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFA
AAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAA
AAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAA
AADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAA
ADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAA
DIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADI
EUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIE
UYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEU
YBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUY
BAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYB
AAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBA
AAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAA
AAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAA
AgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAA
gBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAg
BxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBx
hFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhF
AAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFA
AAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAA
AAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAA
AADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAA
ADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAA
DIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADI
EUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIE
UYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEU
YBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUY
BAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYB
AAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBA
AAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAA
AAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAA
AgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAA
gBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAg
BxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBx
hFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhF
AAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFA
AAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAA
AAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAA
AADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAA
ADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAA
DIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADI
EUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIE
UYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEU
YBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUY
BAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYB
AAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBA
AAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAA
AAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIEUYBAAA
AgBxhFAAAAADIEUYBAAAAgBxhFAAAAADIee69VgAAAAAAIt4i6jEKAAAAAOT8Bg
AdjRPe4M51MAAAAABJRU5ErkJggg=="""




response =request.urlopen(data)
with open('image.png', 'wb') as f:
    f.write(response.file.read())