# Starts the server

# screen -d terraria `/home/jake/terraria/1402/Linux/TerrariaServer.bin.x86_64 -config server.properties`

screen -d -S terraria_server -m /home/jake/terraria/1402/TerrariaServer.bin.x86_64 -config server.properties 

echo "Starting Terraria server."
echo "Feel free to logout."
