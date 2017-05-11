s="Let's take LeetCode contest"
print s
s=[ t[::-1] for t in s.split(' ')]
print ' '.join(s)
# complexity is O(n) + O(n) + O(k) = 2O(n)+O(k)=O(n)