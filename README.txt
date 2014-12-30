Utility Scripts for dmurphy

emailGen.py

Takes a text file of names and domains as a parameter and generates a list of potential email addresses in a given format.
Commandline usage: python emailGen.py <input-file> <format-type>
	- input file must be a text file where each line takes either forms: 
		"firstname lastname @domain" 
		or "lastname, firstname @domain"

	- format type is a non-negative integer, less than 11
		For example, for a given line of the input file such as "drew murphy @sd46"
		0 - dmurphy@sd46
		1 - d.murphy@sd46
		2 - drewmurphy@sd46
		3 - drew.murphy@sd46
		4 - drewm@sd46
		5 - drew.m@sd46
		6 - mdrew@sd46
		7 - m.drew@sd46
		8 - murphydrew@sd46
		9 - murphy.drew@sd46
		10 - murphyd@sd46
		11 - murphy.d@sd46