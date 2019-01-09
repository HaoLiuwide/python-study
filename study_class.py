import math


def getNumber():
    nums = []
    xtr = input('Enter a number(<Enter to quit>): ')
    while xtr != '':
        try:
            x = float(xtr)
            nums.append(x)
            xtr = input('Enter a number(<Enter to quit>): ')
        except ValueError:
            xtr = input('Enter a number(<Enter to quit>): ')
    return nums


def mean(nums):
    nums_sum = 0
    count = 0
    for i in nums:
        nums_sum += i
        count += 1
    average = nums_sum/count
    return average


def stdDev(nums):
    nums_mean = mean(nums)
    dev = 0
    count = 0
    for i in nums:
        dev += (i - nums_mean)**2
        count += 1
    nums_std = math.sqrt(dev/(count - 1))
    return nums_std


def median(nums):
    nums.sort()
    size = len(nums)
    median_size = size // 2
    if size % 2 == 0:
        nums_median = (nums[median_size] + nums[median_size+1])/2.0
    else:
        nums_median = int(nums[median_size])
    return nums_median


def main():
    nums = getNumber()
    nums_mean = mean(nums)
    nums_std = stdDev(nums)
    nums_median = median(nums)
    print('the mean of the numbers is: {0:0.4f}'.format(nums_mean).capitalize())
    print('the std of the numbers is: {0:0.4f}'.format(nums_std).capitalize())
    print('the median of the numbers is: {0:>5}'.format(nums_median).capitalize())


if __name__ == '__main__':
    main()
