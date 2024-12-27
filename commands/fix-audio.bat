@echo off
set input_folder=..\dataset\wavs_original
set output_folder=..\dataset\wavs

for %%f in ("%input_folder%\*.wav") do (
    ffmpeg -i "%%f" -af "loudnorm=i=-20:lra=7:tp=-2" "%output_folder%\%%~nf_normalized.wav"
)
pause
