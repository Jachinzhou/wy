# -*-coding:utf-8-*-
import unittest
from time import sleep
import unittest, random, sys

sys.path.append("./models")
sys.path.append("./page_obj")
from wy_dh.test_case.models import myunit, function
from wy_dh.test_case.page_obj.ContractMPage import *
from wy_dh.test_case.page_obj.loginPage import login


class ContractMTest(myunit.MyTest):

    # 正常房租+电费合同
    def test_add_Contract1(self):
        amount = '1'
        # login(self.driver).user_login(username='周继成', password='12345678')
        # sleep(1)
        # self.driver.get('http://wy.dhwl66.com:8001/dhwy/contracts/load')
        # sleep(2)
        ContractMPage(self.driver).add_contracts(code=random.randint(0000000000, 9999999999),
                                            oldCode='原合同编号',
                                            catalog='房租+电费',
                                            startTime='2019-07-01',
                                            endTime='2021-06-30',
                                            useStartTime='2019-07-01',
                                            useEndTime='2020-06-30',
                                            tenements_name='基站名称',
                                            tenements_address='地址',
                                            tenements_contact='联系人张三',
                                            tenements_mobile='15369585545',
                                            tenements_payPurpose='基站名称缩略名',
                                            signatory='签订人',
                                            annualAmount='1200',
                                            firstRent='1200',
                                            rentCycle='12',
                                            firstCycle='12',
                                            receiveDate='2019-6-01',
                                            signDate='2019-07-11',
                                            rent='2400',
                                            deposit='0',
                                            partyA='甲方',
                                            partyB='',
                                            partyC='',
                                            classification='对私',
                                            coefficient='1.15',
                                            area='233',
                                            followPerson='俞夏雨',
                                            memo='memo',
                                            electricityFeeRate='1.2345',
                                            electricityFeeCycle='1',
                                            contact='联系人李四',
                                            mobile='15364995954',
                                            eleAccountName1='吴远新',
                                            eleBankName1='招商银行深圳龙岗碧湖支行',
                                            eleBankAccountNo1='6214867800913668',
                                            rentAccountName1='邓海新',
                                            rentBankName1='农业银行深圳龙岗支行',
                                            rentBankAccountNo1='6228480120631299316'
                                            )
        sleep(2)
        ContractMPage(self.driver).payment_plan(amount)


    # 正常房租合同
    def test_add_Contract2(self):
        amount = '2'
        # login(self.driver).user_login(username='周继成', password='12345678')
        # sleep(1)
        # self.driver.get('http://wy.dhwl66.com:8001/dhwy/contracts/load')
        # sleep(2)
        ContractMPage(self.driver).add_contracts(code=random.randint(0000000000, 9999999999),
                                            oldCode='原合同编号',
                                            catalog='房租',
                                            startTime='2019-07-01',
                                            endTime='2021-06-30',
                                            useStartTime='2019-07-01',
                                            useEndTime='2020-06-30',
                                            tenements_name='基站名称',
                                            tenements_address='地址',
                                            tenements_contact='联系人张三',
                                            tenements_mobile='15369585545',
                                            tenements_payPurpose='基站名称缩略名',
                                            signatory='签订人',
                                            annualAmount='1200',
                                            firstRent='1200',
                                            rentCycle='12',
                                            firstCycle='12',
                                            receiveDate='2019-6-01',
                                            signDate='2019-07-11',
                                            rent='2400',
                                            deposit='0',
                                            partyA='甲方',
                                            partyB='',
                                            partyC='',
                                            classification='对私',
                                            coefficient='1.15',
                                            area='233',
                                            followPerson='俞夏雨',
                                            memo='memo',
                                            electricityFeeRate='1.2345',
                                            electricityFeeCycle='1',
                                            contact='联系人李四',
                                            mobile='15364995954',
                                            eleAccountName1='吴远新',
                                            eleBankName1='招商银行深圳龙岗碧湖支行',
                                            eleBankAccountNo1='6214867800913668',
                                            rentAccountName1='邓海新',
                                            rentBankName1='农业银行深圳龙岗支行',
                                            rentBankAccountNo1='6228480120631299316'
                                            )
        sleep(2)
        ContractMPage(self.driver).payment_plan(amount)


if __name__ == '__main__':
    unittest.main()
