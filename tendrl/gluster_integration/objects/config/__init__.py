from tendrl.commons.etcdobj import EtcdObj
from tendrl.commons import config as cmn_config


from tendrl.gluster_integration import objects

class Config(objects.GlusterIntegrationBaseObject):
    def __init__(self, config=None, *args, **kwargs):
        super(Config, self).__init__(*args, **kwargs)

        self.value = '_tendrl/config/gluster-integration/data'
        self.data = config or cmn_config.load_config(
            'gluster-integration',
            "/etc/tendrl/gluster-integration/gluster-integration.conf.yaml"
        )
        self._etcd_cls = _ConfigEtcd


class _ConfigEtcd(EtcdObj):
    """Config etcd object, lazily updated
    """
    __name__ = '_tendrl/config/gluster-integration/'
    _tendrl_cls = Config
