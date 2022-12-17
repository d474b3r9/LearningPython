import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+")

webbrowser.open("https://google.com/search?q="+user_term)