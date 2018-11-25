import difflib
from difflib import SequenceMatcher

s1='河北省秦皇岛市长江东道80号'
s2='河北省秦皇岛市海港区长江东道80号'
s3='河北省秦皇岛市开发区长江东道80号'
diff = SequenceMatcher(lambda x: x in " \t",s1,s2)
print('s1 and s2 ratio is %s'%diff.ratio())