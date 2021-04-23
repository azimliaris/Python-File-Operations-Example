import os
import shutil
import xml.etree.cElementTree as ET

List, trueList, falseList = [], [], []


def remove_duplicates(listName):
    res = []
    for x in listName:
        if x not in res:
            res.append(x)

    return res


def Diff(li1, li2):
    li_dif = [y for y in li1 + li2 if y not in li1 or y not in li2]
    return li_dif


def createFolder(directoryLocation):
    try:
        if not os.path.exists(directoryLocation):
            os.makedirs(directoryLocation)

    except OSError:
        print('Error: Creating directory. ' + directoryLocation)


createFolder(r'C:\MMI_Dataset_Splitted') #need to change root

createdFolderPath = r'C:\MMI_Dataset_Splitted' #need to change root

directory = r"C:\mmi-facial-expression-database_download_2020-12-13_20_07_13" #need to change root
for roots, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('oao_aucs.xml'):

            print(type(file))

            path = roots + chr(92) + file
            print(path)

            tree = ET.parse(path)
            root = tree.getroot()

            for child in root:
                if child.tag == "ActionUnit":
                    print(child.get("Number"))
                    createFolder(createdFolderPath + chr(92) + "AU" + child.get("Number") + "_True")
                    List.append(child.get("Number"))
                    createFolder(createdFolderPath + chr(92) + "AU" + child.get("Number") + "_False")

ListWoutR = remove_duplicates(List)
print(ListWoutR)

for roots, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('oao_aucs.xml'):

            path = roots + chr(92) + file
            print(path)

            tree = ET.parse(path)
            root = tree.getroot()

            for child in root:

                if child.tag == "ActionUnit":
                    n = child.get("Number")
                    print(n)

                    i = 0
                    while i < len(ListWoutR):

                        if ListWoutR[i] == n:
                            trueList.append(ListWoutR[i])
                        i += 1

            fileForAVI = file.replace("-oao_aucs.xml", ".avi")
            pathForAVI = roots + chr(92) + fileForAVI

            print(pathForAVI)

            j = 0
            while j < len(trueList):
                shutil.copy(pathForAVI, createdFolderPath + chr(92) + "AU" + trueList[j] + "_True")
                j += 1

            falseList = Diff(ListWoutR, trueList)

            j = 0
            while j < len(falseList):
                shutil.copy(pathForAVI, createdFolderPath + chr(92) + "AU" + falseList[j] + "_False")
                j += 1

            trueList.clear()
            falseList.clear()

