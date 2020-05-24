import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    """ check if packages are installed
    """
    assert host.package('prometheus').is_installed
    assert host.package('prometheus-alertmanager').is_installed


def test_service(host):
    """ Testing whether the service is running and enabled
    """
    assert host.service('prometheus').is_enabled
    assert host.service('prometheus').is_running
    assert host.service('prometheus-alertmanager').is_enabled
    assert host.service('prometheus-alertmanager').is_running
