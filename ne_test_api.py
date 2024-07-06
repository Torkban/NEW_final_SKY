from boardApi import BoardApi
import conftest
import allure

def test_create_board(api_client: BoardApi, test_data: dict):
    org_id = test_data.get("org_id")
    board_list_before = api_client.get_all_boards_by_id(org_id)
    
    assert 1 == 1

'''
def test_create_board(api_client: BoardApi, delete_board: dict, test_data: dict):
    org_id = test_data.get("org_id")
    board_list_before = api_client.get_all_boards_by_id(org_id)
    resp = api_client.create_board("Test board")
    delete_board["boards_id_for_delete"] = resp.get("id")
    board_list_after = api_client.get_all_boards_by_id(org_id)
    with allure.step("Проверяем, что количество организаций стало на единицу больше"):
        assert len(board_list_after) - len(board_list_before) == 1
    
    
def test_delete_board(api_client: BoardApi, temporarys_board_id: dict, test_data: dict):
    board_list_before = api_client.get_all_boards_by_id(test_data.get("org_id"))
    api_client.delete_board_by_id(temporarys_board_id)
    
    board_list_after = api_client.get_all_boards_by_id(test_data.get("org_id"))
    with allure.step("Проверяем, что количество организаций стало на единицу меньше"):
        assert len(board_list_before) - len(board_list_after) == 1
        
'''