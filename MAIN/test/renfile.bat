@echo off
set i=1
for %%f in (*.jpg) do call :renameit "%%f"
goto done

:renameit
ren %1 test%i%.jpg
set /A i+=1

:done
