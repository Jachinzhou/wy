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
    wy_useEndTime_loc = (By.ID,'useEndTime') # 首次支付结束时间

    wy_tenementName_loc = (By.NAME, 'tenementName')  # 物业单位
    wy_add_tenement_loc = (By.XPATH, '//*[@id="popwnd_tenements_getTenements"]/div[2]/div[1]/div[2]/button')  # 添加按钮
    wy_tenements_name_loc = (By.NAME, 'tenements_name')  # 基站名称

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

    wy_yzzhxx_loc = (By.LINK_TEXT,'业主账户信息') #业主账户信息
    wy_contact_loc = (By.NAME, 'contact')  # 出租方联系人
    wy_mobile_loc = (By.NAME, 'mobile')  # 联系电话
    wy_eleAccountName1_loc = (By.NAME, 'eleAccountName1')  # 业主账户户名1
    wy_eleBankName1_loc = (By.NAME, 'eleBankName1')  # 业主开户行1
    wy_eleBankAccountNo1_loc = (By.NAME, 'eleBankAccountNo1')  # 业主账号1
    wy_eleRatio1_loc = (By.NAME, 'eleRatio1')  # 分账比例1

    wy_Submit_loc = (By.NAME, 'Submit')  # 提交按钮



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



    def add_contracts(self,
                      code='code',
                      oldCode='oldCode',
                      catalog='catalog',
                      startTime='startTime',
                      endTime='endTime',
                      useStartTime='useStartTime',
                      useEndTime='useEndTime',
                      tenements_name='tenements_name',
                      ):
        self.add_contracts_button()
        sleep(1)
        self.input_code(code)
        self.input_oldCode(oldCode)
        self.select_catalog(catalog)
        self.input_startTime(startTime)
        self.input_endTime(endTime)
        self.input_useStartTime(useStartTime)
        self.input_useEndTime(useEndTime)
        sleep(1)
        self.add_tenementName()
        sleep(1)
        self.add_tenement_Name()
        sleep(1)
        self.input_tenements_name(tenements_name)



if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://192.168.18.148:8080/dhwy/contracts/load')
    driver.find_element_by_id('username').send_keys('root')
    driver.find_element_by_id('password').send_keys('123')
    driver.find_element_by_id('loginSub').click()
    sleep(1)
    driver.get('http://192.168.18.148:8080/dhwy/contracts/load')
    ContractMPage(driver).add_contracts('合同编号',
                                        '原合同编号',
                                        '电费',
                                        '2019-7-1',
                                        '2021-6-30',
                                        '2019-7-1',
                                        '2020-6-30',
                                        '基站名称'
                                        )
