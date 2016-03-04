class Item:

    def __init__(self, positionName, salary, workYear, positionFirstType, positionSecondType, companyName, city, education,companySize,financeStage, industryField):
        self.positionName = positionName
        self.salary = salary
        self.workYear = workYear
        self.positionFirstType = positionFirstType
        self.positionSecondType = positionSecondType
        self.companyName = companyName
        self.city = city
        self.education = education
        self.companySize = companySize
        self.financeStage = financeStage
        self.industryField = industryField

    def toString(self):
        return (self.positionName, self.salary.encode('utf-8'), self.workYear.encode('utf-8'), self.positionFirstType.encode('utf-8'), self.positionSecondType.encode('utf-8'), self.companyName.encode('utf-8'), self.city.encode('utf-8'), self.education.encode('utf-8'), self.companySize.encode('utf-8'), self.financeStage.encode('utf-8'), self.industryField.encode('utf-8'))
