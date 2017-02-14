# The requests module is used to visit web pages from Python
import requests

# https://github.com/kootenpv/yagmail
import yagmail

def send_email(recipient, subject, body):

    # Intialize yagmail
    yag = yagmail.SMTP('wcc.python', 'montypython932');

    # Send the email
    yag.send(recipient, subject, body)


def load_site(url):

    # Send a request to the given URL; store the results in a variable called `response`
    response = requests.get(url)

    # A response will contain multiple parts such as a header, an encoding type,
    # and the actual body of the response, referred to as `content`
    # This is what we want, so we extract it from the response.
    web_page_content = response.content

    # Return the content, transformed to all lowercase characters using the .lower() method
    # This will allow our searches of this content to be case insensitive
    return web_page_content.lower()

# Test
#print load_site('https://www.travelzoo.com/top20')

def search_for_vacations(destination, url):

    # Convert destination to lowercase so search is case insensitive
    destination = destination.lower()    

    content = load_site(url)

    print('Searching for: ' + destination + '\nChecking site: ' + url)

    if destination in content:
        print('-> FOUND! ')
        # Send email
        recipient = 'leahbrunetto@gmail.com' # Update with your email address
        subject = 'Vacation deal found for ' + destination + '!'
        body = 'Quick! Check out ' + url + ' -- they just posted a deal for a trip to ' + destination + '.'
        send_email(recipient, subject, body)
    else:
        print('-> Not found ')

#search_for_vacations('Vegas', 'https://www.groupon.com/occasion/last-minute-travel-deals')
search_for_vacations('Cuba', 'https://www.travelzoo.com/top20')

