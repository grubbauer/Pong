: Installing some librarys (python needs to be installed)
pip install pyglet 

: Compile
pyinstaller --noconfirm --windowed  "Pong.py"

: Making directorys and placeing files
mkdir dist\Pong\src\aud
mkdir dist\Pong\src\font
mkdir dist\Pong\src\img
copy src\aud dist\Pong\src\aud 
copy src\font dist\Pong\src\font 
copy src\img dist\Pong\src\img 
copy License dist\Pong\

: Cleanup
del Pong.spec
rmdir /s /q build
move dist\Pong .\
rmdir /s /q dist
ren Pong build