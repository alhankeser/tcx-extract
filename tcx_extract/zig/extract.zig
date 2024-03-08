const std = @import("std");
const print = std.debug.print;
const stdout = std.io.getStdOut().writer();
const spineTagName = "<Trackpoint>";

// Usage: ./parse example.tcx Time

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();
    const args = try std.process.argsAlloc(allocator);
    defer std.process.argsFree(allocator, args);

    const filePath = args[1];
    const file = try std.fs.cwd().openFile(filePath, .{});
    const fileSize = (try file.stat()).size;
    defer file.close();
    const readBuf = try file.readToEndAlloc(allocator, fileSize);
    defer allocator.free(readBuf);

    const targetTagText: []u8 = args[2];
    const targetTagStart = try std.fmt.allocPrint(allocator, "<{s}>", .{targetTagText});
    defer allocator.free(targetTagStart);
    const targetTagEnd = try std.fmt.allocPrint(allocator, "</{s}>", .{targetTagText});
    defer allocator.free(targetTagEnd);

    var points = std.mem.split(u8, readBuf, spineTagName);

    // This looks worse than it is:
    // Say we have this:
    // <Trackpoint>
    // <MyTargetValue>2024-03-03T06:01:29.000Z</MyTargetValue>
    // <Altitude>123</Altitude>
    // </Trackpoint>
    // We split the whole thing by <Trackpoint>
    // We want a row per Trackpoint, otherwise, we could have incomplete data
    // If, say, MyTargetValue is null on some Trackpoints, we want to capture that null
    // We split the first substring by </MyTargetValue>
    // Then split the first resulting substring by <MyTargetValue>
    // And return the first substring, which should be the value in the tag
    // If I knew how to index the result of a mem.split, I could avoid using while()
    _ = points.next();
    while (points.next()) |point| {
        var tagBeforeAfters = std.mem.split(u8, point, targetTagEnd);
        while (tagBeforeAfters.next()) |tagBeforeAfter| {
            var tagAfter = std.mem.split(u8, tagBeforeAfter, targetTagStart);
            _ = tagAfter.next();
            while (tagAfter.next()) |tag| {
                _ = try stdout.write(try std.fmt.allocPrint(allocator, "{s}", .{tag}));
                break;
            }
            _ = try stdout.write("\n");
            break;
        }
    }
}
