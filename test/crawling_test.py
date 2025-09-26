import jaycode

core = jaycode.Core()

core.Crawling.init(auto_quit=True,secret=True)
core.Crawling.open("https://www.google.com")