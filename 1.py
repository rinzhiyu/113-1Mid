# 生成⼀個整數 2 維陣列，大小為10*10，名稱為 map，其中每個元素初始為 0。
map = [[0]*10 for _ in range(10)]

# 生成⼀個整數 1 維陣列，大小為 10，名稱為 rowMap。其陣列主要用來儲存上述10*10二維陣列，以列為主的索引值
rowMap = [0]*10

# 承 2，將 rowMap 給值，分別為「0, 7, 13, 28, 44, 62, 74, 75, 87, 90」(此部分可供老師進行調整，並影響最終輸出結果)。上述 10 個數值，每個數值都是記錄「以列為主的二維索引轉為一維索引」之值，其作用用在於之後會作為二維陣列中顯示地雷的部分。
rowMap = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]

# 畫出二維陣列，並將 rowMap 裡面紀錄的值，對應至二維陣列中顯示炸彈，炸彈需以符號「*」作為標記。
for index in rowMap:
    row = index // 10  #計算列
    col = index % 10   #計算行
    map[row][col] = "*" # 用 * 表示炸弹
    
def bombs(map):
    rows = len(map)
    cols = len(map[0]) 
    bombMap = [[" " for _ in range(cols)] for _ in range(rows)] 

    for r in range(rows):
        for c in range(cols):
            if map[r][c] == "*":
                bombMap[r][c] = "*"  # 如果是炸彈則顯示 *
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