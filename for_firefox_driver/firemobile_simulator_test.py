import unittest
import time
from selenium import webdriver
from selenium.webdriver import FirefoxProfile

# SeleniumでFiremobileSimulatorを使ってみるサンプル
#
# refs:
# [まこちの技術情報覚え書き　SeleniumとFireMobileSimulatorの連携](http://wavetalker.blog134.fc2.com/blog-entry-76.html)
# [seleniumでガラケー環境を構築したい人必見！mac上のseleniumでFireMobileSimulatorを動かす方法はこれだ。 \- Qiita](http://qiita.com/hayakawatomoaki/items/6be743ba98cd8ad41248)
class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        profile = FirefoxProfile(self.getProfileData());
        self.browser = webdriver.Firefox(profile)
        self.addCleanup(self.browser.quit)

    def getProfileData(self):
        # ファイルから読み込み、1行目にプロファイルのフルパスが書いてある想定
        f = open('.FireMobileSimulatorSettings')
        lines = f.read()
        f.close()
        lineArray = lines.split('\n')
        for line in lineArray:
            return line
        return

    def testPageOpen(self):
        self.browser.get('http://google.com')
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
