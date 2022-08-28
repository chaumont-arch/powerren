label bedroom_move:
	menu
		"Where to?"
		"bathroom":
			jump None_landing
		"kitchen":
			jump None_landing
		"Cancel":
			jump bedroom_landing

label bathroom_move:
	menu
		"Where to?"
		"bedroom":
			jump None_landing
		"Cancel":
			jump bathroom_landing

label kitchen_move:
	menu
		"Where to?"
		"bedroom":
			jump None_landing
		"frontdoor":
			jump None_landing
		"livingroom":
			jump None_landing
		"Cancel":
			jump kitchen_landing

label frontdoor_move:
	menu
		"Where to?"
		"kitchen":
			jump None_landing
		"outside":
			jump None_landing
		"Cancel":
			jump frontdoor_landing

label livingroom_move:
	menu
		"Where to?"
		"kitchen":
			jump None_landing
		"basement":
			jump basement_flag
		"Cancel":
			jump livingroom_landing

label outside_move:
	menu
		"Where to?"
		"frontdoor":
			jump None_landing
		"car":
			jump None_landing
		"Cancel":
			jump outside_landing

label car_move:
	menu
		"Where to?"
		"outside":
			jump None_landing
		"Cancel":
			jump car_landing

