from dl import DL

class BL:
    def __init__(self) -> None:
        pass

    def filter(self, name, rom, ram, page):
        dl = DL()
        result = []
        totalRecord = 0
        if name == "":
            result = dl.getAll(rom, ram)
            
        else:
            candidate = dl.getPhoneMatching(name)

            if len(candidate) == 0:
                serviceResult = {}
                serviceResult["totalRecord"] = 0
                serviceResult["data"] = []
                return serviceResult

            lstCandidate = []
            for item in candidate:
                lstCandidate.append(item["_source"])

            result = dl.getPhone(lstCandidate)

            if rom != "" and ram == "":
                result = list(filter(lambda x: x.get("Memory") == int(rom), result))
            elif rom == "" and ram != "":
                result = list(filter(lambda x: x.get("Ram") == int(ram), result))
            elif rom != "" and ram != "":
                result = list(filter(lambda x: x.get("Memory") == int(rom) and x.get("Ram") == int(ram), result))
            
        if page == "":
            page = 0
        elif type(page) != int:
            page = int(page)
        
        totalRecord = len(result)
        if(totalRecord > 0):
            result = result[page : page + 10]

        serviceResult = {}
        serviceResult["totalRecord"] = totalRecord
        serviceResult["data"] = result
        return serviceResult