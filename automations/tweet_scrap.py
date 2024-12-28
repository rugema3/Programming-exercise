import twint

c = twint.Config()
c.Search = "Bitcoin"
c.Limit = 100
c.Lang = "en"
c.Since = "2022-01-01"
c.Until = "2022-01-31"

twint.run.Search(c)
