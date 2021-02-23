from slack_webhook import Slack
slack = Slack(url='https://hooks.slack.com/services/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')
slack.post(text="Hello, world.")
