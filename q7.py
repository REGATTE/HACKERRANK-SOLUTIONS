{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue254;\red0\green0\blue0;
\red19\green120\blue72;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c3529\c53333\c35294;}
\paperw11900\paperh16840\margl1440\margr1440\vieww17720\viewh10240\viewkind0
\deftab720
\pard\pardeftab720\sl460\partightenfactor0

\f0\fs30 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def\cf4 \strokec4 \'a0is_leap(year):\cb1 \
\pard\pardeftab720\sl460\partightenfactor0
\cf4 \cb3     leap\'a0=\'a0\cf2 \strokec2 False\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4 (year%\cf5 \strokec5 400\cf4 \strokec4 \'a0==\'a0\cf5 \strokec5 0\cf4 \strokec4 ):\cb1 \
\cb3         leap\'a0=\'a0\cf2 \strokec2 True\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 elif\cf4 \strokec4 (year%\cf5 \strokec5 4\cf4 \strokec4 ==\cf5 \strokec5 0\cf4 \strokec4 \'a0\cf2 \strokec2 and\cf4 \strokec4 \'a0year%\cf5 \strokec5 100\cf4 \strokec4 !=\'a0\cf5 \strokec5 0\cf4 \strokec4 ):\cb1 \
\cb3         leap\'a0=\'a0\cf2 \strokec2 True\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4 \'a0leap\cb1 \
\
\cb3 year\'a0=\'a0\cf2 \strokec2 int\cf4 \strokec4 (\cf2 \strokec2 input\cf4 \strokec4 ())\cb1 \
\pard\pardeftab720\sl460\partightenfactor0
\cf2 \cb3 \strokec2 print\cf4 \strokec4 (is_leap(year))\cb1 \
}