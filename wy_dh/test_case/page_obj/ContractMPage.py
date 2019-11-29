from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from wy_dh.test_case.page_obj.base import Page
from time import sleep


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
    wy_selected_row_loc = (By.XPATH, '//*[@id="tenementsDataTable"]/tbody/tr[1]')  # 选择物业单位
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

    wy_Submit_loc = (By.NAME, 'Submit')  # 合同提交按钮

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

    def selected_row(self):
        self.find_element(*self.wy_selected_row_loc).click()

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
        sleep(1)
        self.add_tenementName()
        # 添加基站
        # sleep(1)
        # self.add_tenement_Name()
        # sleep(1)
        # self.input_tenements_name(tenements_name)
        # self.input_tenements_address(tenements_address)
        # self.input_tenements_contact(tenements_contact)
        # self.input_tenements_mobile(tenements_mobile)
        # self.input_tenements_payPurpose(tenements_payPurpose)
        # self.add_tenements()
        # sleep(1)
        # self.alert_accprt()
        self.selected_row()
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
        self.add_contracts()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://wy.dhwl66.com:8001/dhwy/passport/login')
    driver.find_element_by_id('username').send_keys('周继成')
    driver.find_element_by_id('password').send_keys('12345678')
    driver.find_element_by_id('loginSub').click()
    sleep(1)
    driver.get('http://wy.dhwl66.com:8001/dhwy/contracts/load')
    ContractMPage(driver).add_contracts(code='合同编号',
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
                                        partyB='中移铁通有限公司深圳分公司',
                                        partyC='深圳市东恒网络科技有限公司',
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
