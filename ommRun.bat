echo off

set ommPath="C:\OpenMOM\omm.exe"
set outPath="./omm.out"
set geoPath="./geom3d.htm"
set curPath="./current.log"
set elePath="./element.log"
set logPath="./omm.log"
set far0dPath="./far0d.log"
set far1dPath="./far1d.log"
set far2dPath="./far2d.log"
set near1dPath="./near1d.log"
set near2dPath="./near2d.log"
set ev2dPath="./ev2d.htm"
set ev3dPath="./ev3d.htm"

rem ’¼‰º‚ÌƒtƒHƒ‹ƒ_‚É.omm‚ª‚È‚¢‚©’²‚×‚é

for /d %%a in (*) do (
  for %%b in ("%%a"\*.omm) do (
    echo on
    "%ommPath%" -solver -n 16 -avx "%%b"
    "%ommPath%" -post "%%b"
    move "%outPath%" "%%a"
    move "%geoPath%" "%%a"
    move "%curPath%" "%%a"
    move "%elePath%" "%%a"
    move "%logPath%" "%%a"
    move "%far0dPath%" "%%a"
    move "%far1dPath%" "%%a"
    move "%far2dPath%" "%%a"
    move "%near1dPath%" "%%a"
    move "%near2dPath%" "%%a"
    move "%ev2dPath%" "%%a"
    move "%ev3dPath%" "%%a"
    echo off
  )
)
