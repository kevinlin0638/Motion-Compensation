##### 多媒體系統 HW1 #
將圖片轉換成BW

--------------------------
1.使用PIL讀檔
2.將檔案轉成灰階
3.使用numpy將檔案轉成陣列
4.使用混淆矩陣來判斷並改變原圖

###判斷方式#
cD 為 i % 4
rD 為 j % 4
若 array[i][j] < Dither_Matrix[cD][rD]
		array[i][j] 設成 黑色
其餘
		設成 白色
		
5.輸出圖片


以下為轉換前與轉換後

####轉換前#
![Alt text](https://photos.app.goo.gl/gkWGjCRXQlJfni7q1)

####轉換後#
![Alt text](https://photos.app.goo.gl/rKwHh2DwICU9NFmG2)


ps.丟入任何圖片都可以轉換喔:D

--------------------------
###### Test of Markdowns #

* Item 1
* Item 2
* Item 3

<ol>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ol>


![Alt text](http://image.boomsbeat.com/data/images/full/209/jobs-jpg.jpg)

|Title|colum 1 | colum 2|
|-----|--------|--------|
|__Row 1__|KAPPA 1 | KAPPA 2|
|__Row 2__|Kappa 3 | Kappa 4|


-----------------------------------


