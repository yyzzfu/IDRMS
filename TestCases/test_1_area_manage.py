import pytest
import allure
from PageObjects.SystemManagePages.area_manage_page import AreaManagePage
from PageObjects.home_page import HomePage
from Common import dir_config
from Common.do_excel import DoExcel


@allure.epic('项目名称：配电房平台V1.0')
@pytest.mark.usefixtures('enter_the_homepage')
# @pytest.mark.usefixtures('delete_table_sys_area')
@pytest.mark.usefixtures('refresh')
@allure.feature('系统管理')
@allure.story('区域管理')
# @pytest.mark.skip('跳过')
class TestAreaManage:
    datas = DoExcel('area').get_data(dir_config.archives_data_excel_path)

    @allure.title('区域管理--新增功能')
    @pytest.mark.parametrize('data', datas)
    def test_add_area(self, data, enter_the_homepage):
        AreaManagePage(enter_the_homepage).add_area(area_name=data['area_name'],
                                                    area_code=data['area_code'],
                                                    remark=data['remark'])
        assert '成功' in HomePage(enter_the_homepage).get_success_save_tip()
