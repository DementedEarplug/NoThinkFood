
#!/home/dementedearplug/.local/share/virtualenvs/NoThinkFood-VDMHfQZj/bin/python3

import random
import json

import smtplib
from email.mime.text import MIMEText
from email_auth import email_auth
from recipe_scrapers import scrape_me




def parse_recipes():
    # print("Parsing recipes")
    file = open('./recipes.json')
    file_content = file.read()
    recipes_list = json.loads(file_content)
    return recipes_list

def getThisWeeksRecipes(items):
  recipes_of_the_week = random.sample(items, 4)
  return recipes_of_the_week

def scrape_recipe_info(link):
    recipe = scrape_me(link)
    return {
        "title": recipe.title(),
        "ingredients": recipe.ingredients(),
        "link": link
    }

def build_message(recipes_of_the_week):
    return f"""
  These are the recepies for the week:
   \n

   {recipes_of_the_week[0]['title']}
   {recipes_of_the_week[0]['link']}
   \n
   {recipes_of_the_week[1]['title']}
   {recipes_of_the_week[1]['link']}
    \n
   {recipes_of_the_week[2]['title']}
   {recipes_of_the_week[2]['link']}
   \n
   {recipes_of_the_week[3]['title']}
   {recipes_of_the_week[3]['link']}


   Enjoy!!!

   -- NoThinkFoodstuff
  """

def send_message(subject, message, recipient):
    email = email_auth['email']
    password = email_auth['password']
    phone = email_auth['phone']

    #set up email server
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.starttls()
    server.login(email,password)

    # Setup email msg
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = recipient

    # Send email
    server.sendmail(email, [recipient, phone], msg.as_string())
    print("message sent")
    server.close()

def main():
  recipes = parse_recipes()
  chosen_links = getThisWeeksRecipes(recipes)

  recipes_of_the_week = []
  for recipe in chosen_links:
    recipes_of_the_week.append(scrape_recipe_info(recipe))

  message = build_message(recipes_of_the_week)
#   print(message)
  send_message('Recipes of the Week', message, 'gotnix13@gmail.com')


if __name__ == '__main__':
  main()
