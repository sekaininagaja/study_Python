#! python3
# readCensusExcel.py - 人口と各郡の国勢調査区域の数を表にします。

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
county_data = {}

# countyDataに各郡の人口および区域を入力します。
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # スプレッドシートの各行には、1つの国勢調査区域のデータがあります
    state  = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop    = sheet['D' + str(row)].value

    # この状態のキーが存在することを確認
    county_data.setdefault(state, {})

    # この州のこの郡のキーが存在することを確認
    county_data[state].setdefault(county, {'tracts':0, 'pop':0})

    # 各行は1つの国勢調査地帯を表しますので、1ずつ増加します。
    county_data[state][county]['tracts'] += 1

    # この国勢調査区のポップで郡ポップを増やしてください。
    county_data[state][county]['pop'] += int(pop)

# 新しいテキストファイルを開き、それにcountyDataの内容を書き込む
print('Writing results...')
result_file = open('census2010.py', 'w')
result_file.write('allData = ' + pprint.pformat(county_data))
result_file.close()
print('Done.')
