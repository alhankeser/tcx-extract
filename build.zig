const std = @import("std");

pub fn build(b: *std.Build) void {
    const exe = b.addExecutable(.{ .name = "extract", .root_source_file = .{ .path = "tcx_extract/zig/extract.zig" }, .target = b.host });
    b.installArtifact(exe);
}
