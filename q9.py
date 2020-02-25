{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue254;\red0\green0\blue0;
\red144\green1\blue18;\red19\green120\blue72;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c3529\c53333\c35294;}
\paperw11900\paperh16840\margl1440\margr1440\vieww17720\viewh10240\viewkind0
\deftab720
\pard\pardeftab720\sl460\partightenfactor0

\f0\fs30 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4 \'a0re\cb1 \
\
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \cb3 string\'a0=\'a0\cf2 \strokec2 input\cf4 \strokec4 ()\cb1 \
\cb3 substring\'a0=\'a0\cf2 \strokec2 input\cf4 \strokec4 ()\cb1 \
\
\cb3 pattern\'a0=\'a0re.\cf2 \strokec2 compile\cf4 \strokec4 (substring)\cb1 \
\cb3 match\'a0=\'a0pattern.search(string)\cb1 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 \cb3 \strokec2 if\cf4 \strokec4 \'a0\cf2 \strokec2 not\cf4 \strokec4 \'a0match:\'a0\cf2 \strokec2 print\cf4 \strokec4 (\cf5 \strokec5 '(-1,\'a0-1)'\cf4 \strokec4 )\cb1 \
\cf2 \cb3 \strokec2 while\cf4 \strokec4 \'a0match:\cb1 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 print\cf4 \strokec4 (\cf5 \strokec5 '(\{0\},\'a0\{1\})'\cf4 \strokec4 .\cf2 \strokec2 format\cf4 \strokec4 (match.start(),\'a0match.end()\'a0-\'a0\cf6 \strokec6 1\cf4 \strokec4 ))\cb1 \
\cb3    \'a0match\'a0=pattern.search(string,\'a0match.start()\'a0+\'a0\cf6 \strokec6 1\cf4 \strokec4 )\cb1 \
}