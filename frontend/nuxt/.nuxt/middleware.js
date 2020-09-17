const middleware = {}

middleware['force-auth'] = require('../middleware/force-auth.js')
middleware['force-auth'] = middleware['force-auth'].default || middleware['force-auth']

middleware['persist-auth'] = require('../middleware/persist-auth.js')
middleware['persist-auth'] = middleware['persist-auth'].default || middleware['persist-auth']

export default middleware
