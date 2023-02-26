local component = require("component")
local gpu = component.gpu

function print(text)
    -- Get the current cursor position
    local x, y = gpu.getCursor()

    -- Write the text to the screen
    gpu.set(x, y, text)

    -- Move the cursor to the next line
    y = y + 1
    gpu.setCursor(x, y)
end

print("[BOOT] Starting kernel")