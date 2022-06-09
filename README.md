# bolshye-dannye
## task 1
### `create_bin.py` - generate binary file
### `task1.py` - comparing of single- vs multiprocessing
## task 2
### `create_num.py` - generate txt file with 2000 numbers
### `factor.py` - factorization function used in all parts of the task
### `st.py` - single thread factorization
```
C:\Users\user\Desktop\bolshye dannye> Measure-Command {python .\repo\bolshye-dannye\task2\st.py}


Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 1
Milliseconds      : 594
Ticks             : 15948660
TotalDays         : 1,84590972222222E-05
TotalHours        : 0,000443018333333333
TotalMinutes      : 0,0265811
TotalSeconds      : 1,594866
TotalMilliseconds : 1594,866
```
### `mt.py` - multiproccesing in python
```
C:\Users\user\Desktop\bolshye dannye> Measure-Command {python .\repo\bolshye-dannye\task2\mt.py}


Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 848
Ticks             : 8488652
TotalDays         : 9,8248287037037E-06
TotalHours        : 0,000235795888888889
TotalMinutes      : 0,0141477533333333
TotalSeconds      : 0,8488652
TotalMilliseconds : 848,8652
```
### `dask_mt.py` - factorization via Dask
```
C:\Users\user\Desktop\bolshye dannye> Measure-Command {python .\repo\bolshye-dannye\task2\dask_mt.py}


Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 8
Milliseconds      : 833
Ticks             : 88334662
TotalDays         : 0,00010223919212963
TotalHours        : 0,00245374061111111
TotalMinutes      : 0,147224436666667
TotalSeconds      : 8,8334662
TotalMilliseconds : 8833,4662
```

As it takes quite some time for dask to launch, I measure this one with python time.time too:
```
C:\Users\user\Desktop\bolshye dannye> python .\repo\bolshye-dannye\task2\dask_mt.py
8274
time elapsed: 1.873273s
```
### `mt.cpp` - C/C++ solution
for NUM_THREADS  1:
```
C:\Users\user\source\repos\Project1\Debug> Measure-Command {.\mt.exe}


Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 244
Ticks             : 2449042
TotalDays         : 2,83453935185185E-06
TotalHours        : 6,80289444444444E-05
TotalMinutes      : 0,00408173666666667
TotalSeconds      : 0,2449042
TotalMilliseconds : 244,9042
```
for NUM_THREADS  4:
```
C:\Users\user\source\repos\Project1\Debug> Measure-Command {.\mt.exe}


Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 120
Ticks             : 1206961
TotalDays         : 1,39694560185185E-06
TotalHours        : 3,35266944444444E-05
TotalMinutes      : 0,00201160166666667
TotalSeconds      : 0,1206961
TotalMilliseconds : 120,6961
```
## task3
### `task3.ipynb` - Jupyter notebook with solution
