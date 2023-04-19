class ParamsManager:
    @staticmethod
    def getParams(url):
        urlparams = url.split("?")
        params = []
        if(len(urlparams)==2):
            for param in urlparams[1].split("&"):
                if(len(param.split("="))==2):
                    key = param.split("=")[0]
                    value = param.split("=")[1]
                    params.append((key,value))
        return params
    

# example o fuse
""""
a =ParamsManager.getParams("http://google.com/?a=21&b=432423432&c=4242423")
for key,value in a:
    print(key,value)
"""
