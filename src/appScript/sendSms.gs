function sendSms(body, to) {
  var messages_url = "https://api.twilio.com/2010-04-01/Accounts/AC6b010408bda22c6c38d8933af11d9abc/Messages.json";
 
  var payload = {
    "To": to,
    "Body" : body,
    "From" : "+16197386636"
  };
 
  var options = {
    "method" : "post",
    "payload" : payload
  };
 
  options.headers = { 
    "Authorization" : "Basic :" + Utilities.base64Encode("AC6b010408bda22c6c38d8933af11d9abc:b6ed0f2a87badf3775c9d00618b333b1")
  };
 
  UrlFetchApp.fetch(messages_url, options);
}
