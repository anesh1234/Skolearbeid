reset_password(){
	echo -ne "Provide Username: "
	read -r ans
	sudo passwd -e $ans
	
	echo -ne "Do you wish to quit/do again? y/n: "
	read -r ans
	if [[ "$ans" == "Y" ]] || [[ "$ans" == "y" ]]; then
		exit 0
	else
		reset_password
	fi
}

reset_password