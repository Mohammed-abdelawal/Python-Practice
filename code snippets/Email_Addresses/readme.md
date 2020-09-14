You have started your own company and are creating a Software-as-a-Service solution for tracking missing socks, called where-my-sock.is. You are currently in a beta phase. People who are interested in using the product need to sign up with an email address in order to receive an invite.

You have set up an error monitoring system so that you are notified whenever an error occurs in your software system. Recently, you have noticed several errors from the email system that sends out the invites. You investigate and you discover that a surprisingly large fraction of people trying to sign up misspell their email address when they fill out the signup form. The service you use to send the email messages is very picky about email addresses conforming to specification. This is a bit of shame because these users are not made aware of their mistake and instead end up fruitlessly refreshing their inboxes, never receiving the invite they crave so much.

You decide to do something about this. You look at the error logs and compile a list of the 8 most common mistakes people make. They are (in no particular order):

* @ symbol is missing
* There are multiple @ symbols
* There's nothing before the @ symbol
* There's nothing after the @ symbol
* Email address starts with a dot
* There's a dot just before the @ symbol
* There are consecutive dots
* The top-level-domain (.e.g. com) is missing

You intend to add a validator to the signup form to provide a helpful message to users when they make one of these mistakes, but first you create a prototype in your favourite programming language - Python.