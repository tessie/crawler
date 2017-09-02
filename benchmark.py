import timeit
import matplotlib.pyplot as plt

def benchmark_crawler(depth):
  SETUP = "from crawler import Crawler;depth ={}".format(depth)

  times  = timeit.repeat(setup = SETUP,
                      stmt = "crawler = Crawler(depth); crawler.crawl(['http://python.org'])",
                      number = 3)
  return sum(times)/3

print "Time to crawl 4 urls {} sec". format(benchmark_crawler(4))
print "Time to crawl 8 urls {} sec".format(benchmark_crawler(8))
print "Time to crawl 16 urls {} sec".format(benchmark_crawler(16))
print 'Time to crawl 32  urls {} sec'.format(benchmark_crawler(32))
print 'Time to crawl 64  urls {} sec'.format(benchmark_crawler(64))
print 'Time to crawl 100  urls {} sec'.format(benchmark_crawler(100))


# Time to crawl 4 urls 25.0314807097 sec
# Time to crawl 8 urls 31.137188673 sec
# Time to crawl 16 urls 63.5950013002 sec
# Time to crawl 32  urls 123.348069668 sec
# Time to crawl 64  urls 262.172393322 sec