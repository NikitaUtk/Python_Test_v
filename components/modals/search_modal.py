import datetime
import time

from playwright.sync_api import Page

from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.title import Title
from page_factory.image import Image
from API import Response as r
from page_factory.button import Button
import allure
from datetime import datetime
class SearchModal:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.image_logo = Image(page, locator='svg.logo[xmlns="http://www.w3.org/2000/svg"]', name='Logo is visible')
        self.vertical_line = Image(page, locator='.vertical-line', name='Vertical line is visible')
        self.text_logo = Image(page, locator='span[title="Модуль ПНД"]', name='Text is visible')

        self.search_listofbuttons = ListItem(page, locator='.ant-menu-overflow-item', name='List of buttons')
        self.search_listofhandbook = ListItem(page, locator='li.ant-menu-item[data-menu-id*="rc-menu-uuid-"]', name='Test')
        self.search_listofroles = ListItem(page, locator='ul > li', name='Role list')
        self.table_row = ListItem(page, locator='tr', name='Table row')
        self.list_table_cell = ListItem(page, locator='td.ant-table-cell[data-column-key]', name='Table column')
        self.list_table_row = ListItem(page, locator='tr.ant-table-row[data-row-key]',name='Table row')
        # Фильтры для контрагентов
        self.input_filter_version_date = Input(page, locator='input[id="version_date"]', name='Input filter')
        self.input_filter_shortname = Input(page, locator='input[id="shortName"]', name='Input filter')
        self.input_filter_inn_ogrn_kio = Input(page, locator='input[id="inn_ogrn_kio"]', name='Input filter')
        self.input_filter_modified_date = Input(page, locator='input[id="modified_date"]', name='Input filter')
        self.input_filter_biz_size = Input(page, locator='input[id="bizSizeCD"]', name='Input filter')
        self.input_filter_biz_segment = Input(page, locator='input[id="bizSegmentCD"]', name='Input filter')
        self.input_filter_country = Input(page, locator='input[id="countryCD"]', name='Input filter')
        self.input_filter_kpp = Input(page, locator='input[id="kpp"]', name='Input filter')
        self.input_filter_vzl = Input(page, locator='input[id="flagVZL"]', name='Input filter')
        self.input_filter_byvzl = Input(page, locator='input[id="flagByVZL"]', name='Input filter')
        self.input_filter_ofshore = Input(page, locator='input[id="flagOffshore"]', name='Input filter')
        # Фильтры для сделок

        self.input_filter_deal_type = Input(page, locator='input[id="deal_pnd_types_cd"]', name='Input filter')
        self.input_filter_deal_credit_transh = Title(page, locator='span[title="Кредитная сделка. Транш"]', name='Input filter')
        self.input_filter_currency = Input(page, locator='input[id="currency_cd"]', name='Input filter')
        self.input_filter_deal_sum_from = Input(page, locator='input[id="deal_sum_rur_from"]', name='Input filter')
        self.input_filter_deal_sum_to = Input(page, locator='input[id="deal_sum_rur_to"]', name='Input filter')
        self.input_filter_deal_sign_date_from = Input(page, locator='input[id="contract_sign_date"]', name='Input filter')
        self.input_filter_deal_sign_date_to = Input(page, locator='#root > div > div.layout_contentContainer__2-sNh > div:nth-child(1) > div > form > div > div.ant-row.ant-row-no-wrap.ant-row-space-between > div:nth-child(1) > div:nth-child(5) > div > div > div > div > div > div > div > div > div.ant-picker-input.ant-picker-input-active > input', name='Input filter')
        self.input_filter_deal_shortname = Input(page, locator='input[id="client_short_name"]', name='Input filter')
        self.input_check_vzl = Input(page, locator='.ant-checkbox-input[type="checkbox"]', name='Input filter')
        self.input_check_byvzl = Input(page, locator='.ant-checkbox-input[type="checkbox"]', name='Input filter')
        self.input_check_ofshore = Input(page, locator='.ant-checkbox-input[type="checkbox"]', name='Input filter')
        self.input_filter_abs_code = Input(page, locator='input[id="abs_code"]', name='Input filter')
        self.input_filter_contract_term_from = Input(page, locator='input[id="contract_term_from"]', name='Input filter')
        self.input_filter_contract_term_to = Input(page, locator='input[id="contract_term_to"]', name='Input filter')
        self.input_filter_contract_num = Input(page, locator='input[id="contract_num"]', name='Input filter')
        self.input_filter_rate_type = Input(page, locator='input[id="rate_type_cd"]', name='Input filter')
        self.input_filter_rate_from = Input(page, locator='input[id="rate_from"]', name='Input filter')
        self.input_filter_rate_to = Input(page, locator='input[id="rate_to"]', name='Input filter')
        self.input_filter_extra_rate_from = Input(page, locator='input[id="extra_rate_from"]', name='Input filter')
        self.input_filter_extra_rate_to = Input(page, locator='input[id="extra_rate_to"]', name='Input filter')
        self.input_filter_base_ind = Input(page, locator='input[id="base_ind_cd"]', name='Input filter')
        self.input_filter_base_ind_key_rate = Title(page, locator='.ant-select-item[title="Ключевая ставка ЦБ (RUR)"]', name='Input filter')

        self.button_next = Button(page, locator='.anticon-right', name='Button next')
        self.button_in = ListItem(page, locator='th.ant-table-cell', name='Button sort')
        self.button_sort = Button(page, locator='#undefined_container > div.ant-table-wrapper.data-table_table__2Dpgt.scrollable-data-table > div > div > div > div > div.ant-table-header > table > thead > tr > th.ant-table-cell.ant-table-column-sort.ant-table-column-has-sorters > div > span.ant-table-column-sorter.ant-table-column-sorter-full > span > span.anticon.anticon-caret-up.ant-table-column-sorter-up.active', name='Button next')
        self.button_search = Button(page, locator='button.ant-btn.ant-btn-primary', name='Button search')
        self.button_clear = Button(page, locator='button.ant-btn', name='Button clear')
        self.button_filter_list = Button(page, locator='#root > div > div.layout_contentContainer__2-sNh > div:nth-child(1) > div > div', name='Button filter list')
    error_list=[]
    def check_logo(self):
        self.image_logo.should_be_visible()
        self.vertical_line.should_be_visible()
        # self.text_logo.should_be_visible()



    def compare_list_roles(self):
        roles = r.getResponse(method="api/Roles", typeRequest="GET")
        apiRoles = [i["name"] for i in roles]
        self.search_listofroles.compare_list(apiRoles)
 

    def compare_list_buttons(self, ButtonsList: list):
        self.search_listofbuttons.compare_list(ButtonsList)


    def find_empty_table(self):
        for i in self.search_listofhandbook.list_of_elements():
            if '/' in i.get_attribute('data-menu-id'):
                continue
            else:
                i.click()
                if self.table_row.count_elements() < 1:
                    self.error_list.append(f"In the handbook with the name {i.get_attribute('data-menu-id')} no values")
        assert self.error_list ==[], self.error_list

    def find_empty_column(self):
        column_names = []
        for column_name in self.list_table_cell.list_of_elements():
            if column_name.get_attribute('data-column-key') not in column_names:
                column_names.append(column_name.get_attribute('data-column-key'))
            else:
                break
        while True:
            for i in column_names:
                empty_column = 0;
                for value in self.list_table_cell.list_of_elements(loc=f'td.ant-table-cell[data-column-key="{i}"]'):
                    if value != '':
                        empty_column = 0;
                        break
                    else:
                        empty_column+=1
                if empty_column != 0:
                    self.error_list.append(f'Empty column {i}')
            if len(self.error_list)<=1:
                break
            else:
                self.button_next.click()

        # while True:
        #     for column_name in self.list_table_cell.list_of_elements():
        #         if column_name.inner_text() == '':
        #             dictionaries.setdefault(column_name.get_attribute('data-column-key'), [])
        #             continue
        #         dictionaries.setdefault(column_name.get_attribute('data-column-key'), []).append(
        #             column_name.inner_text())
        #     keys_with_empty_column = [key for key, value in dictionaries.items() if value == []]
        #     if len(keys_with_empty_column) <= 1:
        #         self.error_list.append(f"Empty cell in column {keys_with_empty_column}")
        #         break
        #     self.button_next.click()
        #     # allure.step('Empty column' + str(keys_with_empty_column))
        assert self.error_list == [], self.error_list
        """
        --Возможно понадобится
        column_name_list = []
        for column_name in self.list_name_table_column.listofElements():
            if column_name.get_attribute('data-column-key') not in column_name_list:
                column_name_list.append(column_name.get_attribute('data-column-key'))
        empty_column = []
        # for cell_name in column_name_list:
        #     not_sort_list = self.list_name_table_column.listofElements(
        #         loc=f'td.ant-table-cell[data-column-key="{cell_name}"]')
        #     try:
        #         new_list = [not_sort_list.remove('')]
        #     except ValueError:
        #         continue
        #     else:
        #         print(new_list)
        #         if new_list == []:
        #             empty_column.append(cell_name)
        #     # else:
        #     #     allure.step(f'Sorted {cell_name} is not correct')
        #     column_name_list.remove(cell_name)
        # print(empty_column)"""



    def correct_sort(self, skip_fc=False):
        column_name_list = []
        for column_name in self.list_table_cell.list_of_elements():
            if column_name.get_attribute('data-column-key') not in column_name_list:
                column_name_list.append(column_name.get_attribute('data-column-key'))
        reverse = False
        for i in range(1,3,1):
            tmp_list=list(column_name_list)
            for sorted_name in self.button_in.list_of_elements():
                if skip_fc:
                    print("Skip first column")
                else:
                    if reverse:
                        sorted_name.click()
                        sorted_name.click()
                    else:
                        sorted_name.click()
                time.sleep(3)
                for cell_name in tmp_list:
                    not_sort = [i.lower() for i in self.list_table_cell.list_of_elements(loc=f'td.ant-table-cell[data-column-key="{cell_name}"]')]
                    not_sort_list=[]
                    for i in not_sort:
                            try:
                                not_sort_list.append(datetime.strptime(i, '%d.%m.%Y').date())
                            except ValueError:
                                not_sort_list.append(i)
                    sort_list = sorted(not_sort_list, reverse=reverse)
                    if not_sort_list != sort_list:
                        self.error_list.append(f'Sorted {cell_name} is not correct')
                    tmp_list.remove(cell_name)
                    break
                skip_fc=False
                if (tmp_list == []): break
            reverse = True
        assert self.error_list ==[], self.error_list

    def correct_filter(self, dict={}):
        start = time.time()
        self.button_filter_list.click()
        for key in dict.keys():
            if key in ['modified_date']:
                self.input_filter_version_date.click()
                self.input_filter_version_date.fill(dict.get(key), validate_value=False, enter=True)
                self.button_search.click()
                time.sleep(3)
                if len(self.list_table_cell.list_of_elements()) == 0:
                    self.error_list.append(f'No strings with this filter version_date = {dict.get(key)}')
                self.button_clear.click_by_text(keyword="Сбросить")

                self.input_filter_modified_date.click()
                self.input_filter_modified_date.fill(dict.get(key), validate_value=False, enter=True)
                self.button_search.click()
                if len(self.list_table_cell.list_of_elements()) == 0:
                    self.error_list.append(f'No strings with this filter modified_date = {dict.get(key)}')
                self.button_clear.click_by_text(keyword="Сбросить")
            elif key == 'deals_contractSignDate':
                date_list = dict.get(key)
                self.input_filter_deal_sign_date_from.click()
                self.input_filter_deal_sign_date_from.fill(str(date_list[0]), validate_value=False, enter=True)
                self.input_filter_deal_sign_date_to.click()
                self.input_filter_deal_sign_date_to.fill(str(date_list[1]), validate_value=False, enter=True)
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_table_cell.list_of_elements(
                    loc=f'td.ant-table-cell[data-column-key="{key}"]')
                for i in not_sort_list:
                    # cur_date = datetime.strptime(i, '%d.%m.%Y')
                    if i == '' or (datetime.strptime(i, '%d.%m.%Y') < date_list[0] or datetime.strptime(i, '%d.%m.%Y') > date_list[1]):
                        self.error_list.append(f'The value {i} does not match the filter date from {date_list[0]} and date to {date_list[1]}')
                        break
                self.button_clear.click_by_text(keyword="Сбросить")
            elif key == 'deals_dealSumRur':
                sum_list = dict.get(key)
                self.input_filter_deal_sum_from.fill(sum_list[0], validate_value=False)
                self.input_filter_deal_sum_to.fill(sum_list[1], validate_value=False)
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_table_cell.list_of_elements(
                    loc=f'td.ant-table-cell[data-column-key="{key}"]')
                for i in not_sort_list:
                    if i == '' or float(i.replace(' ', '')) < float(sum_list[0]) or float(i.replace(' ', '')) > float(sum_list[1]):
                        self.error_list.append(f'The value {i} does not match the filter sum from {sum_list[0]} and sum to {sum_list[1]}')
                        break
                self.button_clear.click_by_text(keyword="Сбросить")
            elif key in ['checkbox']:
                self.input_filter_vzl.click()
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_table_cell.list_of_elements()
                for i in not_sort_list:
                    i.click()
                    time.sleep(5)
                    if self.input_check_vzl.check_checkbox('ВЗЛ'):
                        break
                    else:
                        self.error_list.append(f'The checkbox "ВЗЛ" is not checked')
                        self.input_check_vzl.go_back()
                        time.sleep(2)
                        self.input_filter_vzl.click()
                        break
                self.input_filter_byvzl.click()
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_table_cell.list_of_elements()
                for i in not_sort_list:
                    i.click()
                    time.sleep(5)
                    if self.input_filter_byvzl.check_checkbox('Приравнен к ВЗЛ'):
                        break
                    else:
                        self.error_list.append(f'The checkbox "Приравнен к ВЗЛ" is not checked')
                        self.input_check_byvzl.go_back()
                        time.sleep(2)
                        self.input_filter_byvzl.click()
                        break
                self.input_filter_ofshore.click()
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_table_cell.list_of_elements()
                for i in not_sort_list:
                    i.click()
                    time.sleep(5)
                    if self.input_filter_ofshore.check_checkbox('Офшор'):
                        break
                    else:
                        self.error_list.append(f'The checkbox "Офшор" is not checked')
                        self.input_check_ofshore.go_back()
                        time.sleep(2)
                        self.input_filter_ofshore.click()
                        break
            elif key == 'deals_contractTerm':
                day_list = dict.get(key)
                self.input_filter_contract_term_from.fill(day_list[0], validate_value=False)
                self.input_filter_contract_term_to.fill(day_list[1], validate_value=False)
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_table_cell.list_of_elements(
                    loc=f'td.ant-table-cell[data-column-key="{key}"]')
                for i in not_sort_list:
                    if i < day_list[0] or i > day_list[1]:
                        self.error_list.append(f'The value {i} does not match the filter day from {day_list[0]} and day to {day_list[1]}')
                        break
                self.button_clear.click_by_text(keyword="Сбросить")
            elif key == 'abs_code':
                self.input_filter_abs_code.fill(dict.get(key), validate_value=False)
                self.button_search.click()
                time.sleep(3)
                if len(self.list_table_row.list_of_elements()) == 0:
                    self.error_list.append(f'No strings with abs_code filter')
                self.button_clear.click_by_text(keyword="Сбросить")
            elif key == 'deals_inn_ogrn_kio':
                self.input_filter_inn_ogrn_kio.fill(dict.get(key), validate_value=False)
                self.button_search.click()
                time.sleep(3)
                if len(self.list_table_row.list_of_elements()) == 0:
                    self.error_list.append(f'No strings with inn_ogrn_kio filter')
                self.button_clear.click_by_text(keyword="Сбросить")
            elif key == 'deals_kpp':
                self.input_filter_kpp.fill(dict.get(key), validate_value=False)
                self.button_search.click()
                time.sleep(3)
                if len(self.list_table_row.list_of_elements()) == 0:
                    self.error_list.append(f'No strings with kpp filter')
                self.button_clear.click_by_text(keyword="Сбросить")
            elif key == 'deals_rate':
                rate_dict = dict.get(key)
                for rate_type in rate_dict.get('deals_rateTypeCd'):
                    self.input_filter_rate_type.fill(rate_type, validate_value=False, enter=True)
                    match rate_type:
                        case 'Фиксированная':
                            rate_val = rate_dict.get('deals_rateAmount')
                            self.input_filter_rate_from.fill(rate_val[0], validate_value=False)
                            self.input_filter_rate_to.fill(rate_val[1], validate_value=False)
                            self.button_search.click()
                            time.sleep(5)
                            list_rate_amount = self.list_table_cell.list_of_elements(loc=f'td.ant-table-cell[data-column-key="deals_rateAmount"]')
                            base_ind = self.list_table_cell.list_of_elements(loc=f'td.ant-table-cell[data-column-key="deals_rateIndCD"]')
                            for i in list_rate_amount:
                                if i == '' or (float(i)<float(rate_val[0]) or float(i)>float(rate_val[1])):
                                    self.error_list.append(f'The value {i} does not match the filter rate_amount < {rate_val[0]} and rate_amount > {rate_val[1]}')
                                    break
                            for ind in base_ind:
                                if rate_dict.get('deals_rateIndCD') not in ind:
                                    self.error_list.append(f'The value {ind} does not match the filter base_ind =  {rate_dict.get("deals_rateIndCD")}')
                                    break
                            self.button_clear.click_by_text(keyword="Сбросить")
                        case 'Плавающая':
                            rate_fix = rate_dict.get('deals_rateFix')
                            self.input_filter_extra_rate_from.fill(rate_fix[0], validate_value=False)
                            self.input_filter_extra_rate_to.fill(rate_fix[1], validate_value=False)
                            self.input_filter_base_ind.click()
                            self.input_filter_base_ind_key_rate.click()
                            time.sleep(2)
                            self.button_search.click()
                            # time.sleep(5)
                            extra_rates = self.list_table_cell.list_of_elements(loc=f'td.ant-table-cell[data-column-key="deals_rateFix"]')
                            base_ind = self.list_table_cell.list_of_elements(loc=f'td.ant-table-cell[data-column-key="deals_rateIndCD"]')
                            for extra_rate in extra_rates:
                                if  extra_rate == '' or (extra_rate < rate_fix[0] or extra_rate > rate_fix[1]):
                                    self.error_list.append(f'The value {extra_rate} does not match the filter extra_rate < {rate_fix[0]} and extra_rate > {rate_fix[1]}')
                                    break
                            for base_ind in base_ind:
                                if rate_dict.get('deals_rateIndCD') not in base_ind:
                                    self.error_list.append(f'The value {base_ind} does not match the filter base_ind = {rate_dict.get("deals_rateIndCD")}')
                                    break
                            self.button_clear.click_by_text(keyword="Сбросить")
            else:
                match key:
                    case 'clients_shortName':
                        self.input_filter_shortname.fill(dict.get(key), validate_value=False)
                    case 'deals_shortName':
                        self.input_filter_deal_shortname.fill(dict.get(key), validate_value=False)
                    case 'clients_inn'|'clients_ogrn'| 'clients_kio':
                        self.input_filter_inn_ogrn_kio.fill(dict.get(key), validate_value=False)
                    case 'clients_bizSize':
                        self.input_filter_biz_size.fill(dict.get(key), validate_value=False, enter=True)
                    case 'clients_bizSegment':
                        self.input_filter_biz_segment.fill(dict.get(key), validate_value=False, enter=True)
                    case 'clients_countryName':
                        self.input_filter_country.fill(dict.get(key), validate_value=False, enter=True)
                    case 'clients_kpp'|'deals_kpp':
                        self.input_filter_kpp.fill(dict.get(key), validate_value=False)
                    case 'deals_dealTypeCD':
                        self.input_filter_deal_type.click()
                        self.input_filter_deal_type.fill(dict.get(key), validate_value=False)
                        time.sleep(2)
                        self.input_filter_deal_credit_transh.click(enter=True)
                    case 'deals_currencyCd':
                        self.input_filter_currency.fill(dict.get(key), validate_value=False, enter=True)
                    case 'deals_contractNum':
                        self.input_filter_contract_num.fill(dict.get(key), validate_value=False)
                self.button_search.click()
                time.sleep(4)
                not_sort_list = self.list_table_cell.list_of_elements(loc=f'td.ant-table-cell[data-column-key="{key}"]')
                for i in not_sort_list:
                    if dict.get(key).lower() not in i.lower():
                        self.error_list.append(f'The value {i} does not match the filter {dict.get(key)}')
                        break
                self.button_clear.click_by_text(keyword="Сбросить")

        end = time.time() - start
        print(end)

        assert len(self.error_list) == 0, self.error_list