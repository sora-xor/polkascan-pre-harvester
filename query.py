import json
from scalecodec.type_registry import load_type_registry_file
from substrateinterface import SubstrateInterface

substrate = SubstrateInterface(
    url='wss://ws.framenode-1.s1.dev.sora2.soramitsu.co.jp',
    type_registry_preset='default',
    type_registry=load_type_registry_file('../harvester/app/type_registry/custom_types.json'),
)

#block_hash = substrate.get_block_hash(block_id=3077347)

extrinsics = substrate.get_block(block_hash='0x6e8b3d0a3c09b411b141f7d05e28a57bab2f6ffeaf5211edd8bb5d41b8466892')['extrinsics']

print('Extrinsincs:', json.dumps([e.value for e in extrinsics], indent=4))

events = substrate.get_events('0x6e8b3d0a3c09b411b141f7d05e28a57bab2f6ffeaf5211edd8bb5d41b8466892')

print("Events:", json.dumps([e.value for e in events], indent=4))
