from fbrecog import FBRecog
path = 'testImage.jpeg' # Insert your image file path here
access_token = 'EAACEdEose0cBALgQMQth0GyOdIpSZC7kH43Lgu7sSXfHVrZAaHicPgNZBwJIInfxV5ZCAdZCagwO3s5rY6klTwfI6m6m5igwTZAnhqifXf46bvROsHtX3jwZC7PIyHZAGYTtxXA7dfuoRLmucFnYkZBZAztmWIkNgZBWD8xSzQpBd2aJdqFZCVUxt5qAJ1ThBd91XQZCZAd8hymby6nwZDZD' # Insert your access token obtained from Graph API explorer here
cookie = 'datr=cseJVp9ub9shekJt2sfuk-uz; sb=FyiSV40mGEh1Z3jGeOw24Hy1; pl=n; lu=gAIVAxL6LqjM1dAYxmdDChMw; js_ver=2791; c_user=100002351237868; xs=223%3A6DmKM_o7Ljn32A%3A2%3A1502545869%3A18515%3A3016; fr=08zf3ntPbgtKbQiD6.AWU4YtNpPw_7sRn5-Rl63OciF-w.BZjwU0.Fw.FmY.0.0.BZnlcp.AWWpoF4h; presence=EDvF3EtimeF1503551295EuserFA21B02351237868A2EstateFDt3F_5bDiFA2user_3a1B06035175738A2ErF1EoF1EfF2C_5dEutc3F1503551153155G503551295024CEchFDp_5f1B02351237868F19CC; act=1503551297611%2F19; wd=606x651' # Insert your cookie string here
fb_dtsg = 'AQEEIMgB2iZF:AQE9c9WWhGuI' # Insert the fb_dtsg parameter obtained from Form Data here.
# Instantiate the recog class
recog = FBRecog(access_token, cookie, fb_dtsg)
# Recog class can be used multiple times with different paths
print(str(recog.recognize(path)[0]['name']))
