@echo off
cd ../../..
IF EXIST docs\FILETREE.md (
    del docs\FILETREE.md
)
tree /F > docs\FILETREE.md
echo File tree structure has been updated in docs\FILETREE.md