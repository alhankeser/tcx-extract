import tcx_extract as tcx

# Only needs to run once
tcx.build_zig()

watts = tcx.extract(filepath="example.tcx", tag_name="ns3:Watts")
print(watts)