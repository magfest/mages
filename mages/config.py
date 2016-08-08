from mages import *

mages_config = parse_config(__file__)
c.include_plugin_config(mages_config)

invalid_panel_rooms = [room for room in c.MAGES_ROOMS if not getattr(c, room.upper(), None)]
for room in invalid_panel_rooms:
    log.warning('mages plugin: mages_rooms config problem: '
                'Ignoring {!r} because it was not also found in [[event_location]] section.'.format(room.upper()))

c.MAGES_ROOMS = [getattr(c, room.upper()) for room in c.MAGES_ROOMS if room not in invalid_panel_rooms]

# This can go away if/when we implement plugin enum merging
c.ACCESS.update(c.MAGES_ACCESS_LEVELS)
c.ACCESS_OPTS.extend(c.MAGES_ACCESS_LEVEL_OPTS)
c.ACCESS_VARS.extend(c.MAGES_ACCESS_LEVEL_VARS)
