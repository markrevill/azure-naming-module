from urllib.request import urlopen

sourceUrl = "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/master/articles/azure-resource-manager/management/resource-name-rules.md"
sourceFile = (urlopen(sourceUrl).read()).decode()

outputFile = "output.csv"
w = open(outputFile, "w")

w.write("Provider Type,Length\n")

for line in sourceFile.splitlines():
    if "## Microsoft." in line:
        serviceType = line.lstrip('## ')
    elif ("> |" in line and "Entity" not in line and "---" not in line):
    # elif ("> |" in line and "Entity" not in line and "---" not in line and "/" not in line):
        resource = line.rstrip(' |')
        resource = resource.lstrip('> | ')
        resource = resource.replace('<br><br>', ' ')
        resource = resource.replace("Can't use:<br>", 'NOT:')
        resource = resource.replace(" / ", "/")
        resource = resource.replace(' | ', '~')
        # resource = resource.replace(")<br>", "), ")
        # resource = resource.replace("Can't use:", '!=')
        sourceData = (serviceType + "~" + resource + "\n")
        data = sourceData.split("~")
        length = data[3].split(" ")
        w.write(data[0] + "/" + data[1] + "," + length[0] + "\n")
w.close()
