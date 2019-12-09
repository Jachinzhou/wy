from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from wy_dh.test_case.page_obj.base import Page
from wy_dh.test_case.models.DataLoad import *
from wy_dh.test_case.models import function
from time import sleep
import random


class ContractMPage(Page):
    '''
    合同
    '''
    url = '/contracts/load'
    wy_lfn_add_contracts_loc = (By.XPATH, '/html/body/div[2]/div[2]/button[5]')  # 添加合同按钮
    wy_name_loc = (By.NAME, 'name')  # 合同名称
    wy_innerCode_loc = (By.NAME, 'innerCode')  # 合同档案号
    wy_code_loc = (By.NAME, 'code')  # 合同编号
    wy_oldCode_loc = (By.NAME, 'oldCode')  # 原合同编号
    wy_catalog_loc = (By.NAME, 'catalog')  # 合同分类
    wy_type_loc = (By.NAME, 'type')  # 合同类型
    wy_startTime_loc = (By.ID, 'startTime')  # 合同起时间
    wy_endTime_loc = (By.ID, 'endTime')  # 合同止时间
    wy_useStartTime_loc = (By.ID, 'useStartTime')  # 首次支付开始时间
    wy_useEndTime_loc = (By.ID, 'useEndTime')  # 首次支付结束时间

    wy_tenementName_loc = (By.NAME, 'tenementName')  # 物业单位
    wy_add_tenement_loc = (By.XPATH, '//*[@id="popwnd_tenements_getTenements"]/div[2]/div[1]/div[2]/button')  # 添加按钮
    wy_tenements_name_loc = (By.NAME, 'tenements_name')  # 基站名称
    wy_tenements_purpose_loc = (By.NAME, 'tenements_purpose')  # 项目类型
    wy_tenements_spec_loc = (By.NAME, 'tenements_spec')  # 基站类型
    wy_tenements_contractType_loc = (By.NAME, 'tenements_contractType')  # 合同类型
    wy_tenements_address_loc = (By.NAME, 'tenements_address')  # 租赁地址
    wy_tenements_contact_loc = (By.NAME, 'tenements_contact')  # 联系人
    wy_tenements_mobile_loc = (By.NAME, 'tenements_mobile')  # 联系电话
    wy_tenements_payPurpose_loc = (By.NAME, 'tenements_payPurpose')  # 基站缩略名称
    wy_tenements_memo_loc = (By.NAME, 'tenements_memo')  # 备注
    wy_tenements_Submit_loc = (By.XPATH, '(//*[@id="Submit"])[2]')  # 物业单位提交按钮
    wy_selected_tenements_loc = (By.XPATH, '//*[@id="tenementsDataTable"]/tbody/tr[1]')  # 选择物业单位列表第一个
    wy_selected_button_loc = (
        By.XPATH, '//*[@id="popwnd_tenements_getTenements"]/div[2]/div[2]/div/div[2]/button')  # 选择按钮

    wy_signatory_loc = (By.NAME, 'signatory')  # 签订人员
    wy_annualAmount_loc = (By.NAME, 'annualAmount')  # 合同年金额
    wy_firstRent_loc = (By.NAME, 'firstRent')  # 首次支付金额
    wy_rentCycle_loc = (By.NAME, 'rentCycle')  # 后续支付周期
    wy_firstCycle_loc = (By.NAME, 'firstCycle')  # 首次支付周期
    wy_receiveDate_loc = (By.ID, 'receiveDate')  # 收单日期
    wy_signDate_loc = (By.ID, 'signDate')  # 签订日期
    wy_rent_loc = (By.NAME, 'rent')  # 合同总金额
    wy_deposit_loc = (By.NAME, 'deposit')  # 押金
    wy_partyA_loc = (By.NAME, 'partyA')  # 甲方
    wy_partyB_loc = (By.NAME, 'partyB')  # 乙方
    wy_partyC_loc = (By.NAME, 'partyC')  # 丙方
    wy_classification_loc = (By.NAME, 'classification')  # 对公对私类别
    wy_coefficient_loc = (By.NAME, 'coefficient')  # 租金转化系数
    wy_area_loc = (By.NAME, 'area')  # 面积
    wy_followPerson_loc = (By.NAME, 'followPerson')  # 跟进人
    wy_memo_loc = (By.NAME, 'memo')  # 备注
    wy_electricityFeeRate_loc = (By.NAME, 'electricityFeeRate')  # 电费费率
    wy_electricityFeeCycle_loc = (By.NAME, 'electricityFeeCycle')  # 电费的缴费周期

    wy_account_tab_loc = (By.LINK_TEXT, '业主账户信息')  # 业主账户信息
    wy_contact_loc = (By.NAME, 'contact')  # 出租方联系人
    wy_mobile_loc = (By.NAME, 'mobile')  # 联系电话
    wy_eleAccountName1_loc = (By.NAME, 'eleAccountName1')  # 电费业主账户户名1
    wy_eleBankName1_loc = (By.NAME, 'eleBankName1')  # 电费业主开户行1
    wy_eleBankAccountNo1_loc = (By.NAME, 'eleBankAccountNo1')  # 电费业主账号1
    wy_eleRatio1_loc = (By.NAME, 'eleRatio1')  # 电费分账比例1
    wy_rentAccountName1_loc = (By.NAME, 'rentAccountName1')  # 房租业主账户户名1
    wy_rentBankName1_loc = (By.NAME, 'rentBankName1')  # 房租业主开户行1
    wy_rentBankAccountNo1_loc = (By.NAME, 'rentBankAccountNo1')  # 房租业主账号1
    wy_rentRatio1_loc = (By.NAME, 'rentRatio1')  # 房租分账比例1

    wy_Submit_loc = (By.XPATH, '//*[@id="Submit"]')  # 合同提交按钮

    wy_selected_contract_loc = (By.XPATH, '//*[@id="contractsDataTable"]/tbody/tr[1]')  # 选择合同列表第一个
    wy_edit_contracts_loc = (By.XPATH, '/html/body/div[3]/div/div[2]/button[15]')  # 合同编辑按钮
    wy_payment_plan_tab_loc = (By.XPATH, '//*[@id="tabs"]/ul/li[4]/a')  # 合同付款计划tab

    wy_innerCode_query_loc = (By.XPATH, '//*[@id="queryForm"]/input[1]')  # 合同名称查询框

    def query_innerCode(self, innerCode):
        self.find_element(*self.wy_innerCode_query_loc).clear()
        self.find_element(*self.wy_innerCode_query_loc).send_keys(innerCode)

    wy_tenementsname_query_loc = (By.XPATH, '//*[@id="queryForm"]/input[3]')  # 基站名称查询框

    def query_tenementsname(self, tenementsname):
        self.find_element(*self.wy_tenementsname_query_loc).clear()
        self.find_element(*self.wy_tenementsname_query_loc).send_keys(tenementsname)

    wy_contactname_query_loc = (By.XPATH, '//*[@id="queryForm"]/input[5]')  # 合同名称查询框

    def query_contactname(self, contactname):
        self.find_element(*self.wy_contactname_query_loc).clear()
        self.find_element(*self.wy_contactname_query_loc).send_keys(contactname)

    wy_query_loc = (By.XPATH, '//*[@id="queryForm"]/input[14]')  # 查询按钮

    def query_button(self):
        self.find_element(*self.wy_query_loc).click()

    wy_contractsImgs_tab_loc = (By.XPATH, '//*[@id="tabs"]/ul/li[3]/a')  # 合同图片tab

    def contractsImgs_tab(self):
        self.find_element(*self.wy_contractsImgs_tab_loc).click()

    wy_input_imgs_loc = (By.XPATH, '//*[@id="doc"]')  # 图片上传按钮

    def input_imgs(self, imgspath):
        self.find_element(*self.wy_input_imgs_loc).send_keys(imgspath)

    wy_contract_close_loc = (By.XPATH, '//*[@id="popwnd_Contracts_edit"]/div[1]/span[2]')  # 合同编辑界面关闭按钮

    def close_contract(self):
        self.find_element(*self.wy_contract_close_loc).click()

    wy_contract_status_loc = (By.NAME, 'status')  # 合同审核通过按钮

    def contract_status(self):
        self.find_element(*self.wy_contract_status_loc).click()

    wy_contract_return_loc = (By.XPATH, '/html/body/div[3]/div/div[2]/button[12]')  # 回访按钮

    def contract_return(self):
        self.find_element(*self.wy_contract_return_loc).click()

    wy_getinnercode_loc = (By.XPATH, '//*[@id="contractsDataTable"]/tbody/tr[1]/td[1]')  # 合同管理列表第一行合同档案号

    def innerCode(self):
        cls = self.find_element(*self.wy_getinnercode_loc).text
        return cls

    def get_innerCode(self):
        innerCode = self.innerCode()
        return innerCode

    def add_contracts_button(self):
        self.find_element(*self.wy_lfn_add_contracts_loc).click()

    def input_code(self, code):
        self.find_element(*self.wy_code_loc).send_keys(code)

    def input_oldCode(self, oldCode):
        self.find_element(*self.wy_oldCode_loc).send_keys(oldCode)

    def select_catalog(self, catalog):
        Select(self.find_element(*self.wy_catalog_loc)).select_by_visible_text(catalog)

    def input_startTime(self, startTime):
        self.find_element(*self.wy_startTime_loc).send_keys(startTime)

    def input_endTime(self, endTime):
        self.find_element(*self.wy_endTime_loc).send_keys(endTime)

    def input_useStartTime(self, useStartTime):
        self.find_element(*self.wy_useStartTime_loc).send_keys(useStartTime)

    def input_useEndTime(self, useEndTime):
        self.find_element(*self.wy_useEndTime_loc).send_keys(useEndTime)

    def add_tenementName(self):
        self.find_element(*self.wy_tenementName_loc).click()

    def add_tenement_Name(self):
        self.find_element(*self.wy_add_tenement_loc).click()

    def input_tenements_name(self, tenements_name):
        self.find_element(*self.wy_tenements_name_loc).send_keys(tenements_name)

    def input_tenements_address(self, tenements_address):
        self.find_element(*self.wy_tenements_address_loc).send_keys(tenements_address)

    def input_tenements_contact(self, tenements_contact):
        self.find_element(*self.wy_tenements_contact_loc).send_keys(tenements_contact)

    def input_tenements_mobile(self, tenements_mobile):
        self.find_element(*self.wy_tenements_mobile_loc).send_keys(tenements_mobile)

    def input_tenements_payPurpose(self, tenements_payPurpose):
        self.find_element(*self.wy_tenements_payPurpose_loc).send_keys(tenements_payPurpose)

    def add_tenements(self):
        self.find_element(*self.wy_tenements_Submit_loc).click()

    def selected_tenements(self):
        self.find_element(*self.wy_selected_tenements_loc).click()

    def select_button(self):
        self.find_element(*self.wy_selected_button_loc).click()

    def input_signatory(self, signatory):
        self.find_element(*self.wy_signatory_loc).send_keys(signatory)

    def input_annualAmount(self, annualAmount):
        self.find_element(*self.wy_annualAmount_loc).send_keys(annualAmount)

    def input_firstRent(self, firstRent):
        self.find_element(*self.wy_firstRent_loc).send_keys(firstRent)

    def input_rentCycle(self, rentCycle):
        self.find_element(*self.wy_rentCycle_loc).send_keys(rentCycle)

    def input_firstCycle(self, firstCycle):
        self.find_element(*self.wy_firstCycle_loc).send_keys(firstCycle)

    def input_receiveDate(self, receiveDate):
        self.find_element(*self.wy_receiveDate_loc).send_keys(receiveDate)

    def input_signDate(self, signDate):
        self.find_element(*self.wy_signDate_loc).send_keys(signDate)

    def input_rent(self, rent):
        self.find_element(*self.wy_rent_loc).send_keys(rent)

    def input_deposit(self, deposit):
        self.find_element(*self.wy_deposit_loc).send_keys(deposit)

    def input_partyA(self, partyA):
        self.find_element(*self.wy_partyA_loc).send_keys(partyA)

    def input_partyB(self, partyB):
        self.find_element(*self.wy_partyB_loc).send_keys(partyB)

    def input_partyC(self, partyC):
        self.find_element(*self.wy_partyC_loc).send_keys(partyC)

    def select_classification(self, classification):
        Select(self.find_element(*self.wy_classification_loc)).select_by_visible_text(classification)

    def input_coefficient(self, coefficient):
        self.find_element(*self.wy_coefficient_loc).send_keys(coefficient)

    def input_area(self, area):
        self.find_element(*self.wy_area_loc).send_keys(area)

    def select_followPerson(self, followPerson):
        Select(self.find_element(*self.wy_followPerson_loc)).select_by_visible_text(followPerson)

    def input_memo(self, memo):
        self.find_element(*self.wy_memo_loc).send_keys(memo)

    def input_electricityFeeRate(self, electricityFeeRate):
        self.find_element(*self.wy_electricityFeeRate_loc).send_keys(electricityFeeRate)

    def input_electricityFeeCycle(self, electricityFeeCycle):
        self.find_element(*self.wy_electricityFeeCycle_loc).send_keys(electricityFeeCycle)

    def select_account_tab(self):
        self.find_element(*self.wy_account_tab_loc).click()

    def input_contact(self, contact):
        self.find_element(*self.wy_contact_loc).send_keys(contact)

    def input_mobile(self, mobile):
        self.find_element(*self.wy_mobile_loc).send_keys(mobile)

    def input_eleAccountName1(self, eleAccountName1):
        self.find_element(*self.wy_eleAccountName1_loc).send_keys(eleAccountName1)

    def input_eleBankName1(self, eleBankName1):
        self.find_element(*self.wy_eleBankName1_loc).send_keys(eleBankName1)

    def input_eleBankAccountNo1(self, eleBankAccountNo1):
        self.find_element(*self.wy_eleBankAccountNo1_loc).send_keys(eleBankAccountNo1)

    def input_rentAccountName1(self, rentAccountName1):
        self.find_element(*self.wy_rentAccountName1_loc).send_keys(rentAccountName1)

    def input_rentBankName1(self, rentBankName1):
        self.find_element(*self.wy_rentBankName1_loc).send_keys(rentBankName1)

    def input_rentBankAccountNo1(self, rentBankAccountNo1):
        self.find_element(*self.wy_rentBankAccountNo1_loc).send_keys(rentBankAccountNo1)

    def contract_submit(self):
        self.find_element(*self.wy_Submit_loc).click()

    def selected_contract(self):
        self.find_element(*self.wy_selected_contract_loc).click()

    def edit_contracts(self):
        self.find_element(*self.wy_edit_contracts_loc).click()

    def payment_plan_click(self):
        self.find_element(*self.wy_payment_plan_tab_loc).click()

    # wy_account_tab_loc = (By.LINK_TEXT, '业主账户信息')  # 业主账户信息
    # wy_contact_loc = (By.NAME, 'contact')  # 出租方联系人
    # wy_mobile_loc = (By.NAME, 'mobile')  # 联系电话
    # wy_eleAccountName1_loc = (By.NAME, 'eleAccountName1')  # 电费业主账户户名1
    # wy_eleBankName1_loc = (By.NAME, 'eleBankName1')  # 电费业主开户行1
    # wy_eleBankAccountNo1_loc = (By.NAME, 'eleBankAccountNo1')  # 电费业主账号1
    # wy_eleRatio1_loc = (By.NAME, 'eleRatio1')  # 电费分账比例1
    # wy_rentAccountName1_loc = (By.NAME, 'rentAccountName1')  # 房租业主账户户名1
    # wy_rentBankName1_loc = (By.NAME, 'rentBankName1')  # 房租业主开户行1
    # wy_rentBankAccountNo1_loc = (By.NAME, 'rentBankAccountNo1')  # 房租业主账号1
    # wy_rentRatio1_loc = (By.NAME, 'rentRatio1')  # 房租分账比例1
    # 添加合同
    def add_contracts(self,
                      code='code',
                      oldCode='oldCode',
                      catalog='catalog',
                      startTime='startTime',
                      endTime='endTime',
                      useStartTime='useStartTime',
                      useEndTime='useEndTime',
                      tenements_name='tenements_name',
                      tenements_address='tenements_address',
                      tenements_contact='tenements_contact',
                      tenements_mobile='tenements_mobile',
                      tenements_payPurpose='tenements_payPurpose',
                      signatory='signatory',
                      annualAmount='annualAmount',
                      firstRent='firstRent',
                      rentCycle='rentCycle',
                      firstCycle='firstCycle',
                      receiveDate='receiveDate',
                      signDate='signDate',
                      rent='rent',
                      deposit='deposit',
                      partyA='partyA',
                      partyB='partyB',
                      partyC='partyC',
                      classification='classification',
                      coefficient='coefficient',
                      area='area',
                      followPerson='followPerson',
                      memo='memo',
                      electricityFeeRate='electricityFeeRate',
                      electricityFeeCycle='electricityFeeCycle',
                      contact='contact',
                      mobile='mobile',
                      eleAccountName1='eleAccountName1',
                      eleBankName1='eleBankName1',
                      eleBankAccountNo1='eleBankAccountNo1',
                      rentAccountName1='rentAccountName1',
                      rentBankName1='rentBankName1',
                      rentBankAccountNo1='rentBankAccountNo1'
                      ):
        self.add_contracts_button()
        sleep(1)
        self.input_code(code)
        self.input_oldCode(oldCode)
        self.select_catalog(catalog)
        self.remove_readonly("startTime")
        self.input_startTime(startTime)
        self.remove_readonly("endTime")
        self.input_endTime(endTime)
        self.remove_readonly("useStartTime")
        self.input_useStartTime(useStartTime)
        self.remove_readonly("useEndTime")
        self.input_useEndTime(useEndTime)
        self.add_tenementName()
        # 添加基站
        sleep(1)
        self.add_tenement_Name()
        sleep(1)
        self.input_tenements_name(tenements_name)
        self.input_tenements_address(tenements_address)
        self.input_tenements_contact(tenements_contact)
        self.input_tenements_mobile(tenements_mobile)
        self.input_tenements_payPurpose(tenements_payPurpose)
        self.add_tenements()
        sleep(1)
        self.alert_accprt()
        sleep(1)
        self.selected_tenements()
        sleep(1)
        self.select_button()
        self.input_signatory(signatory)
        self.input_annualAmount(annualAmount)
        self.input_firstRent(firstRent)
        self.input_rentCycle(rentCycle)
        self.input_firstCycle(firstCycle)
        self.remove_readonly("receiveDate")
        self.input_receiveDate(receiveDate)
        self.remove_readonly("signDate")
        self.input_signDate(signDate)
        sleep(2)
        self.input_deposit(deposit)
        self.input_partyA(partyA)
        self.input_partyB(partyB)
        self.input_partyC(partyC)
        self.select_classification(classification)
        self.input_area(area)
        self.select_followPerson(followPerson)
        if catalog == '电费':
            self.input_electricityFeeRate(electricityFeeRate)
            self.input_electricityFeeCycle(electricityFeeCycle)
        elif catalog == '房租+电费':
            self.input_electricityFeeRate(electricityFeeRate)
            self.input_electricityFeeCycle(electricityFeeCycle)
        elif catalog == '房租':
            print('房租合同不需要输入电费费率和周期')
        # 业主账户信息
        self.select_account_tab()
        sleep(1)
        self.input_contact(contact)
        self.input_mobile(mobile)
        if catalog == '房租':
            self.input_rentAccountName1(rentAccountName1)
            self.input_rentBankName1(rentBankName1)
            self.input_rentBankAccountNo1(rentBankAccountNo1)
        elif catalog == '电费':
            self.input_eleAccountName1(eleAccountName1)
            self.input_eleBankName1(eleBankName1)
            self.input_eleBankAccountNo1(eleBankAccountNo1)
        elif catalog == '房租+电费':
            self.input_rentAccountName1(rentAccountName1)
            self.input_rentBankName1(rentBankName1)
            self.input_rentBankAccountNo1(rentBankAccountNo1)
            self.input_eleAccountName1(eleAccountName1)
            self.input_eleBankName1(eleBankName1)
            self.input_eleBankAccountNo1(eleBankAccountNo1)
        self.contract_submit()
        sleep(2)
        self.alert_accprt()

    def payment_plan(self, amount):
        self.selected_contract()
        self.edit_contracts()
        self.payment_plan_click()
        function.insert_img(self.driver, 'payment_plan_' + amount + '.png')
        sleep(1)
        self.close_contract()

    def query_contact(self,
                      innerCode='innerCode',
                      contactname='contactname'
                      ):
        self.query_innerCode(innerCode)
        self.query_contactname(contactname)
        self.query_button()
        sleep(1)
        self.selected_contract()

    def upImgs(self,
               innerCode='innerCode',
               contactname='contactname',
               imgspath='imgspath'
               ):
        self.query_innerCode(innerCode)
        self.query_contactname(contactname)
        self.query_button()
        sleep(1)
        self.selected_contract()
        self.edit_contracts()
        sleep(1)
        self.contractsImgs_tab()
        sleep(3)
        self.input_imgs(imgspath)
        sleep(2)
        self.contract_submit()
        sleep(1)
        self.alert_accprt()
        self.close_contract()

    def AtoB(self,
             innerCode='innerCode',
             contactname='contactname',
             ):
        self.query_contact(innerCode, contactname)
        self.edit_contracts()
        sleep(1)
        self.contract_status()
        self.alert_accprt()
        sleep(1)
        self.alert_accprt()

    def return_contracts(self,
                         innerCode='innerCode',
                         contactname='contactname',
                         ):
        self.query_contact(innerCode, contactname)
        self.contract_return()
        self.contract_submit()
        sleep(1)
        self.alert_accprt()

    def A_contact_pass(self,
                       innerCode='innerCode',
                       contactname='contactname',
                       ):
        self.query_contact(innerCode, contactname)
        self.edit_contracts()
        sleep(1)
        self.contract_status()
        self.alert_accprt()
        sleep(1)
        self.alert_accprt()

    def B_contact_pass(self,
                       innerCode='innerCode',
                       contactname='contactname',
                       code='code'
                       ):
        self.query_contact(innerCode, contactname)
        self.edit_contracts()
        sleep(1)
        self.input_code(code)
        sleep(1)
        self.contract_submit()
        sleep(1)
        self.alert_accprt()
        self.contract_status()
        self.alert_accprt()
        sleep(1)
        self.alert_accprt()


