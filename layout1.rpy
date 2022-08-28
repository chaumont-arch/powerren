label bedroom_move:
	menu
		"Where to?"
		"Bathroom":
			jump bathroom_landing
		"Kitchen":
			jump kitchen_landing
		"Cancel":
			jump bedroom_landing

label bathroom_move:
	menu
		"Where to?"
		"Bedroom":
			jump bedroom_landing
		"Cancel":
			jump bathroom_landing

label kitchen_move:
	menu
		"Where to?"
		"Bedroom":
			jump bedroom_landing
		"Front Door":
			jump frontdoor_landing
		"Living Room":
			jump livingroom_landing
		"Cancel":
			jump kitchen_landing

label frontdoor_move:
	menu
		"Where to?"
		"Kitchen":
			jump kitchen_landing
		"outside":
			jump outside_landing
		"Cancel":
			jump frontdoor_landing

label livingroom_move:
	menu
		"Where to?"
		"Kitchen":
			jump kitchen_landing
		"basement":
			jump basement_message
		"Cancel":
			jump livingroom_landing

label outside_move:
	menu
		"Where to?"
		"Front Door":
			jump frontdoor_landing
		"Car":
			jump car_landing
		"Cancel":
			jump outside_landing

label car_move:
	menu
		"Where to?"
		"outside":
			jump outside_landing
		"work":
			jump work_message
		"Cancel":
			jump car_landing

