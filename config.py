# Please note that config files are Python source code!
# A common mistake is to put an option list (such as TemplateChecks,
# JSONRPCAddresses, etc) excluding the final comma.
# For example (this is WRONG):
#     JSONRPCAddresses = (
#         ('', 8337)  # <-- there must be a comma after EVERY item, even last
#     )
# Without the final comma, should the option list ever have only one item in
# it, Python would interpret the "main" parenthesis as a mere sub-expression
# instead of a list of values. If that occurs, you might get crazy errors, or
# things might just not work correctly. Be careful to not miss the commas.

### Settings relating to server identity

# Name of the server
ServerName = 'Private Eloipool'

### Settings relating to server scaling/load

# Share hashes must be below this to be valid shares
# If dynamic targetting is enabled, this is a minimum
ShareTarget = 0x000000000fffffffffffffffffffffffffffffffffffffffffffffffffffffff

# Automatically adjust targets per username
# 0 = disabled
# 1 = arbitrary targets
# 2 = power of two difficulties (zero bit counts)
DynamicTargetting = 2

# How many shares per minute to try to achieve on average
DynamicTargetGoal = 6

# Number of seconds hashrate is measured over
DynamicTargetWindow = 120

# Minimum and maximum of merkle roots to keep queued
WorkQueueSizeRegular = (0x100, 0xB00)

# Minimum and maximum of BLANK merkle roots to keep queued
# (used if we run out of populated ones)
WorkQueueSizeClear = (0x1000, 0x2000)

# Minimum and maximum of BLANK merkle roots to keep queued, one height up
# (used for longpolls)
WorkQueueSizeLongpoll = (0x1000, 0x2000)

# How long to wait between getmemorypool updates normally
MinimumTxnUpdateWait = 5

# How long to wait between retries if getmemorypool fails
TxnUpdateRetryWait = 1

# How long to sleep in idle loops (temporary!)
IdleSleepTime = 0.1

### Settings relating to reward generation

# Address to generate rewards to
# NOTE: TrackerAddr can be any version 0 address (ie, no P2SH yet).
TrackerAddr = '1HXkfPiorRq2BxJYHKoWdBWYk5Q1KwWNT7'  # https://blockchain.info/wallet/user
#TrackerAddr = '1F2EZrrN8Mg7cK6F3zw18A5ykocRiu4dba' # Local bitcoind wallet.

# Coinbaser command to control reward delegation
# NOTE: This example donates 1% of block rewards to Luke-Jr for Eloipool development
#CoinbaserCmd = 'echo -e "1\\n$((%d / 100))\\n1579aXhdwvKZEMrAKoCZhzGuqMa8EonuXU"'

### Settings relating to upstream data providers

# JSON-RPC servers to get block templates from
# See https://en.bitcoin.it/wiki/BIP_0023#Logical_Services for key details
TemplateSources = (
	{
		'name': 'primary',
		'uri': 'http://rpcuser:yighyeg8OnI@localhost:8332', #change the password here and the matching password in bitcoindata/bitcoin.conf
		'priority': 0,
		'weight': 1,
	},
#	{
#		'name': 'secondary',
#		'uri': 'http://user:pass@localhost:18332',
#		'priority': 1,
#		'weight': 1,
#	},
)

# JSON-RPC servers to check block proposals with
# If none provided, and selected source supports proposals, it alone will also
# be used for checking
# NOTE: Any servers listed here MUST support BIP 23 Block Proposals
# NOTE: Mainline bitcoind (as of 0.8) does NOT support this (though the 0.8.0.eligius branch does)
TemplateChecks = (
#	{
#		'name': 'primary',
#		'uri': 'http://user:pass@localhost:8332',
#		
#		# If 'unanimous' is true, no template will be used if this node
#		# rejects it
#		'unanimous': False,
#		
#		# If check servers disagree on all templates, they will be scored and
#		# the highest score will be used; 'weight' can be used to control the
#		# scoring per-server
#		'weight': 1.1,
#	},
#	{
#		'name': 'secondary',
#		'uri': 'http://user:pass@localhost:18332',
#		'unanimous': False,
#		'weight': 1,
#	},
)

