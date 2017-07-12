PythonProject : ChaCha's NoteBook
=
###### tags: `python` 

## 來點介紹
這是一個python的練習專題，是一個command line的記事本。
這個記事本只能透由terminal執行。
之後會有GUI版本釋出。

## 如何使用

這個記事本有4個`功能`。分別為`1.Add 2.List 3.Read 4.Remove`
使用者在執行完這個程式後，需要輸入這4個功能中其中一個。


#### ```Add``` : insert the title and the body
#### ```List```: print all notes (title and body)
#### ```Read```：search the title  and print the note (title and body)
#### ```Remove```: search the title and remove the note


### - 輸入Add:

![](https://i.imgur.com/uMxbr5b.png)


![](https://i.imgur.com/WYLHoVb.png)

![](https://i.imgur.com/Pd3dlFv.png)


```新建的Sam.txt & Dora.txt 就會在這支程式的資料夾裡。listName記錄每個新建檔案名字。```


##
### - 輸入List:

![](https://i.imgur.com/bK1aQh3.png)

```顯示各個檔案名字及內容 ```



### - 輸入Read:

![](https://i.imgur.com/VgS3AIB.png)

```讀取Sam.txt，顯示其內容 ```
## 

### - 輸入Remove:


![](https://i.imgur.com/e7RptiZ.png)

![](https://i.imgur.com/F4QhnH0.png)

![](https://i.imgur.com/YYbw3va.png)

```移除資料夾裡的Dora.txt，且刪除listName裡的Dora.txt  ```

## 檔案的各種事
### 讀檔、創檔、寫檔
### 使用open(  )打開檔案
#### 語法為 
```python=
var = open('fileName','mode')
```
### mode:
```
r - 讀取已存在的file

w - 新建檔案寫入(file存在與否皆沒關係，若存在則清空原本的file，即會覆蓋原本file)

a - 資料附加到舊檔案後面(直接接在原本資料後面，無空格)
```
### 讀檔：
```python=
var = open('fileName','r')
```
### 創檔＆寫檔：
```python=
var = open('fileName','w')
fileContent = input( )
var.write(fileContent)
```
### 從一個file裡刪除資料

#### 1. open the file



```python=
f = open("file.txt","r")
```

#### 2. get lines from the file


```python=
lines = f.readlines()
```

#### 3. close the file 


```python=
f.close()
```


#### 4. reopen it in w mode

```python=
f = open("file.txt","w")
```


#### 5. write the lines back, and don't write the line which you want to delete. Add the "\n" to whatever line ending your file uses.

```python=
for line in lines:
      if line!="The_thing_to_delete"+"\n":
        f.write(line)
```


### 從一個file裡新增資料

#### 1. Open the file and set it to a mode
```python=
f = open('yourfile.txt', 'a', encoding = 'UTF-8') 
```
#### 2. Write the content in it
```python=
FileContent = f.write(the content you want to write)   
```




## License
MIT © MindyTai