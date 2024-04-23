import requests
from bs4 import BeautifulSoup


items = {
    "Vanilla ice cream": {"price": 172.8, "level": 0, "categories": [], "requiredItems": {}},
    "Top hat": {"price": 619.2, "level": 0, "categories": [], "requiredItems": {}},
    "Pomegranate cake": {"price": 316.8, "level": 0, "categories": [], "requiredItems": {}},
    "Strawberry jam": {"price": 270.0, "level": 0, "categories": [], "requiredItems": {}},
    "Cream cake": {"price": 219.6, "level": 0, "categories": [], "requiredItems": {}},
    "Caffè mocha": {"price": 291.6, "level": 0, "categories": [], "requiredItems": {}},
    "Plain cupcake": {"price": 280.8, "level": 0, "categories": [], "requiredItems": {}},
    "Mango juice": {"price": 230.4, "level": 0, "categories": [], "requiredItems": {}},
    "Cream": {"price": 50.4, "level": 0, "categories": [], "requiredItems": {}},
    "Sesame brittle": {"price": 270.0, "level": 0, "categories": [], "requiredItems": {}},
    "Egg sushi": {"price": 550.8, "level": 0, "categories": [], "requiredItems": {}},
    "Potted plant": {"price": 151.2, "level": 0, "categories": [], "requiredItems": {}},
    "Pig feed": {"price": 14.4, "level": 0, "categories": [], "requiredItems": {}},
    "Falafel": {"price": 226.8, "level": 0, "categories": [], "requiredItems": {}},
    "Spicy pasta": {"price": 576.0, "level": 0, "categories": [], "requiredItems": {}},
    "Honey soap": {"price": 327.6, "level": 0, "categories": [], "requiredItems": {}},
    "Cabbage soup": {"price": 270.0, "level": 0, "categories": [], "requiredItems": {}},
    "Flower pendant": {"price": 698.4, "level": 0, "categories": [], "requiredItems": {}},
    "Peanut Noodles": {"price": 597.6, "level": 0, "categories": [], "requiredItems": {}},
    "Silver ore": {"price": 18.0, "level": 0, "categories": [], "requiredItems": {}},
    "Honey peanuts": {"price": 468.0, "level": 0, "categories": [], "requiredItems": {}},
    "Veggie Platter": {"price": 266.4, "level": 0, "categories": [], "requiredItems": {}},
    "Cotton shirt": {"price": 241.2, "level": 0, "categories": [], "requiredItems": {}},
    "Mayonnaise": {"price": 367.2, "level": 0, "categories": [], "requiredItems": {}},
    "Orange salad": {"price": 558.0, "level": 0, "categories": [], "requiredItems": {}},
    "Fish burger": {"price": 226.8, "level": 0, "categories": [], "requiredItems": {}},
    "Fish taco": {"price": 392.4, "level": 0, "categories": [], "requiredItems": {}},
    "Peanut Butter and Jelly Sandwich": {"price": 601.2, "level": 0, "categories": [], "requiredItems": {}},
    "Breakfast bowl": {"price": 604.8, "level": 0, "categories": [], "requiredItems": {}},
    "Tomato juice": {"price": 162.0, "level": 0, "categories": [], "requiredItems": {}},
    "Peach jam": {"price": 464.4, "level": 0, "categories": [], "requiredItems": {}},
    "Iced tea": {"price": 252.0, "level": 0, "categories": [], "requiredItems": {}},
    "Bacon and eggs": {"price": 201.6, "level": 0, "categories": [], "requiredItems": {}},
    "Pickles": {"price": 270.0, "level": 0, "categories": [], "requiredItems": {}},
    "Feta pie": {"price": 223.2, "level": 0, "categories": [], "requiredItems": {}},
    "Hummus wrap": {"price": 374.4, "level": 0, "categories": [], "requiredItems": {}},
    "Spicy pizza": {"price": 226.8, "level": 0, "categories": [], "requiredItems": {}},
    "Cherry juice": {"price": 216.0, "level": 0, "categories": [], "requiredItems": {}},
    "Chocolate roll": {"price": 604.8, "level": 0, "categories": [], "requiredItems": {}},
    "Orange juice": {"price": 234.0, "level": 0, "categories": [], "requiredItems": {}},
    "Red berry cake": {"price": 255.6, "level": 0, "categories": [], "requiredItems": {}},
    "Chocolate popcorn": {"price": 248.4, "level": 0, "categories": [], "requiredItems": {}},
    "Marmalade": {"price": 457.2, "level": 0, "categories": [], "requiredItems": {}},
    "Hot dog": {"price": 370.8, "level": 0, "categories": [], "requiredItems": {}},
    "Peanut Butter Milkshake": {"price": 619.2, "level": 0, "categories": [], "requiredItems": {}},
    "Pineapple cake": {"price": 259.2, "level": 0, "categories": [], "requiredItems": {}},
    "Cotton candy": {"price": 226.8, "level": 0, "categories": [], "requiredItems": {}},
    "Green smoothie": {"price": 320.4, "level": 0, "categories": [], "requiredItems": {}},
    "Vanilla milkshake": {"price": 673.2, "level": 0, "categories": [], "requiredItems": {}},
    "Mushroom soup": {"price": 176.4, "level": 0, "categories": [], "requiredItems": {}},
    "Coal": {"price": 10.8, "level": 0, "categories": [], "requiredItems": {}},
    "Espresso": {"price": 248.4, "level": 0, "categories": [], "requiredItems": {}},
    "Fish pie": {"price": 226.8, "level": 0, "categories": [], "requiredItems": {}},
    "Tropical smoothie": {"price": 475.2, "level": 0, "categories": [], "requiredItems": {}},
    "Grilled onion": {"price": 190.8, "level": 0, "categories": [], "requiredItems": {}},
    "Cheese omelet": {"price": 464.4, "level": 0, "categories": [], "requiredItems": {}},
    "Rice Omelet": {"price": 572.4, "level": 0, "categories": [], "requiredItems": {}},
    "Egg sandwich": {"price": 583.2, "level": 0, "categories": [], "requiredItems": {}},
    "Gnocchi": {"price": 475.2, "level": 0, "categories": [], "requiredItems": {}},
    "Pineapple coconut bars": {"price": 284.4, "level": 0, "categories": [], "requiredItems": {}},
    "Hamburger": {"price": 180.0, "level": 0, "categories": [], "requiredItems": {}},
    "Shepherds pie": {"price": 280.8, "level": 0, "categories": [], "requiredItems": {}},
    "Peach ice cream": {"price": 450.0, "level": 0, "categories": [], "requiredItems": {}},
    "Coleslaw": {"price": 468.0, "level": 0, "categories": [], "requiredItems": {}},
    "Lollipop": {"price": 342.0, "level": 0, "categories": [], "requiredItems": {}},
    "Salsa": {"price": 252.0, "level": 0, "categories": [], "requiredItems": {}},
    "Hot chocolate": {"price": 316.8, "level": 0, "categories": [], "requiredItems": {}},
    "Goat cheese toast": {"price": 302.4, "level": 0, "categories": [], "requiredItems": {}},
    "Winter veggies": {"price": 198.0, "level": 0, "categories": [], "requiredItems": {}},
    "Watermelon juice": {"price": 108.0, "level": 0, "categories": [], "requiredItems": {}},
    "Goat feed": {"price": 14.4, "level": 0, "categories": [], "requiredItems": {}},
    "Stuffed peppers": {"price": 352.8, "level": 0, "categories": [], "requiredItems": {}},
    "Spring omelet": {"price": 230.4, "level": 0, "categories": [], "requiredItems": {}},
    "Flower crown": {"price": 331.2, "level": 0, "categories": [], "requiredItems": {}},
    "Cookie cupcake": {"price": 712.8, "level": 0, "categories": [], "requiredItems": {}},
    "Passion fruit pie": {"price": 111.6, "level": 0, "categories": [], "requiredItems": {}},
    "Flower shawl": {"price": 295.2, "level": 0, "categories": [], "requiredItems": {}},
    "Spicy fish": {"price": 543.6, "level": 0, "categories": [], "requiredItems": {}},
    "Apple pie": {"price": 270.0, "level": 0, "categories": [], "requiredItems": {}},
    "Honey apple cake": {"price": 482.4, "level": 0, "categories": [], "requiredItems": {}},
    "Lobster soup": {"price": 612.0, "level": 0, "categories": [], "requiredItems": {}},
    "Caffè latte": {"price": 219.6, "level": 0, "categories": [], "requiredItems": {}},
    "Violet dress": {"price": 327.6, "level": 0, "categories": [], "requiredItems": {}},
    "Diamond ring": {"price": 824.4, "level": 0, "categories": [], "requiredItems": {}},
    "Bacon Fries": {"price": 302.4, "level": 0, "categories": [], "requiredItems": {}},
    "Guava juice": {"price": 252.0, "level": 0, "categories": [], "requiredItems": {}},
    "Sweet porridge": {"price": 460.8, "level": 0, "categories": [], "requiredItems": {}},
    "Fruit salad": {"price": 597.6, "level": 0, "categories": [], "requiredItems": {}},
    "Lobster skewer": {"price": 417.6, "level": 0, "categories": [], "requiredItems": {}},
    "Bacon toast": {"price": 648.0, "level": 0, "categories": [], "requiredItems": {}},
    "Asparagus quiche": {"price": 302.4, "level": 0, "categories": [], "requiredItems": {}},
    "Honey toast": {"price": 255.6, "level": 0, "categories": [], "requiredItems": {}},
    "Baked potato": {"price": 298.8, "level": 0, "categories": [], "requiredItems": {}},
    "Carrot cake": {"price": 165.6, "level": 0, "categories": [], "requiredItems": {}},
    "Cherry popsicle": {"price": 352.8, "level": 0, "categories": [], "requiredItems": {}},
    "Red scarf": {"price": 288.0, "level": 0, "categories": [], "requiredItems": {}},
    "Guava compote": {"price": 421.2, "level": 0, "categories": [], "requiredItems": {}},
    "Pizza": {"price": 190.8, "level": 0, "categories": [], "requiredItems": {}},
    "Tofu stir fry": {"price": 306.0, "level": 0, "categories": [], "requiredItems": {}},
    "Tomato soup": {"price": 478.8, "level": 0, "categories": [], "requiredItems": {}},
    "Samosa": {"price": 223.2, "level": 0, "categories": [], "requiredItems": {}},
    "Raspberry mocha": {"price": 259.2, "level": 0, "categories": [], "requiredItems": {}},
    "Plain waffles": {"price": 198.0, "level": 0, "categories": [], "requiredItems": {}},
    "Lemon cake": {"price": 896.4, "level": 0, "categories": [], "requiredItems": {}},
    "Honey tea": {"price": 313.2, "level": 0, "categories": [], "requiredItems": {}},
    "Popcorn": {"price": 32.4, "level": 0, "categories": [], "requiredItems": {}},
    "Tea pot": {"price": 219.6, "level": 0, "categories": [], "requiredItems": {}},
    "Blanket": {"price": 1098.0, "level": 0, "categories": [], "requiredItems": {}},
    "Chickpea stew": {"price": 284.4, "level": 0, "categories": [], "requiredItems": {}},
    "Apple porridge": {"price": 522.0, "level": 0, "categories": [], "requiredItems": {}},
    "Chocolate waffles": {"price": 637.2, "level": 0, "categories": [], "requiredItems": {}},
    "Strawberry cake": {"price": 316.8, "level": 0, "categories": [], "requiredItems": {}},
    "Cookie": {"price": 104.4, "level": 0, "categories": [], "requiredItems": {}},
    "Sheep feed": {"price": 14.4, "level": 0, "categories": [], "requiredItems": {}},
    "Fish and chips": {"price": 244.8, "level": 0, "categories": [], "requiredItems": {}},
    "Colourful omelet": {"price": 136.8, "level": 0, "categories": [], "requiredItems": {}},
    "Plain yogurt": {"price": 234.0, "level": 0, "categories": [], "requiredItems": {}},
    "Grape jam": {"price": 162.0, "level": 0, "categories": [], "requiredItems": {}},
    "Strawberry yogurt": {"price": 529.2, "level": 0, "categories": [], "requiredItems": {}},
    "Apple Ginger Tea": {"price": 169.2, "level": 0, "categories": [], "requiredItems": {}},
    "Toffee": {"price": 176.4, "level": 0, "categories": [], "requiredItems": {}},
    "Mushroom pot pie": {"price": 162.0, "level": 0, "categories": [], "requiredItems": {}},
    "Rice noodles": {"price": 100.8, "level": 0, "categories": [], "requiredItems": {}},
    "Candy bouquet": {"price": 554.4, "level": 0, "categories": [], "requiredItems": {}},
    "Mint tea": {"price": 255.6, "level": 0, "categories": [], "requiredItems": {}},
    "Wheat Bundle": {"price": 50.4, "level": 0, "categories": [], "requiredItems": {}},
    "Pumpkin soup": {"price": 392.4, "level": 0, "categories": [], "requiredItems": {}},
    "Chili popcorn": {"price": 122.4, "level": 0, "categories": [], "requiredItems": {}},
    "Mixed smoothie": {"price": 504.0, "level": 0, "categories": [], "requiredItems": {}},
    "Bell Pepper Soup": {"price": 439.2, "level": 0, "categories": [], "requiredItems": {}},
    "Pomegranate tea": {"price": 313.2, "level": 0, "categories": [], "requiredItems": {}},
    "Summer rolls": {"price": 316.8, "level": 0, "categories": [], "requiredItems": {}},
    "Exfoliating soap": {"price": 363.6, "level": 0, "categories": [], "requiredItems": {}},
    "Cheesecake": {"price": 284.4, "level": 0, "categories": [], "requiredItems": {}},
    "Cloche hat": {"price": 468.0, "level": 0, "categories": [], "requiredItems": {}},
    "Passion fruit jam": {"price": 118.8, "level": 0, "categories": [], "requiredItems": {}},
    "Fruit cake": {"price": 450.0, "level": 0, "categories": [], "requiredItems": {}},
    "Cucumber sandwich": {"price": 464.4, "level": 0, "categories": [], "requiredItems": {}},
    "Banana split": {"price": 403.2, "level": 0, "categories": [], "requiredItems": {}},
    "Iced banana latte": {"price": 277.2, "level": 0, "categories": [], "requiredItems": {}},
    "Onion soup": {"price": 327.6, "level": 0, "categories": [], "requiredItems": {}},
    "Passion fruit juice": {"price": 64.8, "level": 0, "categories": [], "requiredItems": {}},
    "Snack mix": {"price": 309.6, "level": 0, "categories": [], "requiredItems": {}},
    "Clay mug": {"price": 212.4, "level": 0, "categories": [], "requiredItems": {}},
    "Summer salad": {"price": 554.4, "level": 0, "categories": [], "requiredItems": {}},
    "Soy sauce": {"price": 154.8, "level": 0, "categories": [], "requiredItems": {}},
    "Fish skewer": {"price": 176.4, "level": 0, "categories": [], "requiredItems": {}},
    "Tart dressing": {"price": 288.0, "level": 0, "categories": [], "requiredItems": {}},
    "Lemon tea": {"price": 241.2, "level": 0, "categories": [], "requiredItems": {}},
    "Fried candy bar": {"price": 658.8, "level": 0, "categories": [], "requiredItems": {}},
    "Chili stew": {"price": 370.8, "level": 0, "categories": [], "requiredItems": {}},
    "Strawberry candle": {"price": 370.8, "level": 0, "categories": [], "requiredItems": {}},
    "Fresh porridge": {"price": 435.6, "level": 0, "categories": [], "requiredItems": {}},
    "Gold bar": {"price": 180.0, "level": 0, "categories": [], "requiredItems": {}},
    "Tropical cupcake": {"price": 572.4, "level": 0, "categories": [], "requiredItems": {}},
    "Veggie bouquet": {"price": 352.8, "level": 0, "categories": [], "requiredItems": {}},
    "Tropical yogurt": {"price": 457.2, "level": 0, "categories": [], "requiredItems": {}},
    "Bacon pie": {"price": 219.6, "level": 0, "categories": [], "requiredItems": {}},
    "Goat cheese": {"price": 162.0, "level": 0, "categories": [], "requiredItems": {}},
    "Carrot juice": {"price": 46.8, "level": 0, "categories": [], "requiredItems": {}},
    "Brown sugar": {"price": 32.4, "level": 0, "categories": [], "requiredItems": {}},
    "Nachos": {"price": 432.0, "level": 0, "categories": [], "requiredItems": {}},
    "Bracelet": {"price": 514.8, "level": 0, "categories": [], "requiredItems": {}},
    "Beetroot salad": {"price": 234.0, "level": 0, "categories": [], "requiredItems": {}},
    "Berry smoothie": {"price": 547.2, "level": 0, "categories": [], "requiredItems": {}},
    "Silver bar": {"price": 147.6, "level": 0, "categories": [], "requiredItems": {}},
    "Chocolate fondue": {"price": 626.4, "level": 0, "categories": [], "requiredItems": {}},
    "Tomato sauce": {"price": 230.4, "level": 0, "categories": [], "requiredItems": {}},
    "Pillow": {"price": 676.8, "level": 0, "categories": [], "requiredItems": {}},
    "Blackberry jam": {"price": 388.8, "level": 0, "categories": [], "requiredItems": {}},
    "Crunchy donut": {"price": 594.0, "level": 0, "categories": [], "requiredItems": {}},
    "Chocolate cake": {"price": 320.4, "level": 0, "categories": [], "requiredItems": {}},
    "Pumpkin pie": {"price": 158.4, "level": 0, "categories": [], "requiredItems": {}},
    "Potato soup": {"price": 255.6, "level": 0, "categories": [], "requiredItems": {}},
    "Butter": {"price": 82.8, "level": 0, "categories": [], "requiredItems": {}},
    "Lemon pie": {"price": 446.4, "level": 0, "categories": [], "requiredItems": {}},
    "Coconut ice cream": {"price": 320.4, "level": 0, "categories": [], "requiredItems": {}},
    "Mushroom pasta": {"price": 280.8, "level": 0, "categories": [], "requiredItems": {}},
    "Pancake": {"price": 108.0, "level": 0, "categories": [], "requiredItems": {}},
    "Breakfast waffles": {"price": 424.8, "level": 0, "categories": [], "requiredItems": {}},
    "Iron ore": {"price": 14.4, "level": 0, "categories": [], "requiredItems": {}},
    "Pasta carbonara": {"price": 410.4, "level": 0, "categories": [], "requiredItems": {}},
    "Onion dog": {"price": 306.0, "level": 0, "categories": [], "requiredItems": {}},
    "Lemon candle": {"price": 457.2, "level": 0, "categories": [], "requiredItems": {}},
    "Guava cupcake": {"price": 583.2, "level": 0, "categories": [], "requiredItems": {}},
    "Frutti di mare pizza": {"price": 403.2, "level": 0, "categories": [], "requiredItems": {}},
    "Green tea": {"price": 241.2, "level": 0, "categories": [], "requiredItems": {}},
    "Bacon donut": {"price": 388.8, "level": 0, "categories": [], "requiredItems": {}},
    "Floral candle": {"price": 442.8, "level": 0, "categories": [], "requiredItems": {}},
    "Mushroom Salad": {"price": 216.0, "level": 0, "categories": [], "requiredItems": {}},
    "Filled donut": {"price": 403.2, "level": 0, "categories": [], "requiredItems": {}},
    "Olive dip": {"price": 468.0, "level": 0, "categories": [], "requiredItems": {}},
    "Gracious bouquet": {"price": 500.4, "level": 0, "categories": [], "requiredItems": {}},
    "Rustic bouquet": {"price": 208.8, "level": 0, "categories": [], "requiredItems": {}},
    "Lemon curd": {"price": 378.0, "level": 0, "categories": [], "requiredItems": {}},
    "Black sesame smoothie": {"price": 313.2, "level": 0, "categories": [], "requiredItems": {}},
    "Chili poppers": {"price": 406.8, "level": 0, "categories": [], "requiredItems": {}},
    "Cherry jam": {"price": 334.8, "level": 0, "categories": [], "requiredItems": {}},
    "Sweater": {"price": 151.2, "level": 0, "categories": [], "requiredItems": {}},
    "Peach tart": {"price": 435.6, "level": 0, "categories": [], "requiredItems": {}},
    "Caramel latte": {"price": 345.6, "level": 0, "categories": [], "requiredItems": {}},
    "Gold ore": {"price": 21.6, "level": 0, "categories": [], "requiredItems": {}},
    "Winter stew": {"price": 295.2, "level": 0, "categories": [], "requiredItems": {}},
    "Soft bouquet": {"price": 298.8, "level": 0, "categories": [], "requiredItems": {}},
    "Peanut fudge": {"price": 1141.2, "level": 0, "categories": [], "requiredItems": {}},
    "Sesame Ice Cream": {"price": 176.4, "level": 0, "categories": [], "requiredItems": {}},
    "Tropical fondue": {"price": 417.6, "level": 0, "categories": [], "requiredItems": {}},
    "Apple jam": {"price": 219.6, "level": 0, "categories": [], "requiredItems": {}},
    "Cow feed": {"price": 14.4, "level": 0, "categories": [], "requiredItems": {}},
    "Banana pancakes": {"price": 352.8, "level": 0, "categories": [], "requiredItems": {}},
    "Milk tea": {"price": 190.8, "level": 0, "categories": [], "requiredItems": {}},
    "Colorful candles": {"price": 324.0, "level": 0, "categories": [], "requiredItems": {}},
    "Wooly chaps": {"price": 309.6, "level": 0, "categories": [], "requiredItems": {}},
    "Potato Omelet": {"price": 270.0, "level": 0, "categories": [], "requiredItems": {}},
    "Chocolate ice cream": {"price": 342.0, "level": 0, "categories": [], "requiredItems": {}},
    "Mint ice cream": {"price": 288.0, "level": 0, "categories": [], "requiredItems": {}},
    "Apple juice": {"price": 129.6, "level": 0, "categories": [], "requiredItems": {}},
    "Feta salad": {"price": 745.2, "level": 0, "categories": [], "requiredItems": {}},
    "Meat Bucket": {"price": 72.0, "level": 0, "categories": [], "requiredItems": {}},
    "Refined coal": {"price": 108.0, "level": 0, "categories": [], "requiredItems": {}},
    "Canned fish": {"price": 471.6, "level": 0, "categories": [], "requiredItems": {}},
    "Mint fudge": {"price": 522.0, "level": 0, "categories": [], "requiredItems": {}},
    "Syrup": {"price": 90.0, "level": 0, "categories": [], "requiredItems": {}},
    "Plum jam": {"price": 385.2, "level": 0, "categories": [], "requiredItems": {}},
    "Seafood salad": {"price": 763.2, "level": 0, "categories": [], "requiredItems": {}},
    "Garlic bread": {"price": 198.0, "level": 0, "categories": [], "requiredItems": {}},
    "Orange sorbet": {"price": 399.6, "level": 0, "categories": [], "requiredItems": {}},
    "Fresh pasta": {"price": 43.2, "level": 0, "categories": [], "requiredItems": {}},
    "Rich fudge": {"price": 644.4, "level": 0, "categories": [], "requiredItems": {}},
    "Blue woolly hat": {"price": 111.6, "level": 0, "categories": [], "requiredItems": {}},
    "Blue sweater": {"price": 208.8, "level": 0, "categories": [], "requiredItems": {}},
    "Raspberry jam": {"price": 252.0, "level": 0, "categories": [], "requiredItems": {}},
    "Platinum Ore": {"price": 32.4, "level": 0, "categories": [], "requiredItems": {}},
    "Fruit sorbet": {"price": 518.4, "level": 0, "categories": [], "requiredItems": {}},
    "Blackberry muffin": {"price": 226.8, "level": 0, "categories": [], "requiredItems": {}},
    "Chocolate": {"price": 460.8, "level": 0, "categories": [], "requiredItems": {}},
    "Mint essential oil": {"price": 172.8, "level": 0, "categories": [], "requiredItems": {}},
    "Cotton fabric": {"price": 108.0, "level": 0, "categories": [], "requiredItems": {}},
    "Rich soap": {"price": 266.4, "level": 0, "categories": [], "requiredItems": {}},
    "Sprinkled donut": {"price": 313.2, "level": 0, "categories": [], "requiredItems": {}},
    "Lobster pasta": {"price": 637.2, "level": 0, "categories": [], "requiredItems": {}},
    "Chili fudge": {"price": 540.0, "level": 0, "categories": [], "requiredItems": {}},
    "Cream donut": {"price": 230.4, "level": 0, "categories": [], "requiredItems": {}},
    "Fish soup": {"price": 298.8, "level": 0, "categories": [], "requiredItems": {}},
    "Eggplant parmesan": {"price": 442.8, "level": 0, "categories": [], "requiredItems": {}},
    "Beeswax": {"price": 234.0, "level": 0, "categories": [], "requiredItems": {}},
    "Grilled Asparagus": {"price": 486.0, "level": 0, "categories": [], "requiredItems": {}},
    "Strawberry ice cream": {"price": 331.2, "level": 0, "categories": [], "requiredItems": {}},
    "Iron bracelet": {"price": 658.8, "level": 0, "categories": [], "requiredItems": {}},
    "Bacon fondue": {"price": 507.6, "level": 0, "categories": [], "requiredItems": {}},
    "Lobster sushi": {"price": 637.2, "level": 0, "categories": [], "requiredItems": {}},
    "Buttered popcorn": {"price": 126.0, "level": 0, "categories": [], "requiredItems": {}},
    "Fried rice": {"price": 205.2, "level": 0, "categories": [], "requiredItems": {}},
    "Corn bread": {"price": 72.0, "level": 0, "categories": [], "requiredItems": {}},
    "Potato feta cake": {"price": 309.6, "level": 0, "categories": [], "requiredItems": {}},
    "Grilled eggplant": {"price": 324.0, "level": 0, "categories": [], "requiredItems": {}},
    "Gingerbread cookie": {"price": 273.6, "level": 0, "categories": [], "requiredItems": {}},
    "Fruity milkshake": {"price": 759.6, "level": 0, "categories": [], "requiredItems": {}},
    "Casserole": {"price": 367.2, "level": 0, "categories": [], "requiredItems": {}},
    "Chocolate pie": {"price": 514.8, "level": 0, "categories": [], "requiredItems": {}},
    "BLT salad": {"price": 723.6, "level": 0, "categories": [], "requiredItems": {}},
    "Honey": {"price": 154.8, "level": 0, "categories": [], "requiredItems": {}},
    "Berry waffles": {"price": 604.8, "level": 0, "categories": [], "requiredItems": {}},
    "Potato bread": {"price": 284.4, "level": 0, "categories": [], "requiredItems": {}},
    "Raspberry candle": {"price": 360.0, "level": 0, "categories": [], "requiredItems": {}},
    "Plum smoothie": {"price": 522.0, "level": 0, "categories": [], "requiredItems": {}},
    "Berry juice": {"price": 205.2, "level": 0, "categories": [], "requiredItems": {}},
    "Honey face mask": {"price": 320.4, "level": 0, "categories": [], "requiredItems": {}},
    "Chicken feed": {"price": 7.2, "level": 0, "categories": [], "requiredItems": {}},
    "Caramel apple": {"price": 255.6, "level": 0, "categories": [], "requiredItems": {}},
    "Orange tea": {"price": 255.6, "level": 0, "categories": [], "requiredItems": {}},
    "Sun hat": {"price": 558.0, "level": 0, "categories": [], "requiredItems": {}},
    "Veggie lasagna": {"price": 532.8, "level": 0, "categories": [], "requiredItems": {}},
    "Platinum bar": {"price": 205.2, "level": 0, "categories": [], "requiredItems": {}},
    "Hand pies": {"price": 295.2, "level": 0, "categories": [], "requiredItems": {}},
    "Jelly beans": {"price": 684.0, "level": 0, "categories": [], "requiredItems": {}},
    "Big sushi roll": {"price": 648.0, "level": 0, "categories": [], "requiredItems": {}},
    "Kimchi": {"price": 219.6, "level": 0, "categories": [], "requiredItems": {}},
    "Macaroon": {"price": 421.2, "level": 0, "categories": [], "requiredItems": {}},
    "Dried fruit": {"price": 266.4, "level": 0, "categories": [], "requiredItems": {}},
    "Iron bar": {"price": 129.6, "level": 0, "categories": [], "requiredItems": {}},
    "Cheese": {"price": 122.4, "level": 0, "categories": [], "requiredItems": {}},
    "Banana bread": {"price": 424.8, "level": 0, "categories": [], "requiredItems": {}},
    "Bread": {"price": 21.6, "level": 0, "categories": [], "requiredItems": {}},
    "Birthday bouquet": {"price": 349.2, "level": 0, "categories": [], "requiredItems": {}},
    "White sugar": {"price": 50.4, "level": 0, "categories": [], "requiredItems": {}},
    "Quesadilla": {"price": 241.2, "level": 0, "categories": [], "requiredItems": {}},
    "Cocoa smoothie": {"price": 511.2, "level": 0, "categories": [], "requiredItems": {}},
    "Hummus": {"price": 277.2, "level": 0, "categories": [], "requiredItems": {}},
    "Sushi roll": {"price": 489.6, "level": 0, "categories": [], "requiredItems": {}},
    "Corn dog": {"price": 529.2, "level": 0, "categories": [], "requiredItems": {}},
    "Yogurt smoothie": {"price": 349.2, "level": 0, "categories": [], "requiredItems": {}},
    "Cucumber smoothie": {"price": 266.4, "level": 0, "categories": [], "requiredItems": {}},
    "Mocha milkshake": {"price": 856.8, "level": 0, "categories": [], "requiredItems": {}},
    "Pineapple juice": {"price": 68.4, "level": 0, "categories": [], "requiredItems": {}},
    "Bright bouquet": {"price": 338.4, "level": 0, "categories": [], "requiredItems": {}},
    "Cheese fondue": {"price": 493.2, "level": 0, "categories": [], "requiredItems": {}},
    "Grape juice": {"price": 104.4, "level": 0, "categories": [], "requiredItems": {}},
    "Pasta salad": {"price": 759.6, "level": 0, "categories": [], "requiredItems": {}},
    "Necklace": {"price": 727.2, "level": 0, "categories": [], "requiredItems": {}},
    "Broccoli soup": {"price": 237.6, "level": 0, "categories": [], "requiredItems": {}},
    "Olive oil": {"price": 277.2, "level": 0, "categories": [], "requiredItems": {}},
    "Lemon essential oil": {"price": 288.0, "level": 0, "categories": [], "requiredItems": {}},
    "Honey popcorn": {"price": 360.0, "level": 0, "categories": [], "requiredItems": {}},
    "Onion melt": {"price": 417.6, "level": 0, "categories": [], "requiredItems": {}},
    "Lemon fudge": {"price": 590.4, "level": 0, "categories": [], "requiredItems": {}},
    "Asparagus soup": {"price": 255.6, "level": 0, "categories": [], "requiredItems": {}},
    "Fancy cake": {"price": 450.0, "level": 0, "categories": [], "requiredItems": {}},
    "Broccoli pasta": {"price": 345.6, "level": 0, "categories": [], "requiredItems": {}},
    "Noodle soup": {"price": 432.0, "level": 0, "categories": [], "requiredItems": {}},
    "Raspberry muffin": {"price": 140.4, "level": 0, "categories": [], "requiredItems": {}},
    "Plain donut": {"price": 129.6, "level": 0, "categories": [], "requiredItems": {}},
    "Taco": {"price": 396.0, "level": 0, "categories": [], "requiredItems": {}},
    "Roasted tomatoes": {"price": 118.8, "level": 0, "categories": [], "requiredItems": {}},
    "Rice ball": {"price": 464.4, "level": 0, "categories": [], "requiredItems": {}},
    "Affogato": {"price": 435.6, "level": 0, "categories": [], "requiredItems": {}},
    "Tofu dog": {"price": 367.2, "level": 0, "categories": [], "requiredItems": {}},
    "Veggie bagel": {"price": 532.8, "level": 0, "categories": [], "requiredItems": {}},
    "Lemon lotion": {"price": 403.2, "level": 0, "categories": [], "requiredItems": {}},
    "Carrot pie": {"price": 82.8, "level": 0, "categories": [], "requiredItems": {}},
    "Rice": {"price": 18.0, "level": 0, "categories": [], "requiredItems": {}},
    "Goat Milk": {"price": 64.8, "level": 0, "categories": [], "requiredItems": {}},
    "Eggplant": {"price": 14.4, "level": 0, "categories": [], "requiredItems": {}},
    "Bell Pepper": {"price": 36.0, "level": 0, "categories": [], "requiredItems": {}},
    "Cabbage": {"price": 18.0, "level": 0, "categories": [], "requiredItems": {}},
    "Ginger": {"price": 28.8, "level": 0, "categories": [], "requiredItems": {}},
    "Cherry": {"price": 68.4, "level": 0, "categories": [], "requiredItems": {}},
    "Guava": {"price": 111.6, "level": 0, "categories": [], "requiredItems": {}},
    "Fish Fillet": {"price": 54.0, "level": 0, "categories": [], "requiredItems": {}},
    "Lemon": {"price": 93.6, "level": 0, "categories": [], "requiredItems": {}},
    "Bacon": {"price": 50.4, "level": 0, "categories": [], "requiredItems": {}},
    "Corn": {"price": 7.2, "level": 0, "categories": [], "requiredItems": {}},
    "Soybean": {"price": 10.8, "level": 0, "categories": [], "requiredItems": {}},
    "Pumpkin": {"price": 32.4, "level": 0, "categories": [], "requiredItems": {}},
    "Sesame": {"price": 18.0, "level": 0, "categories": [], "requiredItems": {}},
    "Pomegranate": {"price": 111.6, "level": 0, "categories": [], "requiredItems": {}},
    "Honeycomb": {"price": 68.4, "level": 0, "categories": [], "requiredItems": {}},
    "Clay": {"price": 18.0, "level": 0, "categories": [], "requiredItems": {}},
    "Chili Pepper": {"price": 36.0, "level": 0, "categories": [], "requiredItems": {}},
    "Lily": {"price": 21.6, "level": 0, "categories": [], "requiredItems": {}},
    "Asparagus": {"price": 43.2, "level": 0, "categories": [], "requiredItems": {}},
    "Cacao": {"price": 86.4, "level": 0, "categories": [], "requiredItems": {}},
    "Banana": {"price": 104.4, "level": 0, "categories": [], "requiredItems": {}},
    "Passion Fruit": {"price": 18.0, "level": 0, "categories": [], "requiredItems": {}},
    "Mango": {"price": 100.8, "level": 0, "categories": [], "requiredItems": {}},
    "Wool": {"price": 54.0, "level": 0, "categories": [], "requiredItems": {}},
    "Watermelon": {"price": 39.6, "level": 0, "categories": [], "requiredItems": {}},
    "Blackberry": {"price": 82.8, "level": 0, "categories": [], "requiredItems": {}},
    "Garlic": {"price": 14.4, "level": 0, "categories": [], "requiredItems": {}},
    "Grapes": {"price": 32.4, "level": 0, "categories": [], "requiredItems": {}},
    "Indigo": {"price": 25.2, "level": 0, "categories": [], "requiredItems": {}},
    "Plum": {"price": 82.8, "level": 0, "categories": [], "requiredItems": {}},
    "Strawberry": {"price": 50.4, "level": 0, "categories": [], "requiredItems": {}},
    "Olive": {"price": 82.8, "level": 0, "categories": [], "requiredItems": {}},
    "Oats": {"price": 7.2, "level": 0, "categories": [], "requiredItems": {}},
    "Tea Leaf": {"price": 43.2, "level": 0, "categories": [], "requiredItems": {}},
    "Egg": {"price": 18.0, "level": 0, "categories": [], "requiredItems": {}},
    "Peanuts": {"price": 234.0, "level": 0, "categories": [], "requiredItems": {}},
    "Cotton": {"price": 28.8, "level": 0, "categories": [], "requiredItems": {}},
    "Carrot": {"price": 7.2, "level": 0, "categories": [], "requiredItems": {}},
    "Coconut": {"price": 108.0, "level": 0, "categories": [], "requiredItems": {}},
    "Lobster Tail": {"price": 201.6, "level": 0, "categories": [], "requiredItems": {}},
    "Chickpea": {"price": 18.0, "level": 0, "categories": [], "requiredItems": {}},
    "Mushroom": {"price": 10.8, "level": 0, "categories": [], "requiredItems": {}},
    "Cucumber": {"price": 14.4, "level": 0, "categories": [], "requiredItems": {}},
    "Raspberry": {"price": 46.8, "level": 0, "categories": [], "requiredItems": {}},
    "Peony": {"price": 36.0, "level": 0, "categories": [], "requiredItems": {}},
    "Wheat": {"price": 3.6, "level": 0, "categories": [], "requiredItems": {}},
    "Pineapple": {"price": 14.4, "level": 0, "categories": [], "requiredItems": {}},
    "Milk": {"price": 32.4, "level": 0, "categories": [], "requiredItems": {}},
    "Duck Feather": {"price": 140.4, "level": 0, "categories": [], "requiredItems": {}},
    "Sunflower": {"price": 21.6, "level": 0, "categories": [], "requiredItems": {}},
    "Beetroot": {"price": 14.4, "level": 0, "categories": [], "requiredItems": {}},
    "Coffee Bean": {"price": 64.8, "level": 0, "categories": [], "requiredItems": {}},
    "Mint": {"price": 32.4, "level": 0, "categories": [], "requiredItems": {}},
    "Orange": {"price": 97.2, "level": 0, "categories": [], "requiredItems": {}},
    "Onion": {"price": 39.6, "level": 0, "categories": [], "requiredItems": {}},
    "Apple": {"price": 39.6, "level": 0, "categories": [], "requiredItems": {}},
    "Tomato": {"price": 43.2, "level": 0, "categories": [], "requiredItems": {}},
    "Sugarcane": {"price": 14.4, "level": 0, "categories": [], "requiredItems": {}},
    "Broccoli": {"price": 21.6, "level": 0, "categories": [], "requiredItems": {}},
    "Peach": {"price": 100.8, "level": 0, "categories": [], "requiredItems": {}},
    "Lettuce": {"price": 32.4, "level": 0, "categories": [], "requiredItems": {}},
    "Potato": {"price": 36.0, "level": 0, "categories": [], "requiredItems": {}},
    "Axe": {"price": 36.0, "level": 0, "categories": [], "requiredItems": {}},
    "Bolt": {"price": 270.0, "level": 0, "categories": [], "requiredItems": {}},
    "Brick": {"price": 342.0, "level": 0, "categories": [], "requiredItems": {}},
    "Duct Tape": {"price": 270.0, "level": 0, "categories": [], "requiredItems": {}},
    "Dynamite": {"price": 25.0, "level": 0, "categories": [], "requiredItems": {}},
    "Hammer": {"price": 342.0, "level": 0, "categories": [], "requiredItems": {}},
    "Hand Drill": {"price": 342.0, "level": 0, "categories": [], "requiredItems": {}},
    "Land Deed": {"price": 403.0, "level": 0, "categories": [], "requiredItems": {}},
    "Mallet": {"price": 403.0, "level": 0, "categories": [], "requiredItems": {}},
    "Map Piece": {"price": 450.0, "level": 0, "categories": [], "requiredItems": {}},
    "Marker Stake": {"price": 403.0, "level": 0, "categories": [], "requiredItems": {}},
    "Nail": {"price": 270.0, "level": 0, "categories": [], "requiredItems": {}},
    "Paint Bucket": {"price": 342.0, "level": 0, "categories": [], "requiredItems": {}},
    "Pickaxe": {"price": 126.0, "level": 0, "categories": [], "requiredItems": {}},
    "Plank": {"price": 270.0, "level": 0, "categories": [], "requiredItems": {}},
    "Saw": {"price": 54.0, "level": 0, "categories": [], "requiredItems": {}},
    "Screw": {"price": 270.0, "level": 0, "categories": [], "requiredItems": {}},
    "Shovel": {"price": 108.0, "level": 0, "categories": [], "requiredItems": {}},
    "Stone Block": {"price": 342.0, "level": 0, "categories": [], "requiredItems": {}},
    "Tar Bucket": {"price": 342.0, "level": 0, "categories": [], "requiredItems": {}},
    "TNT Barrel": {"price": 72.0, "level": 0, "categories": [], "requiredItems": {}},
    "Wood Panel": {"price": 270.0, "level": 0, "categories": [], "requiredItems": {}},
    "Help": {"price": 100.0, "level": 0, "categories": [], "requiredItems": {}},
}


