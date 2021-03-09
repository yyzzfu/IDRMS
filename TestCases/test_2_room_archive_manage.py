import pytest
import allure
from PageObjects.ArchiveManagementPages.room_archive_management_page import RoomArchiveManagementPage
from PageObjects.home_page import HomePage
from Common import dir_config
from Common.do_excel import DoExcel


@allure.epic('项目名称：配电房平台V1.0')
@pytest.mark.usefixtures('enter_the_homepage')
# @pytest.mark.usefixtures('delete_table_ar_distribution_room')
@pytest.mark.usefixtures('refresh')
@allure.feature('档案管理')
@allure.story('配电房档案管理')
# @pytest.mark.skip('跳过')
class TestRoomArchiveManage:

    datas = DoExcel('room').get_data(dir_config.archives_data_excel_path)

    @allure.title('配电房档案管理--新增功能')
    @pytest.mark.parametrize('data', datas)
    def test_add_room(self, data, enter_the_homepage):
        RoomArchiveManagementPage(enter_the_homepage).add_room_archive(room_name=data['room_name'], area=data['area'],
                                                                       room_address=data['room_address'], map_pic_path=data['map_pic_path'],
                                                                       control_pic_path=data['control_pic_path'], primary_diagram_path=data['primary_diagram_path'],
                                                                       remark=data['remark'])
        assert "成功" in HomePage(enter_the_homepage).get_success_save_tip()
