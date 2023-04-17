class CookieManager:
    @staticmethod
    def getCookies(request):
        cookies = []
        requestcookies = request.headers['cookie']
        response = request.response.headers.__str__()

        for line in response.split("\n"):
            if(line.split(':')[0]=="Set-Cookie"):
                responsecookies  = line.split(':')[1]
                name = responsecookies.split(";")[0].split("=")[0]
                value = responsecookies.split(";")[0].split("=")[1]
                cookies.append({"name":name,"value":value})
        
        if(requestcookies is not None):
            for cookie in requestcookies.split(";"):
                name = cookie.split("=")[0]
                value = cookie.split("=")[1]
                cookies.append({"name":name,"value":value})
        return cookies
