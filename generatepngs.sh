#!/bin/bash

mkdir output/png/;
pushd output/svg/; 
for i in `ls *.svg`; 
	do inkscape --export-width=1288px --export-png=../png/$i.png $i; 
done; 
popd;
