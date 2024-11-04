# 期中考
>
>學號：112111225
><br />
>姓名：林芷羽
><br />
>作業撰寫時間：180 (mins，包含程式撰寫時間)
><br />
>最後撰寫文件日期：2024/11/4
>

本份文件包含以下主題：(至少需下面兩項，若是有多者可以自行新增)
- [x] 說明內容

## 說明程式與內容

開始寫說明，該說明需說明想法，
並於之後再對上述想法的每一部分將程式進一步進行展現，
若需引用程式區則使用下面方法，
若為.cs檔內程式除了於敘述中需註明檔案名稱外，
還需使用語法` ```語言種類 程式碼 ``` `，其中語言種類若是要用python則使用py，java則使用java，C/C++則使用cpp，
下段程式碼為語言種類選擇csharp使用後結果：

```csharp
public void mt_getResult(){
    ...
}
```

若要於內文中標示部分網頁檔，則使用以下標籤` ```html 程式碼 ``` `，
下段程式碼則為使用後結果：

```html
<%@ Page Language="C#" AutoEventWireup="true" ...>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" ...>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
    </form>
</body>
</html>
```
更多markdown方法可參閱[https://ithelp.ithome.com.tw/articles/10203758](https://ithelp.ithome.com.tw/articles/10203758)
請在撰寫"說明程式與內容"該塊內容，請把原該塊內上述敘述刪除，該塊上述內容只是用來指引該怎麼撰寫內容。


a. 小題

Ans

```py
map = [[0]*10 for _ in range(10)]
```

b. 小題

Ans

```py
rowMap = [0]*10
```

c. 小題

Ans

```py
rowMap = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]
```


d. 小題

Ans

```py
def bombs(map):
    rows = len(map)
    cols = len(map[0]) 
    bombMap = [[" " for _ in range(cols)] for _ in range(rows)] 

    for r in range(rows):
        for c in range(cols):
            if map[r][c] == "*":
                bombMap[r][c] = "*"  # 如果是炸彈則顯示 *
```


e. 小題

Ans

```py
            else:
                # 計算周圍炸彈數量
                bombCount = 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if 0 <= i < rows and 0 <= j < cols:
                            if map[i][j] == "*":
                                bombCount += 1
                                if bombCount > 0:
                                    bombMap[r][c] = str(bombCount)
                                else:
                                    bombMap[r][c] = " "  # 空白顯示

    return bombMap

result_map = bombs(map)
for row in result_map:
    print(" ".join(row))
```
