echo '###################################'
echo "Setup Banner"
mv banner/banner.sh ~/.banner.sh
chmod u+x ~/.banner.sh
sudo echo "clear;sudo ~/.banner.sh" >> ~/.profile
echo