def get_item_page(item):
    item = "_".join([(i[0].upper() + i[1:]) for i in item.split(" ")])
    item = item.replace("And", "and")
    item = item.replace("Di_Mare", "di_Mare")
    item = item.replace("Shepherds", "Shepherd's")
    url = f"https://hayday.fandom.com/wiki/{item}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Error fetching page for {item} at link {url}")

def get_item_price(page):
    soup = BeautifulSoup(page, "html.parser")
    elem = soup.find(string=lambda text: "maximum price" in text.lower())
    if elem:
        text = elem.lower()
        # Remove anything that isn't a number
        price = "".join([c for c in text if c.isdigit()])
        price = int(price) / 10
    else:
        # find text containing "to" inside portable-infobox
        elem = soup.find("aside", {"class": "portable-infobox"})
        # Find the element containing "to"
        elem = elem.find(string=lambda text: "to" in text.lower())

        if elem:
            text = elem.lower().split("to")[1]
            # Remove anything that isn't a number
            price = "".join([c for c in text if c.isdigit()])
            price = price+".0"
        else:
            price = None

    if "price":
        return price

    return None

def get_item_level(page):
    soup = BeautifulSoup(page, "html.parser")
    elem = soup.find("aside", {"class": "portable-infobox"})
    elem = elem.find(string=lambda text: "exp. lvl(s)" in text.lower())

    if elem:
        text = elem.lower().split("(s)")[1]
        # Remove anything that isn't a number
        level = "".join([c for c in text if c.isdigit()])
        level = level
    else:
        level = None

    if level:
        return level

    return None

