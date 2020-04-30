from os import system
print('setup...')
system('rm -rf /plex_data/tmp')
system('mkdir /plex_data/tmp')
download_command = "curl -s \"https://plex.tv/downloads/details/1?build=linux-ubuntu-x86_64&channel=16&distro=ubuntu\" | grep -Po '(?<=url=\")(\S+)(?=\")' | xargs wget -P /plex_data/tmp/"
print('downloading...')
system(download_command)
#install what was downloaded
print('installing...')
system('sudo dpkg -i /plex_data/tmp/plexmediaserver*')
#clean up
print('cleanin up...')
system('rm -rf /plex_data/tmp')
print('update completed')
