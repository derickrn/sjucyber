#!/bin/bash
# Download and Install Morpehus MITM suite
git clone https://github.com/r00t-3xp10it/morpheus.git
cd morpheus
chmod -R +x *.sh
chmod -R +x *.py
nano settings
sudo ./morpheus.sh
echo "Finished installing/running Morpehus MITM"
# Done
