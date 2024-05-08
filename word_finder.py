# Adeola Adekunle Amos
# 8th May 2024
# 11:23am
import random

displayed_words = ["another", "balance", "central", "defense", "exactly", "fortune", "glasses", "hearing", "improve", "journey",
"kitchen", "letters", "meaning", "nothing", "outside", "present", "quality", "rainbow", "science", "traffic",
"undergo", "victory", "weather", "yankees", "zealous", "abandon", "balance", "capture", "delight", "earnest",
"fiction", "gravity", "honesty", "journey", "kitchen", "largest", "measure", "narrate", "operate", "purpose",
"quarter", "resolve", "support", "tactics", "unknown", "variety", "welcome", "yelling", "zealous"
]

words_dict ={
    "another" : ["Another", "Ant", "Hat", "Hot", "Ear", "Tan", "Hen", "Not", "Her", "Tone", "Tear", "Near", "Note", "Rant",
                 "Rent", "Tar", "Ran", "Toe", "Roe", "Rat", "Art", "Roe", "Oar", "One", "Earn", "Are", "Tan", "Neon", "Thane",
                 "Tone", "Torn", "Tern", "Rot", "Hero", "The", "Another", "Ten", "Eat", "Rate", "Heat", "Ether", "Nor", "Ton",
                 "Honor", "Tar", "Anther", "Thro", "Or", "Eon", "Roan", "Nan", "Tone", "Note", "One", "The", "Net", "Throne",
                 "Toner", "Earth", "Heron", "North", "Other", "Rathe", "Tenor", "Atone", "Trona", "Honer", "Ortho", "Ratan",
                 "Noter", "Torah"],

    "balance" : ["Balance", "Ban", "Ace", "Can", "Lane", "Able", "Bean", "Ale", "Lance", "Cane", "Bone", "One",
                 "Cab", "Ace", "Lean", "Bane", "Lace", "Ace", "Noel", "Elan", "Coal", "Clone", "Lab", "Con", "One",
                 "Bal", "Ace", "Lone", "Ace", "Beacon", "Lob", "Ban", "Noble", "Lob", "Lance", "Canoe", "Bane", "Cone",
                 "Bale", "Alone", "Once", "Lean", "Cane", "Bale", "Eon", "Ban", "Cola", "Aloe", "Lone", "Ace",
                 "Ban", "Lab", "Bane", "Bale", "Bean", "Ace", "Can", "Lace", "Lean", "Lane", "Cane", "Ace"],

    "central" : ["Central", "Can", "Tan", "Rent", "Ale", "Arc", "Ear", "Net", "Ace", "Art", "Lane", "Tale", "Ant", "Late",
                 "Rat", "Cat", "Let", "Ran", "Cent", "Ten", "Near", "Lean", "Lent", "Earl", "Lace", "Real", "Tern", "Car",
                 "Neat", "Rate", "Lean", "Act", "Ante", "Clan", "Alert", "Rent", "Cane", "Caret", "Elan", "Rant", "Talc",
                 "Canter", "Tear", "Rental", "Tan", "Crate", "Acne", "Lent", "Rental", "Lancer",
                 "Clean", "Lance", "Ant", "Can", "Tan", "Rent", "Earl", "Near", "Art", "Ace", "Let", "Lane", "Car", "Cat"],
    "defense" : ["Defense", "Den", "Fed", "End", "See", "Need", "Send", "Fend", "Fee", "Fence", "Fed", "Cede", "Seed", "Dee",
                 "Defend", "Fed", "Ee", "End", "Fed", "Sneef", "Fee", "See", "Need", "Dense", "Fen", "Fed", "Dense", "Fend",
                 "End", "Feed", "Fed", "See", "End", "Fed", "Den", "Fed", "End", "Fed", "Fee", "See", "End", "Fed", "Den",
                 "Fed", "End", "See", "Need", "Send", "Fend",
                 "Deafen", "Den", "End", "Fed", "See", "Send", "Need", "Fence", "Feeds", "Seed", "End", "Fed", "Fee", "Defend"],

    "exactly" : ["Act", "Cat", "Tax", "Ace", "Eat", "Lace", "Let", "Tea", "Yet", "Ace", "Lay", "Eat", "Eat", "Yea", "Tea", "Lye",
                 "Ace", "Tea", "Let", "Tye", "Lye", "Cay", "Lax", "Aye", "Act", "Axe", "Yea", "Ace", "Cat", "Eat", "Tax", "Tale",
                 "Tea", "Lye", "Tea", "Ace", "Eat", "Axe", "Aye", "Yea", "Ace", "Cat", "Let", "Tea", "Lye", "Tea", "Ace", "Eat", "Aye"],

    "fortune" : ["For", "Fun", "Foe", "Tone", "Ten", "True", "Toe", "Torn", "Fur", "Fret", "Fur", "Foe", "Tore", "True", "Font", "Net",
                 "Tun", "Roe", "Tern", "Turf", "Rune", "Rent", "Tun", "One", "Tone", "Fern", "Forte", "Fort", "Fur", "Rote", "Rue", "Nor",
                 "Nut", "Rune", "Eon", "Rot", "Run", "Ton", "Fun", "Note", "Tune", "Rot", "Fore", "Rut", "Fen", "Not", "Tour", "Tern"],

    "glasses" : ["Gas", "Gale", "Leg", "Less", "Age", "Sea", "Seal", "Sag", "Lag", "Ale", "Gel", "Sage", "Lass", "Sale", "Lag",
                 "Gale", "Glasses", "Glass", "Sass", "Lass", "Legs", "Gleam", "Gale", "Glass", "Gas", "Lag", "Ages", "Leg", "Seas",
                 "Gale", "Gems", "Sage", "Gel", "Sea", "Gale", "Glam", "Sag", "Sags", "Leg", "Ages", "Gems", "Sass", "Gasses",
                 "Gels", "Sages", "Gems", "Lass", "Legs"],

    "hearing" : ["Hear", "Ring", "Near", "Rig", "Her", "Hair", "Gain", "Aging", "Reign", "Rage", "Ran", "Era", "Age",
                 "Hinge", "Range", "Grain", "Ear", "Hire", "Rain", "Airing", "Gin", "Ringer", "In", "Hen", "Nag", "Hang",
                 "Aer", "Ear", "Are", "Hi", "Rein", "Ire", "Earing", "Rang", "Rage", "Air", "In", "Re", "Rig", "He", "Gainer",
                 "Gear", "Rhea", "Reg", "Aerie", "Rah", "Nigh", "An"],

    "improve" : ["Move", "Prove", "Rove", "Imp", "Mop", "Pie", "Ripe", "Pier", "Vim", "Vie", "Viper", "Mire", "Rime",
                 "Ripe", "Over", "Per", "Pore", "Rove", "Roe", "Perv", "Per", "Ripe", "Mop", "Ripe", "Vie", "Mop", "Vie",
                 "Per", "Vim", "Rim", "Rev", "Rove", "Pier", "Vie", "Rope", "Rev", "Per", "Rime", "Mop", "Rime", "Mire",
                 "Ripe", "Rove", "Imp", "Rip", "Viper", "Ripe", "Rip"],

    "letters" : ["Letter", "Tee", "Let", "Set", "Eel", "See", "Reel", "Else", "Tree", "Steel", "Stet", "Leer", "Test", "Rest",
                 "Teeter", "Tee", "Steer", "Seer", "Reel", "Ere", "Tres", "Let", "Tee", "Lees", "Sleet", "Leer", "Set", "Reel",
                 "Test", "Seer", "Tee", "Eels", "Steel", "Retest", "Steer", "Trestle", "Stet", "Rest", "Let", "Reel", "Leer",
                 "Steer", "Tee", "Seer", "Reel", "Test", "Steel", "Letter",
                 "Letters", "Settle", "Trestle", "Tress", "Steel", "Trees", "Tester", "Restless", "Teeters", "Streel", "Stere",
                 "Steels", "Reels", "Steer", "Settler"],

    "meaning" : ["Mean", "Meaning", "Name", "Aim", "Man", "Men", "Gain", "Main", "Game", "Ming", "Gin", "Age", "Meg",
                 "Mag", "Nag", "Gem", "Gnaw", "Nan", "Am", "Ming", "An", "Inn", "Mien", "Aim", "Nine", "Min", "Mang",
                 "Mane", "Ane", "Mine", "Mina", "Mein", "Gamine", "Gin", "Mage", "Gan", "Meg", "Eon", "Ane", "Nag",
                 "Am", "Man", "Meg", "Gen", "Gin", "Mean", "Mang", "Me"],

    "nothing" : ["Nothing", "No", "Not", "Thing", "Hing", "Tin", "Hog", "Nigh", "Thin", "Hog", "Tong", "Tin", "Gin", "Hot",
                 "Hon", "In", "Hit", "Hog", "Ton", "Not", "Goth", "Nth", "Goth", "Tin", "Thin", "Hog", "Ton", "Nth", "Tin",
                 "Tong", "Got", "Hog", "Hot", "Hon", "Tong", "Thin", "No", "Not", "Ton", "In", "No", "Not", "Ton", "Thing",
                 "Hog", "Tong", "Thin", "No", "Not"],

    "outside" : ["Outside", "Out", "Side", "Die", "Tide", "Tie", "Due", "Duo", "Sit", "Out", "Sue", "Sot", "Tie", "Do",
                 "Edit", "Its", "Dot", "Use", "To", "Tide", "Die", "Out", "Site", "Dust", "Ties", "Tied", "Tie", "Dote",
                 "Sot", "Tides", "Tods", "Set", "So", "Suit", "Diet", "Tide", "Ode", "Out", "Dots", "Dues", "Duet", "Sited",
                 "Stud", "Sue", "Dots", "Dot", "Douse", "Stud"],

    "present": ["Peer", "Sent", "Pest", "Stern", "Step", "Rent", "Seen", "Pen", "Nest", "Net", "Set", "Ten", "Tree", "Tees",
                "Tense", "Steer", "Pert", "Spent", "Enter", "Erst", "Rest", "Serpent", "Peters", "Reset", "Teen", "Rents",
                "Preen", "Per", "Tree", "Seer", "Teens", "Peters", "Pest", "Rep", "Peer", "Ens", "Pen", "Peers", "Pre",
                "See", "Ten", "Tees", "Seep", "Tee", "Pet", "Reps", "Stern"],

    "quality": ["Quail", "Tail", "Quit", "Lay", "Quay", "Ail", "Lit", "Tally", "Ail", "Lit", "Quilt", "Lit", "Lity", "Ut",
                "At", "Il", "Ut", "It", "It", "Ut", "Ut", "La", "Ya", "Ut", "La", "Ut", "It", "It", "It", "La", "Ut", "Il",
                "Ut", "Il", "La", "Ut", "It", "Ut", "La", "Ut", "La", "Ut", "La", "La", "La", "La", "La", "Ut"],

    "rainbow": ["Brown", "Warn", "Worn", "Own", "Bar", "Brawn", "Bow", "Raw", "Ban", "Boar", "Air", "Brio", "Win", "Iron",
                "Brain", "Row", "Rain", "Bin", "War", "Rib", "Bow", "Wain", "Bran", "Biro", "Nor", "Now", "Air", "Baw", "War",
                "Win", "Wino", "Bow", "Ran", "Wan", "Bra", "Row", "Iron", "Bin", "Air", "Brawn", "Baw", "Oar", "Awn", "Bra",
                "Ran", "Roan"],

    "science": ["Nice", "Sin", "Ice", "Sine", "Cine", "Inn", "Sic", "Sec", "Sice", "Cis", "Is", "Sei", "Inc", "Sen", "Cines",
                "Sine", "Sin", "Ins", "Cis", "Ens", "Sic", "Ice", "Sin", "Nice", "Sec", "Sec", "Sec", "Sei", "Cine", "Cis",
                "Is", "In", "Ne", "Ne", "Ne", "Ne", "Ne", "Ne", "Ne", "Ne", "Ne", "Ne", "Ne", "Ne", "Ne", "Ne", "Ne", "Ne", "Ne"],

    "traffic": ["Act", "Car", "Tar", "Cat", "Far", "Rift", "Fat", "Fir", "Tic", "Rat", "Fit", "Arc", "Art", "Craft", "Air",
                "Rat", "Tic", "Rat", "Act", "Fat", "Tar", "Car", "Rift", "Cat", "Fair", "Rat", "Fact", "Tar", "Rift", "Car",
                "Tic", "Aft", "Traf", "Cart", "Tri", "Fat", "Rift", "Tic", "Arc", "Rat", "Fri", "Calf", "Tic", "Aft", "Frat", "Rif"],

    "undergo": ["Rung", "Red", "Run", "Dog", "Rue", "Roe", "Urge", "Ore", "Rod", "Rug", "Ego", "Dug", "Gun", "Dune", "Urn", "Rude",
                "Ogre", "Due", "Gone", "One", "Duo", "End", "Nod", "Eon", "Roe", "Run", "Urn", "Den", "Ode", "Doe", "Node", "Undo",
                "Redo", "Rug", "Drug", "Ego", "Urged", "Rod", "Dung", "Nor", "Dun", "Rug", "Gun", "Ergo", "Run"],

    "victory": ["City", "Cry", "Ivy", "Riot", "Try", "Trio", "Rot", "Tic", "Toy", "Cot", "Cot", "Coy", "Tiro",
                "Tic", "Tor", "Ivy", "Coy", "Try", "Tic", "Coy", "Rot", "Tic", "Ivy", "Ivy", "Cry", "Ivy", "Rot",
                "Toy", "Tic", "Tor", "Coy", "Coy", "Rot", "Ivy", "Tic", "Ivy", "Ivy", "Ivy", "Ivy", "Ivy", "Ivy",
                "Ivy", "Ivy", "Ivy", "Ivy", "Ivy", "Ivy"],

    "weather": ["Wet", "Tree", "Here", "Tee", "Were", "Wheat", "Tear", "Heat", "Rat", "Eat", "There", "The", "Eat", "Tee",
                "The", "Wear", "Hat", "Here", "There", "Wet", "Ear", "Hate", "Tree", "Her", "Heat", "Were", "Rate", "Were",
                "Era", "Ether", "Her", "Tree", "Rat", "Era", "Rate", "Tea", "Wee", "Hat", "Tee", "Ewe", "There", "The", "Ware",
                "Ear", "The"],

    "yankees": ["Yes", "Any", "Sea", "Say", "Aye", "Kay", "Key", "Sake", "Nay", "See", "Seek", "An", "Nay", "Nay", "An",
                "Key", "Ye", "Yak", "Sneaky", "Sneaky", "Say", "Nay", "Say", "Nay", "Aye", "Aye", "Sea", "Sea", "Say",
                "Key", "Aye", "Aye", "Aye", "Nay", "Sea", "Kay", "Yak", "Ye", "Yak", "An", "See", "Aye", "An", "An", "An", "An", "An"],

    "abandon": ["Band", "And", "Don", "Bad", "Ban", "Nab", "Ad", "Boa", "Dab", "Nod", "Bond", "Dan", "Bod", "Nab", "Ban", "Boa", "Ado", "Don",
                "Bad", "Boa", "Ban", "Nab", "Ado", "Dab", "Ban", "Boa", "Nab", "Band", "Boa", "Boa", "Nab", "Ban", "And", "Ado", "Boa", "Don",
                "Nab", "Ad", "Bad", "Dab", "Band", "Don", "Ad", "Boa", "Dan", "Ban", "Boa"],

    "capture": ["Cape", "Act", "Pace", "Carpet", "Pea", "Tape", "Part", "Cat", "Rat", "Car", "Pare"
                , "Care", "Pact", "Arc", "Pat", "Ace", "Art", "Rap", "Tap", "Apt", "Ape", "Era", "Trap", "Pear", "Rape",
                "Tea", "Crate", "Are", "Rate", "Cart", "Tear", "Tap", "Ace", "Arc", "Rap", "Peat", "Cap", "Ace", "Pate",
                "Pact", "Tar", "Tea", "Rap", "Par", "Tap", "Pot", "Rat"],

    "delight": ["Die", "Led", "Get", "Light", "Tide", "Lid", "Edit", "Tile", "Leg", "Die", "Lid", "Gel", "Hide", "The",
                "Get", "Lit", "Tie", "Tide", "Let", "Lie", "Edit", "Tide", "Legit", "Diet", "Ed", "Del", "Git", "Diet",
                "Let", "Get", "Lie", "Gel", "Tile", "Lid", "Lit", "The", "Hide", "Die", "Light", "Tie", "Ed", "Gel", "Leg",
                "The", "Tide", "Let"],

    "earnest": ["Near", "Rent", "Seat", "East", "Rest", "Teen", "Tree", "Set", "Ten", "Seen", "Net", "Tea", "Rat", "Ear",
                "Ant", "Ern", "Tee", "Ate", "Ease", "Sane", "Seen", "Sat", "Rate", "Ern", "Seat", "Net", "Set", "Teen",
                "Tree", "Set", "Ten", "Near", "Ear", "Ern", "See", "Rent", "Eat", "Neat", "Eaten", "Tern", "Eats", "Ten",
                "Era", "Are", "Tense", "Ar"],

    "fiction": ["Coin", "Icon", "Fit", "Not", "Con", "Font", "Ion", "Tic", "Ton", "Cot", "Tin", "Info", "Into", "If",
                "Ton", "Not", "Fit", "Tic", "Font", "Ion", "Con", "Coin", "Tic", "Icon", "Cot", "Nit", "Tic", "Not",
                "Ion", "Cot", "Coin", "Ton", "Con", "Fit", "Into", "Tic", "Tic", "Ton", "If", "Cot", "Con", "Tic", "Font", "Ion", "Coin", "Cot"],

    "gravity": ["Rat", "Ivy", "Gray", "Air", "Tray", "Art", "Try", "Vat", "Ivy", "Rig", "Tag", "Ray", "Tar", "Via", "Vary",
                "Gay", "Rag", "Git", "Grit", "Rig", "Rag", "Rival", "Air", "Gravy", "Art", "Tag", "Ray", "Ivy", "Rat", "Rag",
                "Rig", "Try", "Ray", "Vary", "Vat", "Ray", "Rig", "Rag", "Ivy", "Ray", "Ray", "Air", "Via", "Ray", "Vary", "Tag"],

    "honesty": ["Yes", "Hen", "Net", "Hot", "Set", "Tone", "One", "Snot", "Nose", "Stone", "Note", "Yet", "Ten", "Ton", "Soy",
                "Shoe", "Hone", "Set", "They", "Hoes", "Eon", "Toy", "Toe", "Stye", "Set", "Not", "One", "Yet", "Yes", "Then",
                "Net", "Son", "Nest", "Toe", "She", "Stony", "Not", "Ten", "Yen", "Ethos", "Hen", "Yet", "Snot", "Sot", "Eon", "Yes"],

    "journey": ["Our", "Jury", "Joy", "Yen", "Joe", "Rue", "You", "Ore", "Run", "One", "Enjoy", "Yon", "Rune", "Urn", "Rye",
                "Roe", "Jun", "Joule", "Rye", "Eon", "Roe", "Joy", "Nor", "Joy", "You", "Joy", "Your", "Urn", "Joy", "Jury",
                "Our", "Ore", "Nor", "Ore", "Rue", "Our", "Eon", "Run", "On", "Roe", "Rue", "Rune", "Joe", "Our", "Yon", "You"],

    "kitchen": ["Kit", "Chin", "Thin", "Tick", "Itch", "Kin", "Tin", "Inch", "Hen", "Hit", "Nth", "Tine", "Ink", "Tie", "Kith",
                "Then", "Hit", "Ice", "Chic", "Kite", "The", "Ten", "Hen", "Ken", "Tech", "Kin", "Net", "Tic", "Ten", "Hit",
                "Tin", "Itch", "The", "It", "Inch", "Hint", "Tic", "Kin", "Kit", "Tin", "The", "In", "Tic", "Tie", "It", "Chin"],

    "largest": ["Sage", "Gas", "Gate", "Get", "Rag", "Rat", "Set", "Salt", "Leg", "Star", "Last", "Tar", "Ear", "Tag", "Tear",
                "Real", "Late", "Gear", "Tea", "Gale", "Let", "Let", "Art", "Alert", "Great", "Rate", "Gale", "Rat", "Let",
                "Ale", "Seal", "Age", "Rage", "Slate", "Large", "Least", "Stage", "Tea", "Alter", "Gales", "Stare", "Sea",
                "Ear", "Rest", "Tale", "Late"],

    "measure": ["Same", "Sea", "Seam", "Mare", "Arm", "Ram", "Seam", "Era", "Mare", "Mare", "Ram", "Mars", "Arm", "Mar",
                "See", "Rem", "Are", "Mars", "Are", "Sea", "Ear", "Sear", "See", "Are", "Ram", "Rem", "Ream", "Erase",
                "Seem", "Mar", "Arm", "Seam", "Rem", "Ream", "Rem", "Arm", "Mere", "Seem", "Mare", "Are", "Ram", "Mar",
                "Rem", "Mar", "Arm"],

    "narrate": ["Rat", "Rate", "Tear", "Near", "Ant", "Net", "Era", "Ear", "Neat", "Rent", "Teen", "Tea", "Tan", "Ten",
                "Tar", "Art", "Tare", "Etna", "Etna", "Ant", "Ret", "Ate", "Ran", "Tern", "Tan", "Ear", "Ant", "Tart",
                "Teat", "Tern", "Rant", "Tern", "Tare", "Ran", "Rat", "Tar", "Rant", "Tart", "Tent", "Earn", "Eat",
                "Rate", "Ran", "Neat", "Net", "Tart"],

    "operate": ["Ape", "Rate", "Tape", "Tear", "Part", "Pear", "Peer", "Port", "Taper", "Tar", "Pat", "Par", "Pro",
                "Poet", "Era", "Rep", "Art", "Eat", "Pea", "Toe", "Pot", "Tap", "Rope", "Rape", "Repo", "Tar", "Opt",
                "Rot", "Ape", "Tore", "Tar", "Pet", "Tea", "Top", "Tap", "Rap", "Par", "Tap", "Pot", "Rat", "Tea", "Rap",
                "Pare", "Rate", "Oar", "Pea"],

    "purpose": ["Pose", "Pore", "Sure", "Rope", "Pure", "Pour", "User", "Rose", "Prose", "Euro", "Sue", "Sour", "Sup", "Per",
                "Use", "Rue", "Sore", "Ops", "Sop", "Pus", "Spur", "Opus", "Roe", "Euro", "Ore", "Souse", "Pore", "Purse",
                "Sue", "Rep", "Suer", "Sue", "Sue", "Sue", "Sue", "Sue", "Souse", "Sure", "Pore", "Sore", "Pure", "Pro",
                "Sue", "Up", "Rope"],

    "quarter": ["Rat", "Tear", "Rate", "Art", "Tea", "Ear", "Rare", "True", "Quart", "Tart", "Era", "Tar", "Quota", "Err",
                "Rater", "Quart", "Quart", "Tare", "Rue", "Quart", "Rater", "Err", "Tar", "Rat", "Quota", "Quart", "Tart",
                "Tear", "Ate", "Rat", "Tare", "Tea", "Quart", "Rue", "Rater", "Rat", "Quart", "Rare", "Era", "Tart", "Rue",
                "Tar", "Tear", "Eat", "Quart"],

    "resolve": ["Rev", "Solve", "Lover", "Lose", "Sole", "Roe", "Lore", "Over", "Vole", "Lore", "Loser", "Solve", "Rove",
                "Role", "Lover", "Sole", "Solve", "Lose", "Sever", "Rev", "Rose", "Reel", "Lose", "Love", "Sole", "Lose",
                "Lose", "Role", "Rev", "Sore", "Ever", "See", "Roe", "Rev", "Sole", "Rev", "Rev", "Rev", "Sever", "Serve",
                "Lose", "Role", "Lover", "Rev", "Rev"],

    "support": ["Sport", "Port", "Spot", "Post", "Tops", "Sup", "Stop", "Pots", "Sort", "Tour", "Pot", "Sop", "Rot", "Sour",
                "Pout", "Opt", "Pus", "Pro", "Up", "Out", "Tops", "Our", "Ours", "Rout", "Out", "Our", "Pro", "Opt", "Pout",
                "Opt", "Up", "Sort", "Put", "Out", "Stop", "Sop", "Top", "Pot", "Rut", "Spot", "Sort", "Port", "Post", "Rot",
                "Port", "Tour"],

    "tactics": ["Cat", "Act", "Its", "Tic", "Sit", "Tacit", "Cast", "Tit", "Tic", "Tac", "Tact", "Tics", "Cats", "Sat", "Sac",
                "Attic", "Sat", "Tacit", "Act", "Cat", "Tic", "Cast", "Tact", "Cat", "Tact", "Tacit", "Tic", "Act", "Sit", "Tic",
                "Tacit", "Tic", "Tic", "Sat", "Act", "Its", "Tic", "Sit", "Cast", "Tics", "Tacit", "Tic", "Tic", "Tic", "Tic"],

    "unknown": ["Know", "Own", "Now", "Won", "Noun", "Nun", "No", "Won", "Wonk", "Won", "Know", "Own", "Won", "Won", "Won", "On",
                "No", "On", "On", "On", "No", "No", "No", "On", "On", "No", "No", "No", "On", "On", "On", "No", "No", "No", "On",
                "No", "On", "On", "On", "On", "No", "No", "No", "No", "No", "No", "No", "No"],

    "variety": ["Yet", "Air", "Rate", "Tear", "Vary", "Aye", "Rite", "Rye", "Art", "Ray", "Tray", "Eat", "Tie", "Ear", "Tar",
                "Ivy", "Tier", "Tea", "Try", "Via", "Try", "Vet", "Vat", "Are", "Year", "Aye", "Try", "Tear", "Aye", "Rate",
                "Vet", "Ivy", "Yet", "Eat", "Very", "Ray", "Vat", "Ivy", "Rat", "Vary", "Rat", "Vie", "Eat", "Vat", "Ray", "Rye"],

    "welcome": ["Come", "Wee", "Eel", "Elm", "Meal", "Cow", "Mewl", "Mew", "Mole", "Low", "Mew", "Ewe", "Clew", "Owe", "Me", "Mew",
                "Cow", "Woe", "Eel", "Elm", "Eel", "We", "Woe", "Elm", "Meow", "Ewe", "Clew", "Wee", "Mewl", "Me", "Cow", "Clew",
                "Mow", "Cow", "Mow", "Eel", "Me", "Eel", "Wee", "Mew", "Mewl", "Elm", "Low", "Mew", "Mole", "We"],
    "yelling": ["Yell", "Yen", "Gel", "Leg", "Lie", "Yin", "Gill", "Ill", "Gin", "Nil", "Line", "Gilly", "Gelly", "Nell", "Lily",
                "Nelly", "Yell", "Nil", "Lye", "Ling", "Nell", "Lye", "Glen", "Yell", "Yen", "Leg", "Lie", "Yin", "Ill", "Lily",
                "Nil", "Gill", "Lye", "Gel", "Gin", "Yin", "Lye", "Nelly", "Yell", "Yen", "Ling", "Gill", "Yell", "Yen"],
}
random.shuffle(displayed_words)
chosen_word = displayed_words[0]
random_word = ''.join(chosen_word)
user_words = []

def game():
    if random_word in words_dict:
        new_word = list(random_word)
        random.shuffle(new_word)
        show_word = ''.join(new_word)
        print(show_word)
        user_points = 0
        for i in range(10):
            user_input = str(input("Enter words:")).capitalize()
            if user_input not in user_words and user_input not in chosen_word:
                user_words.append(user_input)
                if user_input in words_dict[random_word]:
                    points_calc = int(len(user_input) / 2)
                    user_points += points_calc
                    print("You got +", points_calc, "!!")
                else:
                    print("Word do not exist!!!")
            else:
                print("Words already exists")
        print("Total points:", user_points, "Points!!")
game()