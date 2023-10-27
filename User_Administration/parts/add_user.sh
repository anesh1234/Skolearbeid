#! /usr/bin/bash

add_user() {
	clear
	echo -ne "Provide Username:  "
	read -r username

	if getent passwd "$username" &>/dev/null; then
		echo 'User already exists, returning'
		return 0
	else
		echo 'User does not exist, would you like to create it? y/n'
		read -r ans
	fi

	if [[ "$ans" == "Y" ]] || [[ "$ans" == "y" ]]; then
		create_user "$username"
    else
        return 0
    fi

}

create_user() {
	clear
	echo -ne "Enter full name: "
	read -r full_name
	echo -ne "Enter email: "
	read -r email
	echo -ne "Enter main group name: "
	read -r main_group
	echo -ne "Enter up to two additional groups (whitespace separated): "
	read -r add_group1 add_group2
	echo $add_group1 $add_group2

	Groups=("$main_group" "$add_group1" "$add_group2")


	for i in ${Groups[*]}; do
		if [ -z "$i" ]; then
			continue
		fi
		if [ -n $(getent group $i) ]; then
			echo "The group $i exists."
		else
			echo "The group $i does not exist, would you like to create it? y/n"
			read -r ans
			if [[ "$ans" == "Y" ]] || [[ "$ans" == "y" ]]; then
				sudo groupadd $i
			else
				echo "None added."
			fi
		fi
	done
	
	groupId=$(getent group "$main_group" | cut -d: -f3)

	if [ -z "$add_group1" ]; then
			sudo useradd -c "$full_name","$email" -g "$groupId" -s /bin/bash -m -d /home/$1 -k /home/kali/skel_dir $1
	else
		if [ -z "$add_group2" ]; then
			sudo useradd -c "$full_name","$email" -g "$groupId" -G "$add_group1" -s /bin/bash -m -d /home/$1 -k /home/kali/skel_dir $1
		else
			sudo useradd -c "$full_name","$email" -g "$groupId" -G "$add_group1","$add_group2" -s /bin/bash -m -d /home/$1 -k /home/kali/skel_dir $1
		fi
	fi

	sudo systemctl start mysql
	sudo mysql -e "INSERT INTO Accounting.Accounting VALUES ('$1','$full_name','$email')"
	sudo mysql -e "select * from Accounting.Accounting where (username='$1');"

	mail -s "System Login Info" $email < /path/to/file
}
 group office exists.


add_user
