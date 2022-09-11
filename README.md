# NoThinkFood
Get recipes for the week delivered right to your fingertips!!

## Set up
### You need to create a GCP project to make this work.
 Because you need to authenticate with google servers in order to access the google drive API. Here are some useful links:
- [Creating a project in GCP](https://developers.google.com/workspace/guides/create-project)
- [Enable GDrive API](https://developers.google.com/workspace/guides/enable-apis)
- [Configure OAuth consent](https://developers.google.com/workspace/guides/configure-oauth-consent) (make sure to add yourself a tester).
- [Create OAuth credentials](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id), make sure to download the credentials and save them to your project root as `credentials.json`

### Setting up the email service
I recomment using outlook as email provider because it is less restrivtive (and the smtp server is already configured for outlook lmao)
To be able to send emails from your application you'll need to create a file called `email_auth.py` (I should probably use dot env, but I'm fucking lazy) in the root of your folder with the following structure:
```python
email_auth = {
  'email': "<outlook acct >",
  'password':"<password>",
  'phone':'<phone number email addr>'
}
```
- `email` - This is the outlook account that will send the emails on behalf of the program
- `password` - THis is the password for this account.
- `phone` - is your phone email address, look up your carrier in [this list](https://kb.sandisk.com/app/answersweb/detailweb/a_id/17056/~/list-of-mobile-carrier-gateway-addresses) and add your celphone number before the domain.