# JSON-RPC servers to submit found blocks to (when they meet the full target)
# The specific TemplateSource that the block was based on will always be sent
# the block first.
# If setting is not specified, or None, full TemplateSources list will be used.
# If an empty list, no extra submissions will be attempted.
# If an empty list, and the block was found on a "clear" merkle root (not based
# on any TemplateSource), the full TemplateSources list will be used.
#BlockSubmissions = (
#	{
#		'name': 'primary',
#		'uri': 'http://user:pass@localhost:8332',
#	},
#	{
#		'name': 'secondary',
#		'uri': 'http://user:pass@localhost:18332',
#	}
#)

# Templates will not be used unless they have an acceptance ratio above this
# Range: 0.00 - 1.00
MinimumTemplateAcceptanceRatio = 0

# No template with a combined total score below this will be used
MinimumTemplateScore = 1

# Set to True if you want shares meeting the upstream target to wait for a
# response from an upstream server before logging them. Otherwise, for such
# shares, upstreamResult will always be True and upstreamRejectReason will
# always be None. Note that enabling this may cause shares to be logged out of
# order, or with the wrong timestamp (if your share logger uses the log-time
# rather than share-time).
DelayLogForUpstream = True

# Bitcoin p2p server for announcing blocks found
#UpstreamBitcoindNode = ('127.0.0.1', 18333)  # testnet
UpstreamBitcoindNode = ('127.0.0.1', 8333)

# Network ID for the primary blockchain
# Other known network IDs can be found at:
#     https://en.bitcoin.it/wiki/Protocol_specification#Message_structure
# UpstreamNetworkId = b'\xFA\xBF\xB5\xDA'  # testnet
UpstreamNetworkId = b'\xF9\xBE\xB4\xD9'

# Secret username allowed to use setworkaux
#SecretUser = ""

# URI to send gotwork with info for every share submission
#GotWorkURI = ''

# Share hashes must be below this to be submitted to gotwork
GotWorkTarget = 0x00000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff

# Aim to produce blocks with transaction counts that are a power of two
# This helps avoid any chance of someone abusing CVE-2012-2459 with them
# 1 = cut out feeless transactions; 2 = cut out even fee-included transactions (if possible)
#POT = 2

# Avoid mining feeless transactions except to satisfy POT
# Note this only works if POT is in fact enabled in the first place
Greedy = False

### Settings relating to network services
# Note that Eloipool only supports IPv6 sockets, and if you want to bind to an
# IPv4 address you will need to prepend it with ::ffff: eg ::ffff:192.168.1.2

# Addresses to listen on for JSON-RPC GBT/getwork server
JSONRPCAddresses = (
	('', 8337),
)

# Addresses to listen on for Stratum mining server
StratumAddresses = (
	('', 3334),
)

# Addresses to listen on for Bitcoin node
# Note this will only be used to distribute blocks the pool finds, nothing else
BitcoinNodeAddresses = (
	('', 8338),
)

# Addresses that are allowed to "spoof" from address with the X-Forwarded-For header
TrustedForwarders = ('::ffff:127.0.0.1',)


# Logging of shares:
ShareLogging = (
	{
		'type': 'logfile',
		'filename': '../logs/share-logfile',
		'format': "{time} {Q(remoteHost)} {username} {YN(not(rejectReason))} {dash(YN(upstreamResult))} {dash(rejectReason)} {solution}\n",
	},
	#{
	#	'type': 'sql',
	#	'engine': 'mysql',
	#	'dbopts': {
	#		'host': 'localhost',
	#		'db': 'pooldb',
	#		'user': 'eloipool',
	#		'password': 'somethingsecret',
	#	},
	#	'statement': "insert into shares (rem_host, username, our_result, upstream_result, reason, solution, time) values ({Q(remoteHost)}, {username}, {YN(not(rejectReason))}, {YN(upstreamResult)}, {rejectReason}, unhex({solution}), NOW())",
	#},
)

### Settings related to poolserver logging

# By default, significant events will be printed to the interactive console
# You can customize your logging using either simple parameters, or Python's advanced logging framework
# Note that using Python's logging framework will override the default console logging!

# To simply log everything to the system log (syslog) as well:
# LogToSysLog = True

# To make a log file:
# LogFile = 'filename.log'

# For a rotating log file:
LogFile = {
	'filename': '../logs/eloipool.log',
	'when': 'midnight',
	'backupCount': 7,
}
# For details, see:
# http://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler
