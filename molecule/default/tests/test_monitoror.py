import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_monitoror_service(host):
    monitoror = host.service("monitoror")
    assert monitoror.is_running
    assert monitoror.is_enabled
