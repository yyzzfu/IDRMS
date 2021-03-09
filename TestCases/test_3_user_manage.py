import pytest
import allure
from Common.do_excel import DoExcel
from Common import dir_config
from PageObjects.SystemManagePages.user_manage_page import UserManagePage
from PageObjects.home_page import HomePage


@pytest.mark.usefixtures('enter_the_homepage')
# @pytest.mark.usefixtures('delete_table_sys_user')
@pytest.mark.usefixtures('refresh')
@allure.epic('项目名称：配电房平台V1.0')
@allure.feature('系统管理')
@allure.story('用户管理')
# @pytest.mark.skip('跳过')
class TestAddUser:

    datas = DoExcel('user').get_data(dir_config.archives_data_excel_path)

    @allure.title('用户管理--新增功能')
    @pytest.mark.parametrize('data', datas)
    def test_add_user(self, data, enter_the_homepage):
        UserManagePage(enter_the_homepage).add_user(name=data['name'], user_name=data['user_name'], password=data['password'],
                                                    confirm_password=data['confirm_password'], email=data['email'],  phone=data['phone'],
                                                    role=data['role'],  manage_room=data['manage_room'], remark=data['remark'])
        assert "成功" in HomePage(enter_the_homepage).get_success_save_tip()
