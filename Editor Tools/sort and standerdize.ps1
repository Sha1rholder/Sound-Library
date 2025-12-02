$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$path = Join-Path $scriptDir "..\data\over-ear sensitivity official.csv"

# 1. 读取 CSV 文件
$data = Import-Csv -Path $path

# 初始化错误计数器
$hasErrors = $false
$errors = @()

# 2. 检查重复行（brand和model组合）
$brandModelMap = @{}
for ($i = 0; $i -lt $data.Count; $i++) {
    $row = $data[$i]
    $rowNumber = $i + 1  # 转换为1-based行号
    
    # 检查brand和model是否都为空
    if ([string]::IsNullOrWhiteSpace($row.brand) -or [string]::IsNullOrWhiteSpace($row.model)) {
        continue  # 跳过空brand或model的行
    }
    
    $key = "$($row.brand)|$($row.model)"
    
    if ($brandModelMap.ContainsKey($key)) {
        $duplicateRow = $brandModelMap[$key]
        $errors += "错误: 第 ${rowNumber} 行和第 ${duplicateRow} 行的 brand 和 model 相同 (brand: '$($row.brand)', model: '$($row.model)')"
        $hasErrors = $true
    }
    else {
        $brandModelMap[$key] = $rowNumber
    }
}

# 3. 检查每行的字段值
for ($i = 0; $i -lt $data.Count; $i++) {
    $row = $data[$i]
    $rowNumber = $i + 1  # 转换为1-based行号
    
    # 检查 production 字段
    $validProductions = @('discontinued', 'producing', 'inventory', 'developing')
    if ([string]::IsNullOrWhiteSpace($row.production)) {
        $errors += "警告: 第 ${rowNumber} 行 (brand: '$($row.brand)', model: '$($row.model)') 的 production 值为空"
        $hasErrors = $true
    }
    elseif ($row.production -notin $validProductions) {
        $errors += "错误: 第 ${rowNumber} 行 (brand: '$($row.brand)', model: '$($row.model)') 的 production 值无效: '$($row.production)'，有效值为: $($validProductions -join ', ')"
        $hasErrors = $true
    }
    
    # 检查 driver 字段
    $validDrivers = @('dynamic', 'planar', 'AMT', 'planar and dynamic')
    if ([string]::IsNullOrWhiteSpace($row.driver)) {
        $errors += "错误: 第 ${rowNumber} 行 (brand: '$($row.brand)', model: '$($row.model)') 的 driver 值为空"
        $hasErrors = $true
    }
    elseif ($row.driver -notin $validDrivers) {
        $errors += "错误: 第 ${rowNumber} 行 (brand: '$($row.brand)', model: '$($row.model)') 的 driver 值无效: '$($row.driver)'，有效值为: $($validDrivers -join ', ')"
        $hasErrors = $true
    }
    
    # 检查 back 字段
    $validBacks = @('open', 'closed', 'semi-closed', 'speaker', 'uncertain')
    if ([string]::IsNullOrWhiteSpace($row.back)) {
        $errors += "错误: 第 ${rowNumber} 行 (brand: '$($row.brand)', model: '$($row.model)') 的 back 值为空"
        $hasErrors = $true
    }
    elseif ($row.back -notin $validBacks) {
        $errors += "错误: 第 ${rowNumber} 行 (brand: '$($row.brand)', model: '$($row.model)') 的 back 值无效: '$($row.back)'，有效值为: $($validBacks -join ', ')"
        $hasErrors = $true
    }
    
    # 检查 balance 字段（允许为空，但不允许无效值）
    $validBalances = @('yes', 'no', 'both')
    if (-not [string]::IsNullOrWhiteSpace($row.balance) -and $row.balance -notin $validBalances) {
        $errors += "错误: 第 ${rowNumber} 行 (brand: '$($row.brand)', model: '$($row.model)') 的 balance 值无效: '$($row.balance)'，有效值为: $($validBalances -join ', ') 或留空"
        $hasErrors = $true
    }
}

# 4. 如果有错误，输出错误信息并退出
if ($hasErrors) {
    Write-Host "`n发现以下错误：" -ForegroundColor Red
    foreach ($errorMsg in $errors) {
        if ($errorMsg.StartsWith("错误:")) {
            Write-Host $errorMsg -ForegroundColor Red
        }
        else {
            Write-Host $errorMsg -ForegroundColor Yellow
        }
    }
    Write-Host "`n请先修复上述错误，然后再运行脚本。" -ForegroundColor Red
    exit 1
}

# 5. 如果没有错误，继续执行原来的处理逻辑
Write-Host "数据验证通过，开始处理日期和排序..." -ForegroundColor Green

# 获取今天的日期并格式化为要求的格式
$today = Get-Date
$todayFormatted = "{0}-{1:00}-{2:00}" -f $today.Year, $today.Month, $today.Day

# 遍历每一行，处理 date 列
$processedData = $data | ForEach-Object {
    $row = $_
    $dateValue = $row.'date'
    
    # 新增功能：如果 production 为 discontinued，则将 date 更新为今天
    if ($row.'production' -eq 'discontinued') {
        $row.'date' = $todayFormatted
    }
    else {
        # 检查日期值是否为空
        if ([string]::IsNullOrEmpty($dateValue)) {
            # 使用今天的日期
            $row.'date' = $todayFormatted
        }
        else {
            # 按照格式分割日期
            $dateParts = $dateValue -split '-'
            
            if ($dateParts.Count -eq 3) {
                # 获取年、月、日部分
                $year = $dateParts[0]
                $month = $dateParts[1]
                $day = $dateParts[2]
                
                # 处理月份与日期：如果为单位数则补0
                if ($month.Length -eq 1) {
                    $month = "0" + $month
                }
                if ($day.Length -eq 1) {
                    $day = "0" + $day
                }
                
                # 重新组合日期
                $row.'date' = "$year-$month-$day"
            }
            else {
                # 如果日期格式不正确，设置为今天
                Write-Warning "日期格式不正确: '$dateValue'，已设置为今天的日期"
                $row.'date' = $todayFormatted
            }
        }
    }
    
    # 返回处理后的行
    $row
}

# 6. 按 brand 和 model 列升序排序
$sortedData = $processedData | Sort-Object -Property @("brand", "model")

# 7. 导出回原文件，不使用引号
$sortedData | Export-Csv -Path $path -NoTypeInformation -Encoding UTF8 -Force -UseQuotes Never

Write-Host "成功处理行数: $($sortedData.Count)" -ForegroundColor Green
