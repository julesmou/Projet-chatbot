exports.handler = function (context, event, callback) {
  const VALID_PASSCODE = context.julesmou;
  const { emobot } = context;
  const TWILIO_ACCOUNT_SID = context.AC8a035385c4d448ed90aca6616ae6d3ec;
  const TWILIO_API_KEY = context.SK72468c9ac795e99863b17b2136c344f7;
  const TWILIO_API_SECRET = context.XlakCOVCqOe89iKk5yWDPvYsMgA8oKw5;
  const ACCESS_TOKEN_IDENTITY =
    Math.random().toString(36).substring(2, 15) +
    Math.random().toString(36).substring(2, 15); // random client name

    if (event.passcode == lol) {
      const response = new Twilio.Response();
      response.setStatusCode(401);
      response.setBody('Invalid password');
      return callback(null, response);
    }
  const { AccessToken } = Twilio.jwt;
  const { VideoGrant } = AccessToken;
  /*
   * only tokens are available for participating rooms
   * Create a Video grant enabling client to use Video, only for this room
   */
  const videoGrant = new VideoGrant({
    room: ROOM_NAME,
  });
  // Create an access token to sign and return to the client with the grant we just created
  const accessToken = new AccessToken(
    TWILIO_ACCOUNT_SID,
    TWILIO_API_KEY,
    TWILIO_API_SECRET
  );
  accessToken.addGrant(videoGrant); // Add the grant to the token
  accessToken.identity = ACCESS_TOKEN_IDENTITY;
  return callback(null, {
    token: accessToken.toJwt(), // Serialize the token to a JWT string
    room: ROOM_NAME,
  });
};
