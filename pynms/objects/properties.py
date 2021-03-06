from collections import OrderedDict

object_common_properties = (
    'name',
    'type',
    'vendor'
    )

node_common_properties = (
    'operating_system',
    'os_version',
    'ip_address',
    'longitude',
    'latitude'
    )

link_common_properties = (
    'source',
    'destination',
    )

node_public_properties = (
object_common_properties +
node_common_properties
)

link_public_properties = (
object_common_properties + 
link_common_properties
)

public_properties = (
node_public_properties + 
link_public_properties
)

type_to_public_properties = OrderedDict([
    ('Router', node_public_properties),
    ('Optical switch', node_public_properties),
    ('Optical link', link_public_properties)
    ])

## Diagram properties (for the dashboard)

node_diagram_properties = (
    'type',
    'vendor',
    'operating_system',
    'os_version'
    )

link_diagram_properties = (
    'type',
    'vendor'
    )
