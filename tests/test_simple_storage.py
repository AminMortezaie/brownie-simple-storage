from brownie import SimpleStorage, accounts 
import time

def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0 
    assert starting_value == expected

def test_updating_storage():
    #arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    #act
    expected = 15
    simple_storage.store(expected, {"from": account})
    #assert
    assert expected == simple_storage.retrieve()
    time.sleep(1)
