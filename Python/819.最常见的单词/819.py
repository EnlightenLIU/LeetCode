class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        for i in paragraph:
            if (not i.isalpha() and i != ' '):
                paragraph = paragraph.replace(i, '')
                # paragraph.lower()
        list1 = paragraph.split()
        list2=[]
        for i in list1:
            i.strip()
            list2.append(i)

        a = dict()
        for i in list2:
            if a.get(i, 0):
                a[i] += 1
            else:
                a[i] = 1
        a = sorted(a.items(), key=lambda x: x[1], reverse=True)
        length=len(a)
        for i in range(length):
            if a[i][0] not in banned:
                return a[i][0]
            else:
                continue
