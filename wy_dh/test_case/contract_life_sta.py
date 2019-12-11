# -*-coding:utf-8-*-
import unittest
from time import sleep
import unittest, random, sys

sys.path.append("./models")
sys.path.append("./page_obj")
from wy_dh.test_case.models import myunit, function
from wy_dh.test_case.page_obj.TenementsPage import *
from wy_dh.test_case.page_obj.ContractMPage import *
from wy_dh.test_case.page_obj.DayCheckPage import *
from wy_dh.test_case.page_obj.PaymentsPage import *
from wy_dh.test_case.page_obj.loginPage import login


class ContractLife(myunit.MyTest):
    def test_contractlife(self):
        imgpath = r'C:/Users/admin/PycharmProjects/wy/wy_dh/data/contact.jpg'
        e = 'C:/Users/admin/PycharmProjects/wy/wy_dh/data/合同台账2019-12-02.xlsx'
        reader = ExcelReader(e, title_line=True)
        i = 55
        # 新增合同
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
        sleep(1)
        innerCode = ContractMPage(self.driver).get_innerCode()
        sleep(1)
        # 生成B合同
        ContractMPage(self.driver).AtoB(
            innerCode=innerCode,
            contactname='A',
        )
        # 回访
        ContractMPage(self.driver).return_contracts(
            innerCode=innerCode,
            contactname='A',
        )
        # A合同审核通过
        ContractMPage(self.driver).A_contact_pass(
            innerCode=innerCode,
            contactname='A',
        )
        # B合同审核通过
        ContractMPage(self.driver).B_contact_pass(
            innerCode=innerCode,
            contactname='B',
            code=reader.data[i]['东恒-铁通合同编号'] + str(random.randint(000, 999))
        )

        # 基站电表信息 添加电表
        other_windowns_url_2 = 'http://wy.dhwl66.com:8001/dhwy/tenements/load'
        TenementsPage(self.driver).open_other_windowns(other_windowns_url_2, 2)
        TenementsPage(self.driver).add_tenementammeters(innerCode=innerCode,
                                                        chinaCode=str(random.randint(0000000000, 9999999999)),
                                                        chinaMobileInitNumber=str(random.randint(0000, 9999)),
                                                        lastNumber=str(random.randint(000, 999)),
                                                        lastCheckoutDate=reader.data[i]['合同起时间'],
                                                        ratio='1'
                                                        )

        # 新增抄表中抄表
        other_windowns_url_3 = 'http://wy.dhwl66.com:8001/dhwy/day/load'
        TenementsPage(self.driver).open_other_windowns(other_windowns_url_3, 3)
        DayCheckPage(self.driver).day_check(imgpath, innerCode)

        # 电费回访 审核 导出
        other_windowns_url_3 = 'http://wy.dhwl66.com:8001/dhwy/payments/load'
        TenementsPage(self.driver).open_other_windowns(other_windowns_url_3, 4)
        PaymentsPage(self.driver).PayBefore(innerCode=innerCode)
        sleep(1)
        PaymentsPage(self.driver).payments_pass(innerCode=innerCode)
        sleep(1)
        PaymentsPage(self.driver).export_payments(innerCode=innerCode, payType='电费')
