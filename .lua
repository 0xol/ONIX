-- Define the prompt string
local prompt = "> "

-- Define the loop function for the shell
local function shell_loop()
    while true do
        -- Print the prompt and wait for input
        io.write(prompt)
        local input = io.read()
        
        -- If the user entered "exit", break out of the loop
        if input == "exit" then
            break
        end
        
        -- If the user entered a Lua file name, execute the file
        local file = io.open(input, "r")
        if file then
            local content = file:read("*all")
            file:close()
            load(content)()
        else
            -- Otherwise, execute the user's input as a Lua command
            load(input)()
        end
    end
end

-- Call the shell loop function to start the shell
shell_loop()