if __name__ == '__main__':
    e = 'C:/Users/admin/PycharmProjects/wy/wy_dh/data/合同台账2019-12-02.xlsx'
    reader = ExcelReader(e, title_line=True)
    amount = '1'
    i = 3
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://wy.dhwl66.com:8001/dhwy/passport/login')
    driver.find_element_by_id('username').send_keys('周继成')
    driver.find_element_by_id('password').send_keys('12345678')
    driver.find_element_by_id('loginSub').click()
    sleep(1)
    driver.get('http://wy.dhwl66.com:8001/dhwy/contracts/load')
    # ContractMPage(driver).add_contracts(code=reader.data[i]['东恒-业主合同编号'] + str(random.randint(000, 999)),  # 合同编号
    #                                     oldCode=reader.data[i]['原合同编号'],  # 原合同编号
    #                                     catalog=reader.data[i]['合同分类2'],  # 合同分类2
    #                                     startTime=reader.data[i]['合同起时间'],  # 合同起时间
    #                                     endTime=reader.data[i]['合同止时间'],  # 合同止时间
    #                                     useStartTime=reader.data[i]['租金首次支付开始时间'],  # 租金首次支付开始时间
    #                                     useEndTime=reader.data[i]['租金首次支付结束时间'],  # 租金首次支付结束时间
    #                                     tenements_name=reader.data[i]['基站名称'],  # 基站名称
    #                                     tenements_address=reader.data[i]['租赁地址'],  # 地址
    #                                     tenements_contact=reader.data[i]['出租方联系人'],  # 联系人
    #                                     tenements_mobile=reader.data[i]['联系电话'],  # 电话
    #                                     tenements_payPurpose=reader.data[i]['基站缩略名称'],  # 基站名称缩略名
    #                                     signatory='签订人',  # 签订人
    #                                     annualAmount=reader.data[i]['业主合同金额(元/年)'],  # 合同年金额
    #                                     firstRent=reader.data[i]['业主租金首次支付金额'],  # 首次支付金额
    #                                     rentCycle=reader.data[i]['业主租金后续支付周期（月）'],  # 后续支付周期
    #                                     firstCycle=reader.data[i]['租金首次支付周期（月)'],  # 首次支付周期
    #                                     receiveDate=reader.data[i]['收单日期'],  # 收单日期
    #                                     signDate=reader.data[i]['A合同签订时间'],  # 签订日期
    #                                     rent=reader.data[i]['业主合同总金额'],  # 合同总金额
    #                                     deposit=reader.data[i]['押金'],  # 押金
    #                                     partyA=reader.data[i]['出租方'],  # 甲方
    #                                     partyB='',  # 乙方
    #                                     partyC='',  # 丙方
    #                                     classification=reader.data[i]['业主分类'],  # 对公对私类别
    #                                     coefficient='',  # 租金转化系数
    #                                     area=reader.data[i]['面积'],  # 面积
    #                                     followPerson=reader.data[i]['跟进人'],  # 跟进人
    #                                     memo=reader.data[i]['A合同备注'],  # 备注
    #                                     electricityFeeRate=reader.data[i]['业主电费费率（元/度）'],  # 电费费率
    #                                     electricityFeeCycle=reader.data[i]['电费缴费周期（月）'],  # 电费的缴费周期
    #                                     contact=reader.data[i]['出租方联系人'],  # 出租方联系人
    #                                     mobile=reader.data[i]['联系电话'],  # 联系电话
    #                                     eleAccountName1=reader.data[i]['业主户名'],  # 电费业主账户户名1
    #                                     eleBankName1=reader.data[i]['业主开户行'],  # 电费业主开户行1
    #                                     eleBankAccountNo1=reader.data[i]['业主账号'],  # 电费业主账号1
    #                                     rentAccountName1=reader.data[i]['业主户名'],  # 房租业主账户户名1
    #                                     rentBankName1=reader.data[i]['业主开户行'],  # 房租业主开户行1
    #                                     rentBankAccountNo1=reader.data[i]['业主账号']  # 房租业主账号1
    #                                     )
    sleep(1)
    innerCode = ContractMPage(driver).get_innerCode()
    sleep(1)
    # ContractMPage(driver).payment_plan(amount)
    # ContractMPage(driver).upImgs(
    #     tenementsname=reader.data[i]['基站名称'],
    #     contactname='A',
    #     imgspath=r'C:/Users/admin/PycharmProjects/wy/wy_dh/data/contact.jpg'
    # )
    # 生成B合同
    ContractMPage(driver).AtoB(
        innerCode=innerCode,
        contactname='A',
    )
    # 回访
    ContractMPage(driver).return_contracts(
        innerCode=innerCode,
        contactname='A',
    )
    # 审核通过
    ContractMPage(driver).A_contact_pass(
        innerCode=innerCode,
        contactname='A',
    )
    driver.quit()