def get_item_categories(page):
    # Find all a with the title starting with "Category:"
    soup = BeautifulSoup(page, "html.parser")

    # page-header__categories
    elem = soup.find("div", {"class": "page-header__categories"})
    categories = []

    if not elem:
        return []

    category_elems = elem.find_all("a")

    for category_elem in category_elems:
        try:
            if "Category:" not in category_elem["title"]:
                continue

            title = category_elem["title"]

            category = title.split(":")[1].strip()
            categories.append(category)
        except:
            pass

    any_product_categories = False
    for category in categories:
        if "Products" in category:
            any_product_categories = True
            break

    if any_product_categories:
        # Remove " Products" from the end of each category
        categories = [category.split(" Products")[0] for category in categories]
        categories.append("Products")
    return categories

def get_filename_from_url(url):
    # if starts with https://static.wikia.nocookie.net/hayday/images/ 
    if url.startswith("https://static.wikia.nocookie.net/hayday/images/"):
        norev = url.split("/revision")[0]
        # Get File name
        filename = norev.split("/")[-1]

        # Remove .png
        filename = filename.split(".png")[0]

        return filename
    return url

def get_required_items(page):
    soup = BeautifulSoup(page, "html.parser")

    # Find a table with border 0
    table = soup.find("table", {"border": "0"})

    if not table:
        return {}

    ingredients = table.find_all("a")
    # Map all ingredients to their href
    ingredients = [ingredient["href"].replace("/wiki/", "").replace("_", " ") for ingredient in ingredients]

    # If any of the ingredients use an absolute url, extract the filename
    ingredients = [get_filename_from_url(ingredient) for ingredient in ingredients]

    # For each ingredient, match the casing from the actual list
    index = 0

    blacklisted_ingredients = ["Experience"]

    for ingredient in ingredients:
        found = False
        for key in items:
            if key.lower() == ingredient.lower():
                ingredients[index] = key
                found = True
                break
    
        if not found:
            print("!!!!Could not find " + ingredient)

        index += 1

    amounts = table.find_all("b")
    amounts = [amount.text for amount in amounts]


    # print("Checking for " + str(ingredients))
    # print("Amounts: ", amounts)

    amounts = [int("".join([c for c in amount if c.isdigit()])) for amount in amounts]

    
    return dict(zip(ingredients, amounts))

count=0
total = len(items)

# Go through each Key
for key in items:
    try:
        # level = get_item_level(key)
        page = get_item_page(key)

        level = get_item_level(page)
        categories = get_item_categories(page)
        categories_no_requirements = ["Field Crops", "Tree Crops", "Animal Goods", "Bush Crops"]

        if not any(category in categories for category in categories_no_requirements):
            required_items = get_required_items(page)
            items[key]["requiredItems"] = required_items

        items[key]["level"] = int(level)
        items[key]["categories"] = categories

        count += 1
        print(f"{count}/{total} Done with " + key)
    except Exception as e:
        print(f"Error with {key}: {e}")

# Print to console
print("{")
for key in items:
    print(f'"{key}": {items[key]},')