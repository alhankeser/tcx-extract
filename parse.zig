const std = @import("std");
const print = std.debug.print;

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
    const targetTagName = try std.fmt.allocPrint(allocator, "<{s}>", .{targetTagText});
    defer allocator.free(targetTagName);

    var tags = std.mem.split(u8, readBuf, targetTagName);
    const stdout = std.io.getStdOut().writer();
    _ = tags.next();
    while (tags.next()) |tagContent| {
        var tagSplit = std.mem.split(u8, tagContent, "</");
        while (tagSplit.next()) |tag| {
            _ = try stdout.write(try std.fmt.allocPrint(allocator, "{s},", .{tag}));
            break;
        }
    }
}
