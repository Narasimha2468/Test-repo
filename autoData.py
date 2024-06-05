# import re
# import pdfplumber
# import requests

# def can(path, password=None):
#     plumberList = []
#     password = [None,
#                 '46312230']
#     for pwd in password:
#         try:
#             with pdfplumber.open(path, password=pwd) as f:
#                 for i in f.pages:
#                     plumberList.append(i.extract_tables())
#             break
#         except:
#             pass
#     validPlumberList = []
#     for i in plumberList:
#         for j in i:
#             for k in j:
#                 validPlumberList.append(k)
#     opening_bal = None
#     opening_balance = []
#     finaldata = []
#     # print(pwd)
#     if pwd == None:
#         for lines in validPlumberList:
#             # print(lines, len(lines))
#             DateExist = re.search("..-...-..", lines[0])
#             convertdate= "%d-%b-%y"
#             if DateExist:
#                 # print(lines)
#                 del lines[1]
#                 del lines[1]
#                 ChNo = lines[1]
#                 del lines[1]
#                 lines.insert(2, ChNo)
#                 lines[1] = re.sub("\n", " ", lines[1])
#                 try:
#                     if re.search("B/F.*", lines[1]):
#                         opening_bal = lines[-1]
#                         opening_bal = opening_bal.replace(",", "")
#                         opening_bal = re.sub("C.*|D.*", "", opening_bal)
#                         opening_balance.append(opening_bal)
#                         # print(opening_bal)
#                         continue
#                 except:pass
#                 # print(lines)
#                 finaldata.append(lines)
#         if len(finaldata)==0:
#             try:
#                 for count in range(len(validPlumberList)):
#                     lines = validPlumberList[count]
#                     if lines[1]==None:continue
#                     try:
#                         if re.search('OPENING_BALANCE',lines[6]):
#                             opening_bal = lines[-1]
#                             opening_bal = opening_bal.replace(",", "")
#                             opening_bal = re.sub("C.*|D.*", "", opening_bal)
#                             opening_balance.append(opening_bal)
#                             # print(opening_bal)
#                             continue
#                     except:pass
#                     if lines[0]=='':continue
#                     if re.search('DATE', lines[2]):continue
#                     datexist = re.search("^\d{2}-\d{2}-\d{2,4}$", lines[2])
#                     convertdate= "%d-%m-%Y"
#                     if datexist and len(lines)>10:
#                         if re.search('\d+',lines[0]):del lines[0]
#                         if not re.search("^\d{2}-\d{2}-\d{2,4}$",lines[0]):del lines[0]
#                         del lines[1]
#                         for ele in lines:
#                             if ele==None or ele=='None':lines.remove(ele)
#                         del lines[3]
#                         if lines[3]==None:del lines[3]
#                         if re.search('\d+',lines[-4]):
#                             lines[-4]=lines[1]
#                             del lines[1]
#                         finaldata.append(lines)
#                         # print(lines, len(lines))
#             except:pass
#     else:
#         for lines in validPlumberList:
#             if re.search('Date',lines[0]):continue
#             try:
#                 if re.search('OPENING_BALANCE',lines[1]):
#                     opening_bal = lines[-1]
#                     opening_bal = opening_bal.replace(",", "")
#                     opening_bal = re.sub("C.*|D.*", "", opening_bal)
#                     opening_balance.append(opening_bal)
#                     # print(opening_bal)
#                     continue
#             except:pass
#             convertdate = "%d-%b-%y"
#             if len(lines)==5:
#                 lines.insert(2,'')
#             # print(lines, len(lines))
#             finaldata.append(lines)
            

#     try:    
#         for row in finaldata:
#             row[-1] = row[-1].replace(",", "")
#             row[-2] = row[-2].replace(",", "")
#             row[-3] = row[-3].replace(",", "")
#             row[1] = re.sub("\n", "", row[1]).strip()
#             row[2] = re.sub("^0*", "", row[2]).strip()
#             row[2] = row[2][-6:]
#             row[2] = re.sub("^0*", "", row[2]).strip()
#             for val in range(3, 5):
#                 if row[val] == "0.00":
#                     row[val] = row[val].replace("0.00", "")
#             if row[4]!='':row[2]=''
#             row[0] = datetime.strptime(row[0], convertdate).strftime("%d-%b-%Y").upper()
#             # print(row, len(row))
#     except:pass
    
#     if len(opening_balance)>0:opening_bal=opening_balance[0]
#     pypdf2data = enPdfToText(path,"46312230")
#     # if len(opening_balance)>0:opening_bal=opening_balance[0]
#     # else:print(pypdf2data)
#     # print(pypdf2data)
#     pypdf2data = re.sub(" +", " ", pypdf2data)
#     # accno = re.search("Account Nu.*|Account No.*", pypdf2data)
#     # accno = re.findall("\d+", accno[0])
#     # accno = accno[0]
#     # # accno = re.sub("^0*", "", accno)
#     period_0 = re.search("Period.*.\\d{2,4}|period.*.\\d{2,4}|BETWEEN.*.\\d{2,4}", pypdf2data)
#     period = re.findall("\d+|\\b\w{3}\\b", period_0[0])
#     brsdate = []
#     d = {}
#     if len(period)>6:
#         test_period = re.findall("\\b\w{3}\\b", period_0[0])
#         for i in test_period:
#             if i not in d:d[i]=1
#             else:d[i]+=1
#         for k,v in d.items():
#             if v!=2:period.remove(k)
#     if len(period)==6:
#         for p in range(0, len(period), 3):
#             demolist = []
#             demolist.append(period[0 + p])
#             demolist.append(period[1 + p])
#             demolist.append(period[2 + p])
#             date = "-".join(demolist)
#             try:
#                 try:
#                     date = datetime.strptime(date, "%d-%b-%Y").strftime("%d/%m/%Y")
#                 except:
#                     date = datetime.strptime(date, "%b-%d-%Y").strftime("%d/%m/%Y")
#             except:
#                 date = datetime.strptime(date, "%d-%m-%Y").strftime("%d/%m/%Y")
#             brsdate.append(date)
#     reconcilitionperiod = [brsdate[0], brsdate[-1], finaldata, opening_bal]
#     return reconcilitionperiod

import pdfplumber

def fbl(path):
    plumberList = []
    with pdfplumber.open(path) as f:
        for i in f.pages:
            plumberList.append(i.extract_tables())
    
    validPlumberList = []
    for i in plumberList:
        for j in i:
            for k in j:
                validPlumberList.append(k)
    
    # extracted_data = []
    # for table in validPlumberList:
    #     table_data = []
    #     for row in table:
    #         row_data = []
    #         for cell in row:
    #             row_data.append(cell)
    #         table_data.append(row_data)
    #     extracted_data.append(table_data)
    
    return validPlumberList

# Example usage:
path_to_pdf = r"d:\pycharmtest\Testdata\PDFData.pdf"
data = fbl(path_to_pdf)
# print(data)
for i in data:
    print(i)