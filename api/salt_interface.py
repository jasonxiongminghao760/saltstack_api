import salt.client
local = salt.client.LocalClient()


class salt_cmd(object):
    '''
    def __init__参数：
        tgt：目标主机（minion）
        fun：执行模块（如 cmd.run、state.sls ...）a
        mods: 执行sls文件路径
        salt_env：salt sls file环境（如 base、prod、test ...）
        kwargs：接收字典参数，将其传入给salt pillar
    '''
    def __init__(self, tgt, mods,salt_env,**kwargs):
        self.tgt = tgt
        self.mods = mods
        self.salt_env= salt_env
        self.kwargs = kwargs


    def state_sls(self):
        '''
        state_sls 参数：
            mods：执行的sls文件路径
            saltenv：指定的salt sls file环境
            pillar：接收pillar变量
            concurrent：开启并发
        :return:
        '''

        data = {
        'mods':self.mods ,
        'saltenv': self.salt_env,
        'pillar': self.kwargs,
        "concurrent": True
        }

        res = local.cmd(tgt=self.tgt, fun='state.sls', kwarg=data)
        return res
 



