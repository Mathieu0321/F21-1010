
FN=Lect-11
DIR=../..
PP=`pwd`

all: ${FN}.html 
	go build

${FN}.html: ${FN}.md
	blackfriday-tool ./${FN}.md ${FN}.html
	echo cat ./${DIR}/md.css ${FN}.html >/tmp/${FN}.html
	cat ./${DIR}/css/pre ./${DIR}/css/markdown.css ./${DIR}/css/post ./${DIR}/md.css ./${DIR}/css/hpre ${FN}.html ./${DIR}/css/hpost >/tmp/${FN}.html
	mv /tmp/${FN}.html ./${FN}.html
	echo "file://${pp}/${FN}.html" >open.1

aa:
	echo "file://${pp}/${FN}.html" >open.1
