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
        e = 'C:/Users/admin/PycharmProjects/wy/wy_dh/data/合同台账2019-12-02.xlsx'
        reader = ExcelReader(e, title_line=True)
        i = 0
        amount = '1'
        ContractMPage(self.driver).add_contracts(
            code=reader.data[i]['东恒-业主合同编号'] + str(random.randint(000, 999)),  # 合同编号
            oldCode=reader.data[i]['原合同编号'],  # 原合同编号
            catalog=reader.data[i]['合同分类2'],  # 合同分类2
            startTime=reader.data[i]['合同起时间'],  # 合同起时间
            endTime=reader.data[i]['合同止时间'],  # 合同止时间
            useStartTime=reader.data[i]['租金首次支付开始时间'],  # 租金首次支付开始时间
            useEndTime=reader.data[i]['租金首次支付结束时间'],  # 租金首次支付结束时间
            tenements_name=reader.data[i]['基站名称'],  # 基站名称
            tenements_address=reader.data[i]['租赁地址'],  # 地址
            tenements_contact=reader.data[i]['出租方联系人'],  # 联系人
            tenements_mobile=reader.data[i]['联系电话'],  # 电话
            tenements_payPurpose=reader.data[i]['基站缩略名称'],  # 基站名称缩略名
            signatory='签订人',  # 签订人
            annualAmount=reader.data[i]['业主合同金额(元/年)'],  # 合同年金额
            firstRent=reader.data[i]['业主租金首次支付金额'],  # 首次支付金额
            rentCycle=reader.data[i]['业主租金后续支付周期（月）'],  # 后续支付周期
            firstCycle=reader.data[i]['租金首次支付周期（月)'],  # 首次支付周期
            receiveDate=reader.data[i]['收单日期'],  # 收单日期
            signDate=reader.data[i]['A合同签订时间'],  # 签订日期
            rent=reader.data[i]['业主合同总金额'],  # 合同总金额
            deposit=reader.data[i]['押金'],  # 押金
            partyA=reader.data[i]['出租方'],  # 甲方
            partyB='',  # 乙方
            partyC='',  # 丙方
            classification=reader.data[i]['业主分类'],  # 对公对私类别
            coefficient='',  # 租金转化系数
            area=reader.data[i]['面积'],  # 面积
            followPerson=reader.data[i]['跟进人'],  # 跟进人
            memo=reader.data[i]['A合同备注'],  # 备注
            electricityFeeRate=reader.data[i]['业主电费费率（元/度）'],  # 电费费率
            electricityFeeCycle=reader.data[i]['电费缴费周期（月）'],  # 电费的缴费周期
            contact=reader.data[i]['出租方联系人'],  # 出租方联系人
            mobile=reader.data[i]['联系电话'],  # 联系电话
            eleAccountName1=reader.data[i]['业主户名'],  # 电费业主账户户名1
            eleBankName1=reader.data[i]['业主开户行'],  # 电费业主开户行1
            eleBankAccountNo1=reader.data[i]['业主账号'],  # 电费业主账号1
            rentAccountName1=reader.data[i]['业主户名'],  # 房租业主账户户名1
            rentBankName1=reader.data[i]['业主开户行'],  # 房租业主开户行1
            rentBankAccountNo1=reader.data[i]['业主账号']  # 房租业主账号1
        )
        sleep(2)
        ContractMPage(self.driver).payment_plan(amount)

    # 正常房租合同
    def test_add_Contract2(self):
        e = 'C:/Users/admin/PycharmProjects/wy/wy_dh/data/合同台账2019-12-02.xlsx'
        reader = ExcelReader(e, title_line=True)
        i = 1
        amount = '2'
        ContractMPage(self.driver).add_contracts(
            code=reader.data[i]['东恒-业主合同编号'] + str(random.randint(000, 999)),  # 合同编号
            oldCode=reader.data[i]['原合同编号'],  # 原合同编号
            catalog=reader.data[i]['合同分类2'],  # 合同分类2
            startTime=reader.data[i]['合同起时间'],  # 合同起时间
            endTime=reader.data[i]['合同止时间'],  # 合同止时间
            useStartTime=reader.data[i]['租金首次支付开始时间'],  # 租金首次支付开始时间
            useEndTime=reader.data[i]['租金首次支付结束时间'],  # 租金首次支付结束时间
            tenements_name=reader.data[i]['基站名称'],  # 基站名称
            tenements_address=reader.data[i]['租赁地址'],  # 地址
            tenements_contact=reader.data[i]['出租方联系人'],  # 联系人
            tenements_mobile=reader.data[i]['联系电话'],  # 电话
            tenements_payPurpose=reader.data[i]['基站缩略名称'],  # 基站名称缩略名
            signatory='签订人',  # 签订人
            annualAmount=reader.data[i]['业主合同金额(元/年)'],  # 合同年金额
            firstRent=reader.data[i]['业主租金首次支付金额'],  # 首次支付金额
            rentCycle=reader.data[i]['业主租金后续支付周期（月）'],  # 后续支付周期
            firstCycle=reader.data[i]['租金首次支付周期（月)'],  # 首次支付周期
            receiveDate=reader.data[i]['收单日期'],  # 收单日期
            signDate=reader.data[i]['A合同签订时间'],  # 签订日期
            rent=reader.data[i]['业主合同总金额'],  # 合同总金额
            deposit=reader.data[i]['押金'],  # 押金
            partyA=reader.data[i]['出租方'],  # 甲方
            partyB='',  # 乙方
            partyC='',  # 丙方
            classification=reader.data[i]['业主分类'],  # 对公对私类别
            coefficient='',  # 租金转化系数
            area=reader.data[i]['面积'],  # 面积
            followPerson=reader.data[i]['跟进人'],  # 跟进人
            memo=reader.data[i]['A合同备注'],  # 备注
            electricityFeeRate=reader.data[i]['业主电费费率（元/度）'],  # 电费费率
            electricityFeeCycle=reader.data[i]['电费缴费周期（月）'],  # 电费的缴费周期
            contact=reader.data[i]['出租方联系人'],  # 出租方联系人
            mobile=reader.data[i]['联系电话'],  # 联系电话
            eleAccountName1=reader.data[i]['业主户名'],  # 电费业主账户户名1
            eleBankName1=reader.data[i]['业主开户行'],  # 电费业主开户行1
            eleBankAccountNo1=reader.data[i]['业主账号'],  # 电费业主账号1
            rentAccountName1=reader.data[i]['业主户名'],  # 房租业主账户户名1
            rentBankName1=reader.data[i]['业主开户行'],  # 房租业主开户行1
            rentBankAccountNo1=reader.data[i]['业主账号']  # 房租业主账号1
        )
        sleep(2)
        ContractMPage(self.driver).payment_plan(amount)


if __name__ == '__main__':
    unittest.main()
