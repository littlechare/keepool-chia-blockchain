from chia.pools.pool_config import load_pool_config, PoolWalletConfig
from chia.util.byte_types import hexstr_to_bytes
from blspy import G1Element
from pathlib import Path
from typing import List

def custom_load_pool_config(root_path: Path) -> List[PoolWalletConfig]:
    ret_list = []
    config = PoolWalletConfig(hexstr_to_bytes('ae4ef3b9bfe68949691281a015a9c16630fc8f66d48c19ca548fb80768791afa'),
                              'https://www.keepool.net/app/pool',
                              'c2b08e41d766da4116e388357ed957d04ad754623a915f3fd65188a8746cf3e8',
                              hexstr_to_bytes('344587cf06a39db471d2cc027504e8688a0a67cce961253500c956c73603fd58'),
                              hexstr_to_bytes('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'),
                              G1Element.from_bytes(hexstr_to_bytes('84c3fcf9d5581c1ddc702cb0f3b4a06043303b334dd993ab42b2c320ebfa98e5ce558448615b3f69638ba92cf7f43da5')),
                              G1Element.from_bytes(hexstr_to_bytes('970e181ae45435ae696508a78012dc80548c334cf29676ea6ade7049eb9d2b9579cc30cb44c3fd68d35a250cfbc69e29')))
    ret_list.append(config)
    return ret_list

