# coding=utf-8
import os


WEBSITE_INFO = {"website_name": u"example大学 OnlineJudge",
                "website_name_shortcut": u"example oj",
                "website_footer": u"example大学信息学院<a href=\"http://www.miibeian.gov.cn/\">京ICP备xxxxx号-1</a>",
                # url结尾没有/
                "url": u"https://your-domain-or-ip.com"}


SMTP_CONFIG = {"smtp_server": "smtp.xxx.com",
               "email": "noreply@xxx.com",
               "password": os.environ.get("smtp_password", "111111"),
               "tls": False}

# please set your own SECRET_KEY to a long random string
# SECRET_KEY = "123456"


